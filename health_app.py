#!/usr/local/bin/python3
import os
# os.environ["KIVY_NO_CONSOLELOG"] = "1"

import kivy
# kivy.require("1.9.1")

from kivy.config import Config

from kivymd.app import MDApp
from kivymd.uix.screen import Screen

from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.garden.circulardatetimepicker import CircularTimePicker

from kivy.clock import Clock

from kivy.uix.widget import Widget
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition,FadeTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.picker import MDTimePicker,MDDatePicker
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem,OneLineAvatarIconListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget, IconRightWidget, ImageLeftWidget, ImageRightWidget
from kivymd.uix.label import MDLabel

from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDTextButton, MDFlatButton, MDRectangleFlatButton, MDRectangleFlatIconButton, MDIconButton, MDFloatingActionButton,MDFloatingActionButtonSpeedDial,MDRaisedButton,MDRoundFlatIconButton,MDFillRoundFlatIconButton,MDFillRoundFlatButton

from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior

from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivy.uix.floatlayout import FloatLayout

from kivymd.uix.taptargetview import MDTapTargetView

from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDGridBottomSheet

from kivy.animation import Animation
from kivy.uix.image import Image
from kivymd.uix.dialog import MDDialog
from kivy.uix.button import Button

# ==========================
from datetime import datetime
import time


KV_FILE='health_app.kv' # kivy design file

# MAX_SIZE = (1280, 800)
# Config.set('graphics', 'width', MAX_SIZE[0])
# Config.set('graphics', 'height', MAX_SIZE[1])

# These resolutions are in software pixels
resolutions=[(330, 550),(390, 844),(400, 667),(412,732),(1280,800)]
Window.size = resolutions[2]


# ============================ GLOBAL FNs ============================= #

def chevron_left_global(curr,next_pg='RiskAssesmentPage'):
	curr.parent.transition.direction="right"
	curr.parent.current=next_pg

def arrow_right_global(curr,next_pg):
	if curr.curr_tab_num==curr.num_tabs-1:
		curr.parent.transition.direction="left"
		curr.parent.current=next_pg
	else:
		curr.curr_tab_num+=1
		curr.ids['android_tabs'].switch_tab(curr.tab_names[curr.curr_tab_num])

def arrow_left_global(curr,next_pg):
	if curr.curr_tab_num==0:
		curr.parent.transition.direction="right"
		curr.parent.current=next_pg
	else:
		curr.curr_tab_num-=1
		curr.ids['android_tabs'].switch_tab(curr.tab_names[curr.curr_tab_num])

def on_tab_switch_global(curr, instance_tabs, instance_tab, instance_tab_label, tab_text):
		'''
		Called when switching tabs.

		:type instance_tabs: <kivymd.uix.tab.MDTabs object>;
		:param instance_tab: <__main__.Tab object>;
		:param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
		:param tab_text: text or name icon of tab;
		'''
		# get the tab icon.
		# count_icon = instance_tab.text

		curr.curr_tab_num=int(instance_tab.text)-1
		curr.ids['android_tabs'].switch_tab(curr.tab_names[curr.curr_tab_num])

def release_keyboard_global(curr):
	curr._keyboard = Window.request_keyboard(curr.parent._keyboard_closed, curr)
	curr._keyboard.bind(on_key_up=curr.parent._on_keyboard_up)
	Window.release_all_keyboards()

def button_press_global(curr,button):
	print ('pressed: ',button.text)
	curr.responses_dict[curr.curr_tab_num+1]=int(button.text)
	curr.done_dict[curr.curr_tab_num+1]=True
	curr.arrow_right()

def init_subpage_global(curr):
		curr.total_score=0
		curr.num_tabs=len(curr.tab_names)
		curr.curr_tab_num=0

		curr.responses_dict={}
		for i in range(curr.num_tabs):
			curr.responses_dict[i]=0

		curr.done_dict={}
		for i in range(curr.num_tabs):
			curr.done_dict[i]=0

def update_score_global(curr):
	total=0
	for key,val in curr.responses_dict.items():
		total+=val
	curr.total_score=total
	print ('score:',total)


	num_done=0
	for k,v in curr.done_dict.items():
		if v==True:
			num_done+=1
	print (num_done)
	pct=int(round(100*(num_done/curr.num_tabs),0))
	pct_txt=str(pct)+'% Complete'
	print (pct_txt)
	return total, pct_txt

