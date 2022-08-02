import time
import pandas as pd

# from src.tools.utils import create_webdriver
from utils import create_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NFLStatScrapper:
    def __init__(self):
        self.nfl_url = "https://www.espn.com/nfl/stats"
        self.driver = create_webdriver()

    def open_stats(self):
        self.driver.get(self.nfl_url)
        try:
            stat_title = self.driver.find_element_by_xpath(
                '//*[@id="fittPageContainer"]/div[3]/div/div/section[1]/div/div[1]/h1'
            ).text

            if "NFL Stat Leaders" in stat_title:
                print("Calling NFL stat page successful")
            else:
                print("Driver could not find stat page")

            try:
                passing_stats = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[@id="fittPageContainer"]/div[3]/div/div/section[1]/div/div[4]/div[1]/div/div[2]/div/div/div[2]/table/tbody/tr[6]/td/div/a',
                        )
                    )
                )

                passing_stats.click()

                self.driver.find_element_by_xpath(
                    '//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[2]/a'
                ).click()

                rows = 1 + len(
                    self.driver.find_elements_by_xpath(
                        '//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[1]/div/table/tbody/tr'
                    )
                )

                cols = len(
                    self.driver.find_elements_by_xpath(
                        '//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[1]/div/table/thead/tr/th'
                    )
                )

                passing_df = pd.DataFrame(columns=["Player"])

                for r in range(1, rows + 1):
                    for p in range(1, cols + 1):

                        # obtaining the text from each column of the table
                        value = self.driver.find_element_by_xpath(
                            '//*[@id="fittPageContainer"]/div[3]/div/div/section/div/div[4]/div[1]/div/table/tbody/tr['
                            + str(r)
                            + "]/td["
                            + str(p)
                            + "]"
                        ).text

                        if value.isdigit() == True:
                            pass
                        else:
                            passing_df = passing_df.append(
                                {"Player": value}, ignore_index=True
                            )

                    # print()

                print(passing_df)
            except Exception as e:
                print(f"Passing stats failed: {e}")

            time.sleep(5)
        except Exception as e:
            print(f"Stat scrapper failed: {e}")


def test_nfl_open():
    nfl_page = NFLStatScrapper()
    nfl_page.open_stats()


test_nfl_open()
