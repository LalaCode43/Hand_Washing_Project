from kivy.config import Config
Config.set('graphics', 'width', '365')
Config.set('graphics', 'height', "767")
from kivy.lang import Builder
from kivymd.app import MDApp


class DemoApp(MDApp):

    def build(self):
        help_file = Builder.load_file("main.kv")
        return help_file


if __name__ == "__main__":
    DemoApp().run()
