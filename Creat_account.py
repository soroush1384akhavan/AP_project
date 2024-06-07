from tkinter import *
import tkinter.messagebox
from customtkinter import *
import re
import email_sender
import json

# Constants
BG_COLOR_BACK = "#393939"
FONT_LABEL = ('Khula', 50)
FONT_STYLE_ENTRY = ('Kdam Thmor', 28)
FONT_BUTTON = ('Kdam Thmor', 28)
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

CREATE_BUTTON_COLOR_ON = "#94BC74"
CREATE_BUTTON_COLOR_OFF = "#B6DA99"
CREATE_BUTTON_COLOR_CLICK = "#85A869"

STRENGTH_COLOR_WEAK = "#FF6347"
STRENGTH_COLOR_MEDIUM = "#FFA500"
STRENGTH_COLOR_STRONG = "#32CD32"

class Signup(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK)
        self.setup_ui()
        
    def setup_ui(self):
        self.background_image = PhotoImage(file="images/Signup_6.png")
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
        self.first_name_entry.bind("<KeyRelease>", self.check_name)
        self.first_name_entry.bind("<KeyRelease>", self.check_page_1)
        
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
        self.last_name_entry.bind("<KeyRelease>", self.check_last_name)
        self.last_name_entry.bind("<KeyRelease>", self.check_page_1)
        
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
        self.user_name_entry.bind("<KeyRelease>", self.check_user_name)
        self.user_name_entry.bind("<KeyRelease>", self.check_page_1)
        
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
            font=FONT_BUTTON,
            state=DISABLED       
        )
        self.continue_button.place(x=400, y=642.66)
        
        self.continue_button.bind("<Enter>", self.on_enter_continue)
        self.continue_button.bind("<Leave>", self.on_leave_continue)
        self.continue_button.bind("<Button-1>", self.on_click_continue)
        
    def on_enter_continue(self, event):
        if self.continue_button.cget('state') == NORMAL:
            self.continue_button.configure(fg_color=CONTINUE_BUTTON_COLOR_ON)
    
    def on_leave_continue(self, event):
        self.continue_button.configure(fg_color=CONTINUE_BUTTON_COLOR_OFF)
    
    def on_click_continue(self, event):
        if self.continue_button.cget('state') == NORMAL:
            self.continue_button.configure(fg_color=CONTINUE_BUTTON_COLOR_CLICK)
            self.after(100, lambda: self.continue_button.configure(fg_color=CONTINUE_BUTTON_COLOR_OFF))
            self.page_2()

          
    def on_enter_continue_2(self, event):
        if self.continue_2_button.cget('state') == NORMAL:
            self.continue_2_button.configure(fg_color=CONTINUE_BUTTON_COLOR_ON)
        
    def on_leave_continue_2(self, event):
        self.continue_2_button.configure(fg_color=CONTINUE_BUTTON_COLOR_OFF)
    
    def on_click_continue_2(self, event):
        if self.continue_2_button.cget('state') == NORMAL:
            self.continue_2_button.configure(fg_color=CONTINUE_BUTTON_COLOR_CLICK)
            self.after(100, lambda: self.continue_2_button.configure(fg_color=CONTINUE_BUTTON_COLOR_OFF))
            email_sender.email_sender(emailtosent=self.email_entry.get())
            self.page_3()
        
    def on_enter_create(self, event):
        if self.create_button.cget('state') == NORMAL:
            self.create_button.configure(fg_color=CREATE_BUTTON_COLOR_ON)
        
    def on_leave_create(self, event):
        self.create_button.configure(fg_color=CREATE_BUTTON_COLOR_OFF)
    
    def on_click_create(self, event):
        if self.create_button.cget('state') == NORMAL:
            self.create_button.configure(fg_color=CREATE_BUTTON_COLOR_CLICK)
            self.after(100, lambda: self.create_button.configure(fg_color=CREATE_BUTTON_COLOR_OFF))
            if email_sender.check(self.verification_code_entry.get()):
                print("correct")
                self.save_credentials()
            else:
                tkinter.messagebox.showerror("Error", "Verification code is incorrect")
                print("incorrect")
        
    
    def page_2(self):
        self.suggestions_var = StringVar()
        self.new_background_image = PhotoImage(file="images/Signup___2.png")
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
        self.email_entry.bind("<KeyRelease>", self.check_email)
        self.email_entry.bind("<KeyRelease>", self.check_page_2)
        
        
        
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
            text_color="black",
        )
        self.phone_number_entry.place(x=400, y=337)
        self.phone_number_entry.bind("<KeyRelease>", self.check_number)
        
        self.city_var = StringVar()
        
        self.city_entry = CTkEntry(
            master=self,
            
            font=FONT_STYLE_ENTRY,
            width=516.41,
            height=67.19,
            border_width=1,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            border_color="black",
            bg_color="#888888",
            text_color="black",
            textvariable=self.city_var,
            placeholder_text="City"
        )
        self.city_entry.place(x=400, y=427)
        self.city_entry.bind("<KeyRelease>", self.show_suggestions)
        self.city_entry.bind("<KeyRelease>", self.check_city)
        self.city_entry.bind("<KeyRelease>", self.check_page_2)
        
        
        self.suggestion_listbox = Listbox(
            master=self,
            font=FONT_STYLE_ENTRY,
            width=10,
            height=4
        )
        self.suggestion_listbox.bind("<<ListboxSelect>>", self.insert_suggestion)
        
        
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
        self.birth_day_entry.bind("<KeyRelease>", self.check_birth)
        self.birth_day_entry.bind("<KeyRelease>", self.check_page_2)
        
        
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
            state=DISABLED,
            font=FONT_BUTTON       
        )
        self.continue_2_button.place(x=400, y=642.66)
    
        self.continue_2_button.bind("<Enter>", self.on_enter_continue_2)
        self.continue_2_button.bind("<Leave>", self.on_leave_continue_2)
        self.continue_2_button.bind("<Button-1>", self.on_click_continue_2)
        
    def page_3(self):
        self.new_background_image_2 = PhotoImage(file="images/Signup___3.png")
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
        self.password_entry.bind("<KeyRelease>", self.check_password_strength)

        self.strength_rect_1 = Canvas(self, width=160, height=10, bg=BG_COLOR_BACK, highlightthickness=0)
        self.strength_rect_1.place(x=400, y=320)
        self.strength_rect_2 = Canvas(self, width=160, height=10, bg=BG_COLOR_BACK, highlightthickness=0)
        self.strength_rect_2.place(x=560, y=320)
        self.strength_rect_3 = Canvas(self, width=160, height=10, bg=BG_COLOR_BACK, highlightthickness=0)
        self.strength_rect_3.place(x=720, y=320)
        
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
        self.repeat_password_entry.bind("<KeyRelease>", self.check_equality)
        self.repeat_password_entry.bind("<KeyRelease>", self.check_page_3)
        
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
        self.security_q_entry.bind("<KeyRelease>", self.check_secruity_text)
        self.security_q_entry.bind("<KeyRelease>", self.check_page_3)
        
        
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
        self.verification_code_entry.bind("<KeyRelease>", self.check_page_3)
        
        
        self.create_button = CTkButton(
            master=self,
            width=257.03,
            height=64.06,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=CREATE_BUTTON_COLOR_OFF,
            text="create",
            text_color="black",
            bg_color="#888888",
            border_color="black",
            state=DISABLED,
            font=FONT_BUTTON       
        )
        self.create_button.place(x=400, y=642.66)
        
        self.create_button.bind("<Enter>", self.on_enter_create)
        self.create_button.bind("<Leave>", self.on_leave_create)
        self.create_button.bind("<Button-1>", self.on_click_create)
    
    def check_password_strength(self, event):
        password = self.password_entry.get()
        strength = self.evaluate_password_strength(password)
        self.update_strength_box(strength)
    
    def evaluate_password_strength(self, password):
        length = len(password) >= 6
        digit = re.search(r"\d", password) is not None
        uppercase = re.search(r"[A-Z]", password) is not None
        lowercase = re.search(r"[a-z]", password) is not None
        special = re.search(r"[^a-zA-Z0-9]", password) is not None
        score = sum([length, digit, uppercase, lowercase, special])
        return score

    def update_strength_box(self, strength):
        colors = [BG_COLOR_BACK] * 3
        if strength == 3:
            colors = [STRENGTH_COLOR_WEAK, STRENGTH_COLOR_WEAK, BG_COLOR_BACK]
        elif strength == 4:
            colors = [STRENGTH_COLOR_MEDIUM, STRENGTH_COLOR_MEDIUM, BG_COLOR_BACK]
        elif strength >= 5:
            self.password_entry.configure(border_color="green")
            colors = [STRENGTH_COLOR_STRONG] * 3
        
        self.strength_rect_1.configure(bg=colors[0])
        self.strength_rect_2.configure(bg=colors[1])
        self.strength_rect_3.configure(bg=colors[2])
        
    def check_equality(self, event):
        password = self.password_entry.get()
        r_password = self.repeat_password_entry.get()
        if r_password == password:
            self.repeat_password_entry.configure(border_color="green")
        else:
            self.repeat_password_entry.configure(border_color="red")
            
        return r_password == password
        
    def check_name(self, event):
        name = self.first_name_entry.get()
        only_letters = re.fullmatch(r"[A-Za-z]+", name) is not None
    
        if only_letters:
            self.first_name_entry.configure(border_color="green")
        else:
            self.first_name_entry.configure(border_color="red")
        
        return only_letters
                    
    def check_last_name(self, event):
        last_name = self.last_name_entry.get()
        only_letters = re.fullmatch(r"[A-Za-z]+", last_name) is not None
    
        if only_letters:
            self.last_name_entry.configure(border_color="green")
        else:
            self.last_name_entry.configure(border_color="red")
        
        return only_letters
    
    def check_user_name(self, event):
        user_name = self.user_name_entry.get()
        if user_name:
            self.user_name_entry.configure(border_color="green")
            return True
        else:
            self.user_name_entry.configure(border_color="red")
            return False
        
    def check_secruity_text(self, event):
        text = self.security_q_entry.get()
        if text:
            self.security_q_entry.configure(border_color="green")
            return True
        else:
            self.security_q_entry.configure(border_color="red")
            return False
        
    def check_page_1(self, event):
        if self.check_name(None) and self.check_last_name(None) and self.check_user_name(None):
            self.continue_button.configure(state=NORMAL)
        else:
            self.continue_button.configure(state=DISABLED)
    
    def check_page_2(self, event):
        if self.check_email(None) and self.check_number(None) and self.check_city(None) and self.check_birth(None):
            self.continue_2_button.configure(state=NORMAL)
        else:
            self.continue_2_button.configure(state=DISABLED)
            
    def check_page_3(self, event):
        if self.check_equality(None) and self.evaluate_password_strength(self.password_entry.get())>=5 and self.check_secruity_text(None) and self.verification_code_entry.get():
            self.create_button.configure(state=NORMAL)
        else:
            self.create_button.configure(state=DISABLED)
        
            
    def check_birth(self, event):
        date_regex = r'^\d{4}-\d{1,2}-\d{1,2}$'
        date_str = self.birth_day_entry.get()
        
        if not re.match(date_regex, date_str):
            self.birth_day_entry.configure(border_color="red")
            return False
        
        year, month, day = map(int, date_str.split('-'))
        
        if year < 1920 or year >2005 :
            self.birth_day_entry.configure(border_color="red")
            return False
        
        if month < 1 or month > 12:
            self.birth_day_entry.configure(border_color="red")
            return False
        
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day < 1 or day > 31:
                self.birth_day_entry.configure(border_color="red")
                return False
            
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                self.birth_day_entry.configure(border_color="red")
                return False
            
        elif month == 2:
            if day < 1 or day > 28:
                self.birth_day_entry.configure(border_color="red")
                return False
        
        self.birth_day_entry.configure(border_color="green")
        return True
    
   

    def check_email(self, event):
        email = self.email_entry.get()
        email_regex = r'^[a-zA-Z0-9.]+@(?:gmail|yahoo)\.com$'
        
        if re.match(email_regex, email):
            self.email_entry.configure(border_color="green")
            return True
        else:
            self.email_entry.configure(border_color="red")
            return False
        
    def check_number(self, event):
        number = self.phone_number_entry.get()
        number_regex = r'^09\d{9}$'
        if re.match(number_regex, number):
            self.phone_number_entry.configure(border_color="green")
            return True
        else:
            self.phone_number_entry.configure(border_color="red")
            return False

    
    def show_suggestions(self, event):
        typed_text = self.city_var.get().lower()
        import cities
        suggestions = cities.start()  # Or any other list of suggestions
        matched_cities = [city for city in suggestions if typed_text.lower() == city[:len(typed_text)].lower() and len(typed_text) >= 2]
        self.suggestion_listbox.delete(0, END)
        for city in matched_cities:
            self.suggestion_listbox.insert(END, city)
        if matched_cities:
            self.suggestion_listbox.place(x=400, y=240)  
        else:
            self.suggestion_listbox.place_forget()

    def insert_suggestion(self, event):
        selected_index = self.suggestion_listbox.curselection()
        if selected_index:
            selected_suggestion = self.suggestion_listbox.get(selected_index)
            self.city_entry.delete(0, END)
            self.city_entry.insert(0, selected_suggestion)
            self.suggestion_listbox.place_forget()
            
    def check_city(self, event):
        city = self.city_entry.get()
        import cities
        if str(city) in str(cities.start()):
            self.city_entry.configure(border_color="green")
            return True
        else:
            self.city_entry.configure(border_color="red")
            return False
    


    def save_credentials(self):
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        username = self.user_name_entry.get()
        email = self.email_entry.get()
        phonenumber = self.phone_number_entry.get()
        city = self.city_entry.get()
        birthday = self.birth_day_entry.get()
        password = self.password_entry.get()
        securitytext = self.security_q_entry.get()
        
        file_path = "data.json"
        
        try:
            with open(file_path, "r") as file:
                existing_credentials = json.load(file)
        except FileNotFoundError:
            existing_credentials = {}

        if username in existing_credentials:
            tkinter.messagebox.showerror("Error", "This username already exists.")
            return

        existing_credentials[username] = {
            "email": email,
            "password": password,
            "fname": firstname,
            "lname": lastname,
            "phonenumber": phonenumber,
            "city": city,
            "birthday": birthday,
            "securitytext": securitytext
        }
        

        with open(file_path, "w") as file:
            json.dump(existing_credentials, file, indent=4)
        
        tkinter.messagebox.showinfo("Account Created", "Your account has been created successfully!")
        import login
        self.destroy()
        login.start()
        
        default = {
            "admin": {
                "email": "soroush1384.akhavan@gmail.com",
                "password": "123",
                "fname": "Admin",
                "lname": "User",
                "phonenumber": "0000000000",
                "city": "AdminCity",
                "birthday": "1970-01-01",
                "securitytext": "Admin Security Question"
            }
        }
        
        try:
            import data_sheet
            data_sheet.send_to_google()
            with open(file_path, "w") as file:
                json.dump(default, file, indent=4)
        except Exception as e:
            print("Something went wrong:", str(e))





            


def start():
    app = Signup()
    app.mainloop()

if __name__ == "__main__":
    start()
