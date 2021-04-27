from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
home_kv = """
<HomeScreen>:
    name: "home"
    md_bg_color: 1, 1, 1, 1
    NavigationLayout:
        ScreenManager:
            Screen:
                MDTextFieldRound:
                    hint_text: "Type something"
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1
                    pos_hint:{"top": 0.78,"center_x": 0.5}
                    size_hint: 0.75, 0.06
                    color_active: 1, 1, 1, 1
                    normal_color: 1, 1, 1, 1
                MDIconButton:
                    icon: "menu"
                    on_release: nav_drawer.set_state("open")
                    pos_hint: {"top": 0.85,"center_x": 0.1}
                MDIconButton:
                    icon: "bell"
                    pos_hint: {"top": 0.85,"center_x": 0.9}

                MDLabel:
                    text: "6 Steps For Fresh Hands"
                    halign: "center"
                    pos_hint: {"center_x":0.33, "center_y": 0.69}
                MDFlatButton:
                    text: "More>"
                    pos_hint: {"center_x":0.86, "center_y": 0.69}
                    text_color: app.theme_cls.primary_dark

                MDLabel:
                    halign: "center"
                    text: "Hand Washing\\nRecognition"
                    theme_text_color: "Custom"
                    font_size: "30sp"
                    text_color: app.theme_cls.primary_dark
                    pos_hint: {"center_x": 0.5, "center_y":0.9}
                MDIconButton:
                    icon: "source/step_1.jpg"
                    size_hint: 0.27, 0.12
                    pos_hint: {"center_x": 0.2, "center_y": 0.6}
                MDLabel:
                    text: "Rub Palms \\nTogether"
                    halign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.51}
                    font_size: "13dp"

                MDIconButton:
                    icon: "source/step_2.jpg"
                    size_hint: 0.27, 0.12
                    pos_hint: {"center_x": 0.5, "center_y": 0.6}
                MDLabel:
                    text: "Rub the Back \\nof Hands"
                    halign: "center"
                    pos_hint: {"center_x": 0.5, "center_y": 0.51}
                    font_size: "13dp"
                MDIconButton:
                    icon: "source/step_3.jpg"
                    size_hint: 0.27, 0.12
                    pos_hint: {"center_x": 0.8, "center_y": 0.6}
                MDLabel:
                    text: "Interlink Your \\nFingers"
                    halign: "center"
                    pos_hint: {"center_x": 0.8, "center_y": 0.51}
                    font_size: "13dp"
                MDIconButton:
                    icon: "source/step_4.jpg"
                    size_hint: 0.27, 0.12
                    pos_hint: {"center_x": 0.2, "center_y": 0.41}
                MDLabel:
                    text: "Cup Your \\nFingers"
                    halign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.32}
                    font_size: "13dp"
                MDIconButton:
                    icon: "source/step_5.jpg"
                    size_hint: 0.27, 0.12
                    pos_hint: {"center_x": 0.5, "center_y": 0.41}
                MDLabel:
                    text: "Clean The \\nThumbs"
                    halign: "center"
                    pos_hint: {"center_x": 0.5, "center_y": 0.32}
                    font_size: "13dp"
                MDIconButton:
                    icon: "source/step_6.jpg"
                    size_hint: 0.27, 0.12
                    pos_hint: {"center_x": 0.8, "center_y": 0.41}
                MDLabel:
                    text: "Rubs Palms \\nYour Fingers"
                    halign: "center"
                    pos_hint: {"center_x": 0.8, "center_y": 0.32}
                    font_size: "13dp"
                MDLabel:
                    text: "Requirements"
                    halign: "center"
                    pos_hint: {"center_x":0.22, "center_y": 0.27}
                MDFlatButton:
                    text: "More>"
                    pos_hint: {"center_x":0.86, "center_y": 0.27}
                    text_color: app.theme_cls.primary_dark
                MDIconButton:
                    icon: "source/sanitizer.jpg"
                    size_hint: 0.27, 0.12
                    pos_hint: {"center_x": 0.2, "center_y": 0.185}
                MDLabel:
                    text: "Sanitizer"
                    halign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.115}
                    font_size: "13dp"
                MDIconButton:
                    icon: "source/water.png"
                    size_hint: 0.27, 0.12
                    pos_hint: {"center_x": 0.5, "center_y": 0.185}
                MDLabel:
                    text: "Water"
                    halign: "center"
                    pos_hint: {"center_x": 0.5, "center_y": 0.115}
                    font_size: "13dp"
                MDIconButton:
                    icon: "source/dryhand.jpg"
                    size_hint: 0.27, 0.12
                    pos_hint: {"center_x": 0.8, "center_y": 0.185}
                MDLabel:
                    text: "Dry Hand"
                    halign: "center"
                    pos_hint: {"center_x": 0.8, "center_y": 0.115}
                    font_size: "13dp"
                MDFillRoundFlatButton:
                    text: "BEGIN"
                    size_hint : 0.85, 0.05
                    pos_hint: {"center_x": 0.5, "center_y": 0.06}
                    on_release:
                        root.manager.current = "Step 1"
                        root.manager.transition.direction = "left"

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'

                Image:
                    source: "source/robot_4.jpg"
                    size_hint: 0.8, 0.5
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Home"
                            on_release:
                                root.manager.current = "user"
                            IconLeftWidget:
                                icon: "home"
                        OneLineIconListItem:
                            text: "Setting"
                            IconLeftWidget:
                                icon: "account-settings"
                        OneLineIconListItem:
                            text: "Logout"
                            on_release:
                                root.logout()
                            IconLeftWidget:
                                icon: "logout-variant"
"""


class HomeScreen(MDScreen):
    Builder.load_string(home_kv)
    logout_dialog = None

    def logout(self):
        if not self.logout_dialog:
            self.logout_dialog = MDDialog(
                text="Are you sure to logout?",
                size_hint=(0.8, 1),
                buttons=[
                    MDFlatButton(text="Sure", on_release=self.logout_action),
                    MDFlatButton(text="Cancel", on_release=self.close_logout_dialog)
                ]
            )
        self.logout_dialog.open()

    def close_logout_dialog(self, obj):
        self.logout_dialog.dismiss()

    def logout_action(self, obj):
        self.logout_dialog.dismiss()
        self.ids.nav_drawer.set_state("close")
        self.manager.current = "login"
        self.manager.transition.direction = "up"
