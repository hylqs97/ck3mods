# Workshop copy

Paste-ready text for the Steam Workshop page. Keep this file in sync when you
publish — it is the record of what the page currently says.

Steam BBCode: [h1] [h2] [b] [i] [list] [*] [url=] [hr][/hr]

---

## SHORT DESCRIPTION (the one-liner under the title)

Manage your whole realm at once. Bulk grant, revoke, convert and re-contract
vassals from the decisions panel instead of clicking through them one by one.

---

## FULL DESCRIPTION

[h1]Vassal Manager Reboot[/h1]

If you have ever sat there opening forty vassals in turn to fix their
contracts, hand out conquered land, or work out who is about to revolt — this
is for you. Every operation in this mod applies to your entire realm in one
decision.

A continuation of [b]Advanced Vassal Manager[/b] by The Big Bad Wolf, updated
for CK3 1.19 and released by the original author for anyone to pick up:

[i]"If anyone is interested in picking up the torch or using the existing code
for their own projects, please feel free to do so."[/i]

All fourteen original decisions are intact. Nothing was removed.

[hr][/hr]
[h2]What you get[/h2]

Everything opens from [b]Open Advanced Vassal Manager Menu[/b], which leads to
three submenus.

[b]Grant[/b]
[list]
[*] Hand out cities, temples, castles, counties, duchies and kingdoms in bulk
[*] Give duchies to your dynasty
[*] Consolidate de jure land to the vassal who should hold it
[*] Grant down to your domain limit and no further
[*] New holders take the culture and faith of the land they receive, so you
    don't tank county control across a fresh conquest
[/list]

[b]Revoke[/b]
[list]
[*] Strip titles by faith, culture, dynasty, government type, region or opinion
[*] The three unrecoverable sweeps sit behind a separate arming decision that
    lapses on its own after 30 days
[*] Restore Previous Holders undoes the most recent revoke
[/list]

[b]Miscellaneous[/b]
[list]
[*] Convert subject culture and faith
[*] Feudalise tribal and clan vassals — government and holdings both
[*] Set succession laws across the realm
[*] Fund vassals so the AI can actually afford to build
[*] Set vassal contracts to maximum tax or levies, reset them to normal, or set
    tax per vassal according to their opinion of you
[*] Realm Loyalty Report — see where everyone stands before you do any of it
[/list]

[b]Protection[/b]
Two character interactions mark anyone as exempt from every mass operation in
the mod. Flag your marshal, your heir's regent, the one duke holding the
eastern border, and stop worrying about which sweep you just fired. There are
also bulk protect decisions for your dynasty, your council, your powerful
vassals, and everyone who currently likes you.

[b]Game rules[/b]
Disloyalty threshold (lenient / moderate / strict), and whether government
conversion respects the cultural innovations vanilla would demand.

[hr][/hr]
[h2]Compatibility[/h2]

[b]Nothing here overwrites a vanilla file.[/b] Everything is additive —
decisions, two character interactions, two game rules, character templates,
script values and localisation. That is why it sits happily in a large
playset; it is developed inside a 200+ mod install.

CK3 1.19. Ironman-safe as far as achievements are concerned is [b]not[/b]
claimed — this is a cheat-adjacent utility mod and should be treated as one.

[b]Administrative government is not supported.[/b] Under Roads to Power admin
rule, counties are held through governors and estates rather than a liege
chain, and the grant and revoke decisions are not admin-aware. The contract
decisions correctly skip admin vassals.

[b]Contract decisions are feudal-only[/b], by necessity rather than laziness.
Obligation levels are defined per contract group: tribal, theocratic,
republican and herder contracts have a single fixed level with nothing to set,
and clan and administrative vassals use different systems entirely. The
decisions tell you how many vassals they will affect and how many they are
skipping.

[hr][/hr]
[h2]Known limitations[/h2]
[list]
[*] The menu is decisions imitating a UI. A proper Scripted GUI is the right
    long-term answer and is on the list.
[*] The ten non-English localisation files carry English text, not
    translations. Real translations are very welcome.
[*] Mass-converting government resets succession law for everyone affected.
    This is in the decision descriptions, but it bears repeating.
[/list]

[hr][/hr]
[h2]Credit[/h2]

Original mod by The Big Bad Wolf —
[url=https://steamcommunity.com/sharedfiles/filedetails/?id=2453359354]Advanced Vassal Manager[/url].
Continued with the author's explicit blessing, quoted above.

---

## CHANGE NOTE for the 2.4 update

[h1]2.4 — Contract fixes, loyalty reporting[/h1]

[b]Two bugs fixed, both of which had been silently doing nothing.[/b]

The contract decisions were calling feudal obligation types on every direct
vassal. Those types only exist in the feudal contract group — tribal,
theocratic, republican and herder contracts define a single fixed level, and
clan and administrative vassals use different systems. Both decisions are now
correctly gated, and tell you how many vassals they affect and how many they
skip.

Script values in tooltips used the wrong data promote and had never displayed a
number since 2.2. The domain and vassal limit headroom warnings and the revoke
counts now actually show figures.

[b]New[/b]
[list]
[*] [b]Reset All Vassal Contracts to Normal[/b] — the missing counterpart to the
    maximum sweeps. The vanilla contract screen will not lower an obligation
    past your crown authority, so maximum tax used to be a one-way door.
[*] [b]Set Vassal Taxes by Loyalty[/b] — one pass, tax level chosen per vassal
    from their opinion. Takes most from those who can absorb it and eases off
    the ones already near revolt.
[*] [b]Realm Loyalty Report[/b] — changes nothing, reports everything: vassal
    counts by opinion band, how many are protected, and how many powerful
    vassals are unhappy. That last number is the one that predicts a civil war.
[*] [b]Protect All Powerful Vassals[/b] and [b]Protect All Content Vassals[/b].
[/list]

All seven new decisions are in the Miscellaneous submenu, and all ten stub
languages have been updated.
