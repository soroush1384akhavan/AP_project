from tkinter import *
import tkinter.messagebox
from customtkinter import *
import re
import sqlite3


#consts
#------------------------------------------
BG_COLOR_BACK ="#15323E"
BG_COLOR_ENTRY = "#2F657C"
TEXT_COLOR_ENTRY = "#B1B4B5"
TEXT_COLOR_LABEL = "#FFFFFF"
BUTTON_COLOR_OFF = "#6199B1"
BUTTON_COLOR_ON = "#2F657C"
BUTTON_COLOR_CLICK = "#153C4D"

FONT_STYLE_ENTRY = ('Thasadith', 15)
FONT_LABEL = ('Tenor Sans', 40)
FONT_BUTTON  = ('Tenor Sans', 20)
FONT_LABEL_Q = ('Tenor Sans', 15)


setting_window = Tk()
setting_window.title("Setting")
setting_window.config(width=1125, height=800, bg=BG_COLOR_BACK)
def on_setting_click():
    setting_window.mainloop()
    
    
    
setting_window.mainloop()       