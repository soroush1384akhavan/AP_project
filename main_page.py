from tkinter import *
import tkinter.messagebox
from customtkinter import *
import Creat_account
from tkinter import Toplevel
import sqlite3
import re
import pickle

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
        
        self.income_list = ('cash', 'chek', 'cripto') 
        self.option_var1 = StringVar() 
        self.option_var1.set(self.income_list[0]) 
        
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        self.category_list = self.return_category_list(person.username)
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
                text="Type:", 
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
            with open('user_object.pkl', 'rb') as input:
                person = pickle.load(input)
            self.set_income_info_in_db(person.username, self.income_amount_entry.get(), self.date_entry.get(), self.category_menu.get(), self.source_of_income_menu.get(), self.description_entry.get("1.0", END))
            tkinter.messagebox.showinfo('succes', 'the information successfully saved')
            
        
    def set_income_info_in_db(self, user_name, mizan, date, source, type_of_income, description= ''):
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        connect = sqlite3.connect(f'{user_name}.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS income(
                user_name INTEGER NOT NULL, 
                mizan INTEGER NOT NULL,
                date text NOT NULL,
                income_resource text NIT NULL,
                type_of_income text,
                description text);''')
        
        c.execute('''INSERT INTO income (user_name, mizan, date, income_resource, type_of_income, description)
                VALUES (?, ?, ?, ?, ?, ?);''', [user_name, mizan, date, source, type_of_income, description])
        
        connect.commit()
        connect.close()
        
    def return_category_list(self, user_name):
        connect = sqlite3.connect(f'{user_name}.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS categories(user_name TEXT NOT NULL UNIQUE);''')
        c.execute("SELECT * FROM categories WHERE user_name = ?;", (user_name,))
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
        
        self.income_list = ('cash', 'chek', 'cripto') 
        self.option_var1 = StringVar() 
        self.option_var1.set(self.income_list[0]) 
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        self.category_list = self.return_category_list(person.username)
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
                text="Type:", 
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
            self.title_label,
            self.submit_btn
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
            with open('user_object.pkl', 'rb') as input:
                person = pickle.load(input)
            self.set_cost_info_in_db(person.username, self.cost_amount_entry.get(), self.date_entry.get(), self.category_menu.get(), self.source_of_income_menu.get(), self.description_entry.get("1.0", END))
            tkinter.messagebox.showinfo('succes', 'the information successfully saved')
            
        
    def set_cost_info_in_db(self, user_name, mizan, date, source, type_of_cost, description= ''):
        connect = sqlite3.connect(f'{user_name}.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS cost(
                user_name TEXT NOT NULL, 
                mizan INTEGER NoT NULL,
                date text NOT NULL,
                cost_resource text NIT NULL,
                type_of_cost text,
                description text);''')
        
        c.execute('''INSERT INTO cost (user_name, mizan, date, cost_resource, type_of_cost, description)
                VALUES (?, ?, ?, ?, ?, ?);''', [user_name, mizan, date, source, type_of_cost, description])

        connect.commit()
        connect.close()
        
    def return_category_list(self, user_name):
        connect = sqlite3.connect(f'{user_name}.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS categories(user_name TEXT NOT NULL UNIQUE);''')
        c.execute("SELECT * FROM categories WHERE user_name = ?;", (user_name,))
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
            with open('user_object.pkl', 'rb') as input:
                person = pickle.load(input)
            self.set_category_info_in_db(person.username, self.category_entry.get())
            tkinter.messagebox.showinfo('complete', 'the category succesfully saved')
            
    def set_category_info_in_db(self, user_name, category):
        
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        connect = sqlite3.connect(f'{person.username}.db')
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
        
        message_box = tkinter.messagebox.askquestion('delete account','آیا برای حذف اکانت خود مطمین هستید؟', icon = 'warning')
        if message_box == 'yes':
              pass
        
    def on_delete_info_click(self, event):
        
        message_box = tkinter.messagebox.askquestion('delete info','آیا برای حذف اطلاعات خود مطمین هستید؟', icon = 'warning')
        if message_box:
            with open('user_object.pkl', 'rb') as input:
                person = pickle.load(input)
            self.delete_transaction(person.username, self.option_var.get())
            tkinter.messagebox.showinfo('complite', 'the information you chose was deleted')
                
    def delete_transaction(self, user_name, change):
        if change == 'income':
            connect = sqlite3.connect(f'{user_name}.db')
            c = connect.cursor()
            c.execute('''DELETE FROM income WHERE user_name = ?;''' ,(user_name,))
            
            connect.commit()
            connect.close()
            
        elif change == 'price':
            connect = sqlite3.connect(f'{user_name}.db')
            c = connect.cursor()
            c.execute('''DELETE FROM price WHERE user_name = ?;''' ,(user_name,))
            
            connect.commit()
            connect.close()
            
        elif change == 'both':
            connect = sqlite3.connect(f'{user_name}.db')
            c = connect.cursor()
            c.execute('''DELETE FROM income WHERE user_name = ?;''', (user_name,))
            c.execute('''DELETE FROM price WHERE user_name = ?;''', (user_name,))
            
            connect.commit()
            connect.close()

