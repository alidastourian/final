import os
from tkinter import *

from tkinter import messagebox
from tkinter import PhotoImage


root=Tk()
root.geometry("%dx%d+%d+%d"%(400,650,400,30))
root.title("Login")
image = PhotoImage(file = "asasasasasas.png")
Label(root, image= image).pack()
root.resizable(False,False)
####-----frame----------------------------------
frame=Frame(root,width=200,height=100,bg="#000000")
frame.place(x=100,y=300)
####-------def---------------------------------------
def onclicksignup(e):

    Sign_up.showmsg()
####-------def---------------------------------------
def Login(e):
    for item in Sign_up.users:
        if item["user"]==txt_User.get() and item["Password"]==txt_Password.get():
            os.system(f"python main_pro.py")
####-----entry users--------------------------------
def on_enter(e):
    txt_User.delete(0, "end")

def on_leave(e):
    user = txt_User.get()
    if user == "":
        txt_User.insert(0, "UserName")
txt_User=Entry(root,width=17,fg="#ffffff",border=0,bg="#000000")
txt_User.configure(font="arial 15")
txt_User.insert(0,"UserName")
txt_User.bind("<FocusIn>", on_enter)
txt_User.bind("<FocusOut>", on_leave)
txt_User.place(x=105,y=310)
Frame(frame,width=190,height=3,bg="#1fb0dd").place(x=4,y=35)
####-----entry password--------------------------------
def on_enter(e):
    txt_Password.delete(0, "end")

def on_leave(e):
    PASSWORD = txt_Password.get()
    if PASSWORD == "":
        txt_Password.insert(0, "Password")
txt_Password=Entry(root,width=17,fg="#ffffff",border=0,bg="#000000")
txt_Password.configure(font="arial 15")
txt_Password.insert(0,"Password")
txt_Password.bind("<FocusIn>", on_enter)
txt_Password.bind("<FocusOut>", on_leave)
txt_Password.place(x=105,y=350)
Frame(frame,width=190,height=3,bg="#1fb0dd").place(x=4,y=75)
####-----btnlog in--------------------------------
btn_login=Button(root,text="Login",width=18,fg="#ffffff",font="arial 12 bold")
btn_login.configure(bg="#852bd4",fg="#ffffff",border=0)
btn_login.bind("<Button-1>",Login)
btn_login.place(x=106,y=400)
####-----btnsignup--------------------------------
btn_signup = Button(root, text="Sign Up", width=18, fg="#ffffff", font="arial 12 bold")
btn_signup.configure(bg="#852bd4", fg="#ffffff", border=0)
btn_signup.bind("<Button-1>",onclicksignup)
btn_signup.place(x=106,y=450)




















root.mainloop()