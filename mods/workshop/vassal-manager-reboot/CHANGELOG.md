# Changelog

## 2.4

- **Script values in localisation were read with the wrong promote, since 2.2.**
  `[ROOT.MakeScope.ScriptValue('x')]` is not valid in a loc string: `MakeScope`
  is a promote on `Character`, and `ROOT` in localisation is a scope wrapper
  that has no such promote. Every affected key logged
  "Could not find promote for 'MakeScope'", printed nothing, and cascaded into
  vanilla's `TRIGGER_LINE_INACTIVE_PASSED` tooltip renderer, which then threw
  "Unterminated '['" on each render.

  All keys now use `[GetPlayer.MakeScope.ScriptValue('x')|0]`, the documented
  form. Safe here because every decision that uses them is gated `is_ai = no`,
  so the player is always ROOT.

  This affected the 2.2 keys too - `avm_domain_warning_tt`,
  `avm_vassal_limit_warning_tt`, `avm_count_all_tt`, `avm_count_infidel_tt`,
  `avm_count_barbarian_tt`. The domain and vassal headroom warnings and the
  revoke counts have never displayed a number since they were added; the fault
  went unnoticed because the errors only fire when those decisions are
  actually rendered on screen.

- **Contract decisions no longer fire at vassals who have no such contract.**
  Obligation types are not global — they are the contract keys listed for that
  government's `vassal_contract_group` in
  `common/subject_contracts/groups/subject_contract_groups.txt`. Only
  `feudal_vassal` and `japan_feudal_vassal` contain `feudal_government_taxes`
  and `feudal_government_levies`. Both contract decisions previously called
  those types on *every* direct vassal. Now gated on
  `government_has_flag = government_is_feudal`.

  Verified against vanilla 1.19: `tribal_government_obligations`,
  `theocracy_government_obligations`, `republic_government_obligations` and
  `herder_government_obligations` each define a single `default` obligation
  level, so there was never anything to set on those vassals. Clan uses
  `clan_tax_collector_obligations` and administrative uses estates; both are
  different systems, not different level numbers.

- **Reset All Vassal Contracts to Normal.** The missing counterpart to the
  maximum sweeps. The vanilla contract screen will not lower an obligation
  past what crown authority allows, so maximum tax was previously a one-way
  door — a player who maxed everything and then met a faction had no route
  back short of reloading. Sets both tracks to level 2 (`feudal_tax_normal`,
  marked `default = yes` in vanilla).

- **Set Vassal Taxes by Loyalty.** One pass, tax level chosen per vassal from
  their opinion: 50+ extortionate, 0–49 high, -1 to -25 normal, below that
  low. Takes most from those who can absorb it and eases off the ones already
  near revolt, instead of squeezing everyone equally and manufacturing the
  faction you were trying to avoid.

- **Realm Loyalty Report.** A decision that changes nothing and only reports:
  vassal counts by opinion band, how many are protected, how many feudal
  contracts you can actually alter, and — the figure that matters — how many
  powerful vassals are unhappy. This mod makes irreversible things easy; it
  should also make it easy to look before you leap.

- **Protect All Powerful Vassals** and **Protect All Content Vassals**, to sit
  alongside the existing dynasty and council protection decisions. The second
  is the inverse filter to Revoke Every Title of Disloyal Vassals: run it
  first and everyone who behaved is exempt before any revoke is applied.

- Both contract sweeps and the two new contract decisions now carry an
  `is_valid` tooltip stating how many vassals will be affected and how many
  are being skipped for want of a settable contract.

- New files, per the layout convention in `docs/ARCHITECTURE.md`:
  `common/decisions/advancedvassalmanager_decisions_loyalty.txt` and
  `common/script_values/advancedvassalmanager_values_loyalty.txt`. Delete
  both to return to 2.3.

## 2.3

- **Interaction icons fixed.** Both protection interactions used
  `icon = friendly_interaction`, which is not a vanilla icon key — the keys
  resolve literally to `gfx/interface/icons/character_interactions/<key>.dds`
  and no such file exists, so the interactions rendered without an icon. Now
  `powerful_family_shield`.
- **Game rules declare explicit defaults.** Both rules relied on the engine
  picking the first setting; `default =` is now set to the settings the
  descriptions already called the default (`avm_disloyalty_moderate`,
  `avm_conversion_ignore_innovations`).
- Removed `common/game_rule_categories/` — the folder does not exist in
  vanilla, so the game never read the file. Category display names come from
  the `game_rule_category_avm_rules` localisation key, which was already
  in place; nothing visible changes.
- Verified against vanilla 1.19: `vassal_contract_set_obligation_level` with
  numeric `level = 4` is valid (vanilla uses the numeric form itself), and
  both `feudal_government_taxes` and `feudal_government_levies` have five
  obligation levels (0–4, index 4 = extortionate). The contract decisions
  are confirmed sound as written.

## 2.0 – 2.2 (reconstructed)

No entries were written at the time; this section is reconstructed from the
files and their comments, so per-version attribution is approximate.

