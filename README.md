# Data Mining - ITC

A python script to scrape data from the [WhoScored](https://whoscored.com).
It scrapes data from all of the top leagues such as the league table, next matches,
match statistics and players statistics for each match. 

## Installation

Install requirements

```bash
pip install -r requirements.txt
```

You need to download [chromedriver](https://chromedriver.chromium.org/downloads) of the same version of the 
Google Chrome browser installed in your machine. 

## Usage

The usage is the following.

    app.py [-h] [--seed] [--populate]
                  [--league {Premier League,Serie A,LaLiga,Bundesliga,Ligue 1,Liga NOS,Eredivisie,Premier League,Brasileirão,Major League Soccer,Super Lig,Championship,Premiership,League One,League Two,Superliga,Jupiler Pro League,Super league,Bundesliga II,Champions League,Europa League,UEFA Nations League A}]
                  [--match MATCH] [--stat] [--all] [--daterange DATERANGE]

Some example executions:

    python app.py --all
    python app.py --league "Serie A" --match
    python app.py --league "Serie A" --match --stat
    python app.py --league "Serie A" --daterange 01/11/2020
    python app.py --match --stat
    python app.py --match
    
-   `--all`  will get all matches of all leagues.
-   `--league`  specifies a certain league.
-   `--match` 	specifies a match. If the league argument is added, it will get all matches within a league.
-   `--stat`  will get match statistics. The match argument is needed.
-   `--daterange`  specifies a start date for scraping. The end date is always the current date.



## Contributing
Please refer to contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

1. Fork the repo on GitHub
2. Clone the project to your own machine
3. Commit changes to your own branch
4. Push your work back up to your fork
5. Submit a Pull request so that we can review your changes

 
## Team 
 
[![danielsiles](https://avatars2.githubusercontent.com/u/7890950?s=400&v=4)](https://github.com/danielsiles)  | [![AlxZed](https://avatars1.githubusercontent.com/u/34654828?s=400&u=12ecef205a171fbf8bb32342ebbfce94345e9a39&v=4)](https://github.com/AlxZed)
---|---
[Daniel Siles](https://github.com/danielsiles) | [Alex Zabbal](https://github.com/AlxZed)
