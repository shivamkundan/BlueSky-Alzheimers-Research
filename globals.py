from kivy_imports import *

KEY_ESC=27

KEY_Q=113

KEY_H=108

# ============================ GLOBAL FNs ============================= #
def chevron_left_global(curr,next_pg='RiskAssesmentPage'):
	curr.parent.transition.direction="right"
	curr.parent.current=next_pg

def release_keyboard_global(curr):
	curr._keyboard = Window.request_keyboard(curr.parent._keyboard_closed, curr)
	curr._keyboard.bind(on_key_up=curr.parent._on_keyboard_up)
	Window.release_all_keyboards()