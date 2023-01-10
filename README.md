# nfl_stat_scrapper
====================================

Automatically scrape statistics for the NFL using Selenium and Pandas. 
## Requirements

* Python
* Docker

## Run commands
Running the below commands will create a standalone Selenium grid where web scrapping commands will be executed. 
Once the grid image and container have been created, navigate to http://localhost:4444/ to view the running sessions (default password is "secret").
The apscheduler is set to run this script daily at 8:00 UTC.

| Command                        | Description                            |
|--------------------------------|----------------------------------------|
| `docker-compose build`         | Build docker image                     |
| `docker-compose up`            | Run application                        |
| `docker-compose down`          | Bring application down                 |

