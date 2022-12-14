import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TVExtractor:
    def __init__(self, tickers, username, password, download_path, layout_id):

        self.tickers = tickers
        self.username = username
        self.password = password
        self.download_path = download_path
        self.layout_id = layout_id
        self.url = 'https://www.tradingview.com'
        self.completed_tickers = []

    def init_driver(self):

        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument(r"download.default_directory={}".format(self.download_path))
            driver = webdriver.Chrome("C:/\bin/\chromedriver", options=options)

            return driver
        except Exception as e:
            print(e)
            return None

    def authenticate(self, driver):

        try:
            driver.get(self.url)
        except Exception as e:
            print(e)
            return False

        time.sleep(3)

        try:
            auth_person = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div[3]/button[1]')
            auth_person.click()
        except Exception as e:
            print(e)
            return False

        time.sleep(5)

        try:
            sign_up_form = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div/button[1]/span/span')
            sign_up_form.click()
        except Exception as e:
            print(e)
            return False

        time.sleep(5)

        try:
            sign_up_form = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span')
            sign_up_form.click()
        except Exception as e:
            print(e)
            return False

        time.sleep(5)

        try:
            username_field = driver.find_element(By.NAME, 'username')
            username_field.send_keys(self.username)

            password_field = driver.find_element(By.NAME, 'password')
            password_field.send_keys(self.password)

            password_field.submit()

            time.sleep(2)
        except Exception as e:
            print(e)
            return False

        return True

    def pull_data(self, driver):

        try:
            driver.get('{}/chart/{}/'.format(self.url, self.layout_id))
        except Exception as e:
            print(e)
            return False

        time.sleep(5)

        for ticker in self.tickers:

            if ticker in self.completed_tickers:
                continue

            time.sleep(5)

            try:
                search_btn = driver.find_element(By.ID, "header-toolbar-symbol-search")
                search_btn.click()
            except Exception as e:
                print(e)
                return False

            time.sleep(2)

            try:
                search_box = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/div/div[2]/div/div[2]/div[1]/input')
                search_box.send_keys(ticker)
                search_box.send_keys(Keys.RETURN)
            except Exception as e:
                print(e)
                return False

            time.sleep(5)

            action = ActionChains(driver)
            action.send_keys('5')
            action.key_down(Keys.ENTER)
            action.key_up(Keys.ENTER)
            action.perform()

            time.sleep(3)

            action.key_down(Keys.ALT)
            action.send_keys('r')
            action.key_up(Keys.ALT)
            action.perform()

            for _ in range(14):
                time.sleep(2)

                action.key_down(Keys.CONTROL)
                action.send_keys(Keys.ARROW_DOWN)
                action.key_up(Keys.CONTROL)
                action.perform()

            time.sleep(5)

            for _ in range(30):
                time.sleep(1)

                action.key_down(Keys.CONTROL)
                action.send_keys(Keys.ARROW_LEFT)
                action.key_up(Keys.CONTROL)
                action.perform()

            time.sleep(5)

            try:
                menu = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div/div[1]/div[1]/div/div/div/div/div[14]/div[2]/div/div[2]/div')
                menu.click()
            except Exception as e:
                print(e)
                return False

            time.sleep(3)

            try:
                exporter = driver.find_element(By.XPATH, '//*[@id="overlap-manager-root"]/div/span/div[1]/div/div/div[4]')
                exporter.click()
            except Exception as e:
                print(e)
                return False

            time.sleep(7) 

            action.send_keys(Keys.ENTER)
            action.perform()

            time.sleep(5)

            action.send_keys(Keys.ENTER)
            action.perform()

            time.sleep(3)
            
            self.completed_tickers.append(ticker)

        return True

    def deinit(self, driver):
        driver.quit()
