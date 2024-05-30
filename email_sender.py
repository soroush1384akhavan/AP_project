import smtplib
import random
import tkinter.messagebox
def CreateverificationCode():
    verificition_code = random.randint(1000,10000)
    return verificition_code




masg = str(CreateverificationCode())

email_exist = True



def email_sender(emailtosent):
    global email_exist
    try :
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user="soroush1384.akhavan13@gmail.com", password="lowgyaipybirdqbs")
        server.sendmail("soroush1384.akhavan13@gmail.com", emailtosent, masg)
        print("mail sent")
        email_exist = True
        
    except :
        email_exist = False
        tkinter.messagebox.showerror("Error", "Email does not exist.\nplease check your email address.") 
        

def check(input):
    if input == masg :
        print("correct")
        return True
    else :
        print("false")
        return False
    

def email_exists():
    global email_exist
    return email_exist
    

#soroush1384.akhavan@gmail.com



