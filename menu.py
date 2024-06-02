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

FONT_STYLE_ENTRY = ('Thasadith', 15)
FONT_LABEL = ('Tenor Sans', 40)
FONT_BUTTON  = ('Tenor Sans', 20)
FONT_LABEL_Q = ('Tenor Sans', 15)

#--------------------------- UI ---------------------------#

window = Tk()
window.title("Menu")
window.config(width=1125, height=800, bg=BG_COLOR_BACK)

pannel_income_window = Tk()
pannel_income_window.title("income")
pannel_income_window.config(width=600, height=800, bg=BG_COLOR_BACK)
def on_income_click():
    pannel_income_window.mainloop()

category_window = Tk() 
category_window.title("category") 
category_window.config(width=600, height=800, bg=BG_COLOR_BACK)     
def on_category_click():
    category_window.mainloop()
    
setting_window = Tk()
setting_window.title("Setting")
setting_window.config(width=1125, height=800, bg=BG_COLOR_BACK)
def on_setting_click():
    setting_window.mainloop()   
        
def on_income_submit():
    is_valid = True
    if mizan_income.get() == '' or date_income.get() == '':
        if mizan_income.get() == '':
            mizan_income.configure(border_color="red")
        if date_income.get() == '':
            date_income.configure(border_color="red")
            
    else:
        if type(mizan_income.get()) != int or mizan_income.get() <=0:
            is_valid = False
        if not re.findall('[0-9]{4}/[0-9]{2}/[0-9]{2}', date_income.get()):
            is_valid = False 
        if len(income_desc.get()) > 100:
            is_valid = False
    
    if is_valid:
        # set_income_info_in_db(user_id, mizan_income.get(), date_income.get(), main_income, category_income, income_desc.get())
        tkinter.messagebox.showinfo('succes', 'the information successfully saved')
        pannel_income_window.destroy()
    else:
        tkinter.messagebox.showerror('Error', 'something went wrong!!')
    
def on_craete_category():

    if cat_entry.get() != '' and len(cat_entry.get())< 15:
        if not re.findall('[0-9a-zA-Z]+', cat_entry.get()):
            # set_category_info_in_db(user_id, cat_entry.get())
            pass
        else:
            tkinter.messagebox.showerror('Error', 'category not avalibel!')
    else:
        cat_entry.configure(border_color="red")
        tkinter.messagebox.showerror('Error', 'something went wrong!!')
        
def on_change_setting():
    pass        

def on_delete_transaction_click():
    message_box = tkinter.messagebox.askquestion('delete','آیا برای حذف اطلااعت مطمین هستید؟', icon = 'warning')
    if message_box == 'yes':
        # delete_transaction(user_id, radio_check)
        pass
    
def set_income_info_in_db(id, mizan, date, main, category, description= ''):
    
    connect = sqlite3.connect('users.db')
    c = connect.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS income(
              id INTEGER NOT NULL, 
              mizan INTEGER NoT NULL,
              date text NOT NULL,
              main_income text NIT NULL,
              category text,
              description text;)''')
    
    c.execute('''INSERT INTO income (id, mizan, date, main_income, category, description)
              VALUES (?, ?, ?, ?, ?, ?);''' [id, mizan, date, main, category, description])
    
    connect.commit()
    connect.close()

def set_category_info_in_db(id, category):
    
    connect = sqlite3.connect('users.db')
    c = connect.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS categories(id INTEGER NOT NULL, category1 text;)''')
    c.execute("SELECT category FROM categories WHERE id = ?;" (id,))
    category_on_db = c.fetchall()
    
    c.execute('''INSERT INTO categories (id, category) VALUES (?,?)''' [id, '%s,%s' %(category_on_db, category)])
    
    connect.commit()
    connect.close()
    
    
def return_category_list(id):
    connect = sqlite3.connect('users.db')
    c = connect.cursor()
    c.execute("SELECT category FROM categories WHERE id = ?;" (id,))
    category_on_db = c.fetchall()
    
    connect.commit()
    connect.close()
    
    category_list = category_on_db.split(',')
    return category_list

def delete_transaction(id, change):
    if change == 'income':
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''DELETE FROM income WHERE id = ?;''' (id,))
        
        connect.commit()
        connect.close()
        
    elif change == 'price':
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''DELETE FROM price WHERE id = ?;''' (id,))
        
        connect.commit()
        connect.close()
        
    elif change == 'both':
        connect = sqlite3.connect('users.db')
        c = connect.cursor()
        c.execute('''DELETE FROM income WHERE id = ?;''' (id,))
        c.execute('''DELETE FROM price WHERE id = ?;''' (id,))
        
        connect.commit()
        connect.close()

def delete_user_account():
    message_box = tkinter.messagebox.askquestion('delete','آیا برای حذف اکانت خود مطمین هستید؟', icon = 'warning')
    if message_box == 'yes':
        pass # soroush fix it   
    
#   BUTTONS
option_var = StringVar()

income_button = CTkButton(
    master=window,
    width=220,
    height=60,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="income",
    font=FONT_BUTTON, 
    command= on_income_click       
)
income_button.place(x=550, y=200)


price_button = CTkButton(
    master=window,
    width=220,
    height=60,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="price",
    font=FONT_BUTTON,      
)
price_button.place(x=800, y=200)

category_button = CTkButton(
    master=window,
    width=220,
    height=60,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="categories",
    font=FONT_BUTTON,
    command= on_category_click      
)
category_button.place(x=550, y=270)

