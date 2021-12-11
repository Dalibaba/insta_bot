import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv

from pages import LoginPage, StartPage, ProfilePage

load_dotenv()
USERNAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
PROFILE_NAME = os.getenv("PROFILE_NAME")

load_dotenv()
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(options=options, executable_path=r"C:\Users\linke\Projekte\insta_bot/geckodriver.exe")

driver.implicitly_wait(2)
# Login on Login Page
login_page = LoginPage(driver)
driver = login_page.login(USERNAME, PASSWORD)
# Search Profile on feedpage
start_page = StartPage(driver)
driver = start_page.search_profile(PROFILE_NAME)
# get posts of profile and like images
profile_page = ProfilePage(driver)
profile_page.get_posts(PROFILE_NAME)


print("driver returned go to sleep")
sleep(5)
#driver.close()