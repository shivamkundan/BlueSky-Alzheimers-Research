# import the kivy stuff
from kivy_imports import *

# import my stuff
from globals import *
from object_defs import *
from page_templates import *

KEY_ESC=27
KEY_Q=113
KEY_H=104

BTN_COLOR = 69/255, 90/255, 100/255, 0.9
BTN_COLOR_PRESSED = 168/255,50/255,50/255,0.9

RED=(1,0,0,0.5)
GREEN=(0,1,0,0.5)
WHITE=(1,1,1,1)
BLACK=(0,0,0,1)

# ============================ GLOBAL FNs ============================= #
def chevron_left_global(curr,next_pg='RiskAssesmentPage'):
	curr.parent.transition.direction="right"
	curr.parent.current=next_pg

def release_keyboard_global(curr):
	curr._keyboard = Window.request_keyboard(curr.parent._keyboard_closed, curr)
	curr._keyboard.bind(on_key_up=curr.parent._on_keyboard_up)
	Window.release_all_keyboards()