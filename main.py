#written by Tashinga

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#the front end willbe designed using kivy. CXonnect using Builder 
#where as the logic will be in python

Builder.load_file('design.kv')

class  LoginScreen(Screen):
    pass


class RootWidget(ScreenManager): 
    pass

class MainApp(App): 
    def build(self):
        return RootWidget()

#Call the main class
if __name__ == "__main__": 
    MainApp().run()