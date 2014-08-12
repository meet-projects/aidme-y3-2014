import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics import *

sm=ScreenManager()

class Backgruond(Image):
    pass

class SignUpB(Image):
    pass

class Logo(Image):
    pass

class LogIn(Screen):
    pass


class LogInApp(App):
    def build(self):
        self.LogIn=LogIn(name="LogIn")
        sm.add_widget(self.LogIn)
        return sm
        
        

        
if __name__=="__main__":
    LogInApp().run()
