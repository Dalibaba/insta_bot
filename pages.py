from time import sleep

from selenium.webdriver import Keys, ActionChains
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
        password_input.submit()
        sleep(3)
        # return page object for the new page
        return self.browser


class StartPage:
    def __init__(self, browser):
        self.browser = browser

    def search_profile(self, profile_name):
        # click away pop up questions about login and notifications
        sleep(1)
        button_not_now = self.browser.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
        button_not_now[0].click()
        sleep(1)
        button_not_now = self.browser.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
        button_not_now[0].click()
        sleep(1)

        # search_input = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
        # search_input.send_keys(profile_name)
        # sleep(1)
        # #search_input.submit()
        # #search_input.click()
        # search_input.send_keys(Keys.RETURN);
        # search_input.send_keys(Keys.RETURN);
        url = 'https://www.instagram.com/' + profile_name
        self.browser.get(url)

        sleep(2)
        return self.browser


class ProfilePage:
    def __init__(self, browser):
        self.browser = browser

    def get_posts(self, profile_name):
        # click away pop up questions about login and notifications
        sleep(1)
        button_not_now = self.browser.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
        button_not_now[0].click()
        sleep(1)
        button_not_now = self.browser.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
        button_not_now[0].click()
        sleep(1)

        search_input = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
        search_input.send_keys(profile_name)
        sleep(1)
        #search_input.submit()
        #search_input.click()
        search_input.send_keys(Keys.RETURN);
        search_input.send_keys(Keys.RETURN);

        sleep(2)
        return self.browser