import logging
import pandas as pd

from apscheduler.schedulers import background
from stat_scrapper import NFLStatScrapper


logging.basicConfig()
scheduler = background.BlockingScheduler()


def run_stat_scrapper():
    """Run stat scrapper script."""
    nfl_page = NFLStatScrapper()

    # scrape passing stats
    player_names = nfl_page.get_player_names()
    print("Player names located!")
    player_stats = nfl_page.get_player_data()
    print("Player data located!")

    # combine player names and player stats
    # these are two separate tables on ESPN
    stats = pd.concat([player_names, player_stats], axis=1)
    print(stats.head(5))
    logging.info("NFL stat scrapping was successful!")

    # close and quit chrome driver
    nfl_page.tear_down_driver()


scheduler.add_job(run_stat_scrapper, "cron", day_of_week="mon-fri", hour=8, minute=30)
scheduler.start()
