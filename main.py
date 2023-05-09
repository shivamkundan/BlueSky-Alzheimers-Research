#!/usr/local/bin/python3
import os
# os.environ["KIVY_NO_CONSOLELOG"] = "1"

# import the kivy stuff
from kivy_imports import *

# import my stuff
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
		pgs=["LocationPage","AirPollutionPage","DietAndFoodPage","PhysicalActivityPage",\
			"AlcoholUsagePage","DepressionPage","HyperTensionPage","TraumaticBrainInjuryPage"]
		titles=["Location","Air Pollution","Diet & Food","Physical Activity","Alcohol Usage","Depression","Hypertension",
				"Traumatic Brain Injury"]

		# for second line text
		for page,text in zip(pgs,titles):
			if self.parent.ids[page].pct==100:
				C="#00FF00"
			else:
				C="#fcba03"
			self.ids[page+"_label"].text=f"[size=16sp]{text}\n[size=11sp][color={C}]{self.parent.ids[page].pct}% done[/color][/size]"

	def on_enter(self):
		temp=0
		for page,score in self.parent.score_vars_dict.items():
			temp+=score

		self.ids['score_label'].text=f"[b]{temp}[/b]"
		self.update_score()

	def chevron_left(self):
		chevron_left_global(self,next_pg='LandingPage')

# --------------------------------------------------------------------- #

class SociodemographicPage(SubPageTemplate):
	def __init__(self,**kwargs):
		super(SociodemographicPage,self).__init__(**kwargs)
		self.page_name='SociodemographicPage'
		self.prev_page="RiskAssesmentPage"
		self.next_page="SociodemographicPage_Age"
		self.total_score=0
		self.pct=0

		self.num_questions=1 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':'?',			'response':0,'completed':False}}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']


	# def on_numpad_press(self,*args):
	# 	print(args)

	# 	if self.ids['age_text_field'].text=='< MM / DD / YYYY >':
	# 		self.ids['age_text_field'].text=''

	# 	if args[0].text=='del':
	# 		if len(self.ids['age_text_field'].text)>0:
	# 			self.ids['age_text_field'].text=self.ids['age_text_field'].text[0:len(self.ids['age_text_field'].text)-1]
	# 			if len(self.ids['age_text_field'].text)==0:
	# 				self.ids['age_text_field'].text='< MM / DD / YYYY >'
	# 	else:
	# 		self.ids['age_text_field'].text+=args[0].text

class SociodemographicPage_Age(SubPageTemplate):
	def __init__(self,**kwargs):
		super(SociodemographicPage_Age,self).__init__(**kwargs)
		self.page_name='SociodemographicPage_Age'
		self.prev_page="SociodemographicPage"
		self.next_page="SociodemographicPage_Sex"
		self.total_score=0
		self.pct=0

		self.num_questions=1 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':'What is your age?',			'response':0,'completed':False}}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']

		self.score=0
		self.done=False



	def on_numpad_press(self,*args):
		# print(args)
		if self.ids['age_text_field'].text=='< Age >':
			self.ids['age_text_field'].text=''

		if args[0].text=="ENTER":
			self.arrow_right()

		elif args[0].text=='DEL':
			if self.ids['age_text_field'].text!='< Age >':
				if len(self.ids['age_text_field'].text)>0:
					self.ids['age_text_field'].text=self.ids['age_text_field'].text[0:len(self.ids['age_text_field'].text)-1]
					if len(self.ids['age_text_field'].text)==0:
						self.ids['age_text_field'].text='< Age >'
		else:
			self.ids['age_text_field'].text+=args[0].text

	def button_press(self,btn):
		print ("pressed: ")
		print (btn.text)
		# num=int(btn.text)
		# self.questions_dict[self.curr_question_num]['response']=num
		# self.questions_dict[self.curr_question_num]['completed']=True
		# self.arrow_right()

	def update_score(self):
		total=0
		pct_txt="0% done"
		if (self.done):
			total=self.total_score
			self.pct=100
			pct_txt="100% done"
		return total, pct_txt

class SociodemographicPage_Sex(SubPageTemplate):
	def __init__(self,**kwargs):
		super(SociodemographicPage_Sex,self).__init__(**kwargs)
		self.page_name='SociodemographicPage_Sex'
		self.prev_page="SociodemographicPage_Age"
		self.next_page="SociodemographicPage_Military"
		self.total_score=0
		self.pct=0

		self.num_questions=1 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':'?',			'response':0,'completed':False}}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']


	def button_press(self,btn):
		print (btn.text)
		self.arrow_right()