def on_pre_leave_global(curr):
		total,pct_txt=update_score_global(curr)
		curr.parent.score_vars_dict[curr.page_name]=total
		curr.parent.ids['RiskAssesmentPage'].ids[curr.name+"_label"].secondary_text=pct_txt
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
	def button_press(self,num):
		# self.parent.parent.questions_dict[self.parent.parent.curr_question_num]['selected_val']=num
		print('q#: ',self.parent.parent.parent.curr_question_num)
		# print ('pressed: ',num)
		# self.parent.parent.next_question(1)
		self.parent.parent.parent.arrow_right()
		# self.parent.parent.parent.button_press(num)

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

# --------------------------------------------------------------------- #

class LandingPageTemplate(MDScreen):
	def __init__(self,**kwargs):
		super(LandingPageTemplate,self).__init__(**kwargs)

	def chevron_left(self):
		chevron_left_global(self)

class SubPageTemplate(MDScreen):
	def __init__(self,**kwargs):
		super(SubPageTemplate,self).__init__(**kwargs)

		# dummy/placeholder variables
		self.tab_names=None
		self.page_name=None
		self.prev_page=None
		self.next_page=None

	def init_subpage(self):
		init_subpage_global(self)

	def chevron_left(self):
		chevron_left_global(self)

	def arrow_left(self):
		arrow_left_global(self,self.prev_page)

	def arrow_right(self):
		arrow_right_global(self,self.next_page)

	def button_press(self,button):
		button_press_global(self,button)

	def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
		on_tab_switch_global(self, instance_tabs, instance_tab, instance_tab_label, tab_text)

	def on_pre_leave(self):
		on_pre_leave_global(self)

class ScorePageTemplate(MDScreen):
	def __init__(self,**kwargs):
		super(ScorePageTemplate,self).__init__(**kwargs)
		self.prev_page=None
		self.next_page=None
		self.score=0

	def update_score(self,dt):
		try:
			self.ids['score_label'].text=str(self.parent.ids[self.prev_page].total_score)
		except:
			pass

	def on_pre_enter(self):
		self.ids['score_label'].text=str(self.parent.ids[self.prev_page].total_score)
		release_keyboard_global(self)
		Clock.schedule_once(self.update_score,0.2)

	def chevron_left(self):
		chevron_left_global(self)

	def arrow_left(self):
		self.parent.transition.direction="right"
		self.parent.current=self.prev_page

	def arrow_right(self):
		self.parent.transition.direction="left"
		self.parent.current=self.next_page

# ===================================================================== #

