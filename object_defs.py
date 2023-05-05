from kivy_imports import *
from kivy.properties import StringProperty
# ===================================================================== #

# class NavButtons(Widget):
# 	pass

class MyButton(Button):
	pass

class MyButton2(Button):
	pass

class AirP_ActionBar(ActionBar):
	def __init__(self,**kwargs):
		super(AirP_ActionBar,self).__init__(**kwargs)
		NAME=StringProperty("Name")

	def chevron_left(self,name,to_pg='RiskAssesmentPage'):
		print ("chevron_left")
		print (name)
		App.get_running_app().root.transition.direction="right"
		App.get_running_app().root.current=to_pg

class ButtonSet(BoxLayout):
	def __init__(self,**kwargs):
		super(ButtonSet,self).__init__(**kwargs)

class ContentNavigationDrawer(BoxLayout):
	pass

class NavButtons(BoxLayout):
	pass