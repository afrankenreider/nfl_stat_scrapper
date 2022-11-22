import time
import pandas as pd

from tools.utils import create_webdriver
from tools.xpath_links import xpaths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NFLStatScrapper:
    """Driver and web scraping class."""

    def __init__(self):
        """Init."""
        self.nfl_url = "https://www.espn.com/nfl/stats"
        self.driver = create_webdriver()

    def open_stats(self):
        """Open correct stats page."""
        self.driver.get(self.nfl_url)
        try:
            # make sure stat title is visible before continuing
            stat_title = self.driver.find_element_by_xpath(
                '//*[@id="fittPageContainer"]/div[3]/div/div/section[1]/div/div[1]/h1'
            ).text

        except Exception as e:
            print(f"Stat scrapper failed: {e}")
            stat_title is None

        return stat_title

    def scrape_stats(self, stat_category, table_rows, table_cols):
        """Get table rows and columns based on xpath."""
        stat_title = self.open_stats()
        if "NFL Stat Leaders" in stat_title:

            try:
                # click complete leaders
                # specify which category we are scrapping with stat_category
                complete_stats = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, stat_category))
                )

                complete_stats.click()

                self.driver.find_element_by_xpath(
                    '//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/a'
                ).click()

                rows = len(self.driver.find_elements_by_xpath(table_rows))

                cols = len(self.driver.find_elements_by_xpath(table_cols))
            except Exception as e:
                print(f"Failed to find rows, cols: {e}")
        else:
            print("Driver could not find stat page")

        return rows, cols

    def get_player_names(self):
        """Get player names from table."""
        rows, cols = self.scrape_stats(
            xpaths.PASSING_CATEGORY,
            xpaths.PASSING_ROWS,
            xpaths.PASSING_COLS,
        )

        # cap at top 50 players
        if rows > 50:
            rows = 50

        df = pd.DataFrame(columns=["player"])

        # append values to dataframe
        for r in range(1, rows + 1):
            for p in range(1, cols + 1):

                # get player names
                value = self.driver.find_element_by_xpath(
                    xpaths.PASSING_ROWS + "[" + str(r) + "]/td[" + str(p) + "]"
                ).text

                # ignore the rank from webpage
                if value.isdigit() == True:
                    pass
                else:
                    df = df.append({"player": value}, ignore_index=True)

        return df

    def get_player_data(self):
        """Get player names from table."""
        rows, cols = self.scrape_stats(
            xpaths.PASSING_CATEGORY,
            xpaths.PASSING_STAT_ROWS,
            xpaths.PASSING_STAT_COLS,
        )

        # cap at top 50 players
        if rows > 50:
            rows = 50

        df = pd.DataFrame(
            columns=[
                "position",
                "gp",
                "cmp",
                "att",
                "cmp_percent",
                "yrds",
                "avg",
                "yrds_per_game",
                "lng",
                "td",
                "int",
                "sack",
                "syl",
                "qbr",
                "rtg",
            ]
        )

        # append values to dataframe
        for r in range(1, rows + 1):
            value_lst = []
            for p in range(1, cols + 1):

                # get player stats
                value = self.driver.find_element_by_xpath(
                    xpaths.PASSING_STAT_ROWS + "[" + str(r) + "]/td[" + str(p) + "]"
                ).text

                value_lst.append(value)
            # append to dataframe
            df.loc[len(df)] = value_lst

        return df
