from kivy_imports import *

# ===================================================================== #

class tab_template(FloatLayout, MDTabsBase):
	def __init__(self,**kwargs):
		super(tab_template,self).__init__(**kwargs)
		text = StringProperty()

class ItemConfirm(OneLineAvatarIconListItem):
	divider = None

	def set_icon(self, instance_check):
		instance_check.active = True
		check_list = instance_check.get_widgets(instance_check.group)
		for check in check_list:
			if check != instance_check:
				check.active = False

class NavButtons(Widget):
	pass

class ButtonSet(MDBoxLayout):
	def __init__(self,**kwargs):
		super(ButtonSet,self).__init__(**kwargs)

class ContentNavigationDrawer(MDBoxLayout):
	pass

class Tab(FloatLayout, MDTabsBase):
	'''Class implementing content for a tab.'''
	text=StringProperty()

class ItemDrawer(OneLineIconListItem):
	icon = StringProperty()
	text_color = ListProperty((0, 0, 0, 1))

class DrawerList(ThemableBehavior, MDList):
	def set_color_item(self, instance_item):
		"""Called when tap on a menu item."""

		# Set the color of the icon and text for the menu item.
		for item in self.children:
			if item.text_color == self.theme_cls.primary_color:
				item.text_color = self.theme_cls.text_color
				break
		instance_item.text_color = self.theme_cls.primary_color

class MenuHeader(MDBoxLayout):
	'''An instance of the class that will be added to the menu header.'''