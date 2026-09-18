# How this mod works

Written for whoever maintains this next, including future-you. The original
author abandoned it partly because he had forgotten his own logic. This file
exists so that doesn't happen twice.

Nothing here overwrites a vanilla file. Everything is additive: decisions,
two character interactions, three game rules, four character templates and
localisation. That is why it is compatible with almost anything.

---

## 1. The menu system

CK3 gives modders decisions, not windows. This mod fakes a menu out of
character flags.

| Flag | Meaning |
|---|---|
| `advanced_vassal_manager` | The manager is "open" |
| `avm_grant_titles` | The Grant submenu is open |
| `avm_revoke_titles` | The Revoke submenu is open |
| `avm_misc` | The Miscellaneous submenu is open |

`advancedvassalmanager_decisions_structure_open.txt` contains four decisions
that *set* those flags. `..._structure_close.txt` contains four that clear
them. Every functional decision then gates itself in `is_shown`:

```
is_shown = {
    is_ruler = yes
    is_ai = no
    has_character_flag = advanced_vassal_manager
    has_character_flag = avm_revoke_titles
}
```

So a decision only appears when its submenu is open. The open decisions also
use `NOR` blocks so that only one submenu can be open at a time.

This is why the mod has twenty-plus decisions for what looks like a dozen
features. It is clunky and a real Scripted GUI would replace all of it — see
"Known limitations" below.

---

## 2. Anatomy of a decision

Every decision in this mod follows the same shape. Copy it exactly rather
than inventing a new one.

```
my_new_decision = {
    picture = {
        reference = "gfx/interface/illustrations/decisions/decision_realm.dds"
    }
    decision_group_type = courtier
    desc = my_new_decision_desc
    selection_tooltip = my_new_decision_tooltip
    confirm_text = CONFIRM_OKAY

    ai_check_interval = 0

    is_shown = { ... }        # menu flags, see above
    is_valid = { ... }        # optional; greys out with a reason
    cooldown = { days = 1 }

    effect = { ... }

    ai_potential = { always = no }
    ai_will_do = { base = 0 }
}
```

`ai_potential` and `ai_will_do` are not optional. Without them the AI will
take these decisions and mass-revoke titles across the world.

---

## 3. The two loop patterns

This trips people up, so it is worth understanding *why* there are two.

**Revoke pattern — one pass, `every_in_list`.**

```
every_sub_realm_title = {
    limit = { ...filters... }
    add_to_temporary_list = my_targets
}
every_in_list = {
    list = my_targets
    limit = { holder = { target_is_liege_or_above = root } }
    ...transfer...
}
```

`every_in_list` visits every item once. That is all a revoke needs.

**Grant pattern — `while` + `random_in_list` + `remove_from_list`.**

```
while = {
    limit = { any_in_list = { list = my_targets  count >= 1 } }
    random_in_list = {
        list = my_targets
        create_character = { ...  save_scope_as = receiver }
        ...transfer...
        remove_from_list = my_targets
    }
}
```

Grants need this because each iteration calls `save_scope_as = receiver`.
Inside `every_in_list`, that scope is reassigned on every pass and only the
last one survives — every title would end up with the same holder. Picking one
at random and removing it from the list gives each iteration its own scope.

**The trap.** The original mod wrapped the *revoke* loops in `while` too, with
an exit condition nothing could ever satisfy, because nothing removed items
from the list. Those loops ran to the engine's iteration cap on every use and
filled `error.log`. If you add a `while`, something inside it must shrink the
list.

This exact bug is also what broke `grant_duchies_to_dynasty`: it used
`every_in_list` to pick a recipient, so every duchy went to whoever happened to
be last.

---

## 4. Transferring a title

Always three steps, in this order:

```
create_title_and_vassal_change = {
    type = granted
    save_scope_as = change
    add_claim_on_loss = no
}
change_title_holder = {
    holder = <character>
    change = scope:change
}
resolve_title_and_vassal_change = scope:change
```

If you also need to change who the new holder reports to, that is a *second*
change object (`scope:change_two`) with `change_liege` inside it, resolved
separately. See `grant_counties_decision` for the full pattern.

---

## 5. Guards every mass operation needs

Any pool built from `every_sub_realm_title` or `every_held_title` must carry
all three of these. Each one exists because it caused a real logged error.

```
tier <= tier_empire                                          # 1
is_capital_barony = no                                       # 2
NOT = { holder = { has_character_flag = avm_protected } }    # 3
```

1. **Hegemony.** Patch 1.18 added a title tier above empire and applied it
   retroactively to existing grand unifications. Sweeping one into a transfer
   was the crash that killed the original mod. Written as `<=` rather than
   naming the tier, so it survives whatever Paradox adds next.

2. **Capital baronies.** A county's capital barony cannot be transferred on its
   own — it moves with its county. Without this you get
   `Trying to change ownership of a capital barony` on every affected title.

3. **Protection.** See section 7.

Grant decisions that filter on an exact tier (`tier = tier_duchy`) are already
safe from 1, but still need 2 and 3.

---

## 6. The undo system

Each revoke decision records what it did so `avm_restore_previous_holders_decision`
can reverse it.

- At the start of every revoke effect: `clear_variable_list = avm_undo_titles`.
  Only the most recent operation is recoverable — this is deliberate, so the
  record does not grow without limit across a reign.
