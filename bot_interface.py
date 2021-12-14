# Interface between GUI and Bot
from bot import WebDriver


class BotInterface:
    def __init__(self, username, password, target_profile_name, update_liked_images):
        self.username = username
        self.password = password
        self.target_profile_name = target_profile_name
        self.bot = WebDriver()
        self.update_liked_images = update_liked_images

    def start(self):
        amount_liked_images = self.bot.start(self.username, self.password, self.target_profile_name,
                                             self.update_liked_images)

        return amount_liked_images
