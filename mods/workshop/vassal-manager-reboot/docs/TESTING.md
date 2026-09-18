# Testing

This procedure has caught something every single time it has been run. Do not
skip it because a change looks small.

## Setup

1. Steam → CK3 → Properties → Launch Options: add `-debug_mode`
2. Delete `Documents\Paradox Interactive\Crusader Kings III\logs\error.log`
3. Launch with a **vanilla-only playset** containing just this mod

The vanilla-only part matters. With a large modlist you cannot attribute an
error to anything.

## What to run

Load any save and take each decision you touched, one at a time. Some need
setting up first:

| Decision | Needs |
|---|---|
| The three gated revokes | Arm Mass Revocation taken first |
| Feudalise All Tribal Vassals | at least one tribal vassal |
| Feudalise All Clan Vassals | at least one clan vassal |
| Convert Subjects' Culture, county mode | the game rule set to Characters and Counties |
| Restore Previous Holders | a revoke run immediately before it |
| Protection interactions | applied from a character's window, not the decisions list |

`grant_castles_decision` and `grant_duchies_to_dynasty_decision` are the two
that have historically thrown the most errors. Always include them.

## Reading the log

`Documents\Paradox Interactive\Crusader Kings III\logs\error.log`

Search for `avm` and `advancedvassalmanager`. Anything else in that file is
vanilla or another mod — the base game generates thousands of lines of its own,
so a large file is not a bad sign.

Errors seen and fixed so far, for pattern recognition:

| Message | Meaning |
|---|---|
| `should be in utf8-bom encoding` | file saved as plain UTF-8 |
| `Unknown trigger: X` | that trigger was removed from CK3 |
| `Trying to change ownership of a capital barony` | missing `is_capital_barony = no` |
| `will have the same or higher tier` | trying to vassalise someone who outranks the new liege |
| raw key names shown in game | missing or misnamed localisation key |
| `Invalid database object 'X'` | the effect is right but the key does not exist - grep vanilla for the real one |
| `Unknown effect: trigger_if` | `trigger_if` is a trigger; in an effect use `if` / `else_if` / `else`. This one is nasty: the parser falls out of the decision and everything after it in the file silently fails to load |
| `who already has the law` | guard with `NOT = { has_realm_law = ... }` before adding |
| right culture, wrong ethnicity | culture was set AFTER `create_character`. Appearance is generated at creation from the culture passed in, so resolve it into a scope first and pass `culture = scope:x` into `create_character`. Produces no log error at all — only a player will spot it |

Load-time errors (encoding, unknown triggers) appear whether or not you take
any decisions. Runtime errors only appear when the code actually runs — a clean
log proves nothing about a decision you never clicked.

## Then

`logs/database_conflicts.log` should be empty. If it is not, this mod is
overwriting something it should not be.