class LoadingPage(MDScreen):
	def __init__(self,**kwargs):
		super(LoadingPage,self).__init__(**kwargs)

	def animate_logo(self,widget,*args):
		print(widget,args)

		# for item in widget.ids:
		#     print (item)
		anim=Animation(size=(self.ids['my_im'].size[0]//2,self.ids['my_im'].size[1]//2))
		# anim=Animation(anchor_x='top',anchor_y='center')
		anim.start(self.ids['my_im'])

	def transitioner(self,dt):
		# self.parent.transition=FadeTransition()
		self.parent.current='LandingPage'


	def on_enter(self):
		Clock.schedule_once(self.transitioner,5)
		# self.ids['prog'].start()
		for item in self.ids:
			print(item)

class LandingPage(ThemableBehavior,MDScreen):
	def __init__(self,**kwargs):
		super(LandingPage,self).__init__(**kwargs)

	def chevron_left(self,*args):
		self.parent.transition.direction="right"
		self.parent.current='RiskAssesmentPage'

	def animate_logo(self,*args):
		print(args)
		print (dir(self.ids['my_im']))
		anim=Animation(size=(100,100),opacity=0.5,duration=2,pos_hint={'center_x': 0.5, 'center_y': 0.5})
		# anim=Animation(anchor_x='top',anchor_y='center')
		anim.start(self.ids['my_im'])

		anim.bind(on_complete=self.unhide)
		# self.unhide()

	def motion(self,wid,*args):
		print(widget,args)

	def on_pre_enter(self):
		# self._keyboard = Window.request_keyboard(self.parent._keyboard_closed, self)
		# self._keyboard.bind(on_key_up=self.parent._on_keyboard_up)
		# Window.release_all_keyboards()
		release_keyboard_global(self)
		Clock.schedule_once(self.themer,0.1)


	def themer(self,*args):
		self.ids['my_im'].reload()

	def unhide(self,*args):
		print (args)
		# self.ids['logo'].canvas.opacity=1
		self.hide_widget(dohide=False)
		print (Window.size)



	def hide_widget(self,wid=None, dohide=True):
		# print (self.get_widgets())
		for item in ['nav_drawer','l2','btn1','btn2','btn3','btn4']:
		# for item in ['BL']:
			wid=self.ids[item]
			if hasattr(wid, 'saved_attrs'):
				if not dohide:
					wid.height, wid.size_hint_y, wid.opacity, wid.disabled = wid.saved_attrs
					del wid.saved_attrs
			elif dohide:
				wid.saved_attrs = wid.height, wid.size_hint_y, wid.opacity, wid.disabled
				wid.height, wid.size_hint_y, wid.opacity, wid.disabled = 0, None, 0, True

class LoginPage(MDScreen):
	def __init__(self,**kwargs):
		super(LoginPage,self).__init__(**kwargs)
		self.dialog=False

	def chevron_left(self):
		chevron_left_global(self,next_page='LandingPage')

	def show_alert_dialog(self,*args):
		print (args)
		if not self.dialog:
			self.dialog = MDDialog(
				text="This feature has not been implemented yet",
				buttons=[MDFlatButton(text="close",on_release=self.close_dialog),
					# MDFlatButton(text="DISCARD",),
					],
			)
		self.dialog.open()





	def close_dialog(self,*args):
		self.dialog.dismiss()

# --------------------------------------------------------------------- #

class RiskAssesmentPage(MDScreen):
	def __init__(self,**kwargs):
		super(RiskAssesmentPage,self).__init__(**kwargs)
		self.score=0
		self.air_pollution_pct=0
		# Clock.schedule_once(self.init_tap_target, 1)

	# def init_tap_target(self,*args):
	#     self.tap_target_view = MDTapTargetView(
	#         widget=self.ids.button,
	#         title_text="This is an add button",
	#         description_text="This is a description of the button",
	#         widget_position="right_top",
	#         cancelable=True,
	#         # outer_circle_color=(1,0,0),
	#         target_radius=50,
	#         outer_radius=300,
	#         outer_circle_alpha=1.0,
	#         # target_circle_color=(0, 1, 0),
	#     )

	def update_score(self,dt):
		temp=0
		for page,score in self.parent.score_vars_dict.items():
			temp+=score
		self.ids['score_label'].text=str(temp)

	def on_pre_enter(self):
		Clock.schedule_once(self.update_score,0.2)

	def tap_target_start(self):
		if self.tap_target_view.state == "close":
			self.tap_target_view.start()
		else:
		   self.tap_target_view.stop()

	def chevron_left(self):
		chevron_left_global(self,next_pg='LandingPage')

# --------------------------------------------------------------------- #

class SociodemographicPage(MDScreen):
	def __init__(self,**kwargs):
		super(SociodemographicPage,self).__init__(**kwargs)
		self.tab_names=['Age','Sex','Zip Code','Military (1)','Military (2)']
		self.tab_num_dict={'Age':1,'Sex':2,'Zip Code':3,'Military (1)':4,'Military (2)':5}
		self.num_tabs=len(self.tab_names)
		self.curr_tab_num=0

		self.done_dict={}
		for item in self.tab_names:
			self.done_dict[item]=False

		self.option_names_dict={'left_icon_Air Force':None,'left_icon_Army':None,'left_icon_Marines':None,'left_icon_Navy':None,'left_icon_Navy':None,'left_icon_Coast Guard':None,'left_icon_Space Force':None,'left_icon_N/A':None}

		self.wids=[]

		# Clock.schedule_once(self.get_wids,0.1)

	def get_wids(self,*args):
		print (args)
		print ('GET WIDS!!!!!!!!!!!!')
		self.wids.append(args[0])
		# print()
		# # for item in args[0].ids['_left_container'].walk():
		# for item in args[0].walk():
		#     try:
		#         if 'left_icon' in item.name:
		#             print (item.name)
		#             self.wids.append(item)
		#     except :
		#         pass
		#     # print (type(item))

			# print (item)
		print ('----')
			# try:
			#     if ('left_icon' in item.name):
			#         self.wids.append(item)
			# except:
			#     pass

		print (self.wids)

	def toggle_military_2(self,*args):
		# print(dir(args[0]))
		# print('children: ',(args[0].children))
		# # for item in args[0].walk():
		# #     print (item)
		# # print ()

		# for item in self.wids:
		#     print (item.name)
		#     if args[0]!=item:
		#         # try:
		#         item.icon='checkbox-blank-circle-outline'
		#         if item.icon=='circle-slice-8':
		#             item.icon='checkbox-blank-circle-outline'
		#         else:
		#             item.icon='circle-slice-8'
		#         # except:
		#         #     pass
		#     print ()

		# print (type(args[0].ids['_left_container'].walk))
		curr_icon=None

		for item in args[0].ids['_left_container'].walk():
			try:
				if ('left_icon' in item.name):
					self.option_names_dict[item.name]=item
					curr_icon=item.name
					if item.icon=='circle-slice-8':
						item.icon='checkbox-blank-circle-outline'
					else:
						item.icon='circle-slice-8'

						# print (item.name,dir(item))

						# for thing in item.ids:
						#     print (thing)
						# print(item.text_color)
						# print(item.theme_cls)
						# print(item.theme_text_color)
					break
			except:
				pass
		# print ('selected: ',curr_icon)


		for k,v in self.option_names_dict.items():
			if k!=curr_icon:
				try:
					v.icon='checkbox-blank-circle-outline'
				except:
					pass

	def on_checkbox_active(self, checkbox, value):
		if value:
			print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
		else:
			print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')

	def arrow_left(self):
		# if self.curr_tab_num==0:
		#     self.parent.transition.direction="right"
		#     self.parent.current="RiskAssesmentPage"
		# else:
		#     self.curr_tab_num-=1
		#     self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])
		arrow_left_global(self,"RiskAssesmentPage")

	def arrow_right(self):
		self.done_dict[self.tab_names[self.curr_tab_num]]=True
		if self.curr_tab_num==self.num_tabs-1:
			self.parent.transition.direction="left"
			self.parent.current="LocationPage"
		else:
			self.curr_tab_num+=1
			self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])


	def chevron_left(self):
		chevron_left_global(self)

	def on_pre_enter(self):
		self._keyboard = Window.request_keyboard(self.parent._keyboard_closed, self)
		self._keyboard.bind(on_key_up=self.parent._on_keyboard_up)
		Window.softinput_mode=''
		print (Window.softinput_mode)
		# Window.release_all_keyboards()

		self.vkeyboard = VKeyboard(on_key_up=self.parent._on_keyboard_up,target=self.ids.zip_code_work,docked=False,margin_hint=[0,0,0,0]
			)


		Window.release_all_keyboards()

		self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])


	def on_pre_leave(self):
		num_done=0
		total=0
		for k,v in self.done_dict.items():
			if v==True:
				num_done+=1
				total+=1
		print (num_done)
		pct=int(round(100*(num_done/self.num_tabs),0))
		pct_txt=str(pct)+'% Complete'
		print (pct)
		self.parent.ids['RiskAssesmentPage'].ids['SocioDemographicPage_label'].secondary_text=pct_txt
		self.parent.demographics_score=total

	def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
		count_icon = instance_tab.text
		# print it on shell/bash.
		# print(f"Welcome to {count_icon}' tab'")

		self.curr_tab_num=self.tab_num_dict[instance_tab.text]-1
		self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])

	def switch_tab_by_object(self):
		try:
			x = next(self.iter_list_objects)
			print(f"Switch slide by object, next element to show: [{x}]")
			self.root.ids.tabs.switch_tab(x)
		except StopIteration:
			# reset the iterator an begin again.
			self.iter_list_objects = iter(list(self.root.ids.tabs.get_tab_list()))
			self.switch_tab_by_object()

	def switch_tab_by_name(self):
		'''Switching the tab by name.'''
		try:
			x = next(self.iter_list_names)
			print(f"Switch slide by name, next element to show: [{x}]")
			self.root.ids.tabs.switch_tab(x)
		except StopIteration:
			# Reset the iterator an begin again.
			self.iter_list_names = iter(list(self.icons))
			self.switch_tab_by_name()



	def validate_text(self,*args):
		print (args[0])
		print (args[0].name)



	def on_numpad_press(self,*args):
		print(args)

		if self.ids['age_text_field'].text=='< MM / DD / YYYY >':
			self.ids['age_text_field'].text=''



		if args[0].text=='del':
			if len(self.ids['age_text_field'].text)>0:
				self.ids['age_text_field'].text=self.ids['age_text_field'].text[0:len(self.ids['age_text_field'].text)-1]
				if len(self.ids['age_text_field'].text)==0:
					self.ids['age_text_field'].text='< MM / DD / YYYY >'
		else:
			self.ids['age_text_field'].text+=args[0].text

