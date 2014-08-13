import kivy
import smtplib

kivy.require('1.8.0')

from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from email.mime.text import MIMEText
from kivy.uix.image import Image
from kivy.uix.popup import Popup
sm = ScreenManager(transition=NoTransition())

class SignUpB(Image):
    
    pass

class Logo(Image):
    
    pass

class Password(Image):

	pass

class Email(Image):

	pass

class GeneralScreen (Screen):

	pass

class Background(Image):
	
	pass

class HomeScreen(Screen):

	pass

class LogInScreen(Screen):

	def get_info():

		email = self.ids.EmailTI.text
		password = self.ids.PasswordTI.text
		return [email,password]

class SignUpScreen(Screen):

	pass

class MapScreen(Screen):
	
	pass


class MapI(Image):

	pass

class ProfileScreen(Screen):
	pass


class AidMeApp(App):
	
	def build(self):

		Config.set('kivy','keyboard_mode','')
		Config.write()
		self.general_screen = GeneralScreen(name="General")
		self.home_screen = HomeScreen(name="Home")
		self.login_screen = LogInScreen(name="LogIn")
		self.singup_screen = SignUpScreen(name="SignUp")
		self.profile_screen = ProfileScreen(name="Profile")
		self.map_screen=MapScreen(name="Map")
		sm.add_widget(self.map_screen)
		sm.add_widget(self.home_screen)
		sm.add_widget(self.login_screen)
		sm.add_widget(self.singup_screen)
		sm.add_widget(self.profile_screen)
		sm.add_widget(self.general_screen)
		sm.current = "Home"
		
		return sm

	def submit_clicked(self, id2):
		if id2 == "ProfileB":

			sm.current = "Profile"

		elif id2 == "InstructionsB":

			sm.current = "General"

		elif id2 == "LogInB":

			sm.current = "Home"

		elif id2 == "SignUpB":

			sm.current = "SignUp"

		elif id2 == "HomeB":

			sm.current = "Home"

		elif id2 == "LogOutB":

			sm.remove_widget(self.login_screen)
			self.login_screen = LogInScreen(name="LogIn")
			sm.add_widget(self.login_screen)
			sm.current = "LogIn"
		
		elif id2 == "MapB":
		
			sm.current = "Map"
		elif id2 == "HelpB":
			b = Button(text='Dismiss')
			content = BoxLayout(orientation='vertical')
			content.add_widget(Label(text='Help is on the way!'))
			content.add_widget(b)
			popup = Popup(title='Test popup', content=content,size_hint=(None, None), size=(400, 400),id="Popup")
			b.bind(on_press=popup.dismiss)

			popup.open()

if __name__=="__main__":
	AidMeApp().run()
