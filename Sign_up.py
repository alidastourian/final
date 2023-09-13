
from tkinter import *
from tkinter import messagebox



def showmsg():

        root=Tk()
        root.geometry("%dx%d+%d+%d"%(400,650,400,30))
        root.title("Sign_up")
        root.resizable(False,False)
        users=[]
        load = PhotoImage(file = "2335434523542.png")
        Label(root, image=load).pack()
        ####-----frame----------------------------------
        frame=Frame(root,width=200,height=150,bg="#000000")
        frame.place(x=100,y=300)
        ####-----def bind---------------------------
        def onclicksign_up1(e):
            b=False
            for item in users:
                if item["user"]==txt_User.get():
                    messagebox.showinfo("", "alredy existing")
                    b=True
                    break
            if b==False:
                if txt_Password.get()==txt_ConfirmPassword.get():
                    dic={"user":txt_User.get(),"Password":txt_Password.get(),"ConfirmPassword":txt_ConfirmPassword.get()}
                    users.append(dic)
                    messagebox.showinfo("","added to site")
                else:
                     messagebox.showerror("","password not same")


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
        ####-----entry ConfirmPassword--------------------------------
        def on_enter(e):
            txt_ConfirmPassword.delete(0, "end")

        def on_leave(e):
            Confirm = txt_ConfirmPassword.get()
            if Confirm == "":
                txt_ConfirmPassword.insert(0, "ConfirmPassword")
        txt_ConfirmPassword=Entry(root,width=17,fg="#ffffff",border=0,bg="#000000")
        txt_ConfirmPassword.configure(font="arial 15")
        txt_ConfirmPassword.insert(0,"ConfirmPassword")
        txt_ConfirmPassword.bind("<FocusIn>", on_enter)
        txt_ConfirmPassword.bind("<FocusOut>", on_leave)
        txt_ConfirmPassword.place(x=105,y=390)
        Frame(frame,width=190,height=3,bg="#1fb0dd").place(x=4,y=115)
        ####-----btnsignup--------------------------------
        btn_signup=Button(root,text="Sign Up",width=18,fg="#ffffff",font="arial 12 bold")
        btn_signup.configure(bg="#852bd4",fg="#ffffff",border=0)
        btn_signup.bind("<Button-1>",onclicksign_up1)
        btn_signup.place(x=106,y=450)



















        root.mainloop()
showmsg()