# --------------------------------------------------------------------- #

class LocationPage(MDScreen):
	def __init__(self,**kwargs):
		super(LocationPage,self).__init__(**kwargs)
		self.option_names_dict={'left_icon_urban':None,'left_icon_large_rural':None,'left_icon_small_rural':None,'left_icon_isolated':None}

	def chevron_left(self):
		chevron_left_global(self)

	def next_question(self,*args):
		self.parent.ids['RiskAssesmentPage'].ids['location_label'].secondary_text='100% Complete'

	def arrow_right(self):
		pass

	def toggle(self,*args):


		# print (type(args[0].ids['_left_container'].walk))
		curr_icon=None

		for item in args[0].ids['_left_container'].walk():
			try:
				# print(item.name)
				if ('left_icon' in item.name):
					# print (dir(item))
					self.option_names_dict[item.name]=item
					curr_icon=item.name
					if item.icon=='circle-slice-8':
						item.icon='checkbox-blank-circle-outline'
					else:
						item.icon='circle-slice-8'
					break
			except:
				pass
		print ('selected: ',curr_icon)

		try:
			for k,v in self.option_names_dict.items():
				# print (k,v)
				if k!=curr_icon:
					v.icon='checkbox-blank-circle-outline'
		except:
			pass

# ===================================================================== #