class SociodemographicPage_Military(SubPageTemplate):
	def __init__(self,**kwargs):
		super(SociodemographicPage_Military,self).__init__(**kwargs)
		self.page_name='SociodemographicPage_Military'
		self.prev_page="SociodemographicPage_Sex"
		self.next_page="SociodemographicPage_Military_2"
		self.total_score=0
		self.pct=0
		self.score=0 #dummy

		self.num_questions=1 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':'?',			'response':0,'completed':False}}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']

	def button_press(self,btn):
		print (btn.text)
		self.arrow_right()

class SociodemographicPage_Military_2(SubPageTemplate):
	def __init__(self,**kwargs):
		super(SociodemographicPage_Military_2,self).__init__(**kwargs)
		self.page_name='SociodemographicPage_Military_2'
		self.prev_page="SociodemographicPage_Military"
		self.next_page="LocationPage"
		self.total_score=0
		self.pct=0
		self.score=0 #dummy

		self.num_questions=1 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':'?',			'response':0,'completed':False}}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']

		self.options=['Air Force','Army','Marines','Navy','Coast Guard','Space Force','N/A']


	def button_press(self,btn):
		print (btn.text)
		self.arrow_right()

# --------------------------------------------------------------------- #

class LocationPage(SubPageBase):
	def __init__(self,**kwargs):
		super(LocationPage,self).__init__(**kwargs)
		self.option_names_dict={'left_icon_urban':None,'left_icon_large_rural':None,'left_icon_small_rural':None,'left_icon_isolated':None}
		self.prev_page="SociodemographicPage_Military_2"
		self.next_page="LocationScorePage"
		self.btn_names=["B1","B2","B3","B4"]
		self.btn_scores={"B1":4,"B2":3,"B3":2,"B4":1}
		self.total_score=0
		self.pct=0
		self.num_questions=1

		self.score=0 #dummy
		# self.questions_dict={0:{'q':"","completed":False,"response":0}}
		self.done=False

	def update_score(self):
		total=0
		pct_txt="0% done"
		if (self.done):
			total=self.total_score
			self.pct=100
			pct_txt="100% done"
		return total, pct_txt

	def toggle(self,btn,*args):
		self.done=True
		for b_name in self.btn_names:
			if (b_name==btn.name):
				self.ids[b_name].background_color=BTN_COLOR_PRESSED
			else:
				self.ids[b_name].background_color=BTN_COLOR


		self.total_score=self.btn_scores[btn.name]
		self.arrow_right()

	def on_pre_leave(self):
		self.total_score,pct_txt=self.update_score()
		print (f"total: {self.total_score}")
		print (pct_txt)
		self.parent.score_vars_dict[self.page_name]=self.total_score

class LocationScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(LocationScorePage,self).__init__(**kwargs)
		self.landing_page="LocationPage"
		self.prev_page="LocationPage"
		self.next_page="AirPollutionLandingPage"

	# def on_enter(self):
	# 	print (self.parent.ids[self.prev_page])
	# 	# self.ids['score_label'].text=str(self.parent.ids[self.prev_page].total_score)

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
		self.page_name='DietAndFoodPage'
		self.prev_page="DietLandingPage"
		self.next_page="DietScorePage"

		self.num_questions=11 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':f"Eat nuts or peanut butter\n[1/{self.num_questions}]",																	'response':0,'completed':False},
			1: {'q':f"Eat beans, peas, or lentilss\n[2/{self.num_questions}]",																'response':0,'completed':False},
			2: {'q':f"Eat eggssk\n[3/{self.num_questions}]",																'response':0,'completed':False},
			3: {'q':f"Eat pickles, olives, or other vegetables in brines\n[4/{self.num_questions}]",						'response':0,'completed':False},
			4: {'q':f"Eat at least 5 servings of fruits and vegetables\n[5/{self.num_questions}]",							'response':0,'completed':False},
			5: {'q':f"Eat at least 1 serving of fruiton mask\n[6/{self.num_questions}]",									'response':0,'completed':False},
			6: {'q':f"Eat at least 1 serving of vegetables\n[7/{self.num_questions}]",										'response':0,'completed':False},
			7: {'q':f"Drink milk (in a glass, with cereal, or in coffee, tea, or cocoa)\n[8/{self.num_questions}]",			'response':0,'completed':False},
			8: {'q':f"Eat broccoli, collard greens, spinach, potatoes, squash, or sweet potatoes\n[9/{self.num_questions}]",'response':0,'completed':False},
			9: {'q':f"Eat apples, bananas, oranges, melon, or raisins\n[10/{self.num_questions}]",							'response':0,'completed':False},
			10: {'q':f"Eat whole grain breads, cereals, grits, oatmeal, or brown rice\n[11/{self.num_questions}]",			'response':0,'completed':False},
		}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']

		self.init_my_subpage()

	def button_press(self,btn):
		print ("pressed: ")
		print (btn.text)
		num=int(btn.text)
		self.questions_dict[self.curr_question_num]['response']=num
		self.questions_dict[self.curr_question_num]['completed']=True
		self.arrow_right()

	def init_my_subpage(self):
		for item in self.ids:
			print (item)
		print()

	def arrow_right(self):
		print (self.questions_dict[self.curr_question_num])
		if self.curr_question_num<self.num_questions-1:
			self.curr_question_num+=1
			self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']
		else:
			self.parent.transition.direction="left"
			self.parent.current=self.next_page


	def on_pre_enter(self):
		self.curr_question_num=0
		self.ids['q_label'].text=""
		self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']

	# def button_press(self,btn):
	# 	num=btn.text
	# 	self.questions_dict[self.curr_question_num]['response']=num
	# 	self.questions_dict[self.curr_question_num]['completed']=True
	# 	self.arrow_right()

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

class PhysicalActivityScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(PhysicalActivityScorePage,self).__init__(**kwargs)
		self.landing_page="PhysicalActivityLandingPage"
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
		self.page_name="AlcoholUsagePage"
		self.prev_page="AlcoholLandingPage"
		self.next_page="AlcoholScorePage"

		self.num_questions=3 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':f"How often do you have a drink containing alcohol?\n[1/{self.num_questions}]",		'response':0,'completed':False},
			1: {'q':f"How many drinks containing alcohol do you have on a typical day when you are drinking?\n[2/{self.num_questions}]",	'response':0,'completed':False},
			2: {'q':f"How often do you have X (5 for men, 4 for women or men over age 65) or more drinks on one occasion?\n[3/{self.num_questions}]",					'response':0,'completed':False},
		}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']

	def arrow_right(self):
		print (self.questions_dict[self.curr_question_num])
		if self.curr_question_num<self.num_questions-1:
			self.curr_question_num+=1
			self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']
		else:
			self.parent.transition.direction="left"
			self.parent.current=self.next_page


	def on_pre_enter(self):
		self.curr_question_num=0
		self.ids['q_label'].text=""
		self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']

	def button_press(self,num):
		print ("pressed: ")
		print (num)
		self.questions_dict[self.curr_question_num]['response']=num
		self.questions_dict[self.curr_question_num]['completed']=True
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
		self.page_name='DepressionPage'
		self.prev_page="DepressionLandingPage"
		self.next_page="DepressionScorePage"

		self.num_questions=2 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':f"Little interest or pleasure in doing things\n[1/{self.num_questions}]",'response':0,'completed':False},
			1: {'q':f"Feeling down, depressed, or hopeless\n[2/{self.num_questions}]",		'response':0,'completed':False}
		}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']

	def arrow_right(self):
		print (self.questions_dict[self.curr_question_num])
		if self.curr_question_num<self.num_questions-1:
			self.curr_question_num+=1
			self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']
		else:
			self.parent.transition.direction="left"
			self.parent.current=self.next_page


	def on_pre_enter(self):
		self.curr_question_num=0
		# self.ids['q_label'].text=""
		self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']

	def button_press(self,num):
		print ("pressed: ")
		print (num)
		self.questions_dict[self.curr_question_num]['response']=num
		self.questions_dict[self.curr_question_num]['completed']=True
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
		self.pct=0

		self.btn_names=["Yes","No"]
		self.btn_scores={"Yes":0,"No":1}

		self.num_questions=2 # hard-coded for speedy initialization

		self.questions_dict={
			0: {'q':f"Have you ever been told by a doctor or other health professional that you had hypertension, also called high blood pressure?",'response':0,'completed':False},

		}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']

	def button_press(self,num):
		print ('pressed: ',num)
		self.total_score=int(num)
		self.pct_txt="100% Complete"
		self.arrow_right()

	def update_score(self):
		total=0
		pct_txt="0% done"
		if (self.done):
			total=self.total_score
			self.pct=100
			pct_txt="100% done"
		return total, pct_txt

	def toggle(self,btn,*args):
		self.done=True
		for b_name in self.btn_names:
			if (b_name==btn.text):
				self.ids[b_name].background_color=BTN_COLOR_PRESSED
			else:
				self.ids[b_name].background_color=BTN_COLOR


		self.total_score=self.btn_scores[btn.text]
		self.arrow_right()

	def on_pre_leave(self):
		self.total_score,pct_txt=self.update_score()
		print (f"total: {self.total_score}")
		print (pct_txt)
		self.parent.score_vars_dict[self.page_name]=self.total_score

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
		self.num_questions=5 # hard-coded for speedy initialization

		self.pct=0

		self.questions_dict={
			0: {'q':f"Have you ever hit your head or been hit on the head? Think about all incidents that my have occurred at any age, even those that did not seem serious, including vehicle accidents, falls, assault, abuse, sports, etc. A traumatic brain injury can also occur from violent shaking of the head, such as being shaken as a baby or child.\n[1/{self.num_questions}]",'response':0,'completed':False},
			1: {'q':f"Were you ever seen in the emergency room, hospital, or by a doctor because of an injury to your head?\n[2/{self.num_questions}]",'response':0,'completed':False},
			2: {'q':f"Did you ever lose consciousness or experience a period of being dazed and confused because of an injury to your head? People with traumatic brain injury may not lose consciousness but experience an \'alteration of consciousness\', which may include feeling dazed, confused, or disoriented at the time of injury, or being unable to remember the events surrounding the injury.\n[3/{self.num_questions}]",'response':0,'completed':False},
			3: {'q':f"Do you experience any of these problems in your daily life since you hit your head?\n[4/{self.num_questions}]",'response':0,'completed':False},
			4: {'q':f"Any significant sicknesses? Traumatic brain injury implies a physical blow to the head, but acquired brain injury may also be caused by medical conditions, such as brain tumor, meningitis, West Nile virus, stroke, seizures, or instances of oxygen deprivation following a heart attack, carbon monoxide poisoning, near drowning, or near suffocation.\n[5/{self.num_questions}]",'response':0,'completed':False},

		}

		self.curr_question_num=0
		self.curr_question=self.questions_dict[0]['q']



	def on_pre_enter(self):
		self.curr_question_num=0
		# self.ids['q_label'].text=""
		self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']

	def button_press(self,num):
		print ("pressed: ")
		print (num)
		self.questions_dict[self.curr_question_num]['response']=num
		self.questions_dict[self.curr_question_num]['completed']=True
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
		self.tab_names=['1']
		self.num_tabs=len(self.tab_names)
		self.page_name='CognitiveDeclinePage'
		self.prev_page="CognitiveDeclineLandingPage"
		self.next_page="CognitiveDeclineScorePage"
		self.curr_tab_num=1
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
		self.parent.transition.direction="left"
		self.parent.current=self.next_page
	# 	# else:
	# 	# 	self.curr_tab_num+=1
	# 	# 	self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])
	# 	# self.validate_text()
	# 	# print (self.ids['year'].text)

