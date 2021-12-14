from kivy.app import App
from kivy.clock import mainthread
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import threading
import logging
from bot_interface import BotInterface


class BotGui(App):
    def __init__(self):
        super().__init__()
        self.window = GridLayout()

    def build(self):
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.6)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        # add widgets to window

        # image widget
        self.window.add_widget(Image(source="assets/bot.png"))

        # label widget description and login
        self.description = Label(
            text="Instagram-Bot automatically likes posts of certain profile",
            font_size=20,
            color='#e1306c')
        self.login = Label(
            text="Your login data",
            font_size=20,
            color='##833ab4')
        self.window.add_widget(self.description)
        self.window.add_widget(self.login)

        # Login Input
        self.username_input = TextInput(
            multiline=True,
            # padding_y=(20, 20),
            size_hint=(1, 0.5),
            text="username",
            background_color=(193, 53, 132, 0.5))

        self.password_input = TextInput(
            multiline=False,
            size_hint=(1, 0.5),
            text="password",
            background_color=(193, 53, 132, 0.5))
        self.window.add_widget(self.username_input)
        self.window.add_widget(self.password_input)

        # profile label
        self.profile = Label(
            text="Username of target profile",
            font_size=20,
            color='##833ab4')
        self.window.add_widget(self.profile)

        # Profile Input
        self.profile_input = TextInput(
            multiline=False,
            size_hint=(1, 0.5),
            text="username",
            background_color=(193, 53, 132, 0.5)
        )
        self.window.add_widget(self.profile_input)

        # Start Button
        self.button = Button(
            text="START BOT",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#405de6')
        self.button.bind(on_press=self.start_button_clicked)
        self.window.add_widget(self.button)

        # Liked Images
        self.liked_images = Label(
            text="Liked Images: ",
            font_size=20,
            color='##833ab4')
        self.window.add_widget(self.liked_images)

        return self.window

    def start_button_clicked(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        profile_name = self.profile_input.text.strip()
        bot = BotInterface(username, password, profile_name, self.update_liked_images)
        print("start bot")
        # start new thread for bot, preventing to block UI
        bot_thread = threading.Thread(target=bot.start)
        bot_thread.start()

    @mainthread  # kivy performs updates in the UI only on the main thread
    def update_liked_images(self, amount_of_liked_images):
        self.liked_images.text = "Liked Images: " + str(amount_of_liked_images)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main : Start GUI")

    BotGui().run()
