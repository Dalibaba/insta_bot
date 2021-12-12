from abc import ABC
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re

class Page(ABC):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url


class LoginPage(Page):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def login(self, username, password):
        self.browser.get(self.url)
        self.browser.implicitly_wait(2)
        xpath = "//button[text()='Accept All']"
        cookie_link = self.browser.find_element(By.XPATH, xpath)
        cookie_link.click()
        self.browser.implicitly_wait(3)

        username_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        sleep(2)
        password_input.submit()
        # return page object for the new page
        return self.browser


class StartPage(Page):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def search_profile(self, profile_name):
        # click away pop up questions about login and notifications
        sleep(3)
        button_not_now = self.browser.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
        button_not_now[0].click()
        sleep(1)
        button_not_now = self.browser.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
        button_not_now[0].click()
        sleep(1)
        # go to profile url
        url_profile = self.url + profile_name
        self.browser.get(url_profile)

        sleep(2)
        return self.browser


class ProfilePage(Page):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def get_posts(self, profile_name):
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        all_post_urls = []
        # get all post urls
        # TODO Scroll down page to get all posts of a user
        for a_tag in soup.findAll('a', href=True):
            href = a_tag["href"]
            char_count = href.count('/')
            if char_count == 3:
                if href[1] == "p":
                    all_post_urls.append(href)

        print("anzahl posts:", len(all_post_urls))
        for post_url in all_post_urls:
            url = self.url + post_url
            self.like_image(url)

        return self.browser

    def like_image(self, url):
        self.browser.get(url)
        sleep(2)
        # check if post was already liked (aria label is Like or Unlike
        # TODO condition not correct, check color of all found svg elements
        svg_like = self.browser.find_elements_by_xpath("//*[name()='svg'][@aria-label='Like']")
        if len(svg_like) > 0:
            color = svg_like[0].value_of_css_property('background-color')
            # click on like if not already liked
            xpath = "//*[@class='fr66n']"
            like_button = self.browser.find_element(By.XPATH, xpath)
            like_button.click()
            print("liked")
            #print(like_button)
