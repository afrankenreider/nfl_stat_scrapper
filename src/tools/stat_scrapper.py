import time
import pandas as pd

# from src.tools.utils import create_webdriver
from utils import create_webdriver
from xpath_links import xpaths
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# dataframes
PLAYER_NAMES_DF = pd.DataFrame(columns=["player"])


class NFLStatScrapper:
    def __init__(self):
        self.nfl_url = "https://www.espn.com/nfl/stats"
        self.driver = create_webdriver()

    def open_stats(self, stat_category, table_rows, table_cols, player_names_df):
        self.driver.get(self.nfl_url)
        try:
            # make sure stat title is visible before continuing
            stat_title = self.driver.find_element_by_xpath(
                '//*[@id="fittPageContainer"]/div[3]/div/div/section[1]/div/div[1]/h1'
            ).text

            if "NFL Stat Leaders" in stat_title:
                print("Calling NFL stat page successful")

                try:
                    # click complete leaders
                    # specify which category we are scrapping with stat_category
                    complete_stats = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, stat_category))
                    )

                    complete_stats.click()
                    time.sleep(5)

                    self.driver.find_element_by_xpath(
                        '//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/a'
                    ).click()

                    rows = 1 + len(self.driver.find_elements_by_xpath(table_rows))

                    cols = len(self.driver.find_elements_by_xpath(table_cols))

                    df = player_names_df
                    print("find values")
                    time.sleep(2)

                    for r in range(1, rows + 1):
                        for p in range(1, cols + 1):

                            # get player names
                            value = self.driver.find_element_by_xpath(
                                table_rows + "[" + str(r) + "]/td[" + str(p) + "]"
                            ).text

                            if value.isdigit() == True:
                                pass
                            else:
                                df = df.append({"player": value}, ignore_index=True)

                        # print()

                    print(df)
                except Exception as e:
                    print(f"Passing stats failed: {e}")

            else:
                print("Driver could not find stat page")
        except Exception as e:
            print(f"Stat scrapper failed: {e}")


def test_nfl_open():
    nfl_page = NFLStatScrapper()

    # scrape passing stats
    nfl_page.open_stats(
        xpaths.PASSING_CATEGORY,
        xpaths.PASSING_ROWS,
        xpaths.PASSING_COLS,
        PLAYER_NAMES_DF,
    )


test_nfl_open()
