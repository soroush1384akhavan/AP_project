from tkinter import *
import tkinter.messagebox
from customtkinter import *
import Creat_account
from tkinter import Toplevel
import sqlite3
import re

# Constants
BG_COLOR_BACK_ON = "#FBE5B6"
BG_COLOR_BACK_OFF = "#F8E1AF"
FONT_LABEL = ('Kaisei Opi', 75)
FONT_STYLE_ENTRY = ('Kdam Thmor', 20)
FONT_BUTTON = ('Kdam Thmor', 20)
TEXT_COLOR_ENTRY = "#BDB7B4"
BG_COLOR_ENTRY = "#F3EBE8"
LOG_IN_BUTTON_COLOR_OFF = "#F3EBE8"
LOG_IN_BUTTON_COLOR_ON = "#D5CCC8"
LOG_IN_BUTTON_COLOR_CLICK = "#B5ACA9"
SIGN_IN_BUTTON_COLOR_ON = "#C0AC6F"
SIGN_IN_BUTTON_COLOR_OFF = "#E6CD80"
SIGN_IN_BUTTON_COLOR_CLICK = "#9A8A57"

class IncomePage:
    def __init__(self, master):
        self.master = master
        self.widget_list = []

        self.setup_ui()

    def setup_ui(self):
        self.income_amount_label = Label(
                self.master, 
                text="Income amount:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        
        self.income_amount_label.place(
            x=306, 
            y=165, 
            width=200, 
            height=74
        )
        
        self.title_label = Label(
                self.master, 
                text="Set Income:", 
                font=('bold', 40),
                fg="black", 
                bg="white"
            )
        
        self.title_label.place(
            x=313, 
            y=38, 
            width=287, 
            height=74
        )
        
        self.income_amount_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=209,
            height=40,
            border_width=2,
            corner_radius=10,
            border_color="#3300FF",
            bg_color="white",
            fg_color="white",
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        self.income_amount_entry.place(x=520, y=182)
        self.income_amount_entry.bind("<KeyRelease>", self.check_income_amount)
        self.income_amount_entry.bind("<KeyRelease>", self.check_page)
        
        
        
        self.date_label = Label(
                self.master, 
                text="Date:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        
        self.date_label.place(
            x=776, 
            y=165, 
            width=66, 
            height=74
        )
        
        self.date_entry = CTkEntry(
            master=self.master,
            placeholder_text="XXXX/XX/XX",
            font=FONT_STYLE_ENTRY,
            width=209,
            height=40,
            border_width=2,
            bg_color="white",
            corner_radius=10,
            border_color= "#3300FF",
            fg_color="white",
            placeholder_text_color="gray",
            text_color="black"
            )
        self.date_entry.place(x=860, y=182)
        self.date_entry.bind("<KeyRelease>", self.check_date)
        self.date_entry.bind("<KeyRelease>", self.check_page)
        
        
        
        self.source_of_income_label = Label(
                self.master, 
                text="Source of Income:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        self.source_of_income_label.place(
            x=306, 
            y=285, 
            width=244, 
            height=74
        )
        
        self.income_list = ('naghd', 'check', 'cripto') 
        self.option_var1 = StringVar() 
        self.option_var1.set(self.income_list[0]) 
        
        self.category_list = self.return_category_list('amura')
        if len(self.category_list) == 0:
            self.category_list = ["you didn't add a category"]
        else:
            self.category_list = (self.category_list[0])[1:]
            
        self.option_var2 = StringVar() 
        self.option_var2.set(self.category_list[0])
        
        self.source_of_income_menu = CTkOptionMenu(
            master=self.master,
            button_color="#FFCC5C",
            fg_color="#FBE5B6",
            bg_color="white",
            dropdown_fg_color="white",
            dropdown_hover_color="#F8E1AF",
            button_hover_color="#FFCC5C",
            text_color="black",
            dropdown_text_color="black",
            values=self.income_list)
        self.source_of_income_menu.place(x=920, y=310)
        
        self.category_label = Label(
                self.master, 
                text="Category:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        self.category_label.place(
            x=776, 
            y=285, 
            width=120, 
            height=74
        )
        
        self.category_menu = CTkOptionMenu(
            master=self.master,
            button_color="#FFCC5C",
            fg_color="#FBE5B6",
            bg_color="white",
            dropdown_fg_color="white",
            dropdown_hover_color="#F8E1AF",
            button_hover_color="#FFCC5C",
            text_color="black",
            dropdown_text_color="black",
            values=self.category_list)
        self.category_menu.place(x=556, y=310)
        
        self.description_label = Label(
                self.master, 
                text="Description:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        self.description_label.place(
            x=314, 
            y=400, 
            width=146, 
            height=74
        )
        self.description_entry = CTkTextbox(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=614,
            height=190,
            border_width=2,
            corner_radius=10,
            border_color="#3300FF",
            bg_color="white",
            fg_color="white",
            text_color="black"
        )
        self.description_entry.place(x=480, y=422)
        self.description_entry.bind("<KeyRelease>", self.check_description)
        self.description_entry.bind("<KeyRelease>", self.check_page)
        
        
        self.submit_btn = CTkButton(
            master= self.master,
            width=260,
            height=64,
            state=DISABLED,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color="white",
            bg_color="white",
            text="Submit",
            text_color="black",
            font=FONT_BUTTON)
        
        self.submit_btn.place(x=310, y=700)
        self.submit_btn.bind("<Button-1>", self.on_sumbit_clicked)
        self.submit_btn.bind("<Enter>", self.on_enter_submit)
        self.submit_btn.bind("<Leave>", self.on_leave_submit)
        

        
        self.widget_list.extend([
            self.income_amount_label,
            self.income_amount_entry,
            self.date_entry,
            self.date_label,
            self.source_of_income_label,
            self.source_of_income_menu,
            self.category_label,
            self.category_menu,
            self.description_label,
            self.description_entry,
            self.submit_btn
        ])
        
    def clear_widgets(self):
        for widget in self.widget_list:
            widget.place_forget()
        self.widget_list.clear()
        
    def check_income_amount(self, event):
        value = self.income_amount_entry.get()
        pattern = re.fullmatch(r'^[1-9][0-9]*$', value) is not None
        
        if pattern:
            self.income_amount_entry.configure(border_color="green")
            return True
        else:
            self.income_amount_entry.configure(border_color="red")
            return False
        
    def check_description(self, event):
        if len(self.description_entry.get("1.0", END)) > 100:
            self.description_entry.configure(border_color="red")
            return False
        else:
            self.description_entry.configure(border_color="green")
            return True
            
    def check_date(self, event):
        value = self.date_entry.get()
        pattern = re.fullmatch(r'^\d{4}/\d{1,2}/\d{1,2}$', value) is not None
        
        if not pattern:
            self.date_entry.configure(border_color="red")
            return False
        
        year, month, day = map(int, value.split('/'))
        
        if year < 1920 :
            self.date_entry.configure(border_color="red")
            return False
        
        if month < 1 or month > 12:
            self.date_entry.configure(border_color="red")
            return False
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                self.date_entry.configure(border_color="red")
                return False
            
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                self.date_entry.configure(border_color="red")
                return False
            
        elif month == 2:
            if day < 1 or day > 28:
                self.date_entry.configure(border_color="red")
                return False
        
        self.date_entry.configure(border_color="green")
        return True
        
    def check_page(self, event):
        if self.check_date(None) and self.check_income_amount(None) and self.check_description(None):
            self.submit_btn.configure(state=NORMAL) 
        else:
            self.submit_btn.configure(state=DISABLED)
            
        
    def on_enter_submit(self, event):
        if self.submit_btn.cget('state') == NORMAL:
            self.submit_btn.configure(fg_color="#B0B2AE")
        
    def on_leave_submit(self, event):
        self.submit_btn.configure(fg_color="white")
    
        
    def on_sumbit_clicked(self, event):
        if self.submit_btn.cget('state') == NORMAL:
            self.submit_btn.configure(fg_color="gray")
            self.submit_btn.after(200, lambda: self.submit_btn.configure(fg_color="white"))
        
            self.set_income_info_in_db('amura', self.income_amount_entry.get(), self.date_entry.get(), self.option_var1.get(), self.option_var2.get(), self.description_entry.get("1.0", END))
            tkinter.messagebox.showinfo('succes', 'the information successfully saved')
            
        
    def set_income_info_in_db(self, id, mizan, date, main, category, description= ''):
        
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS income(
                id INTEGER NOT NULL, 
                mizan INTEGER NOT NULL,
                date text NOT NULL,
                income_resource text NIT NULL,
                category text,
                description text);''')
        
        c.execute('''INSERT INTO income (id, mizan, date, income_resource, category, description)
                VALUES (?, ?, ?, ?, ?, ?);''', [id, mizan, date, main, category, description])
        
        connect.commit()
        connect.close()
        
    def return_category_list(self, id):
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS categories(user_name TEXT NOT NULL UNIQUE);''')
        c.execute("SELECT * FROM categories WHERE user_name = ?;", (id,))
        category_on_db = c.fetchall()
        
        connect.commit()
        connect.close()
        
        return category_on_db

class CostPage:
    def __init__(self, master):
        self.master = master
        self.widget_list = []

        self.setup_ui()

    def setup_ui(self):
        self.cost_amount_label = Label(
                self.master, 
                text="Cost amount:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        
        self.cost_amount_label.place(
            x=306, 
            y=165, 
            width=200, 
            height=74
        )
        
        self.title_label = Label(
                self.master, 
                text="Set Cost:", 
                font=('bold', 40),
                fg="black", 
                bg="white"
            )
        
        self.title_label.place(
            x=313, 
            y=38, 
            width=287, 
            height=74
        )
        
        self.cost_amount_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=209,
            height=40,
            border_width=2,
            corner_radius=10,
            border_color="#3300FF",
            bg_color="white",
            fg_color="white",
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        self.cost_amount_entry.place(x=520, y=182)
        self.cost_amount_entry.bind("<KeyRelease>", self.check_cost_amount)
        self.cost_amount_entry.bind("<KeyRelease>", self.check_page)
        
        
        
        self.date_label = Label(
                self.master, 
                text="Date:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        
        self.date_label.place(
            x=776, 
            y=165, 
            width=66, 
            height=74
        )
        
        self.date_entry = CTkEntry(
            master=self.master,
            placeholder_text="XXXX/XX/XX",
            font=FONT_STYLE_ENTRY,
            width=209,
            height=40,
            border_width=2,
            bg_color="white",
            corner_radius=10,
            border_color= "#3300FF",
            fg_color="white",
            placeholder_text_color="gray",
            text_color="black"
            )
        self.date_entry.place(x=860, y=182)
        self.date_entry.bind("<KeyRelease>", self.check_date)
        self.date_entry.bind("<KeyRelease>", self.check_page)
        
        
        
        self.source_of_income_label = Label(
                self.master, 
                text="Source of Cost:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        self.source_of_income_label.place(
            x=306, 
            y=285, 
            width=244, 
            height=74
        )
        
        self.income_list = ('naghd', 'check', 'cripto') 
        self.option_var1 = StringVar() 
        self.option_var1.set(self.income_list[0]) 
        
        self.category_list = self.return_category_list('amura')
        if len(self.category_list) == 0:
            self.category_list = ["you didn't add a category"]
        else:
            self.category_list = (self.category_list[0])[1:]
            
        self.option_var2 = StringVar() 
        self.option_var2.set(self.category_list[0])
        
        self.source_of_income_menu = CTkOptionMenu(
            master=self.master,
            button_color="#FFCC5C",
            fg_color="#FBE5B6",
            bg_color="white",
            dropdown_fg_color="white",
            dropdown_hover_color="#F8E1AF",
            button_hover_color="#FFCC5C",
            text_color="black",
            dropdown_text_color="black",
            values=self.income_list)
        self.source_of_income_menu.place(x=920, y=310)
        
        self.category_label = Label(
                self.master, 
                text="Category:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        self.category_label.place(
            x=776, 
            y=285, 
            width=120, 
            height=74
        )
        
        self.category_menu = CTkOptionMenu(
            master=self.master,
            button_color="#FFCC5C",
            fg_color="#FBE5B6",
            bg_color="white",
            dropdown_fg_color="white",
            dropdown_hover_color="#F8E1AF",
            button_hover_color="#FFCC5C",
            text_color="black",
            dropdown_text_color="black",
            values=self.category_list)
        self.category_menu.place(x=556, y=310)
        
        self.description_label = Label(
                self.master, 
                text="Description:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        self.description_label.place(
            x=314, 
            y=400, 
            width=146, 
            height=74
        )
        self.description_entry = CTkTextbox(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=614,
            height=190,
            border_width=2,
            corner_radius=10,
            border_color="#3300FF",
            bg_color="white",
            fg_color="white",
            text_color="black"
        )
        self.description_entry.place(x=480, y=422)
        self.description_entry.bind("<KeyRelease>", self.check_description)
        self.description_entry.bind("<KeyRelease>", self.check_page)
        
        
        self.submit_btn = CTkButton(
            master= self.master,
            width=260,
            height=64,
            state=DISABLED,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color="white",
            bg_color="white",
            text="Submit",
            text_color="black",
            font=FONT_BUTTON)
        
        self.submit_btn.place(x=310, y=700)
        self.submit_btn.bind("<Button-1>", self.on_sumbit_clicked)
        self.submit_btn.bind("<Enter>", self.on_enter_submit)
        self.submit_btn.bind("<Leave>", self.on_leave_submit)
        

        
        self.widget_list.extend([
            self.cost_amount_label,
            self.cost_amount_entry,
            self.date_entry,
            self.date_label,
            self.source_of_income_label,
            self.source_of_income_menu,
            self.category_label,
            self.category_menu,
            self.description_label,
            self.description_entry,
            self.title_label
        ])
        
    def clear_widgets(self):
        for widget in self.widget_list:
            widget.place_forget()
        self.widget_list.clear()
        
    def check_cost_amount(self, event):
        value = self.cost_amount_entry.get()
        pattern = re.fullmatch(r'^[1-9][0-9]*$', value) is not None
        
        if pattern:
            self.cost_amount_entry.configure(border_color="green")
            return True
        else:
            self.cost_amount_entry.configure(border_color="red")
            return False
        
    def check_description(self, event):
        if len(self.description_entry.get("1.0", END)) > 100:
            self.description_entry.configure(border_color="red")
            return False
        else:
            self.description_entry.configure(border_color="green")
            return True
            
    def check_date(self, event):
        value = self.date_entry.get()
        pattern = re.fullmatch(r'^\d{4}/\d{1,2}/\d{1,2}$', value) is not None
        
        if not pattern:
            self.date_entry.configure(border_color="red")
            return False
        
        year, month, day = map(int, value.split('/'))
        
        if year < 1920 :
            self.date_entry.configure(border_color="red")
            return False
        
        if month < 1 or month > 12:
            self.date_entry.configure(border_color="red")
            return False
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                self.date_entry.configure(border_color="red")
                return False
            
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                self.date_entry.configure(border_color="red")
                return False
            
        elif month == 2:
            if day < 1 or day > 28:
                self.date_entry.configure(border_color="red")
                return False
        
        self.date_entry.configure(border_color="green")
        return True
        
    def check_page(self, event):
        if self.check_date(None) and self.check_cost_amount(None) and self.check_description(None):
            self.submit_btn.configure(state=NORMAL) 
        else:
            self.submit_btn.configure(state=DISABLED)
            
        
    def on_enter_submit(self, event):
        if self.submit_btn.cget('state') == NORMAL:
            self.submit_btn.configure(fg_color="#B0B2AE")
        
    def on_leave_submit(self, event):
        self.submit_btn.configure(fg_color="white")
    
        
    def on_sumbit_clicked(self, event):
        if self.submit_btn.cget('state') == NORMAL:
            self.submit_btn.configure(fg_color="gray")
            self.submit_btn.after(200, lambda: self.submit_btn.configure(fg_color="white"))
        
            self.set_cost_info_in_db('amura', self.cost_amount_entry.get(), self.date_entry.get(), self.option_var1.get(), self.option_var2.get(), self.description_entry.get("1.0", END))
            tkinter.messagebox.showinfo('succes', 'the information successfully saved')
            
        
    def set_cost_info_in_db(self, id, mizan, date, main, category, description= ''):
        
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS cost(
                user_name TEXT NOT NULL, 
                mizan INTEGER NoT NULL,
                date text NOT NULL,
                cost_resource text NIT NULL,
                category text,
                description text);''')
        
        c.execute('''INSERT INTO cost (user_name, mizan, date, cost_resource, category, description)
                VALUES (?, ?, ?, ?, ?, ?);''', [id, mizan, date, main, category, description])

        connect.commit()
        connect.close()
        
    def return_category_list(self, id):
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS categories(user_name TEXT NOT NULL UNIQUE);''')
        c.execute("SELECT * FROM categories WHERE user_name = ?;", (id,))
        category_on_db = c.fetchall()
        
        connect.commit()
        connect.close()
        
        return category_on_db

class CategoryPage:
    def __init__(self, master):
        self.master = master
        self.widget_list = []

        self.setup_ui()

    def setup_ui(self):
        self.category_label = Label(
                self.master, 
                text="Categories:", 
                font=('Bold', 40),
                fg="black", 
                bg="white"
            )
        self.category_label.place(
            x=313, 
            y=38, 
            width=287, 
            height=74
        )
        
        self.add_category_label = Label(
                self.master, 
                text="add your category:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        self.add_category_label.place(
            x=316, 
            y=165, 
            width=250, 
            height=74
        )
        
        self.category_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=209,
            height=40,
            border_width=2,
            corner_radius=10,
            border_color="#3300FF",
            bg_color="white",
            fg_color="white",
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        self.category_entry.place(x=600, y=182)
        self.category_entry.bind("<KeyRelease>", self.check_category)
        self.category_entry.bind("<KeyRelease>", self.check_page)
        
        self.create_cat_btn = CTkButton(
            master= self.master,
            width=260,
            height=64,
            state=DISABLED,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color="white",
            bg_color="white",
            text="Submit",
            text_color="black",
            font=FONT_BUTTON)
        
        self.create_cat_btn.place(x=310, y=700)
        self.create_cat_btn.bind("<Button-1>", self.on_create_clicked)
        self.create_cat_btn.bind("<Enter>", self.on_enter_create)
        self.create_cat_btn.bind("<Leave>", self.on_leave_create)
        
        self.widget_list.extend([
            self.create_cat_btn,
            self.category_entry,
            self.add_category_label,
            self.category_label
        ])
        
    def clear_widgets(self):
        for widget in self.widget_list:
            widget.place_forget()
        self.widget_list.clear()
        
    def check_category(self, event):
        value = self.category_entry.get()
        pattern = re.fullmatch(r'[A-Za-z]+', value) is not None
        
        if pattern:
            self.category_entry.configure(border_color="green")
            return True
        else:
            self.category_entry.configure(border_color="red")
            return False
    
    def check_page(self, event):
        if self.check_category(None):
            self.create_cat_btn.configure(state=NORMAL) 
        else:
            self.create_cat_btn.configure(state=DISABLED)
            
    def on_enter_create(self, event):
        if self.create_cat_btn.cget('state') == NORMAL:
            self.create_cat_btn.configure(fg_color="#B0B2AE")
        
    def on_leave_create(self, event):
        self.create_cat_btn.configure(fg_color="white")
    
        
    def on_create_clicked(self, event):
        if self.create_cat_btn.cget('state') == NORMAL:
            self.create_cat_btn.configure(fg_color="gray")
            self.create_cat_btn.after(200, lambda: self.create_cat_btn.configure(fg_color="white"))
        
            self.set_category_info_in_db('amura', self.category_entry.get())
            tkinter.messagebox.showinfo('complete', 'the category succesfully saved')
            
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
            

class SettingPage:  
    def __init__(self, master):
        self.master = master
        self.widget_list = []

        self.setup_ui()

    def setup_ui(self):
        self.setting_label = Label(
                self.master, 
                text="Setting", 
                font=('Bold', 40),
                fg="black", 
                bg="white"
            )
        self.setting_label.place(
            x=313, 
            y=38, 
            width=287, 
            height=74
        )
        
        self.change_theme_label = Label(
                self.master, 
                text="change theme", 
                font=('Kdam Thmor', 19),
                fg="black", 
                bg="white"
            )
        self.change_theme_label.place(
            x=316, 
            y=165, 
            width=250, 
            height=74
        )
        
        self.theme_switch = CTkSwitch(
            self.master,
            bg_color="white",
            text_color="black"
            # command= change_theme
            )
        self.theme_switch.place(x = 580, y= 185)
        
        self.delete_info_label = Label(
                self.master, 
                text="delete user data", 
                font=('Kdam Thmor', 19),
                fg="black", 
                bg="white"
            )
        self.delete_info_label.place(
            x=316, 
            y=230, 
            width=250, 
            height=74
        )
        
        self.item_for_remove = ['income', 'cost', 'both']
        self.option_var = StringVar() 
        self.option_var.set(self.item_for_remove[0])
        
        self.source_of_income_menu = CTkOptionMenu(
            master=self.master,
            button_color="#FFCC5C",
            fg_color="#FBE5B6",
            bg_color="white",
            dropdown_fg_color="white",
            dropdown_hover_color="#F8E1AF",
            button_hover_color="#FFCC5C",
            text_color="black",
            dropdown_text_color="black",
            values=self.item_for_remove)
        self.source_of_income_menu.place(x=556, y=255)
        
        self.delete_info_btn = CTkButton(
            master= self.master,
            width=130,
            height=47,
            state=DISABLED,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color="white",
            bg_color="white",
            text="remove Date",
            text_color="black",
            font=('Kdam Thmor', 17))
        
        self.delete_info_btn.place(x=720, y=246)
        self.delete_info_btn.bind("<Button-1>", self.on_delete_info_click)
        self.delete_info_btn.bind("<Enter>", self.on_enter_del_info)
        self.delete_info_btn.bind("<Leave>", self.on_leave_del_info)
        
        self.delete_account_label = Label(
                self.master, 
                text="delete user account", 
                font=('Kdam Thmor', 19),
                fg="black", 
                bg="white"
            )
        self.delete_account_label.place(
            x=316, 
            y=301, 
            width=250, 
            height=74
        )
        
        self.delete_user_btn = CTkButton(
            master= self.master,
            width=130,
            height=47,
            state=DISABLED,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color="white",
            bg_color="white",
            text="Delete account",
            text_color="black",
            font=('Kdam Thmor', 17))
        
        self.delete_user_btn.place(x=600, y=315)
        self.delete_user_btn.bind("<Button-1>", self.on_delete_user_account)
        self.delete_user_btn.bind("<Enter>", self.on_enter_del_user)
        self.delete_user_btn.bind("<Leave>", self.on_leave_del_user)
        
        self.widget_list.extend([
            self.delete_user_btn,
            self.delete_account_label,
            self.delete_info_btn,
            self.source_of_income_menu,
            self.delete_info_label,
            self.theme_switch,
            self.change_theme_label,
            self.setting_label
        ])
        
    def clear_widgets(self):
        for widget in self.widget_list:
            widget.place_forget()
        self.widget_list.clear()
            
    def on_enter_del_info(self, event):
        self.delete_info_btn.configure(fg_color="#B0B2AE")
        self.delete_info_btn.configure(fg_color="#FBE5B6")
        
    def on_leave_del_info(self, event):
        self.delete_info_btn.configure(fg_color="white")
        
    def on_enter_del_user(self, event):
        self.delete_user_btn.configure(fg_color="#B0B2AE")
        self.delete_user_btn.configure(fg_color='#FBE5B6')
        
    def on_leave_del_user(self, event):
        self.delete_user_btn.configure(fg_color="white")
    
        
    def on_delete_user_account(self, event):
        # self.delete_user_button(fg_color=SIGN_IN_BUTTON_COLOR_CLICK)
        # self.after(200, lambda: self.delete_user_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF))
        
        message_box = tkinter.messagebox.askquestion('delete account','آیا برای حذف اکانت خود مطمین هستید؟', icon = 'warning')
        if message_box == 'yes':
            pass # soroush fix it 
        
    def on_delete_info_click(self, event):
        # self.delete_data_button(fg_color=SIGN_IN_BUTTON_COLOR_CLICK)
        # self.after(200, lambda: self.delete_data_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF))
        
        message_box = tkinter.messagebox.askquestion('delete info','آیا برای حذف اطلاعات خود مطمین هستید؟', icon = 'warning')
        if message_box:
            self.delete_transaction('soroush', self.option_var.get())
            tkinter.messagebox.showinfo('complite', 'the information you chose was deleted')
                
    def delete_transaction(self, user_name, change):
    
        if change == 'income':
            connect = sqlite3.connect('users.db')
            c = connect.cursor()
            c.execute('''DELETE FROM income WHERE user_name = ?;''' ,(user_name,))
            
            connect.commit()
            connect.close()
            
        elif change == 'price':
            connect = sqlite3.connect('users.db')
            c = connect.cursor()
            c.execute('''DELETE FROM price WHERE user_name = ?;''' ,(user_name,))
            
            connect.commit()
            connect.close()
            
        elif change == 'both':
            connect = sqlite3.connect('users.db')
            c = connect.cursor()
            c.execute('''DELETE FROM income WHERE user_name = ?;''', (user_name,))
            c.execute('''DELETE FROM price WHERE user_name = ?;''', (user_name,))
            
            connect.commit()
            connect.close()
            
                
class ReportingPage:
    def __init__(self, master):
        self.master = master
        self.widget_list = []

        self.setup_ui()
        
    def setup_ui(self):
        self.reporting_label = Label(
                self.master, 
                text="Reporting:", 
                font=('Bold', 40),
                fg="black", 
                bg="white"
            )
        self.reporting_label.place(
            x=313, 
            y=38, 
            width=287, 
            height=74
        )
        
        self.date_label = Label(
                self.master, 
                text="chose your period date:", 
                font=('Kdam Thmor', 18),
                fg="black", 
                bg="white"
            )
        self.date_label.place(
            x=316, 
            y=165, 
            width=250, 
            height=74
        )
        
        self.report_day_label = Label(
                self.master, 
                text="Day:", 
                font=('Kdam Thmor', 16),
                fg="black", 
                bg="white"
            )
        self.report_day_label.place(
            x=296, 
            y=215, 
            width=110, 
            height=74
        )
        self.day_report_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            placeholder_text="  from - to",
            width=120,
            height=40,
            border_width=2,
            corner_radius=10,
            border_color="#3300FF",
            bg_color="white",
            fg_color="white",
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        self.day_report_entry.place(x=386, y=235)
        # self.day_report_entry.bind("<KeyRelease>", self.check_category)
        # self.day_report_entry.bind("<KeyRelease>", self.check_page)
        
        self.report_month_label = Label(
                self.master, 
                text="Month:", 
                font=('Kdam Thmor', 16),
                fg="black", 
                bg="white"
            )
        self.report_month_label.place(
            x=550, 
            y=216, 
            width=110, 
            height=74
        )
        self.month_report_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            placeholder_text="  from - to",
            width=120,
            height=40,
            border_width=2,
            corner_radius=10,
            border_color="#3300FF",
            bg_color="white",
            fg_color="white",
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        self.month_report_entry.place(x=650, y=235)
        # self.month_report_entry.bind("<KeyRelease>", self.check_category)
        # self.month_report_entry.bind("<KeyRelease>", self.check_page)
        
        self.report_year_label = Label(
                self.master, 
                text="Year:", 
                font=('Kdam Thmor', 16),
                fg="black", 
                bg="white"
            )
        self.report_year_label.place(
            x=800, 
            y=216, 
            width=110, 
            height=74
        )
        self.year_report_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            placeholder_text="  from - to",
            width=120,
            height=40,
            border_width=2,
            corner_radius=10,
            border_color="#3300FF",
            bg_color="white",
            fg_color="white",
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        self.year_report_entry.place(x=890, y=235)
        # self.year_report_entry.bind("<KeyRelease>", self.check_category)
        # self.year_report_entry.bind("<KeyRelease>", self.check_page)
        
        
        self.report_kind_list = ('naghd', 'check', 'cripto') 
        self.option_var1 = StringVar() 
        self.option_var1.set(self.report_kind_list[0]) 
        
        self.report_source_list = self.return_category_list('amura')
        if len(self.report_source_list) == 0:
            self.report_source_list = ["you didn't add a category"]
        else:
            self.report_source_list = (self.report_source_list[0])[1:]
         
        self.option_var2 = StringVar() 
        self.option_var2.set(self.report_source_list[0])
        
        self.report_source_label = Label(
                self.master, 
                text="source report:", 
                font=('Kdam Thmor', 18),
                fg="black", 
                bg="white"
            )
        self.report_source_label.place(
            x=280, 
            y=315, 
            width=230, 
            height=50
        )
        self.source_menu = CTkOptionMenu(
            master=self.master,
            button_color="#FFCC5C",
            fg_color="#FBE5B6",
            bg_color="white",
            dropdown_fg_color="white",
            dropdown_hover_color="#F8E1AF",
            button_hover_color="#FFCC5C",
            text_color="black",
            dropdown_text_color="black",
            values=self.report_source_list)
        self.source_menu.place(x=480, y=326)
        
        self.report_kind_label = Label(
                self.master, 
                text="kind of report:", 
                font=('Kdam Thmor', 18),
                fg="black", 
                bg="white"
            )
        self.report_kind_label.place(
            x=700, 
            y=315, 
            width=150, 
            height=50
        )
        self.kind_menu = CTkOptionMenu(
            master=self.master,
            button_color="#FFCC5C",
            fg_color="#FBE5B6",
            bg_color="white",
            dropdown_fg_color="white",
            dropdown_hover_color="#F8E1AF",
            button_hover_color="#FFCC5C",
            text_color="black",
            dropdown_text_color="black",
            values=self.report_kind_list)
        self.kind_menu.place(x=870, y=326)
        
        self.price_amount_label = Label(
                self.master, 
                text="price amount:", 
                font=('Kdam Thmor', 18),
                fg="black", 
                bg="white"
            )
        self.price_amount_label.place(
            x=316, 
            y=405, 
            width=150, 
            height=50
        )
        
        self.price_amount_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            placeholder_text="     from - to",
            width=160,
            height=40,
            border_width=2,
            corner_radius=10,
            border_color="#3300FF",
            bg_color="white",
            fg_color="white",
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        self.price_amount_entry.place(x=490, y=410)
        # self.year_report_entry.bind("<KeyRelease>", self.check_category)
        # self.year_report_entry.bind("<KeyRelease>", self.check_page)
        
        self.report_section_list = ('both', 'income', 'cost') 
        self.option_var3 = StringVar() 
        self.option_var3.set(self.report_section_list[0])
        
        self.report_section_label = Label(
                self.master, 
                text="source report:", 
                font=('Kdam Thmor', 18),
                fg="black", 
                bg="white"
            )
        self.report_section_label.place(
            x=280, 
            y=495, 
            width=230, 
            height=50
        )
        self.section_menu = CTkOptionMenu(
            master=self.master,
            button_color="#FFCC5C",
            fg_color="#FBE5B6",
            bg_color="white",
            dropdown_fg_color="white",
            dropdown_hover_color="#F8E1AF",
            button_hover_color="#FFCC5C",
            text_color="black",
            dropdown_text_color="black",
            values=self.report_section_list)
        self.section_menu.place(x=480, y=505)
        
        self.submit_btn = CTkButton(
            master= self.master,
            width=260,
            height=64,
            state=DISABLED,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color="white",
            bg_color="white",
            text="Filtering",
            text_color="black",
            font=FONT_BUTTON)
        
        self.submit_btn.place(x=310, y=700)
        self.submit_btn.bind("<Button-1>", self.on_submit_clicked)
        self.submit_btn.bind("<Enter>", self.on_enter_submit)
        self.submit_btn.bind("<Leave>", self.on_leave_submit)
        

        
        # self.widget_list.extend([
        #     self.date_label,
        #     self.reporting_label,
        #     self.report_day_label,
        #     self.report_month_label,
        #     self.report_year_label,
        #     self.report_kind_label,
        #     self.report_source_label,
        #     self.report_source_list,
        #     self.report_kind_list,
        #     self.report_section_list,
        #     self.day_report_entry,
        #     self.month_report_entry,
        #     self.year_report_entry,
        #     self.price_amount_entry,
        #     self.price_amount_label,
        #     self.kind_menu,
        #     self.source_menu,
        #     self.section_menu,
        # ])
        
    def clear_widgets(self):
        for widget in self.widget_list:
            widget.place_forget()
        self.widget_list.clear()
        
    def on_submit_clicked(self, event):
        self.submit_btn.configure(fg_color="gray")
        self.submit_btn.after(200, lambda: self.submit_btn.configure(fg_color="white"))
        
        
    
    def on_enter_submit(self, event):
        self.submit_btn.configure(fg_color="#B0B2AE")
    
    def on_leave_submit(self, event):
        self.submit_btn.configure(fg_color="white")
        
    # def add_filter(self):
    #     if self.section_menu.get() == 'both':
    #         pass
    #     else:
    #         item_list = self.get_income_from_db(self.section_menu.get(), 'amura')
    #         if len(self.day_report_entry.get()) != 0:
    #             min, max = self.day_report_entry.get().split('-')
    #             for item in item_list:
    #                 if (item[2].split('/'))[2] < min or (item[2].split('/'))[2] > max:
    #                     item_list.remove(item)
                        
    #         if len(self.month_report_entry.get()) != 0:
    #             min, max = self.month_report_entry.get().split('-')
    #             for item in item_list:
    #                 if (item[2].split('/'))[1] < min or (item[2].split('/'))[1] > max:
    #                     item_list.remove(item)
                        
    #         if len(self.year_report_entry.get()) != 0:
    #             min, max = self.year_report_entry.get().split('-')
    #             for item in item_list:
    #                 if (item[2].split('/'))[1] < min or (item[2].split('/'))[1] > max:
    #                     item_list.remove(item)
                        
    #         if len(self.price_amount_entry.get()) !=0:
    #             min , max = self.price_amount_entry.get().split('-')
    #             for item in item_list:
    #                 if item[1] < min 
    
    def check_page(self):
        pass
        
    def return_category_list(self, id):
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS categories(user_name TEXT NOT NULL UNIQUE);''')
        c.execute("SELECT * FROM categories WHERE user_name = ?;", (id,))
        category_on_db = c.fetchall()
        
        connect.commit()
        connect.close()
        
        return category_on_db
    
    def get_income_from_db(self, user_name, source, kind):
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        if source == '':
            c.execute("SELCET * FROM TABLE income WHERE user_name = ? and income_resource = ? ;",
                    (user_name, kind))
        elif kind == '':
            c.execute("SELCET * FROM TABLE income WHERE user_name = ? and category = ? ;",
                    (user_name, source))
        elif source == '' and kind == '':
            c.execute("SELCET * FROM TABLE income WHERE user_name = ? ;", (user_name,))
        else:
            c.execute("SELCET * FROM TABLE income WHERE user_name = ? and income_resource = ? and category = ? ;",
                    (user_name, kind, source))
        item_selcted = c.fetchall()
        
        connect.commit()
        connect.close()
        
        return item_selcted
        
class Main(Tk):
    def __init__(self):
        super().__init__()
        self.title("Accountig")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK_OFF)
        self.object_list = []
        

        self.setup_ui()
        
        
    def setup_ui(self):
        self.background_image = PhotoImage(file="main_2.png")
        self.canvas = Canvas(self, width=1125, height=800, highlightthickness=0, bg=BG_COLOR_BACK_OFF)
        self.canvas.create_image(562.5, 400, image=self.background_image)
        self.canvas.place(relwidth=1, relheight=1)
        
        self.set_income_button = CTkButton(
            master=self,
            width=273,
            height=62,
            corner_radius=0,
            border_width=0,
            hover=TRUE,
            fg_color=BG_COLOR_BACK_OFF,
            text="Set income",
            text_color="#4B3E39",
            font=FONT_BUTTON       
        )
        self.set_income_button.place(x=0, y=187)
        self.set_income_button.bind("<Enter>", self.on_enter_set_income)
        self.set_income_button.bind("<Leave>", self.on_leave_set_income)
        self.set_income_button.bind("<Button-1>", self.show_income_page)
        
        self.cost_register_button = CTkButton(
            master=self,
            width=273,
            height=62,
            corner_radius=0,
            border_width=0,
            hover=TRUE,
            fg_color=BG_COLOR_BACK_OFF,
            text="Cost registration",
            text_color="#4B3E39",
            font=FONT_BUTTON       
        )
        self.cost_register_button.place(x=0, y=237)
        self.cost_register_button.bind("<Enter>", self.on_enter_cost_register)
        self.cost_register_button.bind("<Leave>", self.on_leave_cost_register)
        self.cost_register_button.bind("<Button-1>", self.cost_registration)
        
        
        self.categories_button = CTkButton(
            master=self,
            width=273,
            height=62,
            corner_radius=0,
            border_width=0,
            hover=TRUE,
            fg_color=BG_COLOR_BACK_OFF,
            text="Categories",
            text_color="#4B3E39",
            font=FONT_BUTTON       
        )
        self.categories_button.place(x=0, y=287)
        self.categories_button.bind("<Enter>", self.on_enter_categories)
        self.categories_button.bind("<Leave>", self.on_leave_categories)
        self.categories_button.bind("<Button-1>", self.show_category_page)
        
        self.search_button = CTkButton(
            master=self,
            width=273,
            height=62,
            corner_radius=0,
            border_width=0,
            hover=TRUE,
            fg_color=BG_COLOR_BACK_OFF,
            text="Search",
            text_color="#4B3E39",
            font=FONT_BUTTON       
        )
        self.search_button.place(x=0, y=337)
        self.search_button.bind("<Enter>", self.on_enter_search)
        self.search_button.bind("<Leave>", self.on_leave_search)
        
        self.reporting_button = CTkButton(
            master=self,
            width=273,
            height=62,
            corner_radius=0,
            border_width=0,
            hover=TRUE,
            fg_color=BG_COLOR_BACK_OFF,
            text="Reporting",
            text_color="#4B3E39",
            font=FONT_BUTTON       
        )
        self.reporting_button.place(x=0, y=387)
        self.reporting_button.bind("<Enter>", self.on_enter_reporting)
        self.reporting_button.bind("<Leave>", self.on_leave_reporting)
        self.reporting_button.bind("<Button-1>", self.show_reporting_page)
        
        self.setting_button = CTkButton(
            master=self,
            width=273,
            height=62,
            corner_radius=0,
            border_width=0,
            hover=TRUE,
            fg_color=BG_COLOR_BACK_OFF,
            text="Setting",
            text_color="#4B3E39",
            font=FONT_BUTTON       
        )
        self.setting_button.place(x=0, y=437)
        self.setting_button.bind("<Enter>", self.on_enter_setting)
        self.setting_button.bind("<Leave>", self.on_leave_setting)
        self.setting_button.bind("<Button-1>", self.show_setting_page)
        
        self.exit_button = CTkButton(
            master=self,
            width=273,
            height=62,
            corner_radius=0,
            border_width=0,
            hover=TRUE,
            fg_color=BG_COLOR_BACK_OFF,
            text="Exit",
            text_color="#4B3E39",
            font=FONT_BUTTON       
        )
        self.exit_button.place(x=0, y=487)
        self.exit_button.bind("<Enter>", self.on_enter_exit)
        self.exit_button.bind("<Leave>", self.on_leave_exit)
        self.exit_button.bind("<Button-1>", self.on_exit_click)
        
        
        self.line_canvas = Canvas(self, width=803, height=1, bg=BG_COLOR_BACK_OFF, highlightthickness=0)
        self.line_canvas.place(x=300, y=150)
        self.line_canvas.create_line(0, 0, 803, 0, fill="#000000", width=1)
        
        

    def show_income_page(self, event):
        self.income_page = IncomePage(self)
        self.object_list.append(self.income_page)
        for object in self.object_list:
            object.clear_widgets()
        self.income_page.setup_ui()
        
    def on_enter_set_income(self, event):
        self.set_income_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_set_income(self, event):
        self.set_income_button.configure(fg_color=BG_COLOR_BACK_OFF)
    
    def cost_registration(self, event):
        self.cost_page = CostPage(self)
        self.object_list.append(self.cost_page)
        for object in self.object_list:
            object.clear_widgets()
        self.cost_page.setup_ui()    
        
    def on_enter_cost_register(self, event):
        self.cost_register_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_cost_register(self, event):
        self.cost_register_button.configure(fg_color=BG_COLOR_BACK_OFF)
    
    def show_category_page(self, event):
        self.category_page = CategoryPage(self)
        self.object_list.append(self.category_page)
        for object in self.object_list:
            object.clear_widgets()
        self.category_page.setup_ui()    
    
    def on_enter_categories(self, event):
        self.categories_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_categories(self, event):
        self.categories_button.configure(fg_color=BG_COLOR_BACK_OFF)
     
    def show_search_page(self, event):
        pass
        
    def on_enter_search(self, event):
        self.search_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_search(self, event):
        self.search_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
    def show_reporting_page(self, event):
        self.report_page = ReportingPage(self)
        self.object_list.append(self.report_page)
        for object in self.object_list:
            object.clear_widgets()   
        self.report_page.setup_ui()
        
    def on_enter_reporting(self, event):
        self.reporting_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_reporting(self, event):
        self.reporting_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
    def show_setting_page(self, event):
        self.setting_page = SettingPage(self)
        self.object_list.append(self.setting_page)
        for object in self.object_list:
            object.clear_widgets()
        self.setting_page.setup_ui()
    
    def on_enter_setting(self, event):
        self.setting_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_setting(self, event):
        self.setting_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
    
    def on_exit_click(self, event):
        message_box = tkinter.messagebox.askquestion('Exit','آیا برای خروج مطمین هستید؟', icon = 'warning')
        if message_box == 'yes':
            self.destroy()
    
    def on_enter_exit(self, event):
        self.exit_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_exit(self, event):
        self.exit_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
        
        
        
def start():
    app = Main()
    app.mainloop()   

if __name__ == "__main__":
    start()
