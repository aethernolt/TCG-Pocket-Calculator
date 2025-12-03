# TCG Pocket Calculator
Personal application for processing statistics based on a card collection in Pokémon TCG Pocket. Displays card totals, rarity distribution, ideal next pack for highest chance of new card, mission progress, etc. Built to interact with a local Postgres server. Additional thanks to the [Sun Valley ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme) for easy UI theming.

### Copyright Information
All information (both graphical and literal) presented about Pokémon Trading Card Game Pocket is the sole copyright of The Pokémon Company, Creatures Inc., and/or DeNA Co., Ltd. Card images are not uploaded with the application for this reason and are to be stored in the client side assets folder.

### Reprints
Unfortunately with the release of a host of reprints in Deluxe Pack: ex, it is impossible for a user to determine client side how many copies of a reprinted card they have pulled from a specific set. Thus, dex information will be inaccurate, since in game dex entries only update for cards pulled from that set (until some time in summer 2026) and we lack an API/other direct determiner of source. For this reason, reprinted card totals are linked together just as they appear in the game.

### JSON Key
Underlying card data (*not* owned amounts) is recorded for editing ease in JSON files with information translated as below.

- Cards in regular sets are recorded as `"name": [#, rarity, card type, [booster pack #s]]`
- Cards in promo sets are recorded as `"name": [#, acquiration method, card type]`

Pokémon will also have their type be the last value in the array keys. Booster pack #s are defined at the start of the JSON file for each set.

| Key | Rarity | Method | Card Type | Type |
|----:|:------:|:------:|:---------:|:----:|
|    1|♢|Shop|Pokémon|Grass|
|    2|♢♢|Premium|Item|Fire|
|    3|♢♢♢|Wonder Pick|Supporter|Water|
|    4|♢♢♢♢|Drop Event|Tool|Lightning|
|    5|☆|Mission||Fighting|
|    6|☆☆|Misc||Psychic|
|    7|☆☆☆|||Coloroless|
|    8|#|||Darkness|
|    9|##|||Metal|
|   10|🜲|||Dragon|
|   11||||Fairy|

*Under rarity, the hash/pound sign represents shinies*