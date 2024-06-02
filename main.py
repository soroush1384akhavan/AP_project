from tkinter import *
import tkinter.messagebox
from customtkinter import *
import Creat_account
from tkinter import Toplevel

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

class LoginApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Accountig")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK_OFF)

        self.setup_ui()
        
        
    def setup_ui(self):
        self.background_image = PhotoImage(file="main_2.png")
        self.canvas = Canvas(width=1125, height=800, highlightthickness=0, bg=BG_COLOR_BACK_OFF)
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
    app = LoginApp()
    app.mainloop()   

if __name__ == "__main__":
    start()