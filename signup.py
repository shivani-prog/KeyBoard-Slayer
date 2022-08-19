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
#---------------------------------------------------------------------------------------

def f4():
	signup.destroy()
	os.system('python welcome.py')

def f7():             #for signup       
	con = None
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql = "insert into users values('%s', '%s', 0)"
		username=ent_setusername.get()
		password=ent_setpassword.get()
		cpassword=ent_confrmpassword.get()

		if (username.isalnum()==False) and  (len(password)>10 or len(password)<5):
			showerror("Error","Enter Valid Username or Password !")
		elif username.isalnum()==False:
			showerror("Error","Invalid username, no special characters allowed!")
			ent_setusername.delete(0,END)
			ent_setusername.focus()
		elif len(password)>10 or len(password)<5:
			showerror("Error","Length of Password should be between 5-10 characters only ! ")
			ent_setpassword.delete(0,END)
			ent_setpassword.focus()
		elif password!=cpassword:
			showerror("Warning","Password is Invalid!")
		else:
			cursor.execute(sql % (username, password))
			con.commit()
			showinfo("Successful","Signed-in Successfully !!")
			sql1 = "create table '%s' (test_no integer primary key Autoincrement, speed float, accuracy float)"
			cursor.execute(sql1 % (username))
			sql2 = "insert into rank values('%s', 0, 0)"
			cursor.execute(sql2 % (username))
			con.commit()
			signup.destroy()
			os.system('python login.py')
			'''login.deiconify()
			signup.withdraw()'''
	except Exception as e:
		con.rollback()
		
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
	ent_setusername.delete(0,END)
	ent_setpassword.delete(0,END)
	ent_confrmpassword.delete(0,END)

def f10():
	ent_setusername.delete(0,END)
	ent_setpassword.delete(0,END)
	ent_confrmpassword.delete(0,END)
	ent_setusername.focus()

#----------------------------------------------------------------------------------------

signup=Tk()
signup.title("SignUp page")
signup.geometry("800x600+300+50")
fb=("Arial Rounded MT Bold",29,"normal")
fc=("Arial", 18, "normal")
fd=("Arial Rounded MT", 20, "bold")
check_logo = PhotoImage(file="Images/checkin.png")
filename1 = PhotoImage(file="Images/texture.png")
sign_logo = PhotoImage(file="Images/sign.png")
user_logo = PhotoImage(file="Images/username.png")
password_logo = PhotoImage(file="Images/lock.png")

C2 = Canvas(signup, width=800, height=600)
C2.create_image(400, 300, image=filename1)
C2.create_image(300, 100, image=sign_logo)
C2.create_image(122, 229, image=user_logo)
C2.create_image(122, 309, image=password_logo)
C2.create_image(122, 389, image=check_logo)

C2.create_text(440, 100, text="SIGN-UP", font=fb, fill="black")
C2.create_text(390, 140, text="__________________________________", font=fb, fill="black")
C2.create_text(230, 230, text="USERNAME", font=fd, fill="black")
C2.create_text(230, 310, text="PASSWORD", font=fd, fill="black")
C2.create_text(230, 390, text="PASSWORD", font=fd, fill="black")

ent_setusername=Entry(signup,bd=5,font=fc, width=22)
ent_setpassword=Entry(signup,bd=5,font=fc, width=22, show="*")
ent_confrmpassword=Entry(signup,bd=5,font=fc,width=22, show="*")
btn_reset=Button(signup,text="RESET",width=10,font=("Georgia", 17, "bold"),command=f10)
btn_submit=Button(signup,text="SUBMIT",width=10,font=("Georgia", 17, "bold"),command=f7)
btn_back=Button(signup,text="Back",width=10,height=1,font=("Times New Roman",10,"bold"),command=f4)

ent_setusername.place(x=350,y=210)
ent_setpassword.place(x=350,y=290)
ent_confrmpassword.place(x=350,y=370)
btn_reset.place(x=140,y=460)
btn_submit.place(x=470,y=460)
btn_back.place(x=700,y=10)
C2.pack(expand=True)
signup.mainloop()
