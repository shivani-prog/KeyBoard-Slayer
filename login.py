from tkinter import *    
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter import ttk
from sqlite3 import *
import random
import time
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#---------------------------------------------------------------------------

def f2():
	login.destroy()
	os.system('python welcome.py')

def f3():
	ent_username.delete(0,END)
	ent_password.delete(0,END)
	ent_username.focus()
	

def f5():                 # for login
	con = None
	username = ent_username.get()
	password = ent_password.get()
	f5.usrnm = username
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql = "select * from users where user_name='%s' and user_pass='%s'"
		
		if username=="" or password=="":
			showwarning("Invalid", "Fields can't be empty!!")
		else:
			cursor.execute(sql % (username, password))
			con.commit()
			data = cursor.fetchall()
			if len(data) > 0:
				sql1 = 	"Update logged set curr_user='%s' where No=1"
				cursor.execute(sql1 % (username))
				con.commit()		
				showinfo("Successful", "Login Successful !!")
				login.destroy()
				os.system('python option.py')
			else:
				showerror("Error", "Invalid username or password! Please, try again...")
				ent_username.focus()
	except Exception as e:
		con.rollback()
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
	ent_username.delete(0,END)
	ent_password.delete(0,END)

#--------------------------------------------------------------------------------------------------

login=Tk()
login.title("Login Page")
login.geometry("800x600+300+50")
fb=("Arial Rounded MT Bold",29,"normal")
fc=("Arial", 18, "normal")
fd=("Arial Rounded MT", 20, "bold")
filename1 = PhotoImage(file="Images/texture.png")
login_logo = PhotoImage(file="Images/login.png")
user_logo = PhotoImage(file="Images/username.png")
password_logo = PhotoImage(file="Images/lock.png")

C1 = Canvas(login, width=800, height=600)

C1.create_image(400, 300, image=filename1) # bg image
C1.create_image(300, 110, image=login_logo) 
C1.create_image(122, 250, image=user_logo)
C1.create_image(122, 354, image=password_logo)

C1.create_text(420, 110, text="LOGIN", font=fb, fill="black")
C1.create_text(390, 150, text="__________________________________", font=fb, fill="black")
C1.create_text(230, 251, text="USER-ID", font=fd, fill="black")
ent_username=Entry(login,bd=5,font=fc, width=22)
C1.create_text(230, 355, text="PASSWORD", font=fd, fill="black")
ent_password=Entry(login, bd=5, font=fc, width=22, show="*")
btn_reset=Button(login, text="RESET", width=10, font=("Georgia", 17, "bold"),command=f3)
btn_submit=Button(login, text="SUBMIT", width=10, font=("Georgia", 17, "bold"),command=f5)
btn_back=Button(login,text="Back",width=8,height=1,font=("Times New Roman",15,"bold"),command=f2)

ent_username.place(x=370,y=230)
ent_password.place(x=370,y=331)
btn_reset.place(x=140,y=450)
btn_submit.place(x=470,y=450)
btn_back.place(x=660,y=10)

C1.pack(expand=True)
login.mainloop()
