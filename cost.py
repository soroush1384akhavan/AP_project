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
FONT_BUTTON  = ('Tenor Sans', 15)
FONT_LABEL_Q = ('Tenor Sans', 15)

class costApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("cost")
        self.resizable(width=False, height=False)
        self.config(width=1125, height=800, bg=BG_COLOR_BACK)
        
        self.setup_ui()
        
    def setup_ui(self):
        self.lbl1 = CTkLabel(
            master= self,
            width=100,
            height=35,
            fg_color=BG_COLOR_ENTRY,
            text= 'amount of cost:',
            text_color="white")
        self.lbl1.place(x=10, y=20)

        self.mizan_cost = CTkEntry(
            master=self,
            font=FONT_STYLE_ENTRY,
            width=100,
            height=35,
            border_width=2,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black"
            )
        self.mizan_cost.place(x=120, y=20)
            
        self.lbl2 = CTkLabel(
            master= self,
            width=100,
            height=35,
            fg_color=BG_COLOR_ENTRY,
            text= 'date of cost:',
            text_color="white")
        self.lbl2.place(x=10, y=70)

        self.date_cost = CTkEntry(
            master=self,
            placeholder_text="XXXX/XX/XX",
            font=FONT_STYLE_ENTRY,
            width=100,
            height=35,
            border_width=2,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black")
        self.date_cost.place(x=120, y=70)

        self.cost_list = ('naghd', 'check', 'cripto') 
        self.option_var1 = StringVar() 
        self.option_var1.set(self.cost_list[0]) 
        self.lbl3 = CTkLabel(
            master= self,
            width=100,
            height=35,
            fg_color=BG_COLOR_ENTRY,
            text= 'manbaa daramad',
            text_color="white")
        self.lbl3.place(x=10, y=120)
        self.main_cost = OptionMenu(
            self, 
            self.option_var1,
            # cost_list[0], 
            *self.cost_list)
        self.main_cost.place(x=120, y=120)

        self.category_list = self.return_category_list('amura')
        if len(self.category_list) == 0:
            self.category_list = ["you didn't add a category"]
            
        self.option_var2 = StringVar() 
        self.option_var2.set(self.category_list[0])
        self.lbl4 = CTkLabel(
            master= self,
            width=100,
            height=35,
            fg_color=BG_COLOR_ENTRY,
            text= 'category',
            text_color="white")
        self.lbl4.place(x=10, y=170)
        self.category_cost = OptionMenu(
            self,
            self.option_var2, 
            # category_list[0], 
            *self.category_list)

        self.category_cost.place(x=120, y=170)

        self.lbl5 = CTkLabel(
            master= self,
            width=100,
            height=35,
            fg_color=BG_COLOR_ENTRY,
            text= 'discription',
            text_color="white")
        self.lbl5.place(x=10, y=220)
        self.cost_desc = CTkEntry(
            master=self,
            font=FONT_STYLE_ENTRY,
            width=100,
            height=35,
            border_width=2,
            corner_radius=10,
            fg_color=BG_COLOR_ENTRY,
            placeholder_text_color=TEXT_COLOR_ENTRY,
            text_color="black")
        self.cost_desc.place(x=120, y=220)

        self.submit_btn = CTkButton(
            master= self,
            width=70,
            height=30,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=BG_COLOR_ENTRY,
            text="Submit",
            text_color="#4B3E39",
            font=FONT_BUTTON)
        
        self.submit_btn.place(x=100, y=300)
        self.submit_btn.bind("<Button-1>", self.on_sumbit_clicked)
    
    def return_category_list(self, id):
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS categories(user_name TEXT NOT NULL UNIQUE);''')
        c.execute("SELECT * FROM categories WHERE user_name = ?;", (id,))
        category_on_db = c.fetchall()
        
        connect.commit()
        connect.close()
        
        return (category_on_db[0])[1:]
   
    def on_sumbit_clicked(self, event):
        self.submit_btn.configure(fg_color=SIGN_IN_BUTTON_COLOR_CLICK)
        self.after(200, lambda: self.submit_btn.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF))
        
        is_valid = True
        if self.mizan_cost.get() == '' or self.date_cost.get() == '':
            is_valid = False
            if self.mizan_cost.get() == '':
                self.mizan_cost.configure(border_color="red")
            if self.date_cost.get() == '':
                self.date_cost.configure(border_color="red")
                
        else:
            # if type(self.mizan_cost.get()) != int or self.mizan_cost.get() <=0:
            #     is_valid = False
            if not re.match(r'^\d{4}/\d{1,2}/\d{1,2}$', self.date_cost.get()) and int(self.date_cost.get()>0):
                is_valid = False 
            if not re.match(r'[0-9]+', self.date_cost.get()):
                is_valid = False 
            if len(self.cost_desc.get()) > 100:
                is_valid = False
        
        if is_valid:
            self.set_cost_info_in_db(12, self.mizan_cost.get(), self.date_cost.get(), self.option_var1.get(), self.option_var2.get(), self.cost_desc.get())
            tkinter.messagebox.showinfo('succes', 'the information successfully saved')

        else:
            tkinter.messagebox.showerror('Error', 'something went wrong!!')
            self.on_sumbit_clicked()
        
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
        

def start():
    app = costApp()
    app.mainloop() 
    #app.load_data()   

if __name__ == "__main__":
    start()
    