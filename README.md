# nfl_stat_scrapper
====================================

Automatically scrape statistics for the NFL using Selenium and Pandas. 
## Requirements

* Python
* Docker
* Make

## Run commands
Running the below commands will create a standalone Selenium grid where web scrapping commands will be executed. 

Once the grid image and container have been created, navigate to http://localhost:4444/ to view the running sessions (default password is "secret").

The apscheduler is set to run this script daily at 8:00 UTC.

| Command                        | Description                            |
|--------------------------------|----------------------------------------|
| `make up`                      | Build docker image and start services  |
| `make down`                    | Bring application down                 |

