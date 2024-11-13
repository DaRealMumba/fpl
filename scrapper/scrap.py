import random
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# proxies = ["130.61.171.71:80", "103.148.130.231:8080", "109.236.83.153:8888"]

# proxy = "130.61.171.71:80"

# proxy = random.choice(proxies)

url_stats = "https://fbref.com/en/comps/9/stats/Premier-League-Stats"
element_squad_stats = "//*stats_squads_standard_for"
squad_stats_path = "/Users/mumin/Desktop/DS/personal/fpl/data/pl_team_stats.csv"

url_table = "https://fbref.com/en/comps/9/Premier-League-Stats"
element_table_stats = "//*[@id='results2024-202591_overall']"
table_path = "/Users/mumin/Desktop/DS/personal/fpl/data/pl_table.csv"


service = Service(
    executable_path="/Users/mumin/Desktop/DS/personal/fpl/scrapper/chromedriver.exec"
)

# chrome_options = Options()
# chrome_options.add_argument(f"--proxy-server={proxy}")
# chrome_options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# )

driver = webdriver.Chrome(service=service)

driver.get(url_table)

time.sleep(5)


table = pd.read_html(
    driver.find_element(By.XPATH, element_table_stats).get_attribute("outerHTML")
)[0]

table.to_csv(table_path, index=False)

driver.quit()