class SearchResultWindow:
    def __init__(self, results):
        self.results = results
        
        self.window = Toplevel()
        self.window.title("Search Results")
        
        self.result_text = Text(self.window, wrap="word")
        self.result_text.pack(fill="both", expand=True)
        
        self.display_results()

    def display_results(self):
        for result in self.results:
            self.result_text.insert("end", f"{result}\n")   
      
class SearchPage:
    def __init__(self, master):
        self.master = master
        self.widget_list = []

        self.setup_ui()

    def setup_ui(self):
        self.search_label = Label(
                self.master, 
                text="search", 
                font=('Bold', 40),
                fg="black", 
                bg="white"
            )
        self.search_label.place(
            x=313, 
            y=38, 
            width=287, 
            height=74
        )    
        
        self.filter_label = Label(
                self.master, 
                text="filters:", 
                font=('inter', 20),
                fg="black", 
                bg="white"
            )
        self.filter_label.place(
            x=306, 
            y=165, 
            width=93, 
            height=74
        )     
            
        self.year_label = Label(
                self.master, 
                text="Year:", 
                font=('light', 20),
                fg="black", 
                bg="white"
            )
        self.year_label.place(
            x=306, 
            y=245, 
            width=66, 
            height=74
        ) 
        
        self.month_label = Label(
                self.master, 
                text="Month:", 
                font=('light', 20),
                fg="black", 
                bg="white"
            )
        self.month_label.place(
            x=566, 
            y=245, 
            width=94, 
            height=74
        )  
        
        self.day_label = Label(
                self.master, 
                text="Day:", 
                font=('light', 20),
                fg="black", 
                bg="white"
            )
        self.day_label.place(
            x=866, 
            y=245, 
            width=66, 
            height=74
        )    
        
        self.search_in_label = Label(
                self.master, 
                text="Search in:", 
                font=('light', 20),
                fg="black", 
                bg="white"
            )
        self.search_in_label.place(
            x=306, 
            y=325, 
            width=135, 
            height=74
        )   
        
        self.money_range_label = Label(
                self.master, 
                text="Money range:", 
                font=('light', 20),
                fg="black", 
                bg="white"
            )
        self.money_range_label.place(
            x=666, 
            y=325, 
            width=188, 
            height=74
        ) 
        
        self.search_in_2_label = Label(
                self.master, 
                text="Search in:", 
                font=('light', 20),
                fg="black", 
                bg="white"
            )
        self.search_in_2_label.place(
            x=306, 
            y=405, 
            width=135, 
            height=74
        ) 
        
        self.search_goal_label = Label(
                self.master, 
                text="What do you want to search?", 
                font=('light', 20),
                fg="black", 
                bg="white"
            )
        self.search_goal_label.place(
            x=306, 
            y=487, 
            width=372, 
            height=100
        ) 
        
        self.from_label = Label(
                self.master, 
                text="from", 
                font=('light', 20),
                fg="black", 
                bg="white"
            )
        self.from_label.place(
            x=856, 
            y=325, 
            width=66, 
            height=74
        )
        
        self.to_label = Label(
                self.master, 
                text="to", 
                font=('light', 20),
                fg="black", 
                bg="white"
            )
        self.to_label.place(
            x=976, 
            y=325, 
            width=66, 
            height=74
        )
        
        self.from_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=60,
            height=60,
            border_width=2,
            bg_color="white",
            corner_radius=10,
            border_color= "#3300FF",
            fg_color="white",
            placeholder_text_color="gray",
            text_color="black"
            )
        self.from_entry.place(x=924, y=332)
        self.from_entry.bind("<KeyRelease>", self.check_from_and_to)
        self.from_entry.bind("<KeyRelease>", self.check_page)
        
        self.to_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=60,
            height=60,
            border_width=2,
            bg_color="white",
            corner_radius=10,
            border_color= "#3300FF",
            fg_color="white",
            placeholder_text_color="gray",
            text_color="black"
            )
        self.to_entry.place(x=1040, y=332)
        self.to_entry.bind("<KeyRelease>", self.check_from_and_to)
        self.to_entry.bind("<KeyRelease>", self.check_page)
        
        self.year_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=159,
            height=40,
            border_width=2,
            bg_color="white",
            corner_radius=10,
            border_color= "#3300FF",
            fg_color="white",
            placeholder_text_color="gray",
            text_color="black"
            )
        self.year_entry.place(x=390, y=262)
        self.year_entry.bind("<KeyRelease>", self.check_year)
        self.year_entry.bind("<KeyRelease>", self.check_page)
        
        self.month_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=159,
            height=40,
            border_width=2,
            bg_color="white",
            corner_radius=10,
            border_color= "#3300FF",
            fg_color="white",
            placeholder_text_color="gray",
            text_color="black"
            )
        self.month_entry.place(x=670, y=262)
        self.month_entry.bind("<KeyRelease>", self.check_month)
        self.month_entry.bind("<KeyRelease>", self.check_page)
        
        self.day_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=159,
            height=40,
            border_width=2,
            bg_color="white",
            corner_radius=10,
            border_color= "#3300FF",
            fg_color="white",
            placeholder_text_color="gray",
            text_color="black"
            )
        self.day_entry.place(x=930, y=262)
        self.day_entry.bind("<KeyRelease>", self.check_day)
        self.day_entry.bind("<KeyRelease>", self.check_page)
        
        self.search_goal_entry = CTkEntry(
            master=self.master,
            font=FONT_STYLE_ENTRY,
            width=392,
            height=62,
            border_width=2,
            bg_color="white",
            corner_radius=10,
            border_color= "#3300FF",
            fg_color="white",
            placeholder_text_color="gray",
            text_color="black"
            )
        self.search_goal_entry.place(x=712, y=507)
        
        
        self.search_btn = CTkButton(
            master= self.master,
            width=130,
            height=47,
            state=NORMAL,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color="white",
            bg_color="white",
            text="Search",
            text_color="black",
            font=('Kdam Thmor', 17)
            #command=self.on_search_clicked
            )
        self.search_btn.place(x=300, y=615)
        self.search_btn.bind("<Button-1>", self.on_search_clicked)
        
        
        self.search_list_1 = ['Income', 'Cost']
        self.search_in_menu = CTkOptionMenu(
            master=self.master,
            button_color="#FFCC5C",
            height=40,
            width=150,
            font=("arial", 20),
            fg_color="#FBE5B6",
            bg_color="white",
            dropdown_fg_color="white",
            dropdown_hover_color="#F8E1AF",
            button_hover_color="#FFCC5C",
            text_color="black",
            dropdown_text_color="black",
            values=self.search_list_1 
            )
        self.search_in_menu.place(x=470, y=343)
        
        self.search_list_2 = ['Description', 'money type', 'source', 'all' ]
        self.search_in_2_menu = CTkOptionMenu(
        master=self.master,
        button_color="#FFCC5C",
        height=40,
        width=150,
        font=("arial", 20),
        fg_color="#FBE5B6",
        bg_color="white",
        dropdown_fg_color="white",
        dropdown_hover_color="#F8E1AF",
        button_hover_color="#FFCC5C",
        text_color="black",
        dropdown_text_color="black",
        values=self.search_list_2
        )
        self.search_in_2_menu.place(x=470, y=427)
        
        self.widget_list.extend([
            self.search_in_2_label,
            self.search_in_label,
            self.money_range_label,
            self.day_label,
            self.month_label,
            self.year_label,
            self.filter_label,
            self.search_label,
            self.search_goal_label,
            self.year_entry,
            self.month_entry,
            self.day_entry,
            self.search_goal_entry,
            self.search_in_menu,
            self.search_in_2_menu,
            self.from_label,
            self.to_label,
            self.from_entry,
            self.to_entry,
            self.search_btn
        ])
    
    def clear_widgets(self):
        for widget in self.widget_list:
            widget.place_forget()
        self.widget_list.clear()
        
    def check_year(self, event):
        value = self.year_entry.get()
        if value.isdigit() and 1920 <= int(value) <= 2040 or value == "":
            self.year_entry.configure(border_color="green")
            return True
        else:
            self.year_entry.configure(border_color="red")
            return False

    def check_month(self, event):
        value = self.month_entry.get()
        if value.isdigit() and 1 <= int(value) <= 12 or value == "":
            self.month_entry.configure(border_color="green")
            return True
        else:
            self.month_entry.configure(border_color="red")
            return False
        
    def check_day(self, event):
        value = self.day_entry.get()
        if value.isdigit() and 1 <= int(value) <= 31 or value == "":
            self.day_entry.configure(border_color="green")
            return True
        else:
            self.day_entry.configure(border_color="red")
            return False
        
    def check_from_and_to(self, event):
        from_g = self.from_entry.get()
        to_g = self.to_entry.get()
        try:
            if from_g.isdigit() and  0 <= int(from_g) <= int(to_g) and from_g.isdigit() or(from_g=="" and from_g==""): 
                self.from_entry.configure(border_color="green")
                self.to_entry.configure(border_color="green")
                return True
            else:
                self.from_entry.configure(border_color="red")
                self.to_entry.configure(border_color="red")
                return False
        except:
            pass
        
    def check_page(self, event):
        if self.check_year(None) and self.check_month(None) and self.check_day(None) and self.check_from_and_to(None):
            self.search_btn.configure(state=NORMAL) 
        else:
            self.search_btn.configure(state=DISABLED)
                
    def on_leave_search(self, event):
        if self.search_btn.cget('state') == NORMAL:
            self.search_btn.configure(fg_color="#B0B2AE")
        
    def on_enter_search(self, event):
        self.search_btn.configure(fg_color="white")
    


    def on_search_clicked(self, event):
        year = self.year_entry.get()
        month = self.month_entry.get()
        day = self.day_entry.get()
        from_amount = self.from_entry.get()
        to_amount = self.to_entry.get()
        search_in = self.search_in_menu.get()
        search_in_2 = self.search_in_2_menu.get()
        search_goal = self.search_goal_entry.get()
        print(f'{search_in}:')
        if search_in == "Cost":
            results_cost = self.search_database_cost("cost", year, month, day, from_amount, to_amount, search_in, search_in_2, search_goal)
        elif search_in == 'Income':
            results_cost = self.search_database_income("Income", year, month, day, from_amount, to_amount, search_in, search_in_2, search_goal)
        
        results = results_cost
        search_result_window = SearchResultWindow(results_cost)
        print(results)

    
    def search_database_income(self, table_name, year, month, day, from_amount, to_amount, search_in, search_in_2, search_goal):
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        connect = sqlite3.connect(f'{person.username}.db')
        cursor = connect.cursor()

        query = f"SELECT * FROM {table_name} WHERE 1=1"
        params = []

        if search_goal and search_in_2=="all":
            query += " AND (mizan LIKE ? OR income_resource LIKE ? OR type_of_income LIKE ? OR description LIKE ?)"
            like_pattern = f"%{search_goal}%"
            params.extend([like_pattern, like_pattern, like_pattern, like_pattern])
            
        elif search_goal and search_in_2=="Description":
            query += " AND description LIKE ?"
            like_pattern = f"%{search_goal}%"
            params.extend([like_pattern])
        
        elif search_goal and search_in_2=="money type":
            query += " AND type_of_income LIKE ?"
            like_pattern = f"%{search_goal}%"
            params.extend([like_pattern])
            
        elif search_goal and search_in_2=="source":
            query += " AND income_resource LIKE ?"
            like_pattern = f"%{search_goal}%"
            params.extend([like_pattern])
            
        if year:
            query += " AND substr(date, 1, instr(date, '/')-1) = ?"
            params.append(year)

        if month:
            query += " AND substr(date, instr(date, '/')+1, instr(substr(date, instr(date, '/')+1), '/')-1) = ?"
            params.append(month)

        if day:
            query += " AND (SUBSTR(date, -1) = ? OR SUBSTR(date, -2) = ?)"
            params.extend([day, day])

        cursor.execute(query, params)
        results = cursor.fetchall()

        connect.close()
        return results
    
    
    def search_database_cost(self, table_name, year, month, day, from_amount, to_amount, search_in, search_in_2, search_goal):
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        connect = sqlite3.connect(f'{person.username}.db')
        cursor = connect.cursor()

        query = f"SELECT * FROM {table_name} WHERE 1=1"
        params = []

        if search_goal:
            query += " AND (mizan LIKE ? OR cost_resource LIKE ? OR type_of_cost LIKE ? OR description LIKE ?)"
            like_pattern = f"%{search_goal}%"
            params.extend([like_pattern, like_pattern, like_pattern, like_pattern])
        
        if year:
            query += " AND strftime('%Y', date) = ?"
            params.append(year)
        if month:
            query += " AND strftime('%m', date) = ?"
            params.append(month)
        if day:
            query += " AND strftime('%d', date) = ?"
            params.append(day)
        if from_amount:
            query += " AND mizan >= ?"
            params.append(from_amount)
        if to_amount:
            query += " AND mizan <= ?"
            params.append(to_amount)

        cursor.execute(query, params)
        results = cursor.fetchall()

        connect.close()
        return results





            
        
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
        self.day_report_entry.bind("<KeyRelease>", self.check_day)
        self.day_report_entry.bind("<KeyRelease>", self.check_day)
        
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
        self.month_report_entry.bind("<KeyRelease>", self.check_month)
        self.month_report_entry.bind("<KeyRelease>", self.check_month)
        
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
        self.year_report_entry.bind("<KeyRelease>", self.check_year)
        self.year_report_entry.bind("<KeyRelease>", self.check_year)
        
        
        self.report_kind_list = ('cash', 'chek', 'cripto') 
        self.option_var1 = StringVar() 
        self.option_var1.set(self.report_kind_list[0]) 
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        self.report_source_list = self.return_category_list(person.username)
        if len(self.report_source_list) == 0:
            self.report_source_list = ["","you didn't add a category"]
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
        self.price_amount_entry.bind("<KeyRelease>", self.check_money)
        self.price_amount_entry.bind("<KeyRelease>", self.check_money)
        
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
        
        self.value_listbox = Listbox(
            master= self.master,
            font= FONT_STYLE_ENTRY,
        )
        self.value_listbox.place(x=310, y=560, width=740, height=135)
        
        self.submit_btn = CTkButton(
            master= self.master,
            width=150,
            height=55,
            state=DISABLED,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color="white",
            bg_color="white",
            text="Filtering",
            text_color="black",
            font=FONT_BUTTON)
        
        self.submit_btn.place(x=310, y=720)
        self.submit_btn.bind("<Button-1>", self.on_submit_clicked)
        self.submit_btn.bind("<Enter>", self.on_enter_submit)
        self.submit_btn.bind("<Leave>", self.on_leave_submit)
        

        
        self.widget_list.extend([
            self.submit_btn,
            self.section_menu,
            self.report_section_label,
            self.price_amount_entry,
            self.price_amount_label,
            self.kind_menu,
            self.report_kind_label,
            self.source_menu,
            self.report_source_label,
            self.report_day_label,
            self.year_report_entry,
            self.day_report_entry,
            self.report_year_label,
            self.month_report_entry,
            self.report_month_label,
            self.reporting_label,
            self.value_listbox
        ])
        
    def clear_widgets(self):
        for widget in self.widget_list:
            widget.place_forget()
        self.widget_list.clear()
        
    def on_submit_clicked(self, event):
        self.submit_btn.configure(fg_color="gray")
        self.submit_btn.after(200, lambda: self.submit_btn.configure(fg_color="white"))
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        sum_of_income = 0
        sum_of_cost = 0
        
        income_list = self.get_income_from_db(person.username, self.source_menu.get(), self.kind_menu.get())
        income_list = self.add_filter(income_list)
        for item in income_list:
            sum_of_income += int(item[1])
        
        cost_list = self.get_cost_from_db(person.username, self.source_menu.get(), self.kind_menu.get())
        cost_list = self.add_filter(cost_list)
        for item in cost_list:
            sum_of_cost += int(item[1])
        
        if self.section_menu.get() == "income" :   
            for item in income_list:
                self.value_listbox.insert('end', item[1:-1], r"{:.2f} % of income".format(int(item[1])/sum_of_income))
        elif self.section_menu.get() == 'cost':
            for item in cost_list:
                self.value_listbox.insert('end', item[1:-1], r"{:.2f} % of cost".format(int(item[1])/sum_of_cost))
        elif self.section_menu.get() == 'both':
            for item in income_list:
                self.value_listbox.insert('end', item[1:-1], r"{:.2f} % of income".format(int(item[1])/sum_of_income))
            for item in cost_list:
                self.value_listbox.insert('end', item[1:-1], r"{:.2f} % of cost".format(int(item[1])/sum_of_cost))

    
    def on_enter_submit(self, event):
        self.submit_btn.configure(fg_color="#B0B2AE")
    
    def on_leave_submit(self, event):
        self.submit_btn.configure(fg_color="white")
        
    def add_filter(self, item_list):        
        if len(self.day_report_entry.get()) != 0:
            min, max = self.day_report_entry.get().split('-')
            for item in item_list:
                if (item[2].split('/'))[2] < min or (item[2].split('/'))[2] > max:
                    item_list.remove(item)
                        
        if len(self.month_report_entry.get()) != 0:
            min, max = self.month_report_entry.get().split('-')
            for item in item_list:
                if (item[2].split('/'))[1] < min or (item[2].split('/'))[1] > max:
                    item_list.remove(item)
                        
        if len(self.year_report_entry.get()) != 0:
            min, max = self.year_report_entry.get().split('-')
            for item in item_list:
                if (item[2].split('/'))[1] < min or (item[2].split('/'))[1] > max:
                    item_list.remove(item)
                        
        if len(self.price_amount_entry.get()) != 0:
            min , max = self.price_amount_entry.get().split('-')
            for item in item_list:
                if item[1] < min or item[1] > max:
                    item_list.remove(item)
                    
        return item_list
    
    def check_page(self):
        if self.check_year(None) and self.check_month(None) and self.check_day(None) and self.check_from_and_to(None):
            self.submit_btn.configure(state=NORMAL) 
        else:
            self.submit_btn.configure(state=DISABLED)
    
    def check_year(self, event):
        try:
            value1, value2 = self.year_report_entry.get().split('-')
            if value1.isdigit() and 1920 <= int(value1) <= 2040 and value2.isdigit() and 1920 <= int(value2) <= 2040 and int(value1)> int(value2):
                self.year_report_entry.configure(border_color="red")
                return True
            else:
                self.year_report_entry.configure(border_color="green")
                return False
        except:
            return False

            
    def check_month(self, event):
        try:
            value1, value2 = self.month_report_entry.get().split('-')
            if value1.isdigit() and 1 <= int(value1) <= 12 and value2.isdigit() and 1 <= int(value2) <= 12 and int(value1)> int(value2):
                self.month_report_entry.configure(border_color="red")
                return True
            else:
                self.month_report_entry.configure(border_color="green")
                return False
        except:
            self.month_report_entry.configure(border_color="red")
            return False
        
    def check_day(self, event):
        try:
            value1, value2 = self.day_report_entry.get().split('-')
            if value1.isdigit() and 1 <= int(value1) <= 31 and value2.isdigit() and 1 <= int(value2) <= 31 and int(value1)> int(value2):
                self.day_report_entry.configure(border_color="red")
                return True
            else:
                self.day_report_entry.configure(border_color="green")
                return False
        except:
            self.day_report_entry.configure(border_color="red")
            return False
        
    def check_money(self, event):
        try:
            value1, value2 = self.price_amount_entry.get().split('-')
            if value1.isdigit() and 0 < int(value1) and value2.isdigit() and 0 < int(value2) and int(value1)> int(value2):
                self.price_amount_entry.configure(border_color="red")
                return True
            else:
                self.price_amount_entry.configure(border_color="green")
                return False
        except:
            self.price_amount_entry.configure(border_color="red")
            return False
        
    def return_category_list(self, user_name):
        connect = sqlite3.connect(f'{user_name}.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS categories(user_name TEXT NOT NULL UNIQUE);''')
        c.execute("SELECT * FROM categories WHERE user_name = ?;", (user_name,))
        category_on_db = c.fetchall()
        
        connect.commit()
        connect.close()
        
        return category_on_db
    
    def get_income_from_db(self, user_name, source, type_of_income):
        connect = sqlite3.connect(f'{user_name}.db')
        c = connect.cursor()
        if len(source) == 0 and len(type_of_income) !=0:
            c.execute("SELECT * FROM income WHERE user_name = ? and income_resource = ? ;",
                    (user_name, source))
        elif len(type_of_income) == 0 and len(source) != 0:
            c.execute("SELECT * FROM income WHERE user_name = ? and type_of_income = ? ;",
                    (user_name, type_of_income))
        elif len(source) == 0 and len(type_of_income) == 0:
            c.execute("SELECT * FROM income WHERE user_name = ? ;", (user_name,))
        else:
            c.execute("SELECT * FROM income WHERE user_name = ? and income_resource = ? and type_of_income = ? ;",
                    (user_name, source, type_of_income))
        item_selcted = c.fetchall()
        
        connect.commit()
        connect.close()
        
        return item_selcted
    
    def get_cost_from_db(self, user_name, source, type_of_cost):
        connect = sqlite3.connect(f'{user_name}.db')
        c = connect.cursor()
        if source == '':
            c.execute("SELECT * FROM cost WHERE user_name = ? AND cost_resource = ? ;",
                    (user_name, type_of_cost))
        elif type_of_cost == '':
            c.execute("SELECT * FROM cost WHERE user_name = ? AND type_of_cost = ? ;",
                    (user_name, source))
        elif source == '' and type_of_cost == '':
            c.execute("SELECT * FROM cost WHERE user_name = ? ;", (user_name,))
        else:
            c.execute("SELECT * FROM cost WHERE user_name = ? AND cost_resource = ? AND type_of_cost = ? ;",
                    (user_name, source, type_of_cost))
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
        self.background_image = PhotoImage(file="images/main_2.png")
        self.canvas = Canvas(self, width=1125, height=800, highlightthickness=0, bg=BG_COLOR_BACK_OFF)
        self.canvas.create_image(562.5, 400, image=self.background_image)
        self.canvas.place(relwidth=1, relheight=1)
        
        self.canvas.create_oval(30, 50, 80, 100, outline='black')
        
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
        self.search_button.bind("<Button-1>", self.show_search_page)
        
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
        
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        
        self.first_letter = Label(
          self.master, 
                text=f"{person.fname[0]}{person.lname[0]}", 
                font=('Kdam Thmor', 19),
                fg="black", 
                bg=BG_COLOR_BACK_OFF
            )
        self.first_letter.place(
            x=40, 
            y=60, 
            width=30, 
            height=30
        )
        
        self.user_name_label = Label(
          self.master, 
                text=f"{person.username}", 
                font=('Kdam Thmor', 19),
                fg="black", 
                bg=BG_COLOR_BACK_OFF
            )
        self.user_name_label.place(
            x=100, 
            y=60, 
            width=172, 
            height=30
        )
    
           
        
        
        
        self.line_canvas = Canvas(self, width=803, height=1, bg=BG_COLOR_BACK_OFF, highlightthickness=0)
        self.line_canvas.place(x=300, y=150)
        self.line_canvas.create_line(0, 0, 803, 0, fill="#000000", width=1)
        
        

    def show_income_page(self, event):
        self.income_page = IncomePage(self)
        self.object_list.append(self.income_page)
        for object in self.object_list:
            object.clear_widgets()
        self.income_page.setup_ui()
        
    def show_search_page(self, event):
        self.search_page = SearchPage(self)
        self.object_list.append(self.search_page)
        for object in self.object_list:
            object.clear_widgets()
        self.search_page.setup_ui()
        
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
        
   

import os
import platform

def clear_terminal():
    current_os = platform.system()
    if current_os == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

   
        
        
def start():
    try:
        app = Main()
        
        with open('user_object.pkl', 'rb') as input:
            person = pickle.load(input)
        print(person.fname)
        clear_terminal() 
        app.mainloop()   
    except:
        print("error")
if __name__ == "__main__":
    start()
