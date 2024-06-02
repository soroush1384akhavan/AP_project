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


category_window = Tk() 
category_window.title("category") 
category_window.config(width=600, height=800, bg=BG_COLOR_BACK)     
def on_category_click():
    category_window.mainloop()
    
def on_craete_category():

    if cat_entry.get() != '' and len(cat_entry.get())< 15:
        if not re.findall('[0-9a-zA-Z]+', cat_entry.get()):
            # set_category_info_in_db(user_id, cat_entry.get())
            pass
        else:
            tkinter.messagebox.showerror('Error', 'category not avalibel!')
    else:
        cat_entry.configure(border_color="red")
        tkinter.messagebox.showerror('Error', 'something went wrong!!')
        
def set_category_info_in_db(id, category):
    
    connect = sqlite3.connect('users.db')
    c = connect.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS categories(id INTEGER NOT NULL, category1 text;)''')
    c.execute("SELECT category FROM categories WHERE id = ?;" (id,))
    category_on_db = c.fetchall()
    
    c.execute('''INSERT INTO categories (id, category) VALUES (?,?)''' [id, '%s,%s' %(category_on_db, category)])
    
    connect.commit()
    connect.close()
    
def return_category_list(id):
    connect = sqlite3.connect('users.db')
    c = connect.cursor()
    c.execute("SELECT category FROM categories WHERE id = ?;" (id,))
    category_on_db = c.fetchall()
    
    connect.commit()
    connect.close()
    
    category_list = category_on_db.split(',')
    return category_list


catLbl = CTkLabel(
    master= category_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'add your new category here:',
    text_color="white")
catLbl.place(x=20,y=100)
cat_entry = CTkEntry(
    master=category_window,
    font=FONT_STYLE_ENTRY,
    width=200,
    height=35,
    border_width=2,
    corner_radius=10,
    fg_color=BG_COLOR_ENTRY,
    placeholder_text_color=TEXT_COLOR_ENTRY,
    text_color="black")
cat_entry.place(x=200, y=100)

create_cat_btn = CTkButton(
    master=category_window, 
    width=70,
    height=30,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BG_COLOR_ENTRY,
    text="create",
    text_color="#4B3E39",
    font=FONT_BUTTON,
    command= on_craete_category)
create_cat_btn.place(x=50, y=190)


category_window.mainloop()