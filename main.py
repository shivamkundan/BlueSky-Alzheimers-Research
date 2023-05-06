#!/usr/local/bin/python3
import os
# os.environ["KIVY_NO_CONSOLELOG"] = "1"

# import the kivy stuff
from kivy_imports import *

from globals import *
from object_defs import *
from page_templates import *

from datetime import datetime
import time
# import webbrowser

KV_FILE='health_app.kv' # kivy design file

# MAX_SIZE = (1280, 800)
# Config.set('graphics', 'width', MAX_SIZE[0])
# Config.set('graphics', 'height', MAX_SIZE[1])

# # These resolutions are in software pixels
# resolutions=[(330, 550),(390, 844),(400, 667),(412,732),(1280,800)]
# Window.size = resolutions[2]

LOADING_PAGE_PAUSE_SECONDS=1

# ===================================================================== #
class LoadingPage(Screen):
	def __init__(self,**kwargs):
		super(LoadingPage,self).__init__(**kwargs)

	def animate_logo(self,widget,*args):
		print(widget,args)

		# for item in widget.ids:
		#     print (item)
		print("size: ",(self.ids['my_im'].size[0]//2,self.ids['my_im'].size[1]//2))
		anim=Animation(size=(self.ids['my_im'].size[0]//2,self.ids['my_im'].size[1]//2))
		# anim=Animation(anchor_x='top',anchor_y='center')
		anim.start(self.ids['my_im'])

	def transitioner(self,dt):
		# self.parent.transition=FadeTransition()
		self.parent.current='LandingPage'

	# def on_enter(self):
	# 	# Clock.schedule_once(self.transitioner,LOADING_PAGE_PAUSE_SECONDS)
	# 	# self.ids['prog'].start()
	# 	# self.parent.current='LandingPage'
	# 	for item in self.ids:
	# 		print(item)

class LandingPage(Screen):
	def __init__(self,**kwargs):
		super(LandingPage,self).__init__(**kwargs)
		self.prev_page="LandingPage"

	# def chevron_left(self,*args):
	# 	self.parent.transition.direction="right"
	# 	self.parent.current='RiskAssesmentPage'

class LoginPage(Screen):
	def __init__(self,**kwargs):
		super(LoginPage,self).__init__(**kwargs)
		self.dialog=False
		self.prev_page="LandingPage"

	def chevron_left(self):
		chevron_left_global(self,next_pg='LandingPage')

	def show_alert_dialog(self,*args):
		print (args)
		print ("show_alert_dialog")
		# if not self.dialog:
		# 	self.dialog = MDDialog(
		# 		text="This feature has not been implemented yet",
		# 		buttons=[Button(text="close",on_release=self.close_dialog),
		# 			# MDFlatButton(text="DISCARD",),
		# 			],
		# 	)
		# self.dialog.open()

	def close_dialog(self,*args):
		self.dialog.dismiss()

# --------------------------------------------------------------------- #

class RiskAssesmentPage(Screen):
	def __init__(self,**kwargs):
		super(RiskAssesmentPage,self).__init__(**kwargs)
		self.prev_page="LandingPage"

	def update_score(self):
		pgs=["AirPollutionPage","DietAndFoodPage","PhysicalActivityPage",\
			"AlcoholUsagePage"]
		titles=["Air Pollution","Diet & Food","Physical Activity","Alcohol Usage"]

		for p,t in zip(pgs,titles):
			self.ids[p+"_label"].text=f"{t} [{self.parent.ids[p].pct}% complete]"

	def on_enter(self):
		temp=0
		for page,score in self.parent.score_vars_dict.items():
			temp+=score
		self.ids['score_label'].text=str(temp)
		self.update_score()


	def chevron_left(self):
		chevron_left_global(self,next_pg='LandingPage')

# --------------------------------------------------------------------- #

class SociodemographicPage(Screen):
	def __init__(self,**kwargs):
		super(SociodemographicPage,self).__init__(**kwargs)
		self.tab_names=['Age','Sex','Zip Code','Military (1)','Military (2)']
		self.tab_num_dict={'Age':1,'Sex':2,'Zip Code':3,'Military (1)':4,'Military (2)':5}
		self.num_tabs=len(self.tab_names)
		self.curr_tab_num=0
		self.prev_page="LandingPage"

		self.done_dict={}
		for item in self.tab_names:
			self.done_dict[item]=False

		self.option_names_dict={'left_icon_Air Force':None,'left_icon_Army':None,'left_icon_Marines':None,'left_icon_Navy':None,'left_icon_Navy':None,'left_icon_Coast Guard':None,'left_icon_Space Force':None,'left_icon_N/A':None}

		self.wids=[]

		# Clock.schedule_once(self.get_wids,0.1)

	def get_wids(self,*args):
		# print (args)
		# print ('GET WIDS!!!!!!!!!!!!')
		self.wids.append(args[0])
		# # print()
		# # # for item in args[0].ids['_left_container'].walk():
		# # for item in args[0].walk():
		# #     try:
		# #         if 'left_icon' in item.name:
		# #             print (item.name)
		# #             self.wids.append(item)
		# #     except :
		# #         pass
		# #     # print (type(item))

		# 	# print (item)
		# print ('----')
		# 	# try:
		# 	#     if ('left_icon' in item.name):
		# 	#         self.wids.append(item)
		# 	# except:
		# 	#     pass

		# print (self.wids)

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
		if self.curr_tab_num==0:
			self.parent.transition.direction="right"
			self.parent.current="RiskAssesmentPage"
		else:
			self.curr_tab_num-=1
			# self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])

	def arrow_right(self):
		self.done_dict[self.tab_names[self.curr_tab_num]]=True
		if self.curr_tab_num==self.num_tabs-1:
			self.parent.transition.direction="left"
			self.parent.current="LocationPage"
		else:
			self.curr_tab_num+=1
			# self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])


	def chevron_left(self):
		chevron_left_global(self)

	def on_pre_enter(self):
		self._keyboard = Window.request_keyboard(self.parent._keyboard_closed, self)
		self._keyboard.bind(on_key_up=self.parent._on_keyboard_up)
		Window.softinput_mode=''
		print (Window.softinput_mode)
		# Window.release_all_keyboards()

		# self.vkeyboard = VKeyboard(on_key_up=self.parent._on_keyboard_up,target=self.ids.zip_code_work,docked=False,margin_hint=[0,0,0,0])
		Window.release_all_keyboards()
		# self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])


	def on_pre_leave(self):
		num_done=0
		total=0
		for k,v in self.done_dict.items():
			if v==True:
				num_done+=1
				total+=1
		# print (num_done)
		pct=int(round(100*(num_done/self.num_tabs),0))
		pct_txt=str(pct)+'% Complete'
		# print (pct)
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

class LocationPage(Screen):
	def __init__(self,**kwargs):
		super(LocationPage,self).__init__(**kwargs)
		self.option_names_dict={'left_icon_urban':None,'left_icon_large_rural':None,'left_icon_small_rural':None,'left_icon_isolated':None}
		self.prev_page="LandingPage"

	def chevron_left(self):
		chevron_left_global(self)

	def next_question(self,*args):
		self.parent.ids['RiskAssesmentPage'].ids['location_label'].secondary_text='100% Complete'

	def arrow_right(self):
		pass

	def toggle(self,*args):

		print ("toggle function")
		# # print (type(args[0].ids['_left_container'].walk))
		# curr_icon=None

		# for item in args[0].ids['_left_container'].walk():
		# 	try:
		# 		# print(item.name)
		# 		if ('left_icon' in item.name):
		# 			# print (dir(item))
		# 			self.option_names_dict[item.name]=item
		# 			curr_icon=item.name
		# 			if item.icon=='circle-slice-8':
		# 				item.icon='checkbox-blank-circle-outline'
		# 			else:
		# 				item.icon='circle-slice-8'
		# 			break
		# 	except:
		# 		pass
		# print ('selected: ',curr_icon)

		# try:
		# 	for k,v in self.option_names_dict.items():
		# 		# print (k,v)
		# 		if k!=curr_icon:
		# 			v.icon='checkbox-blank-circle-outline'
		# except:
		# 	pass

# ===================================================================== #

class AirPollutionLandingPage(SubPageBase):
	def __init__(self,**kwargs):
		super(AirPollutionLandingPage,self).__init__(**kwargs)
		self.prev_page="LocationPage"
		self.next_page="AirPollutionPage"

class AirPollutionPage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(AirPollutionPage,self).__init__(**kwargs)
		# self.tab_names=['1','2','3','4','5','6','7']
		self.page_name='AirPollutionPage'
		self.prev_page="AirPollutionLandingPage"
		self.next_page="AirPollutionScorePage"
		self.total_score=0
		self.pct=0

		self.num_questions=7 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':'I expect to wear a pollution mask\n[1/7]',			'response':0,'completed':False},
			1: {'q':'I want to wear a pollution mask\n[2/7]',			'response':0,'completed':False},
			2: {'q':'I intend to wear a pollution mask\n[3/7]',			'response':0,'completed':False},
			3: {'q':'I choose to wear a pollution mask\n[4/7]',			'response':0,'completed':False},
			4: {'q':'I will wear a pollution mask\n[5/7]',				'response':0,'completed':False},
			5: {'q':'I would be better wearing a pollution mask\n[6/7]','response':0,'completed':False},
			6: {'q':'I prefer wearing a pollution mask\n[7/7]',			'response':0,'completed':False},
		}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']

		# self.init_subpage()

	def reset(self):
		for i in range (self.num_questions):
			self.questions_dict[i]['completed']=False
			self.questions_dict[i]['response']=0
		self.curr_question_num=0

	def button_press(self,num):
		print ("num: ",num)
		self.questions_dict[self.curr_question_num]['response']=num
		self.questions_dict[self.curr_question_num]['completed']=True
		self.arrow_right()

	def arrow_right(self):
		print (self.questions_dict[self.curr_question_num])
		if self.curr_question_num<self.num_questions-1:
			self.curr_question_num+=1
			self.ids['air_pollution_q_label'].text=self.questions_dict[self.curr_question_num]['q']
		else:
			self.parent.transition.direction="left"
			self.parent.current=self.next_page


	def arrow_left(self):
		print (self.questions_dict[self.curr_question_num])
		if self.curr_question_num>0:
			self.curr_question_num-=1
			self.ids['air_pollution_q_label'].text=self.questions_dict[self.curr_question_num]['q']
		else:
			self.parent.transition.direction="right"
			self.parent.current=self.prev_page

	def on_pre_enter(self):
		self.curr_question_num=0
		self.ids['air_pollution_q_label'].text=self.questions_dict[self.curr_question_num]['q']

	def update_score(self):
		total=0
		num_done=0
		for i in range (self.num_questions):
			if self.questions_dict[i]['completed']:
				total+=self.questions_dict[i]['response']
				num_done+=1

		pct=int(round(100*(num_done/self.num_questions),0))
		self.pct=pct
		pct_txt=str(pct)+'% Complete'
		# self.parent.ids[self.next_page].score=total
		# self.parent.ids[self.next_page].score=total
		print (f"fself.parent.ids[self.next_page].score: {self.parent.ids[self.next_page].score}")
		return total, pct_txt

	def on_pre_leave(self):
		self.total_score,pct_txt=self.update_score()
		print (f"total: {self.total_score}")
		print (pct_txt)
		self.parent.score_vars_dict[self.page_name]=self.total_score
		# self.parent.ids['RiskAssesmentPage'].ids[self.name+"_label"].secondary_text=pct_txt


class AirPollutionScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(AirPollutionScorePage,self).__init__(**kwargs)
		self.landing_page="AirPollutionLandingPage"
		self.prev_page="AirPollutionPage"
		self.next_page="DietLandingPage"

# --------------------------------------------------------------------- #

class DietLandingPage(SubPageBase):
	def __init__(self,**kwargs):
		super(DietLandingPage,self).__init__(**kwargs)
		self.prev_page="AirPollutionScorePage"
		self.next_page="DietAndFoodPage"

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
		self.landing_page="DietLandingPage"
		self.prev_page="DietAndFoodPage"
		self.next_page="PhysicalActivityLandingPage"

# --------------------------------------------------------------------- #

class PhysicalActivityLandingPage(SubPageBase):
	def __init__(self,**kwargs):
		super(PhysicalActivityLandingPage,self).__init__(**kwargs)
		self.prev_page="DietScorePage"
		self.next_page="PhysicalActivityPage"

class PhysicalActivityPage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(PhysicalActivityPage,self).__init__(**kwargs)

		self.tab_names=['1','2']

		self.page_name="PhysicalActivityPage"
		self.prev_page="PhysicalActivityLandingPage"
		self.next_page="PhysicalActivityScorePage"
		self.init_subpage()


	def validate_text(self,*args):
		print (args[0])
		print (args[0].name)

	def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):


		if self.curr_tab_num==0:
			txtbox=self.ids['mins_per_week1']
		elif self.curr_tab_num==1:
			txtbox=self.ids['mins_per_week2']


	def on_numpad_press(self,*args):

		if self.curr_tab_num==0:
			tab=self.ids['mins_per_week1']
		elif self.curr_tab_num==1:
			tab=self.ids['mins_per_week2']

		if args[0].text=='del':
			if len(tab.text)>0:
				tab.text=tab.text[0:len(tab.text)-1]
		else:
			tab.text+=args[0].text


class PhysicalActivityScorePage(SubPageBase):
	def __init__(self,**kwargs):
		super(PhysicalActivityScorePage,self).__init__(**kwargs)
		self.prev_page="PhysicalActivityPage"
		self.next_page="AlcoholLandingPage"

# --------------------------------------------------------------------- #

class AlcoholLandingPage(SubPageBase):
	def __init__(self,**kwargs):
		super(AlcoholLandingPage,self).__init__(**kwargs)
		self.prev_page="PhysicalActivityScorePage"
		self.next_page="AlcoholUsagePage"

class AlcoholUsagePage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(AlcoholUsagePage,self).__init__(**kwargs)
		self.tab_names=['1','2','3']
		self.page_name="AlcoholUsagePage"
		self.prev_page="AlcoholLandingPage"
		self.next_page="AlcoholScorePage"
		self.init_subpage()

	def button_press(self,num):
		print ("num: ",num)
		self.responses_dict[self.curr_tab_num+1]=int(num)
		self.done_dict[self.curr_tab_num+1]=True
		self.arrow_right()

class AlcoholScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(AlcoholScorePage,self).__init__(**kwargs)
		self.landing_page="AlcoholLandingPage"
		self.prev_page="AlcoholUsagePage"
		self.next_page="DepressionLandingPage"

# --------------------------------------------------------------------- #

class DepressionLandingPage(SubPageBase):
	def __init__(self,**kwargs):
		super(DepressionLandingPage,self).__init__(**kwargs)
		self.prev_page="AlcoholScorePage"
		self.next_page="DepressionPage"

class DepressionPage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(DepressionPage,self).__init__(**kwargs)

		self.tab_names=['1','2']
		self.page_name='DepressionPage'
		self.prev_page="DepressionLandingPage"
		self.next_page="DepressionScorePage"

		self.init_subpage()

	def button_press(self,num):
		print ("num: ",num)
		self.responses_dict[self.curr_tab_num+1]=int(num)
		self.done_dict[self.curr_tab_num+1]=True
		self.arrow_right()

class DepressionScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(DepressionScorePage,self).__init__(**kwargs)
		self.landing_page="DepressionLandingPage"
		self.prev_page="DepressionPage"
		self.next_page="HyperTensionLandingPage"

# --------------------------------------------------------------------- #
class HyperTensionLandingPage(SubPageBase):
	def __init__(self,**kwargs):
		super(HyperTensionLandingPage,self).__init__(**kwargs)
		self.prev_page="DepressionScorePage"
		self.next_page="HyperTensionPage"

class HyperTensionPage(SubPageBase):
	def __init__(self,**kwargs):
		super(HyperTensionPage,self).__init__(**kwargs)
		self.page_name="HyperTensionPage"
		self.prev_page="HyperTensionLandingPage"
		self.next_page="HyperTensionScorePage"
		self.total_score=0
		self.pct_txt="0% Complete"

	def button_press(self,num):
		print ('pressed: ',num)
		self.total_score=int(num)
		self.pct_txt="100% Complete"
		self.arrow_right()

	def on_pre_leave(self):
		self.parent.score_vars_dict[self.page_name]=self.total_score
		self.parent.ids['RiskAssesmentPage'].ids[self.name+"_label"].secondary_text=self.pct_txt

class HyperTensionScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(HyperTensionScorePage,self).__init__(**kwargs)
		self.landing_page="HyperTensionLandingPage"
		self.prev_page="HyperTensionPage"
		self.next_page="TraumaticBrainInjuryLandingPage"

# --------------------------------------------------------------------- #

class TraumaticBrainInjuryLandingPage(SubPageBase):
	def __init__(self,**kwargs):
		super(TraumaticBrainInjuryLandingPage,self).__init__(**kwargs)
		self.prev_page="HyperTensionScorePage"
		self.next_page="TraumaticBrainInjuryPage"

class TraumaticBrainInjuryPage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(TraumaticBrainInjuryPage,self).__init__(**kwargs)
		self.tab_names=['1','2','3','4','5']
		self.page_name='TraumaticBrainInjuryPage'
		self.prev_page="TraumaticBrainInjuryLandingPage"
		self.next_page="TraumaticBrainInjuryScorePage"
		self.init_subpage()

	def button_press(self,num):
		print ("num: ",num)
		self.responses_dict[self.curr_tab_num+1]=int(num)
		self.done_dict[self.curr_tab_num+1]=True
		self.arrow_right()

class TraumaticBrainInjuryScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(TraumaticBrainInjuryScorePage,self).__init__(**kwargs)
		self.landing_page="TraumaticBrainInjuryLandingPage"
		self.prev_page="TraumaticBrainInjuryPage"
		self.next_page="CognitiveDeclineLandingPage"

# --------------------------------------------------------------------- #
class CognitiveDeclineLandingPage(SubPageBase):
	def __init__(self,**kwargs):
		super(CognitiveDeclineLandingPage,self).__init__(**kwargs)
		self.prev_page="TraumaticBrainInjuryScorePage"
		self.next_page="CognitiveDeclinePage"

class CognitiveDeclinePage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(CognitiveDeclinePage,self).__init__(**kwargs)
		self.tab_names=['1','2','3']
		self.num_tabs=len(self.tab_names)
		self.page_name='CognitiveDeclinePage'
		self.prev_page="CognitiveDeclineLandingPage"
		self.next_page="CognitiveDeclineScorePage"

		self.total_score=0

	def validate_text(self,*args):
		print (args)
		print (args[0])
		print (args[0].name)
		print (args[0].text)

	def on_numpad_press(self,*args):
		if args[0].text=='del':
			if len(self.ids['year'].text)>0:
				self.ids['year'].text=self.ids['year'].text[0:len(self.ids['year'].text)-1]
		else:
			self.ids['year'].text+=args[0].text

	def arrow_right(self):
		print ("arrow_right")
		# if self.curr_tab_num==self.num_tabs-1:
		# 	self.parent.transition.direction="left"
		# 	self.parent.current=self.next_page
		# else:
		# 	self.curr_tab_num+=1
		# 	self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])
		# self.validate_text()
		# print (self.ids['year'].text)

class CognitiveDeclineScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(CognitiveDeclineScorePage,self).__init__(**kwargs)
		self.landing_page="CognitiveDeclineLandingPage"
		self.prev_page="CognitiveDeclinePage"
		self.next_page="RiskAssesmentPage"

# --------------------------------------------------------------------- #

class AboutPage(Screen):
	def __init__(self,**kwargs):
		super(AboutPage,self).__init__(**kwargs)
		self.prev_page="LandingPage"

	def chevron_left(self):
		self.parent.transition.direction = 'right'
		self.parent.current='LandingPage'

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
		Window.bind(on_keyboard=self._on_keyboard_up)
		# self.on_pre_enter()

	def _keyboard_closed(self):
		if self._keyboard!=None:
			self._keyboard.unbind(on_key_up=self._on_keyboard_up)
		self._keyboard = None

	def _on_keyboard_up(self, keyboard, keycode,*largs):#, text, modifiers):
		if keycode=='close':
			Window.release_all_keyboards()
		if keycode == KEY_Q:
			exit()
		if keycode == KEY_H:
			self.current='LandingPage'

		# Same as android 'back' key
		if keycode == KEY_ESC:
			print(f"self.current: {self.current}")
			self.transition.direction = 'right'
			if (self.current in ["RiskAssesmentPage","LoginPage","AboutPage"]):
				self.current="LandingPage"
			# elif (self.current=="LandingPage"):
			# 	exit()
			else:
				self.current="RiskAssesmentPage" # all other pages return to risk assesment

	def on_pre_enter(self):
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
		self._keyboard.bind(on_key_up=self._on_keyboard_up)

class BlueSkyApp(App):
	def __init__(self,**kwargs):
		super(BlueSkyApp,self).__init__(**kwargs)
		self.curr_state='close'

		self.BG_COLOR="BLACK"
		Window.clearcolor=(0,0,0,1)

	# --------------------------------------------------------------------- #

	def build(self):
		self.WindowManager=Builder.load_file(KV_FILE)
		self.title='Blue Sky'
		return self.WindowManager


	def toggle_theme(self):

		WHITE=(1,1,1,1)
		BLACK=(0,0,0,1)
		# bg color and logo path
		if (self.BG_COLOR=="BLACK"):
			self.BG_COLOR="WHITE"
			Window.clearcolor=WHITE
			App.get_running_app().root.ids["LandingPage"].ids["my_im"].source='pics/logo_minimal.png'
			App.get_running_app().root.ids["LandingPage"].ids["landing_page_bottom_label"].color=BLACK

			# App.get_running_app().root.ids["AirPollutionLandingPage"].ids["label1"].color=BLACK
			# App.get_running_app().root.ids["AirPollutionLandingPage"].ids["label2"].color=BLACK

			# App.get_running_app().root.ids["AirPollutionPage"].ids["label1"].color=BLACK
			# App.get_running_app().root.ids["AirPollutionPage"].ids["air_pollution_q_label"].color=BLACK
			C=BLACK

		else:
			self.BG_COLOR="BLACK"
			Window.clearcolor=BLACK
			App.get_running_app().root.ids["LandingPage"].ids["my_im"].source='pics/logo_minimal_white.png'
			App.get_running_app().root.ids["LandingPage"].ids["landing_page_bottom_label"].color=WHITE
			C=WHITE
			# App.get_running_app().root.ids["AirPollutionLandingPage"].ids["label1"].color=WHITE
			# App.get_running_app().root.ids["AirPollutionLandingPage"].ids["label2"].color=WHITE

			# App.get_running_app().root.ids["AirPollutionPage"].ids["label1"].color=WHITE
			# App.get_running_app().root.ids["AirPollutionPage"].ids["air_pollution_q_label"].color=WHITE


		# self.WindowManager.get_screen('AirPollutionPage').ids["air_pollution_q_label"].color=(1,0,0,1)
		# print ("----->",App.get_running_app().root.ids["AirPollutionPage"].ids["air_pollution_q_label"].color)
		# print ("----->",self.WindowManager.get_screen('AirPollutionPage').ids["air_pollution_q_label"].color)

		t=type(Label(text=""))
		print(dir(t))
		# print(self.WindowManager.screen_names)

		for s in self.WindowManager.screen_names:
			curr=self.WindowManager.get_screen(s)
			print(curr)
			for w in [widget for widget in curr.walk(loopback=True)]:
				if type(w)==t:
					w.color=C


		# reload image
		App.get_running_app().root.ids["LandingPage"].ids["my_im"].reload()


if __name__=='__main__':
	# Config.set('kivy', 'keyboard_mode', 'systemandmulti')
	# Config.set("kivy", "keyboard_layout", 'numeric.json')
	try:
		BlueSkyApp().run()
	except KeyboardInterrupt:
		print ("KeyboardInterrupt\n exiting")
		exit()