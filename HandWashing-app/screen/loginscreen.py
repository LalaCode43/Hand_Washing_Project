from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import requests
login_kv = """
<LoginScreen>:
    name: "login"
    md_bg_color: 1, 1, 1, 1
    FloatLayout:
        MDCard:
            border_radius: 70
            radius: [70,]
            elevation: 8
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
            text: "WELCOME"
            font_size: "65dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
        MDLabel:
            halign: "center"
            font_size: "38dp"
            text: "Login"
            pos_hint: {"center_x": 0.5, "center_y": 0.67}
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_dark

        MDTextFieldRound:
            id: email
            hint_text: "Email Address"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            icon_right: "account"
            pos_hint: {"center_x": 0.5, "center_y": 0.58}
            size_hint: 0.75, 0.06
            normal_color: 1, 1, 1, 1
            color_active: 1, 1, 1, 1

        MDTextFieldRound:
            id: password
            hint_text: "Password"
            pos_hint: {"center_x": 0.5, "center_y": 0.48}
            password: True
            size_hint: 0.75, 0.06
            normal_color: 1, 1, 1, 1
            color_active: 1, 1, 1, 1
        MDIconButton:
            id: eye
            icon: "eye-off"
            elevation_normal: 12
            pos_hint: {"center_x": 0.85, "center_y": 0.4787}
            on_release:
                self.icon = "eye" if self.icon == "eye-off" else "eye-off"
                root.ids.password.password = False if root.ids.password.password == True else True


        MDFillRoundFlatButton:
            pos_hint: {"center_x": 0.5, "center_y": 0.38}
            text: "LOGIN"
            size_hint : 0.85, 0.05
            theme_color: "Custom"

            on_release:
                root.check_login()

        MDLabel:
            text: "Don't have an account?"
            pos_hint: {"center_x": 0.7, "center_y": 0.31}
        MDFlatButton
            pos_hint: {"center_x": 0.72 ,"center_y": 0.31}
            text: "Sign up"
            text_color: app.theme_cls.primary_color
            on_release:
                root.manager.current = "signup"
                root.manager.transition.direction = "right"

        MDFlatButton:
            halign: "center"
            text: "Forgot password?"
            pos_hint: {"center_x": 0.5, "center_y": 0.27}
            text_color: app.theme_cls.primary_color
            on_release:
                root.manager.current = "forgot"
                root.manager.transition.direction = "left"

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


class LoginScreen(MDScreen):
    # Build .kv file
    Builder.load_string(login_kv)

    ###############################################################################################################################################################

    dialog = None
    login_success = False

    ###############################################################################################################################################################

    def check_login(self):
        # get email and password from user's inputs
        login_info = self.get_login_info()
        email = login_info['email']
        password = login_info['password']      
        print(login_info)

        # check if email =="None" or password == "None"
        if not (email and password):
            self.show_dialog("Please enter all the email and password!")
            return -1

        # request to server and recive response
        response = requests.post("http://127.0.0.1:5000/users/signin",json=login_info)
        str_response = response.text

        print(str_response)

        if str_response == "Login successfully!":
            # if the response is 'Login successfully!', login and switch to introduce page
            self.login_success = True
            self.show_dialog(str_response)
        else: 
            # else show the dialog with message
            self.show_dialog(str_response)

    def get_login_info(self):
        email = self.ids.email.text
        password = self.ids.password.text

        login_info = {'email': email,
                        'password': password}

        return login_info
    
    ###############################################################################################################################################################

    def show_dialog(self, str_mess):
        ''' Show the dialog with the message
            str_mess: <string>  '''
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(
                text= str_mess,
                size_hint=(0.8, 1),
                buttons=[
                    # MDFlatButton(text="Cancel", on_release=self.close_dialog if not self.login_success else self.close_dialog_and_switch),
                    MDFlatButton(text="OK", on_release=self.close_dialog if not self.login_success else self.close_dialog_and_switch)
                ]
            )
        self.dialog.open()

    ###############################################################################################################################################################

    def close_dialog(self, obj):
        ''' Close the dialog '''
        self.dialog.dismiss()    

    ###############################################################################################################################################################

    def close_dialog_and_switch(self, obj):
        ''' Close the dialog and then switch to introduce page '''
        self.dialog.dismiss()
        self.manager.current = "introduce"
        self.manager.transition.direction = "down"

   
    
        
        
    