class AirPollutionLandingPage(LandingPageTemplate):
	def __init__(self,**kwargs):
		super(AirPollutionLandingPage,self).__init__(**kwargs)

class AirPollutionPage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(AirPollutionPage,self).__init__(**kwargs)
		self.tab_names=['1','2','3','4','5','6','7']
		self.page_name='AirPollutionPage'
		self.prev_page="RiskAssesmentPage"
		self.next_page="AirPollutionScorePage"
		self.init_subpage()

	def button_press(self,num):
		print ("num: ",num)
		self.responses_dict[self.curr_tab_num+1]=int(num)
		self.done_dict[self.curr_tab_num+1]=True
		self.arrow_right()

class AirPollutionScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(AirPollutionScorePage,self).__init__(**kwargs)
		self.prev_page="AirPollutionPage"
		self.next_page="DietLandingPage"

# --------------------------------------------------------------------- #

class DietLandingPage(LandingPageTemplate):
	def __init__(self,**kwargs):
		super(DietLandingPage,self).__init__(**kwargs)

class DietAndFoodPage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(DietAndFoodPage,self).__init__(**kwargs)
		self.tab_names=['1','2','3','4','5','6','7','8','9','10','11']
		self.page_name='DietAndFoodPage'
		self.prev_page="DietLandingPage"
		self.next_page="DietScorePage"
		self.init_subpage()

class DietScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(DietScorePage,self).__init__(**kwargs)
		self.prev_page="DietAndFoodPage"
		self.next_page="PhysicalActivityPage"

	def reset_quiz(self):
		self.parent.ids.DietAndFoodPage.ids.android_tabs.switch_tab('1')
		self.parent.current='DietLandingPage'
		self.parent.transition.direction="right"


# --------------------------------------------------------------------- #

