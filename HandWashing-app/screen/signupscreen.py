from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import requests

signup_kv = """
<SignupScreen>
    name: "signup"
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
            text: "WELCOME"
            font_size: "65dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
        MDLabel:
            halign: "center"
            font_size: "38dp"
            text: "Register"
            pos_hint: {"center_x": 0.5, "center_y": 0.67}
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_dark         
        MDTextFieldRound:
            id: email
            hint_text: "Email Address"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.59}
            size_hint: 0.75, 0.06
            color_active: 1, 1, 1, 1
            normal_color: 1, 1, 1, 1
        MDTextFieldRound:
            id: fullname
            hint_text: "Fullname"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.51}
            size_hint: 0.75, 0.06
            color_active: 1, 1, 1, 1
            normal_color: 1, 1, 1, 1
        
        MDTextFieldRound:
            id: password
            hint_text: "Password"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.43}
            size_hint: 0.75, 0.06
            password: True
            color_active: 1, 1, 1, 1
            normal_color: 1, 1, 1, 1    
        MDTextFieldRound:
            id: confirm_password
            hint_text: "Confirm Password"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
            size_hint: 0.75, 0.06
            password: True
            color_active: 1, 1, 1, 1
            normal_color: 1, 1, 1, 1    
        MDCheckbox:
            size_hint: None, None
            size: "48dp", "48dp"
            pos_hint: {'center_x': 0.14, 'center_y': .295}
            on_active: root.show_password()
        MDLabel:
            text: "Show password"
            pos_hint: {'center_x': 0.68, 'center_y': .295}
            
        MDFillRoundFlatButton:
            pos_hint: {"center_x": 0.5, "center_y": 0.24}
            size_hint : 0.85, 0.05
            text: "REGISTER"

            on_release: root.registion()


        MDFlatButton:
            halign: "center"
            text: "Forgot password?"
            pos_hint: {"center_x": 0.5, "center_y": 0.17}
            text_color: app.theme_cls.primary_color
            on_release:
                root.manager.current = "forgot"
                root.manager.transition.direction = "left"

        MDLabel:
            halign: "center"
            text: "Already have an account?"
            pos_hint: {"center_x": 0.45, "center_y": 0.13}


        MDFlatButton:
            halign: "center"
            text: "Login"
            pos_hint: {"center_x": 0.75, "center_y": 0.13}
            text_color: app.theme_cls.primary_color
            on_release:
                root.manager.current = "login"
                root.manager.transition.direction = "left"


        MDLabel:
            halign: "center"
            text: "VAS Coporation 2020"
            pos_hint: {"center_x": 0.5, "center_y": 0.05}

"""


class SignupScreen(MDScreen):
    # build .kv file
    Builder.load_string(signup_kv)

    dialog = None
    res_success = False

    ###############################################################################################################################################################

    def registion(self):
        res_info = self.get_info()

        email = res_info['email']
        password = res_info['password']
        fullname = res_info['fullname']
        confirm_password = self.ids.confirm_password.text

        # check if the user's inputs is full
        if not (email and password and fullname and confirm_password):
            self.show_dialog("Please enter all information!")
            return -1
        
        # check if confirm_password == res_password
        if not (confirm_password == password):
            self.show_dialog('Enter correct confirm password!')
            return -1

        response  = requests.post("http://127.0.0.1:5000/users/signup", json=res_info)
        str_response = response .text


        if str_response == "Registed Scuccessfully!":
            # if the response is 'Login successfully!', login and switch to login page
            self.res_success = True
            self.show_dialog(str_response)
        else: 
            # else show the dialog with message
            self.show_dialog(str_response)


    ###############################################################################################################################################################
    

    def get_info(self):
        email = self.ids.email.text
        fullname = self.ids.fullname.text
        password = self.ids.password.text
        res_info = {"email": email,
                    "fullname": fullname,
                    "password": password}

        return res_info

    ###############################################################################################################################################################

    def show_dialog(self, str_mess):
        ''' Show the dialo with the message
            str_mess: <string>  '''
        self.dialog = None
        if not self.dialog:
            self.dialog = MDDialog(
                text= str_mess,
                size_hint=(0.8, 1),
                buttons=[
                    # MDFlatButton(text="Cancel", on_release=self.close_dialog),
                    MDFlatButton(text="OK", on_release=self.close_dialog if (not self.res_success) else self.close_dialog_and_switch)
                ]
            )
        self.dialog.open()

    
    ###############################################################################################################################################################

    def close_dialog(self, obj):

        self.dialog.dismiss()

    ###############################################################################################################################################################

    def close_dialog_and_switch(self, obj):
        self.dialog.dismiss()
        self.manager.current = "login"
        self.manager.transition.direction = "left"

    ###############################################################################################################################################################

    def show_password(self):
        if self.ids.password.password:
            self.ids.password.password = False
            self.ids.confirm_password.password = False
        else:
            self.ids.password.password = True
            self.ids.confirm_password.password = True


