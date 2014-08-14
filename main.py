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

sm = ScreenManager(transition=NoTransition())

# def send_email():

# 	fp = open(textfile, 'rb')
# 	# Create a text/plain message
# 	msg = MIMEText(fp.read())
# 	fp.close()

# 	# me == the sender's email address
# 	# you == the recipient's email address
# 	msg['Subject'] = 'The contents of %s' % textfile
# 	msg['From'] = me
# 	msg['To'] = you

# 	# Send the message via our own SMTP server, but don't include the
# 	# envelope header.
# 	s = smtplib.SMTP('localhost')
# 	s.sendmail(me, [you], msg.as_string())
# 	s.quit()

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

		Config.set('kivy','keyboard_mode','systemanddock')
		Config.write()
		print "window:"
		self.width = Config.getint('graphics','width')
		self.height= Config.getint('graphics','height')

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
		sm.current = "LogIn"
		
		return sm

	def submit_clicked(self, id2):

		if id2 == "HelpB" :

			pass

		elif id2 == "ProfileB":

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

			sm.current = "LogIn"
		elif id2 == "MapB":
			sm.current = "Map"

if __name__=="__main__":
	AidMeApp().run()