- Before each `change_title_holder`, the title stores
  `set_variable = { name = avm_prev_holder  value = this.holder }` and adds
  itself to `avm_undo_titles` on the player.
- The restore decision walks that list, checks the title is still held by root
  and the old holder is still alive, transfers it back, and clears the record.

**If you add a new revoke decision, you must add both halves**, or your
decision will silently leave a stale undo record from a previous operation.

---

## 7. Protection and arming

**`avm_protected`** is a character flag set by the two interactions in
`common/character_interactions/`. Any character carrying it is skipped by every
mass operation. This is the guard in section 5, item 3.

**`avm_armed`** is a 30-day character flag gating the three unrecoverable
revokes (Every Title, Non-Dynasty, Not Pinned). Set by
`avm_arm_mass_revocation_decision`, cleared by the disarm decision or by lapsing.
The gate uses a `custom_tooltip` so the requirement reads as an instruction
rather than a raw flag name:

```
is_valid = {
    custom_tooltip = {
        text = avm_requires_arming_tt
        has_character_flag = avm_armed
    }
}
```

---

## 8. Game rules

In `common/game_rules/`, with a category in `common/game_rule_categories/`.
The localisation key prefixes are not obvious and are easy to get wrong:

| Thing | Key |
|---|---|
| The rule's name | `rule_<rule_name>` |
| The rule's description | `rule_<rule_name>_desc` |
| An option's name | `setting_<option_name>` |
| An option's description | `setting_<option_name>_desc` |
| The category | `game_rule_category_<category_name>` |

There is no `default =` field that works reliably. **The first option listed in
the file is the default**, so put the sensible one first.

Read a rule in script with `has_game_rule = <option_name>`, not the rule name.

---

## 9. File layout

```
descriptor.mod
thumbnail.png                       512x512, 1:1, under 1MB
common/
  decisions/
    advancedvassalmanager_decisions.txt              original 14 decisions
    advancedvassalmanager_decisions_structure_open.txt
    advancedvassalmanager_decisions_structure_close.txt
    advancedvassalmanager_decisions_v13.txt          disloyal, arming, tribal conversion
    advancedvassalmanager_decisions_extras.txt       clan conversion, culture, undo
  scripted_character_templates/                      generated holders
  character_interactions/                            protect / unprotect
  game_rules/  +  game_rule_categories/
localization/
  english/ + ten stub languages
docs/
```

Additions live in separate files on purpose. Deleting
`..._extras.txt` returns you to 1.2.1; deleting `..._v13.txt` as well returns
you to 1.2. That has made every debugging session faster and is worth keeping up.

**Encoding: every `.txt` and `.yml` must be UTF-8 with BOM.** The game will
load without it but logs an error for each file. Most editors call this
"UTF-8 with BOM" or "UTF-8-SIG"; plain "UTF-8" is wrong.

---

## 9b. Vassal contracts are per-government

The single most common way to get contract script wrong: obligation "types"
are **not** global tokens. Each government points at a `vassal_contract_group`
(set in `common/governments/`), and that group lists which contracts exist, in
`common/subject_contracts/groups/subject_contract_groups.txt`.

| Group | Tax/levy contracts | Settable levels? |
|---|---|---|
| `feudal_vassal`, `japan_feudal_vassal` | `feudal_government_taxes`, `feudal_government_levies` | Yes, 5 each (0-4) |
| `clan_vassal` | `clan_tax_collector_obligations` | Different system |
| `tribal_vassal` | `tribal_government_obligations` | No - one `default` |
| `theocracy_vassal` | `theocracy_government_obligations` | No - one `default` |
| `republic_vassal`, `herder_vassal` | own keys | No - one `default` |
| `admin_vassal` | `administrative_obligations` | Estates |
| `nomad_vassal`, `mandala_vassal` | own tax/levy keys | Yes, own levels |

So **every loop that touches a contract must be gated on government**, or it
is calling a contract type that does not exist for most of the realm. That is
what 2.4 fixed. The gate used is `government_has_flag = government_is_feudal`
rather than naming governments, so modded feudal variants that set the flag
are included automatically.

If you ever extend this to clan, nomad or mandala vassals, add a *separate*
loop with its own gate and its own contract key. Do not try to make one loop
serve two contract groups.

---

## 10. Known limitations

**No administrative government support.** Under Roads to Power admin rule,
counties are held through governors and estates rather than a liege chain.
Nothing here accounts for that. Before writing any of it, load an
administrative save, run Grant Counties and one revoke, and read `error.log` —
find out what actually breaks rather than guessing.

**The menu is decisions pretending to be a UI.** A Scripted GUI
(`common/scripted_guis/` plus a `.gui` file) would collapse the eight
open/close decisions and the filter sprawl into one screen with checkboxes and
live counts. It is the right long-term answer and a significant piece of work
in a language none of the rest of this uses.

**Triggers that no longer exist.** `is_correct_bastard_status` and
`is_correct_gender` were both removed from CK3 and both had to be deleted from
`grant_duchies_to_dynasty_decision`. The second only surfaced after the first
was gone — the parser reports one unknown trigger per block. If you delete a
dead trigger, re-test rather than assuming the file is now clean.

**`grant_duchies_to_dynasty_decision` is the roughest code in the mod.** It has
produced three separate logged errors. If it misbehaves again, rewrite it
rather than patching it.
