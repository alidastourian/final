from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

root=Tk()
root.geometry("%dx%d+%d+%d"%(700,550,200,30))
root.title("register")
root.configure(bg="#1a1c37")
root.resizable(False,False)
users=[]


def onclickregister(e):
    if btn_register.cget("state")==NORMAL:
        try:
            dic={"name":txt_name.get(),"family":txt_family.get(),"age":int(txt_age.get()),"id-Code":int(txt_id_Code.get()),"phone":int(txt_phone.get())}
            if exist(dic)==False:
                id_Code()
                register(dic)
                insert(dic)
                cleartxt()
                phonenumber()
                messagebox.showinfo("","added sussesfuly")
            else:
                messagebox.showwarning("rep","person existing")
        except:
                messagebox.showwarning("warning","there is an issue")
def activebtn(e):
    if txt_name.get()=="":
        btn_register.configure(state=DISABLED)
    else:
        btn_register.configure(state=NORMAL)

def cleartxt():
    txt_name.focus_set()
    txtnamevar.set("")
    txtfamilyvar.set("")
    txtagevar.set("")
    txtphonevar.set("")
    txtid_Codevar.set("")




def register(value):
    users.append(value)


def insert(value):
    tbl.insert('',"end",values=[value["name"],value["family"],str(value["id-Code"]),str(value["age"]),str(value["phone"])])

def getselection(e):
    selection=tbl.selection()
    if selection!=():
        s=tbl.item(selection)["values"]
        txtnamevar.set(s[0])
        txtfamilyvar.set(s[1])
        txtid_Codevar.set(s[2])
        txtagevar.set(s[3])
        txtphonevar.set(s[4])

def onclicksearch(e):
    search1=txt_search.get()
    result=search(search1)
    clear()
    for item in result:
        insert(item)

def search(value):
    resultlist=[]
    for item in users:
        if item["name"]==txt_search.get() or item["family"]==txt_search.get() or str(item["id-Code"])==txt_search.get() or str(item["age"])==txt_search.get() or str(item["phone"])==txt_search.get():
            resultlist.append(item)

    return resultlist
def clear():
    for item in tbl.get_children():
        sel=str(item,)
        tbl.delete(sel)

def load_and_clear(value):
    for item in tbl.get_children():
        sel=str(item,)
        tbl.delete(sel)
    for item in vlaue:
        tbl.insert('',"end",values=[item["name"],item["family"],str(item["id-Code"]),str(item["age"]),str(item["phone"])])

def exist(value):
    for item in users:
      if item["name"]==value["name"] and item["family"]==value["family"] and item["id-Code"]==value["id-Code"] and item["age"]==value["age"] and item["phone"]==value["phone"]:
          return True
    return False

def onclickdelete(e):
    dialog=messagebox.askyesno("delete warning","are you sure about it?")
    if dialog==True:
        dic={"name":txt_name.get(),"family":txt_family.get(),"id-Code":int(txt_id_Code.get()),"age":int(txt_age.get()),"phone":int(txt_phone.get())}
        delete(dic)
        remove_tbl()
        cleartxt()

def delete(value):
    for item in users:
        if item["name"] == value["name"] and item["family"] == value["family"] and item["id-Code"] == value["id-Code"] and item["age"] == value["age"] and item["phone"] == value["phone"]:
            users.remove(value)

def remove_tbl():
    selection=tbl.selection()
    if selection!=():
        tbl.delete(selection)
def onclickupdate(e):
    select=tbl.selection()
    if select!=():
        select.item=tbl.item(select)["values"]
        dic={"name":select.item[0],"family":select.item[1],"id-Code":int(select.item[2]),"age":int(select.item[3]),"phone":int(select.item[4])}
        index1=update(dic)
        p=users[index1]
        tbl.item(select,values=[p["name"],p["family"],p["id-Code"],p["age"],p["phone"]])



def update(value):
    index=users.index(value)
    users[index]={"name":txt_name.get(),"family":txt_family.get(),"id-Code":int(txt_id_Code.get()),"age":int(txt_age.get()),"phone":int(txt_phone.get())}
    return index

