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
SIGN_IN_BUTTON_COLOR_CLICK = "#9A8A57"
SIGN_IN_BUTTON_COLOR_OFF = "#E6CD80"

FONT_STYLE_ENTRY = ('Thasadith', 15)
FONT_LABEL = ('Tenor Sans', 40)
FONT_BUTTON  = ('Tenor Sans', 20)
FONT_LABEL_Q = ('Tenor Sans', 15)

class CategoryApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("cost")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK)
        
        self.setup_ui()
        
    def setup_ui(self):
        self.catLbl = CTkLabel(
        master= self,
            width=100,
            height=35,
            fg_color=BG_COLOR_ENTRY,
            text= 'add your new category here:',
            text_color="white")
        self.catLbl.place(x=20,y=100)
        self.cat_entry = CTkEntry(
            master=self,
            font=FONT_STYLE_ENTRY,
            width=200,
            height=35,
            border_width=2,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black")
        self.cat_entry.place(x=200, y=100)

        self.create_cat_btn = CTkButton(
            master= self, 
            width=70,
            height=30,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=BG_COLOR_ENTRY,
            text="create",
            text_color="#4B3E39",
            font=FONT_BUTTON,
            command= self.on_craete_category)
        self.create_cat_btn.place(x=50, y=190)
        self.create_cat_btn.bind("<Button-1>", self.on_craete_category)
        
    def on_craete_category(self, event):
        self.create_cat_btn.configure(fg_color=SIGN_IN_BUTTON_COLOR_CLICK)
        self.after(200, lambda: self.create_cat_btn.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF))
        
        if self.cat_entry.get() != '' and len(self.cat_entry.get())< 15:
            if re.match('[0-9a-zA-Z]+', self.cat_entry.get()):
                self.set_category_info_in_db('amura', self.cat_entry.get())
                tkinter.messagebox.showinfo('complete', 'the category succesfully saved')
            else:
                tkinter.messagebox.showerror('Error', 'category not avalibel!')
        else:
            self.cat_entry.configure(border_color="red")
            tkinter.messagebox.showerror('Error', 'something went wrong!!')
            
    def set_category_info_in_db(self, user_name, category):
        
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS categories(user_name TEXT NOT NULL UNIQUE);''')
        try:
            c.execute("INSERT INTO categories (user_name) VALUES (?);", (user_name,))
        except:
            pass
        c.execute("SELECT * FROM categories WHERE user_name = ?;", (user_name,))
        
        cat_list = c.fetchall()
        n = len(cat_list[0])
        column = 'cat' + '%s'%(n)
        c.execute(f"ALTER TABLE categories ADD {column} TEXT;")
        c.execute(f"UPDATE categories SET {column} = '{category}' WHERE user_name = ?", (user_name,))
        
        connect.commit()
        connect.close()
        

def start():
    app = CategoryApp()
    app.mainloop() 
    #app.load_data()   

if __name__ == "__main__":
    start()