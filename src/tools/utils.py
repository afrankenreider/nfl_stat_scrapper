from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def create_webdriver(driver=None, headless=True):
    """Creates a general webdriver session, sets default wait time to 90 sec"""

    options = Options()
    options.headless = headless
    options.add_argument("--incognito")
    options.add_experimental_option("w3c", False)
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--whitelisted-ips=""')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(90)
    driver.get("https://www.google.com")

    return driver
