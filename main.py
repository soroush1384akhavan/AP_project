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
        self.cost_amount_entry.place(x=490, y=182)
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
        
        self.category_list = ('bank', 'company', 'personal')
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
        self.source_of_income_menu.place(x=556, y=310)
        
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
        self.category_menu.place(x=920, y=310)
        
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
            self.description_entry
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
        
            self.set_income_info_in_db(12, self.cost_amount_entry.get(), self.date_entry.get(), self.option_var1.get(), self.option_var2.get(), self.description_entry.get("1.0", END))
            tkinter.messagebox.showinfo('succes', 'the information successfully saved')
            
        
    def set_income_info_in_db(self, id, mizan, date, main, category, description= ''):
        
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS income(
                id INTEGER NOT NULL, 
                mizan INTEGER NoT NULL,
                date text NOT NULL,
                income_resource text NIT NULL,
                category text,
                description text);''')
        
        c.execute('''INSERT INTO income (id, mizan, date, income_resource, category, description)
                VALUES (?, ?, ?, ?, ?, ?);''', [id, mizan, date, main, category, description])
        
        connect.commit()
        connect.close()

class Main(Tk):
    def __init__(self):
        super().__init__()
        self.title("Accountig")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK_OFF)
        self.widget_list = []

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
        
        
        self.line_canvas = Canvas(self, width=803, height=1, bg=BG_COLOR_BACK_OFF, highlightthickness=0)
        self.line_canvas.place(x=300, y=150)
        self.line_canvas.create_line(0, 0, 803, 0, fill="#000000", width=1)
        
        
        self.income_page = IncomePage(self)

    def show_income_page(self, event):
        self.income_page.clear_widgets()
        self.income_page.setup_ui()
        
    def cost_registration(self, event):
        for widget in self.income_page.widget_list:
            widget.place_forget() 
            print("meow")
        self.widget_list.clear()
        self.cost_label = Label(
                self, 
                text="meow:", 
                font=('Kdam Thmor', 20),
                fg="black", 
                bg="white"
            )
        
        self.cost_label.place(
            x=306, 
            y=165, 
            width=200, 
            height=74
        )
        
        self.widget_list.append(self.cost_label)
        
        
    def on_enter_set_income(self, event):
        self.set_income_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_set_income(self, event):
        self.set_income_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
        
    def on_enter_cost_register(self, event):
        self.cost_register_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_cost_register(self, event):
        self.cost_register_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
    
    def on_enter_categories(self, event):
        self.categories_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_categories(self, event):
        self.categories_button.configure(fg_color=BG_COLOR_BACK_OFF)
     
        
    def on_enter_search(self, event):
        self.search_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_search(self, event):
        self.search_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
        
    def on_enter_reporting(self, event):
        self.reporting_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_reporting(self, event):
        self.reporting_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
    
    def on_enter_setting(self, event):
        self.setting_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_setting(self, event):
        self.setting_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
    
    def on_enter_exit(self, event):
        self.exit_button.configure(fg_color=BG_COLOR_BACK_ON)
        
    def on_leave_exit(self, event):
        self.exit_button.configure(fg_color=BG_COLOR_BACK_OFF)
        
        
        
        
def start():
    app = Main()
    app.mainloop()   

if __name__ == "__main__":
    start()
