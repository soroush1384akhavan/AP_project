from tkinter import *
import tkinter.messagebox
from customtkinter import *
import Creat_account
from tkinter import Toplevel
        
# Constants
BG_COLOR_BACK = "#FBE5B6"
FONT_LABEL = ('Kaisei Opi', 75)
FONT_STYLE_ENTRY = ('Kdam Thmor', 28.13)
FONT_BUTTON = ('Kdam Thmor', 28.13)
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
        self.title("Login")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK)

        self.setup_ui()
        #self.load_data()
        
    def setup_ui(self):
        self.background_image = PhotoImage(file="back_ground.png")
        self.canvas = Canvas(width=1201, height=800, highlightthickness=0, bg=BG_COLOR_BACK)
        self.canvas.create_image(550, 400, image=self.background_image)
        self.canvas.place(relwidth=1, relheight=1)

        self.username_entry = CTkEntry(
            master=self,
            placeholder_text="Username:",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=2,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
        )
        self.username_entry.place(x=562.5, y=277.34)
        



        self.forgot_password_button = CTkButton(
            master=self,
            width=257.03,
            height=64.06,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=SIGN_IN_BUTTON_COLOR_OFF,
            text="Forgot Password",
            text_color="#4B3E39",
            font=FONT_BUTTON       
        )
        self.forgot_password_button.place(x=574.22, y=650)  # Adjust the position as needed
        self.forgot_password_button.bind("<Enter>", self.on_enter_forgot_password)
        self.forgot_password_button.bind("<Leave>", self.on_leave_forgot_password)
        self.forgot_password_button.bind("<Button-1>", self.on_click_forgot_password)


        self.password_entry = CTkEntry(
            master=self,
            placeholder_text="Password:",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=2,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black",
            show="●" 
        )
        self.password_entry.place(x=562.5, y=402.34)

        self.log_in_button = CTkButton(
            master=self,
            width=175,
            height=64.06,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=LOG_IN_BUTTON_COLOR_OFF,
            text="login",
            text_color="black",
            font=FONT_BUTTON       
        )
        self.log_in_button.place(x=894.53, y=572.66)
        self.log_in_button.bind("<Enter>", self.on_enter_log_in)
        self.log_in_button.bind("<Leave>", self.on_leave_log_in)
        self.log_in_button.bind("<Button-1>", self.on_click_log_in)

        self.sign_in_button = CTkButton(
            master=self,
            width=257.03,
            height=64.06,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=SIGN_IN_BUTTON_COLOR_OFF,
            text="create account",
            text_color="#4B3E39",
            font=FONT_BUTTON       
        )
        self.sign_in_button.place(x=574.22, y=572.66)
        self.sign_in_button.bind("<Enter>", self.on_enter_sign_in)
        self.sign_in_button.bind("<Leave>", self.on_leave_sign_in)
        self.sign_in_button.bind("<Button-1>", self.on_click_sign_in)

    def load_data(self):
        import get_from_sheet
        data = get_from_sheet.get_from_google()
        return(data)
    
    def on_enter_sign_in(self, event):
        self.sign_in_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_ON)
      
    def on_leave_sign_in(self, event):
        self.sign_in_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF)
    
    def on_click_sign_in(self, event):
        self.sign_in_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_CLICK)
        self.after(200, lambda: self.sign_in_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF))
        self.destroy()
        Creat_account.start()
    
    def on_enter_log_in(self, event):
        self.log_in_button.configure(fg_color=LOG_IN_BUTTON_COLOR_ON)

    def on_leave_log_in(self, event):
        self.log_in_button.configure(fg_color=LOG_IN_BUTTON_COLOR_OFF)
    
    def on_click_log_in(self, event):
        self.log_in_button.configure(fg_color=LOG_IN_BUTTON_COLOR_CLICK)
        self.after(200, lambda: self.log_in_button.configure(fg_color=LOG_IN_BUTTON_COLOR_OFF))
        if self.is_username_exists():
            self.is_valid_credentials()
            if self.is_valid_credentials():
                self.destroy()
                import menu
        
    def is_username_exists(self):
        data = self.load_data()
        username = self.username_entry.get()
        for account in data["sheet1"]:
            if account["username"] == username :
                return True
        tkinter.messagebox.showinfo("account does not exist", "check your username")
        return False
    
    def is_valid_credentials(self):
        data = self.load_data()
        username = self.username_entry.get()
        password = self.password_entry.get()
        for account in data["sheet1"]:
            if account["username"] == username and account["password"] == password:
                print("welcome")
                return True
        tkinter.messagebox.showinfo("incorrect password", "check your password")  
        return False

    def on_enter_forgot_password(self, event):
        self.forgot_password_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_ON)

    def on_leave_forgot_password(self, event):
        self.forgot_password_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF)

    def on_click_forgot_password(self, event):
        self.forgot_password_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_CLICK)
        self.after(200, lambda: self.forgot_password_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF))
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
        
        def is_valid_q():
            data = self.load_data()
            username = username_2_entry.get()
            question = security_2_entry.get()
            for account in data["sheet1"]:
                if account["username"] == username and account["securitytext"] == question:
                    print(account["password"])
                    return True
            tkinter.messagebox.showinfo("incorrect answer", "check your answer")  
            return False
        def on_click_submit():
            if is_valid_q():
                

        


def start():
    app = LoginApp()
    app.mainloop() 
    #app.load_data()   

if __name__ == "__main__":
    start()
