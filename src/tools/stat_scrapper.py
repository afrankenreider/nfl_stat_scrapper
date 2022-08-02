import time

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
            except:
                print("fail")

            time.sleep(5)
        except Exception as e:
            print(f"Stat scrapper failed: {e}")


def test_nfl_open():
    nfl_page = NFLStatScrapper()
    nfl_page.open_stats()


test_nfl_open()
