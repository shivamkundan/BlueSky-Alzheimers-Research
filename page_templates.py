from kivy_imports import MDScreen
from globals import release_keyboard_global

class SubPageBase(MDScreen):
	def __init__(self,**kwargs):
		super(SubPageBase,self).__init__(**kwargs)
		self.page_name=None
		self.prev_page=None
		self.next_page=None

	def chevron_left(self,next_pg='RiskAssesmentPage'):
		self.parent.transition.direction="right"
		self.parent.current=next_pg

	def arrow_left(self):
		self.parent.transition.direction="right"
		self.parent.current=self.prev_page

	def arrow_right(self):
		self.parent.transition.direction="left"
		self.parent.current=self.next_page

class SubPageTemplate(SubPageBase):
	def __init__(self,**kwargs):
		super(SubPageTemplate,self).__init__(**kwargs)

		# dummy/placeholder variables
		self.tab_names=None
		self.num_tabs=None
		self.curr_tab_num=0

		self.total_score=0
		self.responses_dict={}
		self.done_dict={}

	def init_subpage(self):
		self.num_tabs=len(self.tab_names)
		for i in range(self.num_tabs):
			self.responses_dict[i]=0
			self.done_dict[i]=0

	def button_press(self,button):
		print ('pressed: ',button.text)
		self.responses_dict[self.curr_tab_num+1]=int(button.text)
		self.done_dict[self.curr_tab_num+1]=True
		self.arrow_right()

	def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
		# get the tab icon.
		# count_icon = instance_tab.text
		self.curr_tab_num=int(instance_tab.text)-1
		self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])

	def update_score(self):
		total=0
		for key,val in self.responses_dict.items():
			total+=val
		self.total_score=total

		num_done=0
		for k,v in self.done_dict.items():
			if v==True:
				num_done+=1

		pct=int(round(100*(num_done/self.num_tabs),0))
		pct_txt=str(pct)+'% Complete'
		return total, pct_txt

	def on_pre_leave(self):
		total,pct_txt=self.update_score()
		self.parent.score_vars_dict[self.page_name]=total
		self.parent.ids['RiskAssesmentPage'].ids[self.name+"_label"].secondary_text=pct_txt

	def arrow_right(self):
		if self.curr_tab_num==self.num_tabs-1:
			self.parent.transition.direction="left"
			self.parent.current=self.next_page
		else:
			self.curr_tab_num+=1
			self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])

	def arrow_left(self):
		if self.curr_tab_num==0:
			self.parent.transition.direction="right"
			self.parent.current=self.prev_page
		else:
			self.curr_tab_num-=1
			self.ids['android_tabs'].switch_tab(self.tab_names[self.curr_tab_num])

class ScorePageTemplate(SubPageBase):
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

	def reset_quiz(self):
		try:
			self.parent.ids[self.prev_page].ids.android_tabs.switch_tab('1')
		except:
			pass
		self.parent.transition.direction="right"
		self.parent.current=self.landing_page
