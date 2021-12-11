from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def login(self, username, password):
        xpath = "//button[text()='Accept All']"
        cookie_link = self.browser.find_element(By.XPATH, xpath)
        cookie_link.click()
        self.browser.implicitly_wait(2)

        username_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        sleep(2)
        password_input.submit()
        # return page object for the new page
        return self.browser


class StartPage:
    def __init__(self, browser):
        self.browser = browser

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
        url = 'https://www.instagram.com/' + profile_name
        self.browser.get(url)

        sleep(2)
        return self.browser


class ProfilePage:
    def __init__(self, browser):
        self.browser = browser

    def get_posts(self, profile_name):
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        all_post_urls = []
        for a_tag in soup.findAll('a', href=True):
            href = a_tag["href"]
            char_count = href.count('/')
            if char_count == 3:
                if href[1] == "p":
                    all_post_urls.append(href)

        print("anzahl posts:", len(all_post_urls))
        for post_url in all_post_urls:
            url = 'https://www.instagram.com' + post_url
            self.like_image(url)


        # click away pop up questions about login and notifications
        return self.browser

    def like_image(self, url):
        self.browser.get(url)
        sleep(2)
        xpath = "//*[@class='fr66n']"
        like_button = self.browser.find_element(By.XPATH, xpath)
        print(like_button)
        like_button.click()
        sleep(2)
