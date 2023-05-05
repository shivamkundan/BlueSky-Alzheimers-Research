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

# class Tab(FloatLayout, MDTabsBase):
# 	'''Class implementing content for a tab.'''
# 	text=StringProperty()

# class ItemDrawer(OneLineIconListItem):
# 	icon = StringProperty()
# 	text_color = ListProperty((0, 0, 0, 1))

# class DrawerList(ThemableBehavior, MDList):
# 	def set_color_item(self, instance_item):
# 		"""Called when tap on a menu item."""

# 		# Set the color of the icon and text for the menu item.
# 		for item in self.children:
# 			if item.text_color == self.theme_cls.primary_color:
# 				item.text_color = self.theme_cls.text_color
# 				break
# 		instance_item.text_color = self.theme_cls.primary_color

class MenuHeader(BoxLayout):
	'''An instance of the class that will be added to the menu header.'''

class NavButtons(BoxLayout):
	pass