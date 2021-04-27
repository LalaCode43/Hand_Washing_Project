from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
step_kv = """
<StepScreen>:
    name: "Step 1"
    md_bg_color: 0, 153/255, 204/255, 1
    FloatLayout:
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"top":0.97, "left": 0.95}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: root.back_screen()

        MDIconButton:
            icon: "account-circle"
            pos_hint: {"top":0.97, "right": 0.97}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: root.back_user()

        MDLabel:
            id: step_current
            text: "Step 1"
            halign: "center"
            font_style: "Caption"
            font_size: "30dp"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint:{"center_x": 0.5, "center_y": 0.9}
        MDLabel:
            id: step_current_name
            text: "Rub Palms Together"
            halign: "center"
            font_style: "Caption"
            font_size: "20dp"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint:{"center_x": 0.5, "center_y": 0.85}
        MDCard:
            md_bg_color: 1, 1, 1, 1
            size_hint: 1, 0.75
            border_radius: dp(30)
            radius: [dp(30), dp(30), 0 ,0]
            FloatLayout:
                MDLabel:
                    text: "Camera Checking"
                    halign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.9}
                    font_size: "17dp"
                MDLabel:
                    text: "Remaining: 5s"
                    halign: "center"
                    pos_hint: {"center_x": 0.8, "center_y": 0.9}
                    font_size: "17dp"
                Image:
                    id: img_1
                    source:"source/step_1.jpg"
                    size_hint: 0.6, 0.6
                    pos_hint: {"center_x": 0.5, "center_y": 0.66}
                Image:
                    id: img_2
                    source:"source/step_1.jpg"
                    size_hint: 0.4, 0.4
                    pos_hint: {"center_x": 0.5, "center_y": 0.25}
                MDIconButton:
                    icon: "source/green_tick.jpg"
                    size_hint: 0.24, 0.15
                    pos_hint: {"center_x": 0.85, "center_y": 0.25}
                    on_release:
                        root.pass_screen()
                MDIconButton:
                    icon: "source/red_cross.png"
                    size_hint: 0.24, 0.15
                    pos_hint: {"center_x": 0.15, "center_y": 0.25}
                MDLabel:
                    text: "Pass"
                    halign: "center"
                    pos_hint: {"center_x": 0.85, "center_y": 0.15}
                    font_size: "30dp"
                MDLabel:
                    text: "Retry"
                    halign: "center"
                    pos_hint: {"center_x": 0.15, "center_y": 0.15}
                    font_size: "30dp"
                MDLabel:
                    text: "Instruction"
                    halign: "center"
                    pos_hint: {"center_x": 0.2, "center_y": 0.4}
                    font_size: "25dp"
"""


class StepScreen(MDScreen):
    Builder.load_string(step_kv)
    step_name = ["Rub Palms Together",
                 "Rub the Back of Hands",
                 "Interlink Your Fingers",
                 "Cup Your Fingers",
                 "Clean The Thumbs",
                 "Rubs Palms Your Finger"
                 ]

    def move_screen(self, screen_move, number_move):
        self.name = screen_move
        self.ids.step_current.text = screen_move
        self.ids.step_current_name.text = self.step_name[number_move - 1]
        self.ids.img_1.source = "source/step_{}.jpg".format(number_move)
        self.ids.img_2.source = "source/step_{}.jpg".format(number_move)

    def back_screen(self):
        screen_current = self.name
        number_current = int(screen_current[-1])
        if number_current == 1:
            screen_move = "home"
            self.manager.current = screen_move
            self.manager.transition.direction = "right"
        else:
            number_move = number_current - 1
            screen_move = "Step {}".format(number_move)
            self.move_screen(screen_move, number_move)

    def pass_screen(self):
        screen_current = self.name
        number_current = int(screen_current[-1])
        if number_current == 6:
            screen_move = "result"
            self.manager.current = screen_move
            self.manager.transition.direction = "left"
            self.move_screen("Step 1", 1)
        else:
            screen_move = "Step {}".format(number_current + 1)
            number_move = number_current + 1
            self.move_screen(screen_move, number_move)

    def back_user(self):
        self.manager.current = "user"
        self.manager.transition.direction = "left"
        self.move_screen("Step 1", 1)