####-----stringvar------------------------------
txtnamevar=StringVar()
txtfamilyvar=StringVar()
txtid_Codevar=StringVar()
txtagevar=StringVar()
txtphonevar=StringVar()
txtsearchvar=StringVar()

frame=Frame(root,width=235,height=300,bg="#1a1c37")
frame.place(x=20,y=40)
####-----entry name--------------------------------
def on_enter(e):
    txt_name.delete(0, "end")

def on_leave(e):
    name = txt_name.get()
    if name == "":
        txt_name.insert(0, "name")
txt_name=Entry(frame,width=235,fg="#ffffff",border=0,bg="#222642")
txt_name.configure(font="arial 15",textvariable=txtnamevar)
txt_name.insert(0,"name")
txt_name.bind("<FocusIn>", on_enter)
txt_name.bind("<FocusOut>", on_leave)
txt_name.bind("<KeyRelease>", activebtn)
Frame(frame,width=235,height=3,bg="#8658ee").place(x=0,y=25)
txt_name.place(x=0,y=0)
####-----entry family--------------------------------
def on_enter(e):
     txt_family.delete(0, "end")

def on_leave(e):
     family=txt_family.get()
     if family=="":
         txt_family.insert(0, "family")
txt_family=Entry(frame,width=235,fg="#ffffff",border=0,bg="#222642")
txt_family.configure(font="arial 15",textvariable=txtfamilyvar)
txt_family.insert(0,"family")
txt_family.bind("<FocusIn>", on_enter)
txt_family.bind("<FocusOut>", on_leave)
Frame(frame,width=235,height=3,bg="#8658ee").place(x=0,y=75)
txt_family.place(x=0,y=50)
####-----entry id code--------------------------------
def on_enter(e):
    txt_id_Code.delete(0, "end")

def on_leave(e):
    id_Code = txt_id_Code.get()

    if id_Code == "":
        txt_id_Code.insert(0, "id-Code")
txt_id_Code=Entry(frame,width=235,fg="#ffffff",border=0,bg="#222642")
txt_id_Code.configure(font="arial 15",textvariable=txtid_Codevar)
txt_id_Code.insert(0,"id-Code")
txt_id_Code.bind("<FocusIn>", on_enter)
txt_id_Code.bind("<FocusOut>", on_leave)
Frame(frame,width=235,height=3,bg="#8658ee").place(x=0,y=125)
txt_id_Code.place(x=0,y=100)
####-----entry age--------------------------------
def on_enter(e):
    txt_age.delete(0, "end")

def on_leave(e):
    age = txt_age.get()
    if age == "":
        txt_age.insert(0, "age")
txt_age=Entry(frame,width=235,fg="#ffffff",border=0,bg="#222642")
txt_age.configure(font="arial 15",textvariable=txtagevar)
txt_age.insert(0,"age")
txt_age.bind("<FocusIn>", on_enter)
txt_age.bind("<FocusOut>", on_leave)
Frame(frame,width=235,height=3,bg="#8658ee").place(x=0,y=175)
txt_age.place(x=0,y=150)
####-----entry phone--------------------------------
def on_enter(e):
    txt_phone.delete(0, "end")

def on_leave(e):
    phone = txt_phone.get()
    if phone == "":
        txt_phone.insert(0, "phone")
txt_phone=Entry(frame,width=235,fg="#ffffff",border=0,bg="#222642")
txt_phone.configure(font="arial 15",textvariable=txtphonevar)
txt_phone.insert(0,"phone")
txt_phone.bind("<FocusIn>", on_enter)
txt_phone.bind("<FocusOut>", on_leave)
Frame(frame,width=235,height=3,bg="#8658ee").place(x=0,y=225)
txt_phone.place(x=0,y=200)
####-----entry search--------------------------------
def on_enter(e):
    txt_search.delete(0, "end")

