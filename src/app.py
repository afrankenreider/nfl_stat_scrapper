import logging
import pandas as pd

from stat_scrapper import NFLStatScrapper


def run_stat_scrapper():
    """Run stat scrapper script."""
    nfl_page = NFLStatScrapper()

    # scrape passing stats
    player_names = nfl_page.get_player_names()
    player_stats = nfl_page.get_player_data()

    stats = pd.concat([player_names, player_stats], axis=1)
    print(stats.head(5))
    logging.info("NFL stat scrapping was successful!")


if __name__ == "__main__":
    run_stat_scrapper()
