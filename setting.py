from tkinter import *
import tkinter.messagebox
from customtkinter import *
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


class SettingApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("setting")
        self.resizable(width=False, height=False)
        self.config(width=600, height=800, bg=BG_COLOR_BACK)
        
        self.setup_ui()
        
    def setup_ui(self):
        self.chk_state = BooleanVar()
        self.theme_switch = CTkSwitch(
            self,
            # command= change_theme
            )
        self.theme_switch.place(x = 50, y= 20)
        self.theme_label = CTkLabel(
            master=self,
            text= 'change theme',
            text_color= BG_COLOR_ENTRY
        )
        self.theme_label.place(x=120, y=20)

        self.option_delete = ('income', 'cost', 'both')
        self.option_var = StringVar()
        self.option_var.set(self.option_delete[0])
        self.delete_data_optionMenu = OptionMenu(
            self, 
            self.option_var,
            # option_delete[0],
            *self.option_delete
            )
        self.delete_data_optionMenu.place(x=70, y= 70)
        self.delete_data_button = CTkButton(
            master=self, 
            width=70,
            height=30,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=BG_COLOR_ENTRY,
            text='delete info',
            text_color="#4B3E39",
            font=FONT_BUTTON,
            )
        self.delete_data_button.place(x= 150, y= 70)
        self.delete_data_button.bind("<Button-1>", self.on_delete_info_click)
    
        self.delete_data_label = CTkLabel(
            master= self, 
            text='Delete user info from dataBase',
            text_color= BG_COLOR_ENTRY)
        self.delete_data_label.place(x=10, y=120)

        self.delete_user_button = CTkButton(
            master=self, 
            width=70,
            height=30,
            corner_radius=10,
            border_width=1,
            hover=TRUE,
            fg_color=BG_COLOR_ENTRY,
            text='delete user account',
            text_color="#4B3E39",
            font=FONT_BUTTON)
        self.delete_user_button.place(x=170, y=160)
        self.delete_user_button.bind("<Button-1>", self.on_delete_user_account)
        
        self.delete_user_label = CTkLabel(
            master= self, 
            text='Delete user account from dataBase',
            text_color= BG_COLOR_ENTRY)
        self.delete_data_label.place(x=10, y=160)
        
    def on_delete_user_account(self, event):
        # self.delete_user_button(fg_color=SIGN_IN_BUTTON_COLOR_CLICK)
        # self.after(200, lambda: self.delete_user_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF))
        
        message_box = tkinter.messagebox.askquestion('delete','آیا برای حذف اکانت خود مطمین هستید؟', icon = 'warning')
        if message_box == 'yes':
            pass # soroush fix it 
        
        
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
            
    def on_delete_info_click(self, event):
        # self.delete_data_button(fg_color=SIGN_IN_BUTTON_COLOR_CLICK)
        # self.after(200, lambda: self.delete_data_button.configure(fg_color=SIGN_IN_BUTTON_COLOR_OFF))
        
        message_box = tkinter.messagebox.askquestion('delete','آیا برای حذف اطلاعات خود مطمین هستید؟', icon = 'warning')
        if message_box:
            self.delete_transaction('soroush', self.option_var.get())
            tkinter.messagebox.showinfo('complite', 'the information you chose was deleted')
        

      
       
def start():
    app = SettingApp()
    app.mainloop() 
    #app.load_data()   

if __name__ == "__main__":
    start()