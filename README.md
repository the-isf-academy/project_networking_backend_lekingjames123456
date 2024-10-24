# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
This API is a player stat tracker for basketball, where you can input statistics from games and view other people's stats

### Model
Player: The player is someone where you can input a player and it will give you their statistics and information

| **Parameter**        | **HTTP Method** | **Description**                                            | **Payload**                                                                                                                                                                                                                                                                                                                        | **Example**                                                                                  |
|----------------------|-----------------|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| input_stats          | post            | inputs stats of player after a game                        | player - the player you want to input the stats for points - their points assists - their assists rebounds - their rebounds blocks - their blocks steals - their steals                                                                                                                                                            | player - lebron points - 20 assists - 2 rebounds - 4 blocks - 4 steals - 2                   |
| input_stats_advanced | post            | inputs the advanced stats of a player after a game         | player - the player you want to input advanced stats for shotstaken - the amount of shots taken by the player threestaken - the amount of three pointers taken by the player plusminus = the player's plus minus rating shotsmade - the amount of shots the player made threesmade - the amount of three pointers the player made  | player - lebron shotstaken - 10 threestaken - 3 plusminus = +13 shotsmade - 7 threesmade - 2 |
| new                  | post            | adds a new player into the database                        | player - the player's name player - the player's position                                                                                                                                                                                                                                                                          | player - kanye player - point guard                                                          |
| set_inactive         | post            | deletes a player/sets inactive in the database             | player - the player's name                                                                                                                                                                                                                                                                                                         | player - kanye                                                                               |
| set_active           | post            | restores a player after the player has been set inactive   | player - the player's name                                                                                                                                                                                                                                                                                                         | player - kanye                                                                               |
| leaders              | get             | shows you who has the most of each stat                    | none needed                                                                                                                                                                                                                                                                                                                        | none                                                                                         |
| stats                | get             | tells you the individual stats of the player you choose    | player - the player's name                                                                                                                                                                                                                                                                                                         | player - kendrick                                                                            |
| players              | get             | gives you every player in the database, sorted by position | none needed                                                                                                                                                                                                                                                                                                                        | none                                                                                         |
| stats/advanced       | get             | tells you the advanced stats of the player you choose      | player - the player's name                                                                                                                                                                                                                                                                                                         | player - cardi b                                                                             |                                                                  |
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



