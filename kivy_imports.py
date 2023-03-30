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