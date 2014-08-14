import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics import *

sm=ScreenManager()



class MapApp(App):
    def build(self):
        self.Map=LogIn(name="Map")
        sm.add_widget(self.Map)
        return sm
        
        

        
if __name__=="__main__":
    LogInApp().run()