- **2.2** — Grant decisions now prefer an existing unlanded adult courtier
  over inventing a new character, cutting long-game save bloat
  (`avm_get_or_make_holder_effect`). Five script-token fixes for CK3 1.19.
  Contract decisions isolated into
  `advancedvassalmanager_decisions_contracts.txt` so a parse failure there
  cannot cascade into other decisions.
- **2.1** — Spawn-identity resolution rewritten: culture and faith are
  resolved into scopes *before* `create_character`, fixing the "right
  culture, wrong ethnicity" bug reported against 2.0 (ethnicity is generated
  from the culture the character is created with).
- **2.0** — Major expansion of the decision set: menu structure
  (open/close decisions for Grant / Revoke / Misc), per-government revokes
  (tribal, clan, administrative, other), non-de-jure revoke, grant de jure
  to vassals, target-region system (set/clear region plus revoke in target
  kingdom/empire), protection decisions (protect dynasty, protect council,
  clear all), primogeniture setters for own and vassal titles, tiered
  funding decisions (modest/standard/lavish, replacing the 1.5 Development
  Funding game rule with script-value costs that scale with landed vassals),
  spawn-identity decisions (match land / match me / capital), grant down to
  domain limit, and the prefer-courtiers / prefer-new-characters toggle.
  Max tax / max levy contract decisions added.

## 1.5

- **Fund Realm Development.** Distributes gold to every landed vassal so the AI
  can afford to build. Costs 250 gold, five-year cooldown.
- **Game rule: Development Funding** — 100, 250 or 500 gold per vassal.

Deliberately does not construct buildings directly. CK3 building keys are
terrain- and holding-gated, so hardcoding a list means trying to build a
fishing village inland. Vassal AI construction is limited by gold, not by
judgement, so funding them and letting the game pick produces sensible results
without a forty-entry list of building IDs that breaks on the next patch.

Continuation of Advanced Vassal Manager 1.1 by The Big Bad Wolf, released by
the original author for anyone to pick up.

## 1.4

- **Restore Previous Holders.** Every revoke decision now records who held each
  title; this puts them back. Covers the most recent revoke only, skips holders
  who have since died, skips titles granted away since.
- Revoke Every Title now excludes titular titles, matching the other five.

## 1.3

- **Feudalise All Clan Vassals.** Clan to feudal government. No holdings change.
- **Convert Subjects' Culture.** The culture mirror of Convert Subjects' Faith.
- **Game rule: Culture Conversion Scope.** Characters Only by default;
  Characters and Counties additionally rewrites county cultures.
- Game rule category now displays a name instead of a raw key.

## 1.2

- Capital baronies no longer targeted directly. They move with their county;
  attempting to transfer one alone was erroring on every use of Grant Castles
  and the revoke decisions.
- Removed `is_correct_bastard_status` and `is_correct_gender`, both deleted
  from CK3. Both were in Grant Duchies to Dynasty, silently breaking its filter.
  **Behaviour change:** that decision no longer respects realm gender law.
- Grant Duchies to Dynasty no longer tries to vassalise a higher-tier ruler
  under a new duke.
- All script files now UTF-8 with BOM.
- Game rules display proper names and default correctly.
- The gated revokes now name the Arm Mass Revocation decision in their
  requirement text.
- **Protected characters.** Two character interactions; a protected character is
  skipped by every mass operation.
- **Game rules** for the disloyalty threshold and whether government conversion
  respects innovations.
- Ten stub language files so non-English players see text, not key names.

## 1.0 — Reboot

Updated for CK3 1.19.

- **Hegemony titles excluded from all mass operations.** Patch 1.18 added a
  tier above empire and applied it retroactively; the old code swept them into
  transfers. This was the crash.
- Removed `while` wrappers whose exit condition could never be satisfied. They
  ran to the engine's iteration cap on every use.
- Grant Duchies to Dynasty gave every duchy to one person; the loop overwrote
  its own target scope each pass.
- Granted holders take the culture and faith of the county they receive rather
  than the liege's.
- **Revoke Every Title of Disloyal Vassals** — opinion-based filter.
- **Feudalise All Tribal Vassals** and **Convert All Tribal Vassals to Clan.**
  The original only converted holdings and skipped tribal-government holders,
  so tribal vassals stayed tribal forever.
- **Arm / Disarm Mass Revocation** gating the three unrecoverable revokes.

---

## Outstanding

- **No administrative government support.** Grant and revoke decisions are not
  admin-aware. The contract decisions correctly skip admin vassals as of 2.4.
- **The menu is decisions imitating a UI.** A Scripted GUI would collapse the
  eight open/close decisions and the filter sprawl into one screen with
  checkboxes and live counts. The right long-term answer, and a significant
  piece of work in a language none of the rest of this uses.
- **No rules-based automation.** Setting a policy once and having it reapply on
  succession needs an `on_action` hook and has not been attempted.
- **Ten stub languages carry English text**, not translations.
- `grant_duchies_to_dynasty_decision` is the roughest code in the mod and has
  produced three separate logged errors. If it misbehaves again, rewrite it
  rather than patching it.
