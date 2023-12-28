from tkinter import*
import tkinter.ttk as ttk
from tkinter import messagebox as tkMessageBox
import sqlite3

def Database():
    global conn,cursor
    conn=sqlite3.connect("D:\student.db")
    cursor=conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUD_REGISTRATION (STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,STU_NAME TEXT,STU_CONTACT TEXT,STU_EMAIL TEXT,STU_ROLLNO TEXT, STU_BRANCH TEXT)")
def register():
    Database()
    name1=name.get()
    con1=contact.get()
    email1=email.get()
    roll=rollno.get()
    branch1=branch.get()
    if name1=="" or con1=="" or email==" " or roll=="" or branch1=="":
        tkMessageBox.showinfo("Warning","insert the value Empty field!")
    else:
        conn.execute('INSERT INTO STUD_REGISTRATION(STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_BRANCH) VALUES (?,?,?,?,?)',(name1,con1,email1,roll,branch1));
        conn.commit()
        tkMessageBox.showinfo("Message","stored successfully")
        DisplayData()
        conn.close()
def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
    name.set("")
    contact.set("")
    email.set("")
    rollno.set("")
    branch.set("")
def Delete():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","select data to delete")
    else:
        result=tkMessageBox.askquestion("confirm", "Are you sure you want delete this record ?",icon="warning")
        if result=="yes":
            curItem=tree.focus()
            contents=(tree.item(curItem))
            selecteditem=contents["values"]
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM STUD_REGISTRATION WHERE STU_ID=%d" % selecteditem[0])
            conn.commit()
                       
            cursor.close()
            conn.close()
def SearchRecord():
    Database()
    if SEARCH.get()!="":
        tree.delete(*tree.get_children())
        cursor=conn.execute("SELECT * FROM STUD_REGISTRATION")
        fetch= cursor.fetchall()
        for data in fetch:
            tree.insert("","end",values=(data))
        cursor.close()
        conn.close()
def DisplayData():
    Database()
    tree.delete(*tree.get_children())
    cursor=conn.execute("SELECT *FROM STUD_REGISTRATION")
    fetch=cursor.fetchall()
    for data in fetch:
        tree.insert("","end",values=(data))
    cursor.close()           
    conn.close()
display_screen=Tk()
display_screen.geometry("900x400")
display_screen.title("STUDENT DATABASE MANAGEMENT SYSTEM")
global tree
global SEARCH
global name,contact,email,rollno,branch
SEARCH=StringVar()
name=StringVar()
contact=StringVar()
email=StringVar()
rollno=StringVar()
branch=StringVar()
TopViewForm=Frame(display_screen, width=600,bd=1,relief=SOLID)
TopViewForm.pack(side=TOP, fill=X)
LFrom=Frame(display_screen,width="350")
LFrom.pack(side=LEFT,fill=Y)
LeftViewForm=Frame(display_screen,width=800,bg='red')
LeftViewForm.pack(side=LEFT,fill=Y)
MidView=Frame(display_screen,width=600)
MidView.pack(side=RIGHT)
lbl_text=Label(TopViewForm,text="Student Management System",font=("verdana",18),width=600,bg="#271c33",fg="white")
lbl_text.pack(fill=X)
Label(LFrom,text="Name ",font=("Arial",12)).pack(side=TOP)
Entry(LFrom,font=("Arial",10,"bold"),textvariable=name).pack(side=TOP,padx=10,fill=X)
Label(LFrom,text="Contact",font=("Arial",12)).pack(side=TOP)
Entry(LFrom,font=("Arial",10,"bold"),textvariable=contact).pack(side=TOP,padx=10,fill=X)
Label(LFrom,text="Email",font=("Arial",12)).pack(side=TOP)
Entry(LFrom,font=("Arial",10,"bold"),textvariable=email).pack(side=TOP,padx=10,fill=X)
Label(LFrom,text="Rollno",font=("Arial",12)).pack(side=TOP)
Entry(LFrom,font=("Arial",10,"bold"),textvariable=rollno).pack(side=TOP,padx=10,fill=X)
Label(LFrom,text="Branch",font=('Arial',12)).pack(side=TOP)
Entry(LFrom,font=("Arial",10,"bold"),textvariable=branch).pack(side=TOP,padx=10,fill=X)
Button(LFrom,text="Submit",font=("Arial",10,"bold"),command=register).pack(side=TOP,padx=10,pady=5,fill=X)
lbl_txtsearch=Label(LeftViewForm,text="Enter name to Search",font=("verdana",10),bg="gray")
lbl_txtsearch.pack()
search=Entry(LeftViewForm,textvariable=SEARCH,font=("verdana",15),width=10)
search.pack(side=TOP,padx=10,pady=10,fill=X)
btn_search=Button(LeftViewForm,text="Search",command=SearchRecord)
btn_search.pack(side=TOP,padx=10,pady=10,fill=X)
btn_view=Button(LeftViewForm,text="View All",command=DisplayData)
btn_view.pack(side=TOP,padx=10,pady=10,fill=X)
btn_reset=Button(LeftViewForm,text="reset",command=Reset)
btn_reset.pack(side=TOP,padx=10,pady=10,fill=X)
btn_delete=Button(LeftViewForm,text="Delete",command=Delete)
btn_delete.pack(side=TOP,padx=10,pady=10,fill=X)
scrollbarx=Scrollbar(MidView,orient=HORIZONTAL)
scrollbary=Scrollbar(MidView,orient=VERTICAL)
tree=ttk.Treeview(MidView,columns=("Student ID","Name","Contact","Email","Rollno","Branch"),
                  selectmode="extended",height=100,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT,fill=Y)
scrollbarx.config(command=tree.yview)
scrollbarx.pack(side=RIGHT,fill=X)
tree.heading('Name',text="Name",anchor=W)
tree.heading("Contact",text="Contact",anchor=W)
tree.heading("Email",text="Email",anchor=W)
tree.heading("Rollno",text="Rollno",anchor=W)
tree.heading("Branch",text="Branch",anchor=W)
tree.column("#0",stretch=NO,minwidth=0,width=0)
tree.column("#1",stretch=NO,minwidth=0,width=100)
tree.column("#2",stretch=NO,minwidth=0,width=150)
tree.column("#3",stretch=NO,minwidth=0,width=80)
tree.column("#4",stretch=NO,minwidth=0,width=120)
tree.pack()
DisplayData()
display_screen.mainloop()
    
               
            

