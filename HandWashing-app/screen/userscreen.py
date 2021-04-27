from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

user_kv = """
<UserScreen>:
    name: "user"
    md_bg_color: 0, 153/255, 204/255, 1
    FloatLayout:
        MDLabel:
            text: "Total Activitives"
            halign: "center"
            pos_hint: {"center_x": 0.21, "center_y": 0.73}

        MDCard:
            md_bg_color: 1, 1, 1, 1
            elevation: 0
            border_radius: dp(30)
            radius: [dp(5)]
            size_hint: 0.12, 0.06
            pos_hint: {"center_x": 0.1, "center_y": 0.86}
            FloatLayout:
                MDIconButton:
                    icon: "arrange-send-backward"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDCard: 
            md_bg_color: 1, 1, 1, 1
            elevation: 0
            border_radius: dp(30)
            radius: [dp(5)]
            size_hint: 0.12, 0.06
            pos_hint: {"center_x": 0.3, "center_y": 0.86}
            FloatLayout:
                MDIconButton:

                    icon: "share-variant"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDCard:
            md_bg_color: 1, 1, 1, 1
            elevation: 0
            border_radius: dp(30)
            radius: [dp(5)]
            size_hint: 0.12, 0.06
            pos_hint: {"center_x": 0.5, "center_y": 0.86}
            FloatLayout:
                MDIconButton:
                    icon: "ticket-percent"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDCard:
            md_bg_color: 1, 1, 1, 1
            elevation: 0
            border_radius: dp(30)
            radius: [dp(5)]
            size_hint: 0.12, 0.06
            pos_hint: {"center_x": 0.7, "center_y": 0.86}
            FloatLayout:
                MDIconButton:
                    icon: "wallet-membership"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDCard:
            md_bg_color: 1, 1, 1, 1
            elevation: 0
            border_radius: dp(30)
            radius: [dp(5)]
            size_hint: 0.12, 0.06
            pos_hint: {"center_x": 0.9, "center_y": 0.86}
            FloatLayout:
                MDIconButton:
                    icon: "earth"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            text: "News"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.9, "center_y": 0.81}
        MDLabel:
            text: "Send"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.1, "center_y": 0.81}
        MDLabel:
            text: "Share"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.3, "center_y": 0.81}
        MDLabel:
            text: "Voucher"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.81}
        MDLabel:
            text: "E-Wallet"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.7, "center_y": 0.81}

        MDCard:
            md_bg_color: 1, 1, 1, 1
            elevation: 0
            border_radius: dp(30)
            radius: [dp(5)]
            size_hint: 0.12, 0.06
            pos_hint: {"center_x": 0.87, "center_y": 0.73}
            FloatLayout:
                MDIconButton:
                    icon: "magnify"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDCard:
            md_bg_color: 1, 1, 1, 1
            elevation: 0
            border_radius: dp(30)
            radius: [dp(5)]
            size_hint: 0.12, 0.06
            pos_hint: {"center_x": 0.7, "center_y": 0.73}
            FloatLayout:
                MDIconButton:
                    icon: "tune"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"top":0.97, "left": 0.95}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release:
                root.manager.current = "home"
                root.manager.transition.direction = "right"

        MDIconButton:
            icon: "account-circle"
            pos_hint: {"top":0.97, "right": 0.97}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
        MDLabel:
            text: "Lam Nguyen"
            halign: "center"
            font_style: "Caption"
            font_size: "25dp"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint:{"center_y": 0.94}
        MDCard:
            md_bg_color: 1, 1, 1, 1
            size_hint: 0.9, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.58}
            border_radius: dp(30)
            radius: [dp(30)]
            FloatLayout:
                MDLabel:
                    text: "+323"
                    theme_text_color: "Custom"
                    text_color: 0, 153/255, 204/255, 1
                    halign: "center"
                    pos_hint: {"center_x": 0.9, "center_y": 0.7}
                MDLabel:
                    text: "-150"
                    theme_text_color: "Custom"
                    text_color: 0, 153/255, 204/255, 1
                    halign: "center"
                    pos_hint: {"center_x": 0.9, "center_y": 0.3}
                MDList:
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    TwoLineAvatarIconListItem:
                        text: "Washing hand rewards"
                        secondary_text: "21/06/2020"
                        IconLeftWidget:
                            icon: "hand-right"

                    TwoLineAvatarIconListItem:
                        text: "Get Voucher discount 10%"
                        secondary_text: "21/06/2020"
                        IconLeftWidget:
                            icon: "wallet-giftcard"
        MDCard:
            md_bg_color: 1, 1, 1, 1
            size_hint: 1, 0.45
            FloatLayout:
                MDLabel:
                    text: "More"
                    halign: "center"
                    pos_hint: {"center_x": 0.15, "center_y": 0.93}
                MDCard:
                    elevation: 10
                    md_bg_color: 1, 1, 1, 1
                    size_hint: 0.95, 0.7
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    border_radius: dp(30)
                    radius: [dp(30)]
                    BoxLayout:
                        MDList:
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
                            TwoLineAvatarIconListItem:
                                text: "Customer satisfaction survey"
                                secondary_text: "21/06/2020"
                                IconLeftWidget:
                                    icon: "cellphone"
                                IconRightWidget:
                                    icon: "chevron-right"

                            TwoLineAvatarIconListItem:
                                text: "My Goals"
                                secondary_text: "Reach 1000 points/day"
                                IconLeftWidget:
                                    icon: "bullseye-arrow"
                                IconRightWidget:
                                    icon: "chevron-right"

                            TwoLineAvatarIconListItem:
                                text: "Friends"
                                secondary_text: "68 people"
                                IconLeftWidget:
                                    icon: "account-multiple"
                                IconRightWidget:
                                    icon: "chevron-right"
"""


class UserScreen(MDScreen):
    Builder.load_string(user_kv)