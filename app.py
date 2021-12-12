from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from bot_interface import BotInterface


class Instagram_Bot(App):
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
            #padding_y=(20, 20),
            size_hint=(1, 0.5),
            text="username",
            background_color=(193,53,132,0.5))

        self.password_input = TextInput(
            multiline=False,
            size_hint=(1, 0.5),
            text="password",
            background_color=(193,53,132,0.5))
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

        return self.window

    def start_button_clicked(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        profile_name = self.profile_input.text
        bot = BotInterface(username, password, profile_name)
        bot.start()
        print("start bot")


if __name__ == "__main__":
    Instagram_Bot().run()
