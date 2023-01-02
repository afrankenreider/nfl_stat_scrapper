# nfl_stat_scrapper
====================================

Automatically scrape statistics for the NFL using Selenium and Pandas. 
## Requirements

* Python
* Docker

## Run commands
Running the below commands will create a standalone Selenium grid where web scrapping commands will be executed. 
Once the grid image and container have been created, navigate to http://localhost:4444/ to view the running sessions (default password is "secret").

| Command         | Description                                           |
|-----------------|-------------------------------------------------------|
| `docker-compose up -d --build` | Build and run script                   |
| `docker-compose down`          | Bring application down                 |

