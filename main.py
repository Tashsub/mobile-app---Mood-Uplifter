#written by Tashinga

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

#the front end willbe designed using kivy. CXonnect using Builder 
#where as the logic will be in python

Builder.load_file('design.kv')

class  LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

class SignUpScreen(Screen):
    def add_user(self, name, passw):

      
        full_day = datetime.now().strftime("%d-%m-%Y")
        with open("users.json") as file:
            users = json.load(file)

        users[name] = {'username': name, 'password': passw,'created at':full_day}
        print(users)

        with open("users.json", 'w') as file: 
            json.dump(users, file)
        
class RootWidget(ScreenManager): 
    pass

class MainApp(App): 
    def build(self):
        return RootWidget()

#Call the main class
if __name__ == "__main__": 
    MainApp().run()