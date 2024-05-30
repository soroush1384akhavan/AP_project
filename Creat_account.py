from tkinter import *
from customtkinter import *

# Constants
BG_COLOR_BACK = "#393939"
FONT_LABEL = ('Khula', 50)
FONT_STYLE_ENTRY = ('Kdam Thmor', 28.13)
FONT_BUTTON = ('Kdam Thmor', 28.13)
TEXT_COLOR_ENTRY = "#BDB7B4"
BG_COLOR_ENTRY = "#888888"

LOG_IN_BUTTON_COLOR_OFF = "#F3EBE8"
LOG_IN_BUTTON_COLOR_ON = "#D5CCC8"
LOG_IN_BUTTON_COLOR_CLICK = "#B5ACA9"

SIGN_IN_BUTTON_COLOR_ON = "#C0AC6F"
SIGN_IN_BUTTON_COLOR_OFF = "#E6CD80"
SIGN_IN_BUTTON_COLOR_CLICK = "#9A8A57"

CONTINUE_BUTTON_COLOR_ON = "#736F6F"
CONTINUE_BUTTON_COLOR_OFF = "#787575"
CONTINUE_BUTTON_COLOR_CLICK = "#524E4E"

class Signup(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK)

        self.setup_ui()
        
    def setup_ui(self):
        self.background_image = PhotoImage(file="Signup_6.png")
        self.canvas = Canvas(width=1125, height=800, highlightthickness=0, bg=BG_COLOR_BACK)
        self.canvas.create_image(562, 400, image=self.background_image)
        self.canvas.place(relwidth=1, relheight=1)
        
        self.first_name_entry = CTkEntry(
            master=self,
            placeholder_text="First name",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.first_name_entry.place(x=400, y=308)
        
        self.last_name_entry = CTkEntry(
            master=self,
            placeholder_text="Last name",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.last_name_entry.place(x=400, y=417.34)
        
        self.user_name_entry = CTkEntry(
            master=self,
            placeholder_text="Username",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.user_name_entry.place(x=400, y=527.34)
        
        self.continue_button = CTkButton(
            master=self,
            width=257.03,
            height=64.06,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=CONTINUE_BUTTON_COLOR_OFF,
            text="create account",
            text_color="black",
            bg_color="#888888",
            border_color="black",
            font=FONT_BUTTON       
        )
        self.continue_button.place(x=400, y=642.66)
        
        self.continue_button.bind("<Enter>", self.on_enter_continue)
        self.continue_button.bind("<Leave>", self.on_leave_continue)
        self.continue_button.bind("<Button-1>", self.on_click_continue)
        
    def on_enter_continue(self, event):
        self.continue_button.configure(fg_color=CONTINUE_BUTTON_COLOR_ON)
    
    def on_leave_continue(self, event):
        self.continue_button.configure(fg_color=CONTINUE_BUTTON_COLOR_OFF)
    
    def on_click_continue(self, event):
        self.continue_button.configure(fg_color=CONTINUE_BUTTON_COLOR_CLICK)
        self.after(100, lambda: self.continue_button.configure(fg_color=CONTINUE_BUTTON_COLOR_OFF))
        self.page_2()
          
          
    def on_enter_continue_2(self, event):
        self.continue_2_button.configure(fg_color=CONTINUE_BUTTON_COLOR_ON)
        
    def on_leave_continue_2(self, event):
        self.continue_2_button.configure(fg_color=CONTINUE_BUTTON_COLOR_OFF)
    
    def on_click_continue_2(self, event):
        self.continue_2_button.configure(fg_color=CONTINUE_BUTTON_COLOR_CLICK)
        self.after(100, lambda: self.continue_2_button.configure(fg_color=CONTINUE_BUTTON_COLOR_OFF))
        self.page_3()
        
        
    def page_2(self):
        self.new_background_image = PhotoImage(file="Signup___2.png")
        self.canvas.create_image(562, 400, image=self.new_background_image)
        self.canvas.place(relwidth=1, relheight=1)
        for widget in [self.first_name_entry, self.last_name_entry, self.user_name_entry, self.continue_button]:
            widget.place_forget()
            
        self.label = Label(
            self, 
            text="Now some details!", 
            font=FONT_LABEL, 
            fg="#000000", 
            bg="#888888"
        )
        self.label.place(
            x=350, 
            y=49, 
            width=550, 
            height=182
        )
        self.email_entry = CTkEntry(
            master=self,
            placeholder_text="Email",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.email_entry.place(x=400, y=248)
        
        self.phone_number_entry = CTkEntry(
            master=self,
            placeholder_text="Phone number",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.phone_number_entry.place(x=400, y=337)
        
        self.city_entry = CTkEntry(
            master=self,
            placeholder_text="City",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.city_entry.place(x=400, y=427)
        
        self.birth_day_entry = CTkEntry(
            master=self,
            placeholder_text="Birth day",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.birth_day_entry.place(x=400, y=517)
        
        self.continue_2_button = CTkButton(
            master=self,
            width=257.03,
            height=64.06,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=CONTINUE_BUTTON_COLOR_OFF,
            text="create account",
            text_color="black",
            bg_color="#888888",
            border_color="black",
            font=FONT_BUTTON       
        )
        self.continue_2_button.place(x=400, y=642.66)
        
        self.continue_2_button.bind("<Enter>", self.on_enter_continue_2)
        self.continue_2_button.bind("<Leave>", self.on_leave_continue_2)
        self.continue_2_button.bind("<Button-1>", self.on_click_continue_2)
        
    def page_3(self):
        self.new_background_image_2 = PhotoImage(file="Signup___3.png")
        self.canvas.create_image(562, 400, image=self.new_background_image_2)
        self.canvas.place(relwidth=1, relheight=1)
        for widget in [self.label, self.email_entry, self.continue_2_button, self.phone_number_entry, self.city_entry, self.birth_day_entry]:
            widget.place_forget()
    
        self.password_entry = CTkEntry(
        master=self,
        placeholder_text="Password",
        font=FONT_STYLE_ENTRY,
        width=516.41,
        height=67.19,
        border_width=1,
        corner_radius=10,
        fg_color=BG_COLOR_ENTRY,
        placeholder_text_color=TEXT_COLOR_ENTRY,
        border_color="black",
        bg_color="#888888",
        text_color="black"
        )
        self.password_entry.place(x=400, y=248)
        
        self.repeat_password_entry = CTkEntry(
            master=self,
            placeholder_text="Repeat password",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.repeat_password_entry.place(x=400, y=337)
        
        self.security_q_entry = CTkEntry(
            master=self,
            placeholder_text="What was your school name?",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.security_q_entry.place(x=400, y=427)
        
        self.verification_code_entry = CTkEntry(
            master=self,
            placeholder_text="Verification code",
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black"
        )
        self.verification_code_entry.place(x=400, y=517)
        
        self.create_button = CTkButton(
            master=self,
            width=257.03,
            height=64.06,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=CONTINUE_BUTTON_COLOR_OFF,
            text="create",
            text_color="black",
            bg_color="#888888",
            border_color="black",
            font=FONT_BUTTON       
        )
        self.create_button.place(x=400, y=642.66)
        
        
    
if __name__ == "__main__":
    app = Signup()
    app.mainloop()