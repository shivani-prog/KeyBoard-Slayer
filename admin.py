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

def back():
	admin.destroy()
	os.system('python welcome.py')

def reset():
	ent_username.delete(0,END)
	ent_password.delete(0,END)
	ent_username.focus()

def submit():             #for signup       

	x=ent_username.get()
	y=ent_password.get()
	if x=='Terna123' and y=='12345':
		admin.destroy()
		os.system('python admininfo.py')
	else:
		showwarning("Warning","Please enter valid login credentials")
		



	'''if (username.isalnum()==False) and  (len(password)>10 or len(password)<5):
		showerror("Error","Enter Valid Username or Password !")
	elif username.isalnum()==False:
		showerror("Error","Invalid username, no special characters allowed!")
		ent_setusername.delete(0,END)
		ent_setusername.focus()
	elif len(password)>10 or len(password)<5:
		showerror("Error","Length of Password should be between 5-10 characters only ! ")
		ent_setpassword.delete(0,END)
		ent_setpassword.focus()
	else:
		login.deiconify()
		signup.withdraw()'''

admin=Tk()
admin.title("Admin Page")
admin.geometry("800x600+300+50")
Admin=PhotoImage(file="Images/admin2.png")
Adminicon=PhotoImage(file="Images/adminicon.png")
Back=PhotoImage(file="Images/back.png")
small_logo1 = PhotoImage(file="Images/medium_logo.png")
p=Canvas(admin,width=800,height=600)
p.create_image(400,300,image=Admin)
p.create_image(220,100,image=Adminicon)
p.create_image(700, 70, image=small_logo1)
p.create_text(400, 100, text="WELCOME ADMIN", font=("Bahnschrift SemiBold SemiConden",28,"normal"), fill="white")
p.create_text(390, 150, text="_________________________________________________________________________________________________________________",fill="white")
p.create_text(230, 251, text="USER-ID", font=("Bahnschrift SemiBold SemiConden",18,"normal"), fill="white")
ent_username=Entry(admin,bd=5,font=("Bahnschrift SemiBold SemiConden",18,"normal"), width=22)
p.create_text(230, 355, text="PASSWORD", font=("Bahnschrift SemiBold SemiConden",18,"normal"), fill="white")
ent_password=Entry(admin, bd=5, font=("Bahnschrift SemiBold SemiConden",18,"normal"), width=22, show="*")
p.create_text(390, 400, text="_________________________________________________________________________________________________________________",fill="white")
btn_reset=Button(admin, text="RESET", width=10, font=("Georgia", 17, "bold"),command=reset)
btn_submit=Button(admin, text="SUBMIT", width=10, font=("Georgia", 17, "bold"),command=submit)
btn_back=Button(admin,image=Back,borderwidth=0,bg="navy blue",command=back)

ent_username.place(x=370,y=230)
ent_password.place(x=370,y=331)
btn_reset.place(x=140,y=450)
btn_submit.place(x=470,y=450)
btn_back.place(x=6,y=10)


p.pack()
admin.mainloop()