from kivy_imports import *
from kivy.properties import StringProperty
from kivy.graphics import Color
from kivy.graphics import RoundedRectangle


# ===================================================================== #
# class QuestionsPage(SubPageTemplate):
# 	def __init__(self,**kwargs):
# 		super(QuestionsPage,self).__init__(**kwargs)
# 		self.prev_page=None
# 		self.next_page=None
# 		self.total_score=0
# 		self.pct=0
# 		self.num_questions=1 # hard-coded for speedy initialization

# 		self.questions_dict={
# 			0: {'q':'Example question\n[1/7]',			'response':0,'completed':False},
# 		}
# 		self.curr_question_num=0
# 		self.curr_question=self.questions_dict[0]['q']

# 		# self.init_subpage()

# 	def reset(self):
# 		for i in range (self.num_questions):
# 			self.questions_dict[i]['completed']=False
# 			self.questions_dict[i]['response']=0
# 		self.curr_question_num=0

# 	def button_press(self,num):
# 		print ("num: ",num)
# 		self.questions_dict[self.curr_question_num]['response']=num
# 		self.questions_dict[self.curr_question_num]['completed']=True
# 		self.arrow_right()

# 	def arrow_right(self):
# 		print (self.questions_dict[self.curr_question_num])
# 		if self.curr_question_num<self.num_questions-1:
# 			self.curr_question_num+=1
# 			self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']
# 		else:
# 			self.parent.transition.direction="left"
# 			self.parent.current=self.next_page


# 	def arrow_left(self):
# 		print (self.questions_dict[self.curr_question_num])
# 		if self.curr_question_num>0:
# 			self.curr_question_num-=1
# 			self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']
# 		else:
# 			self.parent.transition.direction="right"
# 			self.parent.current=self.prev_page

# 	def on_pre_enter(self):
# 		self.curr_question_num=0
# 		self.ids['q_label'].text=self.questions_dict[self.curr_question_num]['q']

# 	def update_score(self):
# 		total=0
# 		num_done=0
# 		for i in range (self.num_questions):
# 			if self.questions_dict[i]['completed']:
# 				total+=self.questions_dict[i]['response']
# 				num_done+=1

# 		pct=int(round(100*(num_done/self.num_questions),0))
# 		self.pct=pct
# 		pct_txt=str(pct)+'% Complete'
# 		# self.parent.ids[self.next_page].score=total
# 		# self.parent.ids[self.next_page].score=total
# 		print (f"fself.parent.ids[self.next_page].score: {self.parent.ids[self.next_page].score}")
# 		return total, pct_txt

# 	def on_pre_leave(self):
# 		self.total_score,pct_txt=self.update_score()
# 		print (f"total: {self.total_score}")
# 		print (pct_txt)
# 		self.parent.score_vars_dict[self.page_name]=self.total_score

class MyButton(Button):
	def on_release_custom(self,to_page,direction="left",*args,**kwargs):
		App.get_running_app().root.current=to_page
		App.get_running_app().root.transition.direction=direction

class MyButton2(Button):
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

class MyActionBar(ActionBar):
	NAME=StringProperty("None")
	def __init__(self,**kwargs):

		super(MyActionBar,self).__init__(**kwargs)


	def chevron_left(self,scr,to_pg='RiskAssesmentPage'):
		print ("chevron_left")
		print (scr.name)

		if scr.name in ["AboutPage","RiskAssesmentPage"]:
			to_pg="LandingPage"
		# print ()
		App.get_running_app().root.transition.direction="right"
		App.get_running_app().root.current=to_pg

class ButtonSet(BoxLayout):
	def __init__(self,**kwargs):
		super(ButtonSet,self).__init__(**kwargs)

class ContentNavigationDrawer(BoxLayout):
	pass

class NavButtons(BoxLayout):
	pass