from tkinter import *
import tkinter as tk
import mysql.connector 
root = Tk()
def login():
    global username
    global password
    user = username.get()
    passw = password.get()
    con = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "login")
    c = con.cursor()
    c.execute('select * from user_detail')
    r = c.fetchall()
    for row in r:
            if user.lower() == row[1] and passw.lower() == row[2]:
                lo = Tk()
                lo.geometry("200x200")
                greet = Label(lo,text="welcome to python course").pack()
                lo.mainloop()
                break
            else:
                lo1 = Tk()
                lo1.geometry("200x200")
                wro = Label(lo1,text="click register to create account").pack()
                lo1.mainloop()
            break 
    con.close()   
# def homeclear():
#     self.username.delete(0, END)
#     self.password.delete(0, END)
# def regclear():
#         nusername.delete(0, END)
#         npassword.delete(0, END)
#         confirmpass.delete(0, END)

def reg():
     root2 = Tk()
     def add():
         global user
         global passw
         global conpass
         user = nusername.get()
         passw = npassword.get()
         conpass = confirmpass.get()
         if passw.lower() == conpass.lower():
            con = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database = "login")
            c = con.cursor()
            c.execute(f"Insert INTO user_detail(username, password) VALUES ('{user}','{passw}')")
            con.commit()
            con.close()
         else:
             messlable = Label(root2,text="Confirm password is not matching").pack()
     root2.geometry("370x400")
     labelframe1 = LabelFrame(root2, text=" REGISTER YOUR DETAILS ")  
     labelframe1.pack(fill="both", expand="yes")  
     toplabel = Label(labelframe1)  
     toplabel.pack()
     new_label = Label(root2,text="New Username")
     nusername = Entry(root2)
     nusername.focus_set()
     nlabel = Label(root2,text=" Enter Password")
     npassword = Entry(root2,show ='*')
     npassword.focus_set()
     conflabel = Label(root2,text="Confirm password")
     confirmpass = Entry(root2,show ='*')
     confirmpass.focus_set()
     Add_btn = Button(root2,text="Click Add",command=add)
     new_label.place(x=30,y = 70) 
     nusername.place(x=120,y= 70,width=100 )
     nlabel.place(x= 30,y= 120)
     npassword.place(x=120,y= 120,width=100)
     conflabel.place(x = 30,y = 170)
     confirmpass.place(x = 135 ,y = 170,width=100)
     Add_btn.place(x = 30,y= 200)
     root2.mainloop()
root.geometry("370x400")
labelframe1 = LabelFrame(root, text="WELCOME TO LOGIN PAGE")  
labelframe1.pack(fill="both", expand="yes")  
root.title("LOGIN PAGE")  
toplabel = Label(labelframe1)  
toplabel.pack()  
login_btn = Button(root,text="Login",command=login)
register_btn = Button(root,text="REGISTER",command=reg)
label1 = Label(root,text="Username")
username = Entry(root)
username.focus_set()
label2 = Label(root,text="Password")
password = Entry(root,show ='*')
password.focus_set()
# username = StringVar()
# password = StringVar()
label1.place(x=30,y = 70)
username.place(x=100,y= 70,width=100 )
label2.place(x= 30,y= 110)
password.place(x=100,y= 110,width=100)
login_btn.place(x = 30,y= 150)
register_btn.place(x=80,y = 150)
root.mainloop()


