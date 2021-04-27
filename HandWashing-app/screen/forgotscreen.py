from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
forgot_kv = """
<ForgotScreen>
    name: "forgot"
    md_bg_color: 1, 1, 1, 1
    FloatLayout:
        MDCard:
            elevation: 11
            border_radius: 70
            radius: [70,]
            size_hint: 0.8, 0.1
            pos_hint: {"center_x": 0.5, "center_y": 0.9}
            FloatLayout:
                MDLabel:
                    text: "HAND WASHING RECOGNITION"
                    halign: "center"
                    font_size: "13dp"
                    pos_hint: {"center_x": 0.42, "center_y": 0.7}
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                MDLabel:
                    text: "AI FOR THE BETTER WORLD"
                    halign: "center"
                    font_size: "12dp"
                    pos_hint: {"center_x": 0.42, "center_y": 0.35}
                Image:
                    source: "source/camera.jpg"
                    size_hint: 0.83, 0.83
                    pos_hint: {"center_x": 0.85, "center_y": 0.53}
        MDLabel:
            halign: "center"
            text: "RESET PASSWORD"
            font_size: "30dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
        MDTextFieldRound:
            hint_text: "Enter Your Email Address"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            icon_right: "account"
            pos_hint: {"center_x": 0.5, "center_y": 0.65}
            size_hint: 0.75, 0.06
            normal_color: 1, 1, 1, 1
            color_active: 1, 1, 1, 1
        

        MDFillRoundFlatButton:
            pos_hint: {"center_x": 0.5, "center_y": 0.55}
            text: "RECOVER"
            size_hint : 0.85, 0.05
            

        MDLabel:
            halign: "center"
            text: "Back to"
            pos_hint: {"center_x": 0.43, "center_y": 0.41}
        MDFlatButton
            pos_hint: {"center_x": 0.559 ,"center_y": 0.41}
            text: "Login"
            text_color: app.theme_cls.primary_color
            on_release:
                root.manager.current = "login"
                root.manager.transition.direction = "right"


        MDLabel:
            text: "Don't have an account?"
            pos_hint: {"center_x": 0.7, "center_y": 0.27}
        MDFlatButton
            pos_hint: {"center_x": 0.72 ,"center_y": 0.27}
            text: "Sign up"
            text_color: app.theme_cls.primary_color
            on_release:
                root.manager.current = "signup"
                root.manager.transition.direction = "right"


        MDIconButton:
            icon: "twitter"
            pos_hint: {"center_x": 0.4 ,"center_y": 0.15}
        MDIconButton:
            icon: "facebook"
            pos_hint: {"center_x": 0.5 ,"center_y": 0.15}
        MDIconButton:
            icon: "instagram"
            pos_hint: {"center_x": 0.6 ,"center_y": 0.15}
        MDLabel:
            halign: "center"
            text: "VAS Coporation 2020"
            pos_hint: {"center_x": 0.5, "center_y": 0.05}
"""


class ForgotScreen(MDScreen):
    Builder.load_string(forgot_kv)