search_button = CTkButton(
    master=window,
    width=220,
    height=60,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="search",
    font=FONT_BUTTON       
)
search_button.place(x=800, y=270)

exit_button = CTkButton(
    master=window,
    width=220,
    height=60,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="Exit",
    font=FONT_BUTTON,
    command= window.destroy     
)
exit_button.place(x=550, y=340)

# _______________ panel_incom_window ________________ 

lbl1 = CTkLabel(
    master= pannel_income_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'mizan daramad:',
    text_color="white")
lbl1.place(x=10, y=20)

mizan_income = CTkEntry(
    master=pannel_income_window,
    font=FONT_STYLE_ENTRY,
    width=100,
    height=35,
    border_width=2,
    corner_radius=10,
    fg_color=BG_COLOR_ENTRY,
    placeholder_text_color=TEXT_COLOR_ENTRY,
    text_color="black"
    )
mizan_income.place(x=120, y=20)
    
lbl2 = CTkLabel(
    master= pannel_income_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'tarikh daramad:',
    text_color="white")
lbl2.place(x=10, y=70)

date_income = CTkEntry(
    master=pannel_income_window,
    placeholder_text="XXXX/XX/XX",
    font=FONT_STYLE_ENTRY,
    width=100,
    height=35,
    border_width=2,
    corner_radius=10,
    fg_color=BG_COLOR_ENTRY,
    placeholder_text_color=TEXT_COLOR_ENTRY,
    text_color="black")
date_income.place(x=120, y=70)

income_list = ('naghd', 'check', 'cripto')   
lbl3 = CTkLabel(
    master= pannel_income_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'manbaa daramad',
    text_color="white")
lbl3.place(x=10, y=120)
main_income = OptionMenu(
    pannel_income_window, 
    option_var,
    # income_list[0], 
    *income_list)
main_income.place(x=120, y=120)

category_list = ('bank', 'company', 'personal')
# category_list = return_category_list(user_id)

lbl4 = CTkLabel(
    master= pannel_income_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'category',
    text_color="white")
lbl4.place(x=10, y=170)
category_income = OptionMenu(
    pannel_income_window,
    option_var, 
    # category_list[0], 
    *category_list)

category_income.place(x=120, y=170)

lbl5 = CTkLabel(
    master= pannel_income_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'discription',
    text_color="white")
lbl5.place(x=10, y=220)
income_desc = CTkEntry(
    master=pannel_income_window,
    font=FONT_STYLE_ENTRY,
    width=100,
    height=35,
    border_width=2,
    corner_radius=10,
    fg_color=BG_COLOR_ENTRY,
    placeholder_text_color=TEXT_COLOR_ENTRY,
    text_color="black")
income_desc.place(x=120, y=220)

submit_btn = CTkButton(
    master=pannel_income_window,
    width=70,
    height=30,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BG_COLOR_ENTRY,
    text="Submit",
    text_color="#4B3E39",
    font=FONT_BUTTON,
    command= on_income_submit       
        )
submit_btn.place(x=100, y=300)

# _______________ category_window ________________ 

catLbl = CTkLabel(
    master= category_window,
    width=100,
    height=35,
    fg_color=BG_COLOR_ENTRY,
    text= 'add your new category here:',
    text_color="white")
catLbl.place(x=20,y=100)
cat_entry = CTkEntry(
    master=category_window,
    font=FONT_STYLE_ENTRY,
    width=200,
    height=35,
    border_width=2,
    corner_radius=10,
    fg_color=BG_COLOR_ENTRY,
    placeholder_text_color=TEXT_COLOR_ENTRY,
    text_color="black")
cat_entry.place(x=200, y=100)

create_cat_btn = CTkButton(
    master=category_window, 
    width=70,
    height=30,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BG_COLOR_ENTRY,
    text="create",
    text_color="#4B3E39",
    font=FONT_BUTTON,
    command= on_craete_category)
create_cat_btn.place(x=50, y=190)

# _______________ setting_window ________________ 

chk_state = BooleanVar()
theme_switch = CTkSwitch(
    setting_window,
    # command= change_theme
    )
theme_switch.grid(row= 0, column= 0,padx=20, pady=10)
theme_label = CTkLabel(
    master=setting_window,
    text= 'change theme',
    text_color= BG_COLOR_ENTRY
)
theme_label.place(x=10, y=20)

option_delete = ('income', 'price', 'both')
delete_data_optionMenu = OptionMenu(
    setting_window, 
    option_var,
    # option_delete[0],
    *option_delete
    )
delete_data_optionMenu.place()
delete_data_button = CTkButton(
    master=setting_window, 
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
delete_data_button.place(x= 150, y= 70)
delete_data_label = CTkLabel(
    master= setting_window, 
    text='Delete user info from dataBase',
    text_color= BG_COLOR_ENTRY)
delete_data_label.place(x=10, y=70)

delete_user_button = CTkButton(
    master=setting_window, 
    width=70,
    height=30,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BG_COLOR_ENTRY,
    text='delete user account',
    text_color="#4B3E39",
    font=FONT_BUTTON,  
    command= delete_user_account)
delete_user_button.place(x=150, y=110)
delete_user_label = CTkLabel(
    master= setting_window, 
    text='Delete user account from dataBase',
    text_color= BG_COLOR_ENTRY)
delete_data_label.place(x=10, y=110)

window.mainloop()