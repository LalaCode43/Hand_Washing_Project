from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
introduce_kv = """
<IntroduceScreen>:
    name: "introduce"
    md_bg_color: 1, 1, 1, 1
    MDLabel:
        halign: "center"
        text: "Hand Washing\\nRecognition"
        theme_text_color: "Custom"
        font_size: "30sp"
        text_color: app.theme_cls.primary_dark
        pos_hint: {"center_x": 0.5, "center_y":0.9}
    MDLabel:
        halign: "center"
        text: "Hand Washing\\nRecognition"
        theme_text_color: "Custom"
        font_size: "30sp"
        text_color: app.theme_cls.primary_dark
        pos_hint: {"center_x": 0.5, "center_y":0.9}
    MDFillRoundFlatButton:
        text: "GET STARTED"
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        size_hint : 0.85, 0.05
        on_release:
            root.manager.current = "home"
            root.manager.transition.direction = "left"

    MDLabel:
        halign: "center"
        text: "Intelligent Creative Partner\\nWelcome"
        theme_text_color: "Custom"

        font_size: "17dp"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x": 0.5, "center_y":0.8}

    MDLabel:
        halign: "center"
        text: "AI Remote For Better Health"
        theme_text_color: "Custom"
        font_size: "17dp"
        text_color: app.theme_cls.primary_light
        pos_hint: {"center_x": 0.5, "center_y":0.65}

    Image:
        source: "source/camera.jpg"
        size_hint: 0.15, 0.15
        pos_hint: {"center_x": 0.5, "center_y": 0.72}
    Image:
        source: "source/robot_2.jpg"
        pos_hint: {"center_y": 0.37}
"""


class IntroduceScreen(MDScreen):
    Builder.load_string(introduce_kv)
