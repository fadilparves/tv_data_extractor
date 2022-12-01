import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("C:/\bin/\chromedriver", chrome_options=options)
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

time.sleep(5)

timeframe_selector = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[1]/div/div/div/div/div/div[4]')
timeframe_selector.click()

time.sleep(1)

timeframes = driver.find_elements(By.CSS_SELECTOR, 'span.label-RhC5uhZw')
for tfs in timeframes:
    if tfs.text == "5 minutes":
        tfs.click()
        break

time.sleep(3)

for i in range(14):
    time.sleep(2)
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL)
    action.send_keys(Keys.ARROW_DOWN)
    action.key_up(Keys.CONTROL)
    action.perform()

time.sleep(5)

driver.quit()