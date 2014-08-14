import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics import *

sm=ScreenManager()

class SignUp(Screen):
	pass


class Name(Image):
	pass

class Password(Image):
	pass

class RPassword(Image):
	pass

class Disease(Image):
	pass

class PCode(Image):
	pass

class Skills(Image):
	pass
	

class Background(Image):
	pass

class SignUpApp(App):
    def build(self):
        self.SignUp=SignUp(name="SignUp")
        sm.add_widget(self.SignUp)
        return sm
        
        

        
if __name__=="__main__":
    SignUpApp().run()
