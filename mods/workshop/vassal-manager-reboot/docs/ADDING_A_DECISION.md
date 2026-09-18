# Adding a new decision

Checklist. Read ARCHITECTURE.md first, particularly sections 3 and 5.

## 1. Pick a file and a menu

New features go in `advancedvassalmanager_decisions_extras.txt`, not in the
original decisions file. Keeping additions separable has made every debugging
session faster.

Decide which submenu it belongs to — that determines the second flag in
`is_shown`:

| Menu | Flag |
|---|---|
| Grant | `avm_grant_titles` |
| Revoke | `avm_revoke_titles` |
| Miscellaneous | `avm_misc` |

## 2. Copy the template

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

	is_shown = {
		is_ruler = yes
		is_ai = no
		has_character_flag = advanced_vassal_manager
		has_character_flag = avm_misc
	}

	is_valid = {
		any_vassal_or_below = {
			# something that must be true for this to do anything
			count >= 1
		}
	}

	cooldown = { days = 1 }

	effect = {
		every_sub_realm_title = {
			limit = {
				tier <= tier_empire
				is_capital_barony = no
				NOT = { holder = { has_character_flag = avm_protected } }
				# your own filters here
			}
			add_to_temporary_list = my_targets
		}
		every_in_list = {
			list = my_targets
			limit = {
				holder = { target_is_liege_or_above = root }
			}
			create_title_and_vassal_change = {
				type = granted
				save_scope_as = change
				add_claim_on_loss = no
			}
			change_title_holder = {
				holder = root
				change = scope:change
			}
			resolve_title_and_vassal_change = scope:change
		}
	}

	ai_potential = { always = no }
	ai_will_do = { base = 0 }
}
```

## 3. If it creates characters, use the grant pattern instead

`while` + `random_in_list` + `remove_from_list`. See ARCHITECTURE.md section 3
for why. Also set the new holder to the land's culture and faith:

```
save_scope_as = avm_target_title
create_character = {
	template = avm_county_holder_character
	location = root.location

	save_scope_as = receiver
}
scope:receiver = {
	set_culture = scope:avm_target_title.title_province.culture
	set_character_faith = scope:avm_target_title.title_province.faith
}
```

## 4. If it revokes, wire up undo

Add at the top of `effect`:

```
clear_variable_list = avm_undo_titles
```

And immediately before `create_title_and_vassal_change`:

```
save_scope_as = avm_undo_title
set_variable = {
	name = avm_prev_holder
	value = this.holder
}
root = {
	add_to_variable_list = {
		name = avm_undo_titles
		target = scope:avm_undo_title
	}
}
```

Miss this and Restore Previous Holders will try to undo an older operation.

## 5. Add three localisation keys

In `localization/english/advancedvassalmanager_decisions_l_english.yml`:

```
my_new_decision:0 "Display Name"
my_new_decision_desc:0 "What it does, and any consequence the player should know before clicking."
my_new_decision_tooltip:0 "Something in the ruler's voice."
```

Then copy the whole file into the ten stub language folders, changing only the
`l_english:` header on line one to `l_french:` and so on. The file must stay
UTF-8 with BOM.

If the description mentions an irreversible consequence — resetting succession
law, for instance — say so there. That text is the only warning a player gets.

## 6. Test before you upload

See TESTING.md. Every single release so far has had at least one error that
only appeared in the log.
