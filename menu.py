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
window.resizable(width=False, height=False)
window.config(width=620, height=568, bg=BG_COLOR_BACK)

pannel_income_window = Tk()
pannel_income_window.title("income")
def on_income_click():
    pannel_income_window.geometry('%dx%d' %(500,200))
    pannel_income_window.mainloop()

category_window = Tk() 
category_window.title("category")      
def on_category_click():
    category_window.geometry('%dx%d' %(600,300))
    category_window.mainloop()
    
setting_window = Tk()
setting_window.title("Setting")
def on_setting_click():
    setting_window.geometry('%dx%d' %(600,300))
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
income_button = CTkButton(
    master=window,
    width=100,
    height=41,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="income",
    font=FONT_BUTTON, 
    command= on_income_click       
)
income_button.place(x=30, y=50)


price_button = CTkButton(
    master=window,
    width=100,
    height=41,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="price",
    font=FONT_BUTTON       
)
price_button.place(x=180, y=50)

category_button = CTkButton(
    master=window,
    width=100,
    height=41,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="categorys",
    font=FONT_BUTTON,
    command= on_category_click      
)
category_button.place(x=30, y=100)

search_button = CTkButton(
    master=window,
    width=100,
    height=41,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="search",
    font=FONT_BUTTON       
)
search_button.place(x=180, y=100)

exit_button = CTkButton(
    master=window,
    width=100,
    height=41,
    corner_radius=10,
    border_width=1,
    hover=TRUE,
    fg_color=BUTTON_COLOR_OFF,
    text="Exit",
    font=FONT_BUTTON,
    command= window.destroy     
)
exit_button.place(x=30, y=150)

# _______________ panel_incom_window ________________ 

lbl1 = Label(pannel_income_window, text= 'میزان درامد')
lbl1.grid(row=0, column=0, padx=5, pady=5)
mizan_income = Entry(pannel_income_window)
mizan_income.grid(row=0, column=1, padx=5, pady=5)
    
lbl2 = Label(pannel_income_window, text= 'تازیخ درامد')
lbl2.grid(row=1, column=0, padx=5, pady=5)
date_income = Entry(pannel_income_window)
date_income.grid(row=1, column=1, padx=5, pady=5)

income_list = ['naghd', 'check', 'cripto']    
lbl3 = Label(pannel_income_window, text= 'منبع درامد')
lbl3.grid(row=2, column=0, padx=5, pady=5)
main_income = OptionMenu(pannel_income_window, 'naghd', *income_list)
main_income.grid(row=2, column=1, padx=5, pady=5)

category_list = ['bank', 'company', 'personal'] 
# category_list = return_category_list(user_id)

lbl3 = Label(pannel_income_window, text= 'دسته بندی')
lbl3.grid(row=3, column=0, padx=5, pady=5)
category_income = OptionMenu(pannel_income_window, 'bank', *category_list)
category_income.grid(row=3, column=1, padx=5, pady=5)

lbl4 = Label(pannel_income_window, text='توضیحات')
lbl4.grid(row=4, column=0, padx=5, pady=5)
income_desc = Entry(pannel_income_window)
income_desc.grid(row=4, column=1, padx=5, pady=5)

submit_btn = Button(pannel_income_window, text= 'submit', command=on_income_submit)
submit_btn.grid(row=5, column=0, padx=10, pady=10)

# _______________ category_window ________________ 

catLbl = Label(category_window, text='دسته بندی خود را وارد کنید:')
catLbl.grid(row=0, column=0, padx=5, pady=5)
cat_entry = Entry(category_window)
cat_entry.grid(row=1, column=0, padx=5, pady=5)

create_cat_btn = Button(category_window, text='create', command= on_craete_category)
create_cat_btn.grid(row=2, column=0, padx=10, pady=10)

# _______________ setting_window ________________ 

chk_state = BooleanVar()
theme_switch = CTkSwitch(setting_window)
theme_switch.grid(row= 0, column= 0,padx=20, pady=10)
theme_label = Label(setting_window, text='change theme')
theme_label.grid(row=0, column=1)

# یک رادیو باتن بین سه گزینه: income, price, both
delete_data_button = Button(setting_window, text='delete info')
delete_data_button.grid(row=1, column=0, padx=5, pady=5)
delete_data_label = Label(setting_window, text='Delete user info from dataBase')
delete_data_label.grid(row=1, column=1, padx=5, pady=5)

delete_user_button = Button(setting_window, text='delete user account', command= delete_user_account)
delete_user_button.grid(row=2, column=0, padx=5, pady=5)
delete_user_label = Label(setting_window, text='Delete user account from dataBase')
delete_user_label.grid(row=2, column=1, padx=5, pady=5)

window.mainloop()