class CognitiveDeclineScorePage(ScorePageTemplate):
	def __init__(self,**kwargs):
		super(CognitiveDeclineScorePage,self).__init__(**kwargs)
		self.landing_page="CognitiveDeclineLandingPage"
		self.prev_page="CognitiveDeclinePage"
		self.next_page="RiskAssesmentPage"

	def arrow_right(self):
		self.parent.transition.direction="right"
		self.parent.current=self.next_page

# --------------------------------------------------------------------- #

class AboutPage(Screen):
	def __init__(self,**kwargs):
		super(AboutPage,self).__init__(**kwargs)
		self.prev_page="LandingPage"

	def chevron_left(self):
		self.parent.transition.direction = 'right'
		self.parent.current=self.prev_page

class EducationalResourcesPage(Screen):
	def __init__(self,**kwargs):
		super(EducationalResourcesPage,self).__init__(**kwargs)
		self.prev_page="LandingPage"

	def chevron_left(self):
		self.parent.transition.direction = 'right'
		self.parent.current=self.prev_page

class CognitiveRehabPage(Screen):
	def __init__(self,**kwargs):
		super(CognitiveRehabPage,self).__init__(**kwargs)
		self.prev_page="LandingPage"

	def chevron_left(self):
		self.parent.transition.direction = 'right'
		self.parent.current=self.prev_page

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

		self.BG_COLOR="WHITE"
		Window.clearcolor=(1,1,1,1)

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
			I='pics/logo_minimal.png'
			C=BLACK

		else:
			self.BG_COLOR="BLACK"
			Window.clearcolor=BLACK
			I='pics/logo_minimal_white.png'
			C=WHITE

		self.WindowManager.get_screen("LandingPage").ids["my_im"].source=I
		self.WindowManager.get_screen("LandingPage").ids["landing_page_bottom_label"].color=C

		self.WindowManager.get_screen("RiskAssesmentPage").ids["score_label"].color=C
		t=type(Label(text=""))


		t1=self.WindowManager.get_screen("AirPollutionLandingPage").ids["label1"].__class__

		# toggle label text colors in all screen
		for s in self.WindowManager.screen_names:
			curr=self.WindowManager.get_screen(s)
			# print(curr)
			for w in [widget for widget in curr.walk(loopback=True)]:
				if (type(w)==t) or (type(w)==t1):
					# print (t1)
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