class PhysicalActivityPage(MDScreen):
	def __init__(self,**kwargs):
		super(PhysicalActivityPage,self).__init__(**kwargs)
		self.curr_tab_num=0
		self.tab_names=['1','2']
		self.num_tabs=len(self.tab_names)

	def chevron_left(self):
		chevron_left_global(self)

	def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
		on_tab_switch_global(self, instance_tabs, instance_tab, instance_tab_label, tab_text)

	def on_numpad_press(self,*args):
		print(args)

		if args[0].text=='del':
			if len(self.ids['mins_per_week1'].text)>0:
				self.ids['mins_per_week1'].text=self.ids['mins_per_week1'].text[0:len(self.ids['mins_per_week1'].text)-1]
		else:
			self.ids['mins_per_week1'].text+=args[0].text


	def arrow_left(self):
		arrow_left_global(self,"DietScorePage")

	def arrow_right(self,increment=True):
		arrow_right_global(self,"AlcoholUsagePage")

# --------------------------------------------------------------------- #

class AlcoholLandingPage(LandingPageTemplate):
	def __init__(self,**kwargs):
		super(AlcoholLandingPage,self).__init__(**kwargs)

class AlcoholUsagePage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(AlcoholUsagePage,self).__init__(**kwargs)
		self.tab_names=['1','2','3']
		self.page_name="AlcoholUsagePage"
		self.prev_page="AlcoholLandingPage"
		self.next_page="DepressionPage"
		self.init_subpage()

# --------------------------------------------------------------------- #

class DepressionPage(MDScreen):
	def __init__(self,**kwargs):
		super(DepressionPage,self).__init__(**kwargs)

		self.tab_names=['1','2']
		self.prev_page="AlcoholUsagePage"
		self.next_page="HyperTensionPage"

		self.init_subpage()

	def init_subpage(self):
		init_subpage_global(self)

	def chevron_left(self):
		chevron_left_global(self)

	def arrow_left(self):
		arrow_left_global(self,self.prev_page)

	def arrow_right(self):
		arrow_right_global(self,self.next_page)

	def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
		on_tab_switch_global(self, instance_tabs, instance_tab, instance_tab_label, tab_text)

# --------------------------------------------------------------------- #

class HyperTensionPage(MDScreen):
	def __init__(self,**kwargs):
		super(HyperTensionPage,self).__init__(**kwargs)

	def chevron_left(self):
		chevron_left_global(self)

# --------------------------------------------------------------------- #

class TraumaticBrainInjuryPage(MDScreen):
	def __init__(self,**kwargs):
		super(TraumaticBrainInjuryPage,self).__init__(**kwargs)

	def chevron_left(self):
		chevron_left_global(self)

# --------------------------------------------------------------------- #

class CognitiveDeclinePage(MDScreen):
	def __init__(self,**kwargs):
		super(CognitiveDeclinePage,self).__init__(**kwargs)

	def chevron_left(self):
		chevron_left_global(self)

# --------------------------------------------------------------------- #

class AboutPage(MDScreen):

	def chevron_left(self):
		self.parent.transition.direction = 'right'
		self.parent.current='LandingPage'

	def earth(self,instance, value):
		print(instance, value)
		# print (args)

# ----------------------------------------
class WindowManager(ScreenManager):
	def __init__(self,**kwargs):
		super(WindowManager,self).__init__(**kwargs)
		self.score_vars_dict={
			'LocationPage':0,
			'AirPollutionPage':0,
			'DietAndFoodPage':0,
			'AlcoholUsagePage':0,
			'DepressionPage':0,
			'HyperTensionPage':0,
			'TraumaticBrainInjuryPage':0,
			'CognitiveDeclinePage':0
		}

		self._keyboard=None
		Window.bind(on_resize=self.on_window_resize)
		self.on_pre_enter()

	def on_window_resize(self, window, width, height):
		print (width,height)

	def toggle_theme(self):
		self.parent.theme_cls='Dark'

	def _keyboard_closed(self):
		if self._keyboard!=None:
			self._keyboard.unbind(on_key_up=self._on_keyboard_up)
		self._keyboard = None

	def _on_keyboard_up(self, keyboard, keycode):#, text, modifiers):
		print(keyboard,keycode)
		if keycode[1]=='close':
			Window.release_all_keyboards()
		if keycode[1] == 'q':
			exit()
		if keycode[1] == 'h':
			self.current='LandingPage'

		if keycode[1] == 'l':
			self.current='LoadingPage'


	def on_pre_enter(self):
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
		self._keyboard.bind(on_key_up=self._on_keyboard_up)

