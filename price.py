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


pannel_price_window = Tk()
pannel_price_window.title("price")
pannel_price_window.config(width=600, height=800, bg=BG_COLOR_BACK)
def on_price_click():
    pannel_price_window.mainloop()
    
def on_price_submit():
    is_valid = True
    if mizan_price.get() == '' or date_price.get() == '':
        if mizan_price.get() == '':
            mizan_price.configure(border_color="red")
        if date_price.get() == '':
            date_price.configure(border_color="red")
            
    else:
        if type(mizan_price.get()) != int or mizan_price.get() <=0:
            is_valid = False
        if not re.findall('[0-9]{4}/[0-9]{2}/[0-9]{2}', date_price.get()):
            is_valid = False 
        if len(price_desc.get()) > 100:
            is_valid = False
    
    if is_valid:
        # set_price_info_in_db(user_id, mizan_price.get(), date_price.get(), main_price, category_price, price_desc.get())
        tkinter.messagebox.showinfo('succes', 'the information successfully saved')
        pannel_price_window.destroy()
    else:
        tkinter.messagebox.showerror('Error', 'something went wrong!!')
        
        
def set_price_info_in_db(id, mizan, date, main, category, description= ''):
    
    connect = sqlite3.connect('users.db')
    c = connect.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS price(
              id INTEGER NOT NULL, 
              mizan INTEGER NoT NULL,
              date text NOT NULL,
              main_price text NIT NULL,
              category text,
              description text;)''')
    
    c.execute('''INSERT INTO price (id, mizan, date, main_price, category, description)
              VALUES (?, ?, ?, ?, ?, ?);''' [id, mizan, date, main, category, description])
    
    connect.commit()
    connect.close()

option_var = StringVar()

lbl1 = CTkLabel(
    master= pannel_price_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'mizan daramad:',
    text_color="white")
lbl1.place(x=10, y=20)

mizan_price = CTkEntry(
    master=pannel_price_window,
    font=FONT_STYLE_ENTRY,
    width=100,
    height=35,
    border_width=2,
    corner_radius=10,
    fg_color=BG_COLOR_ENTRY,
    placeholder_text_color=TEXT_COLOR_ENTRY,
    text_color="black"
    )
mizan_price.place(x=120, y=20)
    
lbl2 = CTkLabel(
    master= pannel_price_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'tarikh daramad:',
    text_color="white")
lbl2.place(x=10, y=70)

date_price = CTkEntry(
    master=pannel_price_window,
    placeholder_text="XXXX/XX/XX",
    font=FONT_STYLE_ENTRY,
    width=100,
    height=35,
    border_width=2,
    corner_radius=10,
    fg_color=BG_COLOR_ENTRY,
    placeholder_text_color=TEXT_COLOR_ENTRY,
    text_color="black")
date_price.place(x=120, y=70)

price_list = ('naghd', 'check', 'cripto')   
lbl3 = CTkLabel(
    master= pannel_price_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'manbaa daramad',
    text_color="white")
lbl3.place(x=10, y=120)
main_price = OptionMenu(
    pannel_price_window, 
    option_var,
    # price_list[0], 
    *price_list)
main_price.place(x=120, y=120)

category_list = ('bank', 'company', 'personal')
# category_list = return_category_list(user_id)

lbl4 = CTkLabel(
    master= pannel_price_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'category',
    text_color="white")
lbl4.place(x=10, y=170)
category_price = OptionMenu(
    pannel_price_window,
    option_var, 
    # category_list[0], 
    *category_list)

category_price.place(x=120, y=170)

lbl5 = CTkLabel(
    master= pannel_price_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'discription',
    text_color="white")
lbl5.place(x=10, y=220)
price_desc = CTkEntry(
    master=pannel_price_window,
    font=FONT_STYLE_ENTRY,
    width=100,
    height=35,
    border_width=2,
    corner_radius=10,
    fg_color=BG_COLOR_ENTRY,
    placeholder_text_color=TEXT_COLOR_ENTRY,
    text_color="black")
price_desc.place(x=120, y=220)

submit_btn = CTkButton(
    master=pannel_price_window,
    width=70,
    height=30,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BG_COLOR_ENTRY,
    text="Submit",
    text_color="#4B3E39",
    font=FONT_BUTTON,
    command= on_price_submit       
        )
submit_btn.place(x=100, y=300)

pannel_price_window.mainloop()