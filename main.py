from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

import os
from dotenv import load_dotenv

load_dotenv()

MAIL = os.getenv("TWITTER_EMAIL")
PASSWORD = os.getenv("TWITTER_PASSWORD")
NUMBER = os.getenv("PHONE_NUMBER")
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(2)
        # clicking on GO for internet speed test
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(40)
        # finding the download and upload speed
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(4)
        self.driver.maximize_window()
        # field for mail Id
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(MAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(4)
        try:
            # field for phone number
            number = self.driver.find_element(By.NAME, 'text')
            number.send_keys(NUMBER)
            number.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass
        time.sleep(4)
        # field for password
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(4)
        # field for tweet
        self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block").send_keys(
            f"Hey internet provider why my internet has {bot.down} Download and {bot.up} Upload when I pay for {PROMISED_DOWN} Download and {PROMISED_UP} Upload ?")
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
        time.sleep(10)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
print(f"download speed-----{bot.down}")
print(f"upload speed----{bot.up}")

if float(bot.up) < PROMISED_UP or float(bot.down) < PROMISED_DOWN:
    bot.tweet_at_provider()
