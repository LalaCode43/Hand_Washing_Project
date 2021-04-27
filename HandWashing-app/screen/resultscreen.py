from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

result_kv = """
<ResultScreen>
    name: "result"
    md_bg_color: 0, 153/255, 204/255, 1
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"top":0.97, "left": 0.95}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1


    MDIconButton:
        icon: "account-circle"
        pos_hint: {"top":0.97, "right": 0.97}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        on_release: root.manager.current = "user"

    MDLabel:
        text: "CONGRATULATION"
        font_size: "30dp"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        pos_hint: {"center_y": 0.7}
    MDLabel:
        text: "Lam nguyen"
        halign: "center"
        pos_hint: {"center_y": 0.64}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDCard:
        md_bg_color: 1, 1, 1, 1
        size_hint: 0.82, 0.11
        pos_hint: {"center_x": 0.5, "center_y": 0.53}
        border_radius: dp(30)
        radius: [dp(20)]
        BoxLayout:
            orientation: "vertical"
            MDLabel:
                halign: "center"
                text: "6789"
                font_size: "20dp"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
            MDLabel:
                halign: "center"
                text: "Total Points"

    MDCard:
        md_bg_color: 1, 1, 1, 1
        size_hint: 1, 0.45
        FloatLayout:
"""


class ResultScreen(MDScreen):
    Builder.load_string(result_kv)

    def back_user(self):
        self.manager.current = "user"
        self.manager.transition.direction = "left"