def on_leave(e):
    search = txt_search.get()
    if search == "":
        txt_search.insert(0, "search")

txt_search=Entry(root,fg="#ffffff",width=13,border=0,bg="#222642")
txt_search.configure(font="arial 15",textvariable=txtsearchvar)
txt_search.insert(0,"search")
txt_search.bind("<FocusIn>", on_enter)
txt_search.bind("<FocusOut>", on_leave)
Frame(root,width=146,height=3,bg="#8658ee").place(x=280,y=36)
txt_search.place(x=280, y=10)
####-----btnregister--------------------------------
btn_register=Button(root,text="Register",width=15,fg="#ffffff",font="arial 8 bold")
btn_register.configure(bg="#cb4382",fg="#ffffff",border=0,state=DISABLED)
btn_register.bind("<Button-1>",onclickregister)
btn_register.place(x=145,y=460)
####-----btnsearch---------------------------------
btn_search=Button(root,text="Search",width=15,border=0,bg="#cb4382",fg="#ffffff",font="arial 8 bold")
btn_search.configure(bg="#cb4382")
btn_search.place(x=280, y=50)
btn_search.bind("<Button-1>", onclicksearch)
####-----btndelete--------------------------------
btn_delete=Button(root,text="Delete",width=15,fg="#ffffff",font="arial 8 bold")
btn_delete.configure(bg="#cb4382",fg="#ffffff",border=0)
btn_delete.bind("<Button-1>",onclickdelete)
btn_delete.place(x=145,y=520)
####-----btnupdate---------------------------------
btn_update=Button(root,text="update",width=15,border=0,bg="#cb4382",fg="#ffffff",font="arial 8 bold")
btn_update.configure(bg="#cb4382")
btn_update.place(x=20,y=460)
btn_update.bind("<Button-1>", onclickupdate)
####-----heading--------------------------------
heading=Label(root,text="Person's Profile",bg="#1a1c37",fg="#ffe400")
heading.configure(font="arial 15 bold")
heading.place(x=20,y=5)
####-----radio btn--------------------------------
radiovar=IntVar()
radio1=ttk.Radiobutton(root,text="male",value=1,variable=radiovar)
radio1.place(x=18,y=300)
radio2=ttk.Radiobutton(root,text="female",value=2,variable=radiovar)
radio2.place(x=80,y=300)
####-----lb--------------------------------
lbl2=Label(root,text="Choose Gender",bg="#1a1c37",fg="#fff")
lbl2.configure(font="arial 12")
lbl2.place(x=18,y=270)
####-----lbl--------------------------------
lbl3=Label(root,text="Choose reg point",bg="#1a1c37",fg="#fff")
lbl3.configure(font="arial 12")
lbl3.place(x=18,y=325)
####-----columnttk------------------------------
column=("c1","c2","c3","c4","c5")
tbl=ttk.Treeview(root,column=column,show="headings")
tbl.heading(column[0],text="Name")
tbl.column(column[0],width=90)
tbl.heading(column[1],text="Family")
tbl.column(column[1],width=90)
tbl.heading(column[2],text="Id_Code")
tbl.column(column[2],width=70)
tbl.heading(column[3],text="age")
tbl.column(column[3],width=50)
tbl.heading(column[4],text="phone")
tbl.column(column[4],width=90)
tbl.bind("<Button-1>",getselection)
tbl.place(x=280,y=80)
####-----check------------------------------
checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()
checkbox1=ttk.Checkbutton(root,text="with class",variable=checkvar1)
checkbox1.place(x=18,y=350)
checkbox2=ttk.Checkbutton(root,text="with certificate",variable=checkvar2)
checkbox2.place(x=100,y=350)
checkbox3=ttk.Checkbutton(root,text="with test",variable=checkvar3)
checkbox3.place(x=18,y=380)
####-----combo------------------------------
combo=ttk.Combobox(root)
a=[]
for i in range(1,120):
    a.append(i)
combo["value"]=a
combo.current(16)
combo.place(x=18,y=405)














root.mainloop()