# Vassal Manager Reboot

Bulk vassal management for CK3 1.19. Grant, revoke, convert and re-contract
your whole realm from the decisions panel instead of clicking through vassals
one at a time.

A continuation of **Advanced Vassal Manager** by The Big Bad Wolf (Workshop
item 2453359354), released by the original author for anyone to pick up:

> "If anyone is interested in picking up the torch or using the existing code
> for their own projects, please feel free to do so."

All fourteen original decisions and their behaviour are intact. Nothing was
removed.

---

## What it does

Everything lives under **Open Advanced Vassal Manager Menu**, which then opens
one of three submenus: Grant, Revoke, or Miscellaneous.

**Grant** — hand out cities, temples, castles, counties, duchies and kingdoms
in bulk; give duchies to your dynasty; consolidate de jure land to the vassal
who should hold it; grant down to your domain limit and no further.

**Revoke** — strip titles by faith, culture, dynasty, government type, region,
or opinion. The three unrecoverable sweeps sit behind an arming decision. The
most recent revoke can be undone with Restore Previous Holders.

**Miscellaneous** — convert subject culture and faith, feudalise tribal and
clan vassals, set succession laws, fund vassals so the AI can actually build,
set vassal contracts, and read a loyalty report before you do any of it.

**Protection** — two character interactions mark anyone as exempt from every
mass operation in the mod. Protect your marshal, your heir's regent, the one
duke holding the border, and stop worrying about which sweep you just fired.

**Game rules** — disloyalty threshold, and whether government conversion
respects cultural innovations.

---

## Compatibility

Nothing here overwrites a vanilla file. Everything is additive: decisions, two
character interactions, two game rules, character templates, script values and
localisation. That is why it sits happily in a large playset — it is currently
developed inside a 200+ mod install.

**Administrative government is not supported.** Under Roads to Power admin
rule, counties are held through governors and estates rather than a liege
chain. The grant and revoke decisions are not admin-aware and will likely
produce nonsense on an admin realm. The contract decisions correctly skip
admin vassals.

**Contract decisions are feudal-only, by necessity.** Obligation levels are
defined per contract group; tribal, theocratic, republican and herder contracts
have a single fixed level, and clan and administrative vassals use different
systems entirely. See `docs/ARCHITECTURE.md` section 9b.

---

## Install

**From the Workshop:** subscribe and enable in a playset. Unsubscribe from the
original Advanced Vassal Manager first — the launcher will not load both.

**Locally, for development:**

1. Copy the `vassal_manager_reboot` folder into
   `Documents\Paradox Interactive\Crusader Kings III\mod\`.
2. Copy `vassal_manager_reboot.mod` into that same `mod` folder — alongside the
   folder, not inside it.
3. Check the `path=` line in `vassal_manager_reboot.mod` points at your copy.
   Forward slashes only.
4. Launcher → Playsets → enable "Vassal Manager Reboot".

---

## Documentation

| File | For |
|---|---|
| `docs/ARCHITECTURE.md` | How the mod works. Read before changing anything. |
| `docs/ADDING_A_DECISION.md` | Template and checklist for a new decision. |
| `docs/TESTING.md` | The debug procedure. It has caught something every time. |
| `CHANGELOG.md` | What changed and why, 1.0 onward. |

---

## Contributing and translations

The ten non-English localisation folders carry English text, not translations.
They exist so players outside English see readable strings instead of raw keys.
Real translations are welcome — replace the file in the matching folder and
keep the encoding.

**Encoding: every `.txt` and `.yml` must be UTF-8 with BOM.** The game loads
without it but logs an error per file. Editors call this "UTF-8 with BOM" or
"UTF-8-SIG"; plain "UTF-8" is wrong.

---

## Testing procedure

Full version in `docs/TESTING.md`. The short form, which has caught a real bug
every time it has been run:

1. Vanilla-only playset. Not your main one — you cannot attribute anything in
   a 200-mod log.
2. `-debug_mode` in Steam launch options.
3. Delete `logs/error.log`, launch, exercise the decisions, quit, read the log.
4. Cluster the errors before reading them individually. One mistake can produce
   several hundred lines and three distinct-looking error types.

A clean log means nothing broke. It does not mean everything worked — a
decision that never rendered logs nothing. Check the numbers on screen too.
