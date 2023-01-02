# nfl_stat_scrapper
====================================

Automatically scrape statistics for the NFL using Selenium and Pandas. 
## Requirements

* Python
* Docker

## Creating Selenium grid
* `docker pull selenium/standalone-chrome`
* `docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome`

## Run commands

| Command    | Description                                                |
|-----------------|-------------------------------------------------------|
| `docker-compose up -d --build` | Build and run script                   |
| `docker-compose down`     | Bring application down                      |

