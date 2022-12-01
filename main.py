import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("C:/\bin/\chromedriver", hrome_options=options)  # Optional argument, if not specified will search path.
driver.get('https://www.tradingview.com/chart');

time.sleep(5)

watchlist = driver.find_element(By.XPATH, '/html/body/div[3]/div[6]/div/div[2]/div/div/div/div/div[1]')
watchlist.click()

time.sleep(1)
search_btn = driver.find_element(By.ID, "header-toolbar-symbol-search")
search_btn.click()

time.sleep(2)
search_box = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input')
search_box.send_keys('FCPOG2023')
search_box.send_keys(Keys.RETURN)

time.sleep(2)

timeframe_selector = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div/div[4]')
timeframe_selector.click()

time.sleep(1)

timeframes = driver.find_elements(By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/div[10]/div/span[1]/span')
for tfs in timeframes:
    print(tfs.text)

time.sleep(5)

driver.quit()