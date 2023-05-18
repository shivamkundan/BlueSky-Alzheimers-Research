'''Definitions of objects'''
# import the kivy stuff
from kivy_imports import *

# import my stuff
from globals import *
from object_defs import *
from page_templates import *

# from kivy_imports import *
from kivy.properties import StringProperty
from kivy.graphics import Color
from kivy.graphics import RoundedRectangle

# ===================================================================== #
class WrapLabel(Label):
	pass
# ===================================================================== #

class MyButton(Button):
	def on_release_custom(self,to_page,direction="left",*args,**kwargs):
		App.get_running_app().root.current=to_page
		App.get_running_app().root.transition.direction=direction

class MyButton2(Button):
	pass

class MyButton3(Button):
	pass

class RoundedButton(MyButton):
	def __init__(self,**kwargs):
		super(RoundedButton,self).__init__(**kwargs)
		self.btn_radius=[8]
		self.pressed_color=(69/255, 90/255, 100/255, 0.6)

	def on_press(self):
		print ("on_press")
		self.change_color()

	def on_release(self):
		self.change_color_back()

	def on_release_custom(self,to_page,direction="left",*args,**kwargs):
		print ("on_release")
		self.change_color_back()
		App.get_running_app().root.current=to_page
		App.get_running_app().root.transition.direction=direction

	def change_color(self, *args,**kwargs):
		print ("change_color")
		# self.background_color=(69/255, 90/255, 100/255, 0.4)
		self.background_color=self.pressed_color
		with self.canvas.before:
			# Color(1/255, 0/255, 0/255, 0.9)
			Color(self.background_color)
			self.rect=RoundedRectangle(pos=self.pos, size=self.size,radius=self.btn_radius)

	def change_color_back(self, *args):
		print ("change_color_back")
		self.background_color=(0,0,0,0)
		with self.canvas.before:
			Color(69/255, 90/255, 100/255, 0.9)
			self.rect=RoundedRectangle(pos=self.pos, size=self.size,radius=self.btn_radius)

# ===================================================================== #

class MyActionBar(ActionBar):
	NAME=StringProperty("None")
	def __init__(self,**kwargs):

		super(MyActionBar,self).__init__(**kwargs)


	def chevron_left(self,scr,to_pg='RiskAssesmentPage'):
		print ("chevron_left")
		print (scr.name)

		if scr.name in ["AboutPage","RiskAssesmentPage","EducationalResourcesPage","CognitiveRehabPage"]:
			to_pg="LandingPage"
		# print ()
		App.get_running_app().root.transition.direction="right"
		App.get_running_app().root.current=to_pg

# ===================================================================== #

class NavButtons(BoxLayout):
	pass