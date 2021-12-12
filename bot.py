import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
from pages import LoginPage, StartPage, ProfilePage


class WebDriver:

    def __init__(self):
        load_dotenv()
        self.url = "https://www.instagram.com/"
        self.options = Options()
        self.options.binary_location = os.getenv("PATH_TO_FIREFOX")
        self.driver = webdriver.Firefox(options=self.options, executable_path=os.getenv("PATH_TO_GECKO"))

    def start(self, username, password, profile_name):  # Passed the URL as a variable
        try:
            # Login on Login Page
            login_page = LoginPage(self.driver, self.url)
            self.driver = login_page.login(username, password)
            # Search Profile on feedpage
            start_page = StartPage(self.driver, self.url)
            self.driver = start_page.search_profile(profile_name)
            # get posts of profile and like images
            profile_page = ProfilePage(self.driver, self.url)
            profile_page.get_posts(profile_name)
            self.driver.close()
        except Exception as e:
            print("e", e)
            self.driver.quit()
            return e


if __name__ == "__main__":
    load_dotenv()
    driver = WebDriver()
    USERNAME = os.getenv("USER_NAME")
    PASSWORD = os.getenv("PASSWORD")
    PROFILE_NAME = os.getenv("PROFILE_NAME")
    driver.start(USERNAME, PASSWORD, PROFILE_NAME)
