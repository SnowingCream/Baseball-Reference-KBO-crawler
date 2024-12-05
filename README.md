# KBO crawler

### Moviation
Baseball Reference recently added a section for KBO (Korea Baseball Organization) players (https://www.baseball-reference.com/register/korean-baseball-league-stats.shtml). While it contains a noticeable amount of players (3405 players as of 12/04/2024), Its accessbility is not very practical, since there is no standard of English notation for those players' Korean names.

![BR STATUS 1](image/BR_status1.png?raw=true)
![BR STATUS 2](image/BR_status2.png?raw=true)


### Goal
The goal of this project was to provide the connection between Baseball Reference and Statiz (https://statiz.sporki.com/), which is a sabermetrics website for KBO. It will help those who know Korean access the player's data in Baseball Reference with the Korean name, and those who found Korean player's record in Baseball Reference can get the player's game in Korean.

### How
This projects craweled all KBO player's data from both sides. Each website's data is stored in a csv file. Starting point of crawling for websites are:
- Baseball Reference: https://www.baseball-reference.com/register/league.cgi?code=KBO&class=Fgn
- Statiz: https://statiz.sporki.com/team/

Then, those csv tables are merged, based on the player's name and birthday. Since there is no standard for 1-to-1 Korean character translation into English, some generalization and manipulation for player's English names are applied (the original data is still remained in the original column).

### What & Where
- data(repo): contains all csv files.
    - br_player.csv: crawled players data from Baseball Reference
    - br_team_year.csv: crawled team summary data from Baseball Reference
    - st_player.csv: crawled players data from Statiz
    - merged.csv: merged output of br_player and st_player
    - left_off.csv: the rest of st_player after merging. This is because Statiz has more players than Baseball Reference
- image(repo): contains screenshots for README.md (you will not need these).
- script(repo): contains codes for crawling and merging.
    - br_player.ipynb: crawling players' data from Baseball Reference
    - br_team_year.ipynb: crawling teams' data from Baseball Reference
    - st_player.ipynb: crawling players' data from Statiz
    - mapping.ipynb: merging br_player and st_player.
    - helper(repo): python files that contains helper functions.
        - df_handler.py: data manipulation functions for merging
        - ref_dict.py: dictionaries for data manipulation
        - session.py: web crawler class
        - url_parser.py: url processing helper for web crawling


