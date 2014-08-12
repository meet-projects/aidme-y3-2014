import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

sm=ScreenManager()

class Background(Image):
	pass
class ProfileScreen(Screen):
	pass
class ProfileApp(App):
	def build(self):
	        self.profile=ProfileScreen(name='h1')
	        sm.add_widget(self.profile)
	        return sm

if __name__=="__main__":
    ProfileApp().run()
