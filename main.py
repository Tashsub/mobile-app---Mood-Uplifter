#written by Tashinga

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
import glob
from pathlib import Path
import random
import os

#the front end willbe designed using kivy. CXonnect using Builder 
#where as the logic will be in python

Builder.load_file('design.kv')


cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files))

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

     #add functions to check if the user exists when trying to login
    def login(self, name, passw):
        with open("users.json", 'r') as file:
            users = json.load(file) 
        #checking username exists match it against the password stored
        #for that username
        try: 
            person = users[name]
            stored_password = person["password"]
            if name in users and stored_password == passw: 
                self.manager.current = "login_success"
        except KeyError: 
            self.ids.error_login.text = "Password or Username is incorrect. Try Again"    

        else: 
            self.ids.error_login.text = "Password or Username is incorrect. Try Again"

        
class SignUpScreen(Screen):
    def add_user(self, name, passw):

        full_day = datetime.now().strftime("%d-%m-%Y")
        with open("users.json") as file:
            users = json.load(file)

        users[name] = {'username': name, 'password': passw,'created at':full_day}
        print(users)

        with open("users.json", 'w') as file: 
            json.dump(users, file)
        self.manager.current = "sign_up_success"

    def back_to_home(self):
        self.manager.transition.direction = "left"
        self.manager.current= "login_screen"

        
class SignUpSuccess(Screen):
    def back_to_mainpage(self):
        self.manager.current = "login_screen"

class LoginSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    #read each file and assign it a value

    #happy
    def quotes(self, word):

        feels = glob.glob("quotes/*txt")
        feels_without_txt = [Path(filename).stem for filename in feels]

        #open all files
        word = word.lower()
        if word in feels_without_txt:
            with open(f"quotes/{word}.txt", encoding='utf-8') as file:
                quotes = file.readlines()
                size = len(quotes)
                chosen_quote_num = random.randint(0,(size-1)) 
                self.ids.show_quote.text = quotes[chosen_quote_num]
        else: 
            with open("quotes/random.txt") as file: 
                quotes = file.readlines()
                size = len(quotes)
                chosen_quote_num = random.randint(0,(size-1)) 
                self.ids.show_quote.text = quotes[chosen_quote_num]


class RootWidget(ScreenManager): 
    pass

class MainApp(App): 
    def build(self):
        return RootWidget()

#Call the main class
if __name__ == "__main__": 
    MainApp().run()