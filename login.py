from tkinter import *
import tkinter.messagebox
from customtkinter import *
import Creat_account
from tkinter import Toplevel
import pandas as pd
import time

# Constants
BG_COLOR_BACK = "#FBE5B6"
FONT_LABEL = ('Kaisei Opi', 60)
FONT_STYLE_ENTRY = ('Kdam Thmor', 20)
FONT_BUTTON = ('Kdam Thmor', 28.13)
TEXT_COLOR_ENTRY = "#BDB7B4"
BG_COLOR_ENTRY = "#F3EBE8"
LOG_IN_BUTTON_COLOR_OFF = "#FE8716"
LOG_IN_BUTTON_COLOR_ON = "#DD7A1C"
LOG_IN_BUTTON_COLOR_CLICK = "#B36317"
SIGN_IN_BUTTON_COLOR_ON = "#C0AC6F"
SIGN_IN_BUTTON_COLOR_OFF = "#E6CD80"
SIGN_IN_BUTTON_COLOR_CLICK = "#9A8A57"

class LoginApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK)
        
        self.failed_attempts = 0
        self.locked_until = 0
        
        self.setup_ui()
        #self.load_data()
        
    def setup_ui(self):
        self.background_image = PhotoImage(file="images/bg_4.png")
        self.canvas = Canvas(width=1201, height=800, highlightthickness=0, bg="#FBE4B8")
        self.canvas.create_image(550, 400, image=self.background_image)
        self.canvas.place(relwidth=1, relheight=1)

        self.username_entry = CTkEntry(
            master=self,
            placeholder_text="Username",
            font=FONT_STYLE_ENTRY,
            width=369,
            height=67.19,
            border_width=2,
            corner_radius=20,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        self.username_entry.place(x=649.5, y=328)
        
        self.password_entry = CTkEntry(
            master=self,
            placeholder_text="Password",
            font=FONT_STYLE_ENTRY,
            width=369,
            height=67.19,
            border_width=2,
            corner_radius=20,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black",
            show="●"
        )
        self.password_entry.place(x=649.5, y=412)
        
        self.label = Label(
            self, 
            text="Welcome!", 
            font=FONT_LABEL, 
            fg="#FF8D07", 
            bg=BG_COLOR_BACK
        )
        self.label.place(
            x=649.5, 
            y=158, 
            width=374.22, 
            height=101.56
        )

        self.log_in_button = CTkButton(
            master=self,
            width=376,
            height=64,
            corner_radius=20,
            border_width=1,
            hover=TRUE,
            fg_color=LOG_IN_BUTTON_COLOR_OFF,
            text="Login",
            text_color="white",
            font=FONT_BUTTON
        )
        self.log_in_button.place(x=647.5, y=516)
        self.log_in_button.bind("<Enter>", self.on_enter_log_in)
        self.log_in_button.bind("<Leave>", self.on_leave_log_in)
        self.log_in_button.bind("<Button-1>", self.on_click_log_in)
        
        self.signup = Label(
            self, 
            text="Don't have an account? ", 
            font=("Regular", 14), 
            fg="black", 
            bg=BG_COLOR_BACK
        )
        self.signup.place(
            x=709.5, 
            y=619, 
            width=198, 
            height=16
        )

        self.sign_in_button = CTkButton(
            master=self,
            width=50,
            height=16,
            corner_radius=0,
            border_width=0,
            hover=TRUE,
            fg_color=BG_COLOR_BACK,
            text="sign up",
            bg_color=BG_COLOR_BACK,
            text_color=LOG_IN_BUTTON_COLOR_OFF,
            font=("Regular", 18)
        )
        self.sign_in_button.place(x=910, y=615)
        self.sign_in_button.bind("<Enter>", self.on_enter_sign_in)
        self.sign_in_button.bind("<Leave>", self.on_leave_sign_in)
        self.sign_in_button.bind("<Button-1>", self.on_click_sign_in)

        self.forgot_password_button = CTkButton(
            master=self,
            width=102,
            height=16,
            corner_radius=10,
            border_width=0,
            hover=TRUE,
            fg_color=BG_COLOR_BACK,
            bg_color=BG_COLOR_BACK,
            text="Forgot Password",
            text_color=LOG_IN_BUTTON_COLOR_OFF,
            font=("Regular", 18)
        )
        self.forgot_password_button.place(x=765.5, y=586)
        self.forgot_password_button.bind("<Enter>", self.on_enter_forgot_password)
        self.forgot_password_button.bind("<Leave>", self.on_leave_forgot_password)
        self.forgot_password_button.bind("<Button-1>", self.on_click_forgot_password)

    def load_data(self):
        import get_from_sheet
        data = get_from_sheet.get_from_google()
        return data
    
    def on_enter_sign_in(self, event):
        self.sign_in_button.configure(text_color=LOG_IN_BUTTON_COLOR_ON)
      
    def on_leave_sign_in(self, event):
        self.sign_in_button.configure(text_color=LOG_IN_BUTTON_COLOR_OFF)
    
    def on_click_sign_in(self, event):
        self.sign_in_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_CLICK)
        self.after(200, lambda: self.sign_in_button.configure(text_color=SIGN_IN_BUTTON_COLOR_OFF))
        self.destroy()
        Creat_account.start()
    
    def on_enter_log_in(self, event):
        self.log_in_button.configure(fg_color=LOG_IN_BUTTON_COLOR_ON)

    def on_leave_log_in(self, event):
        self.log_in_button.configure(fg_color=LOG_IN_BUTTON_COLOR_OFF)
    
    def on_click_log_in(self, event):
        current_time = time.time()
        if self.locked_until > current_time:
            tkinter.messagebox.showinfo("Account Locked", "Too many failed attempts. Please try again later.")
            return
        
        self.log_in_button.configure(fg_color=LOG_IN_BUTTON_COLOR_CLICK)
        self.after(200, lambda: self.log_in_button.configure(teext_color=LOG_IN_BUTTON_COLOR_OFF))
        if self.is_username_exists():
            if self.is_valid_credentials():
                self.create_person()
                self.destroy()
                try:
                    import main_page
                    main_page.start()
                except:
                    print("error")
            else:
                self.failed_attempts += 1
                if self.failed_attempts >= 3:
                    self.locked_until = current_time + 60
                    self.failed_attempts = 0
                    tkinter.messagebox.showinfo("Account Locked", "Too many failed attempts. Please try again after 1 minute.")
    
    def create_person(self):
        data = self.load_data()
        data_2 = pd.DataFrame(data['sheet1'])
        username = self.username_entry.get()
        user_row = data_2[data_2['username'] == username]
        user_dict = user_row.iloc[0].to_dict()
        import Person
        person = Person.Person(**user_dict)
        import pickle

        with open('user_object.pkl', 'wb') as output:
            pickle.dump(person, output, pickle.HIGHEST_PROTOCOL)
        
    def is_username_exists(self):
        data = self.load_data()
        username = self.username_entry.get()
        for account in data["sheet1"]:
            if account["username"] == username:
                return True
        tkinter.messagebox.showinfo("Account does not exist", "Check your username")
        return False
    
    def is_valid_credentials(self):
        data = self.load_data()
        username = self.username_entry.get()
        password = self.password_entry.get()
        for account in data["sheet1"]:
            if account["username"] == username and account["password"] == password:
                print("Welcome")
                return True
        tkinter.messagebox.showinfo("Incorrect password", "Check your password")
        return False

    def on_enter_forgot_password(self, event):
        self.forgot_password_button.configure(text_color=LOG_IN_BUTTON_COLOR_ON)

    def on_leave_forgot_password(self, event):
        self.forgot_password_button.configure(text_color=LOG_IN_BUTTON_COLOR_OFF)

    def on_click_forgot_password(self, event):
        self.forgot_password_button.configure(text_color=LOG_IN_BUTTON_COLOR_CLICK)
        self.after(200, lambda: self.forgot_password_button.configure(text_color=SIGN_IN_BUTTON_COLOR_OFF))
        self.open_forgot_password_window()

    def open_forgot_password_window(self):
        forgot_password_window = Toplevel(self)
        forgot_password_window.title("Forgot Password")
        forgot_password_window.geometry("600x400")
        forgot_password_window.configure(bg=BG_COLOR_BACK)

        username_2_entry = CTkEntry(
            master=forgot_password_window,
            placeholder_text="Username:",
            font=FONT_STYLE_ENTRY,
            width=400,
            height=67.19,
            border_width=2,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        username_2_entry.pack(pady=20)
        
        security_2_entry = CTkEntry(
            master=forgot_password_window,
            placeholder_text="What was your school name:",
            font=FONT_STYLE_ENTRY,
            width=400,
            height=67.19,
            border_width=2,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        security_2_entry.pack(pady=20)
        
        def is_valid_q():
            data = self.load_data()
            username = username_2_entry.get()
            question = security_2_entry.get()
            for account in data["sheet1"]:
                if account["username"] == username and account["securitytext"] == question:
                    tkinter.messagebox.showinfo("Password Retrieved", f"Your password is: {account['password']}")
                    return True
            tkinter.messagebox.showinfo("Incorrect Answer", "Check your answer")
            return False
        
        def on_click_submit(event):
            is_valid_q()
        
        what_is_button = CTkButton(
            master=forgot_password_window,
            width=175,
            height=64.06,
            corner_radius=10,
            border_width=1,
            hover=True,
            fg_color=LOG_IN_BUTTON_COLOR_OFF,
            text="Submit",
            text_color="black",
            font=FONT_BUTTON
        )
        what_is_button.pack(pady=20)
        what_is_button.bind("<Button-1>", on_click_submit)


def start():
    app = LoginApp()
    app.mainloop()

if __name__ == "__main__":
    start()
