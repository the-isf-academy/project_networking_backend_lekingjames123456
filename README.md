# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
This API is a player stat tracker for basketball, where you can input statistics from games and view other people's stats

### Model

### Endpoints

*Replace this with a guide to your endpoints and model. You can write a Markdown chart [here](https://www.tablesgenerator.com/markdown_tables)*

| **Parameter**         | **Description**                                            | **Payload**                                                                                                                                                                                                                                                                                                                     | **Example**                                                                               |
| **Parameter**         | **HTTP Method** | **Description**                                            | **Payload**                                                                                                                                                                                                                                                                                                                     | **Example**                                                                               |
|-----------------------|-----------------|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| input_stats           | post            | inputs stats of player after a game                        | player - the player you want to input the stats for points - their points assists - their assists rebounds - their rebounds blocks - their blocks steals - their steals                                                                                                                                                         | player - lebron points - 20 assists - 2 rebounds - 4 blocks - 4 steals - 2                |
| input_stats_advanced  | post            | inputs the advanced stats of a player after a game         | player - the player you want to input advanced stats for shots taken - the amount of shots taken by the player threes taken - the amount of three pointers taken by the player +- = the player's plus minus rating shots made - the amount of shots the player made threes made - the amount of three pointers the player made  | player - lebron shots taken - 10 threes taken - 3 +- = +13 shots made - 7 threes made - 2 |
| new_player            | post            | adds a new player into the database                        | player name - the player's name player position - the player's position                                                                                                                                                                                                                                                         | player name - kanye player position - point guard                                         |
| delete_player         | post            | deletes a player/sets inactive in the database             | player name - the player's name                                                                                                                                                                                                                                                                                                 | player name - kanye                                                                       |
| stat_leaders          | get             | shows you who has the most of each stat                    | none needed                                                                                                                                                                                                                                                                                                                     | none                                                                                      |
| stats_player          | get             | tells you the individual stats of the player you choose    | player - the player's name                                                                                                                                                                                                                                                                                                      | player - kendrick                                                                         |
| players               | get             | gives you every player in the database, sorted by position | none needed                                                                                                                                                                                                                                                                                                                     | none                                                                                      |
| stats_player_advanced | get             | tells you the advanced stats of the player you choose      | player - the player's name                                                                                                                                                                                                                                                                                                      | player name - cardi b                                                                     |
## Setup
poetry shell
poetry update
banjo --debug
### Contents

Here's what is included:
- `\app`
    - `models.py` - `Player` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/player/)



