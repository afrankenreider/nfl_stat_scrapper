import logging
import pandas as pd

from stat_scrapper import NFLStatScrapper


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


if __name__ == "__main__":
    run_stat_scrapper()