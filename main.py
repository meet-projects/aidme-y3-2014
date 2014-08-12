import kivy
import smtplib

kivy.require('1.8.0')

from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from email.mime.text import MIMEText
from kivy.uix.image import Image

sm = ScreenManager()

def send_email():

	# E-Mail code
	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	fp = open(textfile, 'rb')
	# Create a text/plain message
	msg = MIMEText(fp.read())
	fp.close()

	# me == the sender's email address
	# you == the recipient's email address
	msg['Subject'] = 'The contents of %s' % textfile
	msg['From'] = me
	msg['To'] = you

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	s = smtplib.SMTP('localhost')
	s.sendmail(me, [you], msg.as_string())
	s.quit()

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

class ProfileScreen(Screen):

	pass

class AidMeApp(App):

	def build(self):

		Config.set('kivy','keyboard_mode','systemanddock')
		Config.write()

		self.home_screen = HomeScreen(name="Home")
		self.login_screen = LogInScreen(name="LogIn")
		self.singup_screen = SignUpScreen(name="SignUp")
		self.profile_screen = ProfileScreen(name="Profile")
		sm.add_widget(self.home_screen)
		sm.add_widget(self.login_screen)
		sm.add_widget(self.singup_screen)
		sm.add_widget(self.profile_screen)

		return sm

	def submit_clicked(self, id):

		if id == "HelpB" :

			pass

		elif id == "ProfileB":

			sm.current = "Profile"
			self.home_screen.change

		elif id == "InstructionsB":

			pass

		elif id == "LogInB":

			sm.current = "LogIn"
			self.login_screen.change

		elif id == "SignUpB":

			sm.current = "SignUp"
			self.login_screen.change









if __name__=="__main__":
	AidMeApp().run()