class BlueSkyApp(MDApp):
	def __init__(self,**kwargs):
		super(BlueSkyApp,self).__init__(**kwargs)
		self.curr_state='close'

	def sidebar(self,dt=None):
		# self.root.current='LoadingPage'
		icons_item = {
			"home-outline": "Home",
			"account-outline": "Account",
			"brush": "Themes",
			"cogs": "Settings",
			"wrench-outline": "Developer",
			"upload": "Share",
			"exit-run": "Exit",
			"information-variant": "About",
		}

		for icon_name in icons_item.keys():
			self.root.ids['LandingPage'].ids['content_drawer'].ids['md_list'].add_widget(
				ItemDrawer(icon=icon_name, text=icons_item[icon_name]))

		Clock.schedule_once(self.SocioDemographicPage,0.1)

	def SocioDemographicPage(self,dt):
		print ('switching to SocioDemographicPage')
		self.root.current="SociodemographicPage"
		Clock.schedule_once(self.LocationPage,0.1)

	def LocationPage(self,dt):
		print ('switching to LocationPage')
		self.root.current="LocationPage"
		Clock.schedule_once(self.AirPollutionLandingPage,0.1)

	# --------------------------- Air Pollution --------------------------- #
	def AirPollutionLandingPage(self,dt):
		print ('switching to AirPollutionLandingPage')
		self.root.current='AirPollutionLandingPage'
		Clock.schedule_once(self.AirPollutionPage,0.1)

	def AirPollutionPage(self,dt):
		print ('switching to AirPollutionPage')
		self.root.current='AirPollutionPage'
		Clock.schedule_once(self.AirPollutionScorePage,0.1)

	def AirPollutionScorePage(self,dt):
		print ('switching to AirPollutionScorePage')
		self.root.current='AirPollutionScorePage'
		Clock.schedule_once(self.DietLandingPage,0.1)

	# --------------------------------------------------------------------- #

	def DietLandingPage(self,dt):
		print ('switching to DietLandingPage')
		self.root.current="DietLandingPage"
		Clock.schedule_once(self.DietAndFoodPage,0.1)

	def DietAndFoodPage(self,dt):
		print ('switching to DietAndFoodPage')
		self.root.current="DietAndFoodPage"
		Clock.schedule_once(self.DietScorePage,0.1)

	def DietScorePage(self,dt):
		print ('switching to DietScorePage')
		self.root.current="DietScorePage"
		Clock.schedule_once(self.PhysicalActivityPage,0.1)

	# --------------------------------------------------------------------- #

	def PhysicalActivityPage(self,dt):
		print ('switching to PhysicalActivityPage')
		self.root.current="PhysicalActivityPage"
		Clock.schedule_once(self.AlcoholUsagePage,0.1)

	# --------------------------------------------------------------------- #

	def AlcoholUsagePage(self,dt):
		print ('switching to AlcoholUsagePage')
		self.root.current="AlcoholUsagePage"
		Clock.schedule_once(self.AlcoholLandingPage,0.1)

	def AlcoholLandingPage(self,dt):
		print ('switching to AlcoholLandingPage')
		self.root.current="AlcoholLandingPage"
		Clock.schedule_once(self.DepressionPage,0.1)

	# --------------------------------------------------------------------- #

	def DepressionPage(self,dt):
		print ('switching to DepressionPage')
		self.root.current="DepressionPage"
		Clock.schedule_once(self.HyperTensionPage,0.1)

	# --------------------------------------------------------------------- #

	def HyperTensionPage(self,dt):
		print ('switching to HyperTensionPage')
		self.root.current="HyperTensionPage"
		Clock.schedule_once(self.TraumaticBrainInjuryPage,0.1)

	# --------------------------------------------------------------------- #

	def TraumaticBrainInjuryPage(self,dt):
		print ('switching to TraumaticBrainInjuryPage')
		self.root.current="TraumaticBrainInjuryPage"
		Clock.schedule_once(self.CognitiveDeclinePage,0.1)

	# --------------------------------------------------------------------- #


	def CognitiveDeclinePage(self,dt):
		print ('switching to CognitiveDeclinePage')
		self.root.current="CognitiveDeclinePage"
		Clock.schedule_once(self.LandingPage,0.1)

	# --------------------------------------------------------------------- #


	def LandingPage(self,dt):
		print ('switching to LandingPage')
		self.root.current="LandingPage"

	# --------------------------------------------------------------------- #

	def build(self):
		self.theme_cls.primary_palette = "BlueGray"
		self.theme_cls.primary_hue = "700"

		self.icon = 'logo5.png'
		# self.theme_cls.accent_palette = "Orange"
		# self.theme_cls.theme_style = "Dark"

		self.theme_cls.accent_palette = "Amber"
		self.theme_cls.theme_style = "Light"

		self.WindowManager=Builder.load_file(KV_FILE)
		self.title='Blue Sky'

		print (dir(self.theme_cls))
		print (self.theme_cls.primary_hue)
		print (self.theme_cls.primary_light_hue)
		print (self.theme_cls.sync_theme_styles)
		print (self.theme_cls.on_theme_style)
		print (self.theme_cls.colors['Light']['AppBar'])
		print (self.theme_cls.colors['Light']['StatusBar'])
		print (self.theme_cls.colors['Dark']['AppBar'])
		print (self.theme_cls.colors['Dark']['StatusBar'])

		# self.sidebar()
		Clock.schedule_once(self.sidebar, 1)
		# menu_items = [
		#     {
		#         "text": f"Item {i}",
		#         "viewclass": "OneLineListItem",
		#         "height": 56,
		#         "on_release": lambda x=f"Item {i}": self.menu_callback(x),
		#     } for i in range(5)
		# ]
		# self.menu = MDDropdownMenu(
		#     header_cls=MenuHeader(),
		#     caller=self.WindowManager.ids.button,
		#     items=menu_items,
		#     width_mult=4,
		# )
		# Clock.max_iteration=100
		# print (Clock.max_iteration)

		return self.WindowManager

	def menu_callback(self, text_item):
		print(text_item)

	def callback_2(self):
		print ('hello')

	def themer(self,*args):
		print ('themer')

		if self.theme_cls.theme_style=='Dark':
			self.root.ids['LandingPage'].ids['my_im'].source='pics/logo_minimal_white.png'

		elif self.theme_cls.theme_style=='Light':
			self.root.ids['LandingPage'].ids['my_im'].source='pics/logo_minimal.png'

	def show_theme_picker(self):
		theme_dialog = MDThemePicker(on_dismiss=self.themer)
		for item in theme_dialog.ids:
			print (item)

		for item in theme_dialog.ids['theme_tab'].walk():
			print (item)
		print ('---')
		for item in theme_dialog.ids['primary_box'].walk():
			print (item.ids)

		theme_dialog.open()

	def nav_handler(self):
		print ('nav_handler')
		self.root.ids['LandingPage'].ids['nav_drawer'].set_state("open")
		curr_state=self.root.ids['LandingPage'].ids['nav_drawer'].state

	def nav_closer(self,*args):
		print ('nav_closer')
		print(args)
		print(args[0].icon)
		print(args[0].text)

		selected_button=args[0].text

		print ('selected_button: ',selected_button)

		if selected_button=='About':
			self.root.current='AboutPage'


		elif selected_button=='Account':
			print ('log')
			self.root.current='LoginPage'
			self.root.transition.direction='left'

		elif selected_button=='Home':
			self.root.current='LandingPage'

		elif selected_button=='Exit':
			exit()

		# elif selected_button=='Developer':
		#     MDApp.open_settings(self.App)

		elif selected_button=='Themes':
			self.show_theme_picker()

		self.root.ids['LandingPage'].ids['nav_drawer'].set_state("close")
		curr_state=self.root.ids['LandingPage'].ids['nav_drawer'].state
		print(self.root.ids['LandingPage'].ids['nav_drawer'].status)
		print('curr_state: ',curr_state)
		print ()

	# def unhide(self):
	#     self.root.ids['DietAndFoodPage'].hide_widget(dohide=False)

class MenuHeader(MDBoxLayout):
	'''An instance of the class that will be added to the menu header.'''

if __name__=='__main__':
	# Config.set('kivy', 'keyboard_mode', 'systemandmulti')
	# Config.set("kivy", "keyboard_layout", 'numeric.json')
	BlueSkyApp().run()