# Interface between GUI and Bot
from bot import WebDriver


class BotInterface:
    def __init__(self, username, password, target_profile_name):
        self.username = username
        self.password = password
        self.target_profile_name = target_profile_name
        self.bot = WebDriver()

    def start(self):
        self.bot.start(self.username, self.password, self.target_profile_name)
