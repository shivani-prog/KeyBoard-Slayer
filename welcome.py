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

#---------------------------------------------------------------------------------

def f1():
	welcome.destroy()
	os.system('python login.py')

def f3():
	welcome.destroy()
	os.system('python signup.py')
def admin():
	welcome.destroy()
	os.system('python admin.py')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Welcome Page ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

welcome=Tk()
welcome.title("Welcome page")
welcome.geometry("800x600+300+50")

f=("Berlin Sans FB",25,"normal")
fa=("Bell MT",20,"bold")
filename = PhotoImage(file="Images/welcome.png")
proj_logo = PhotoImage(file="Images/big_logo.png")
C= Canvas(welcome, width=800, height=600)
C.create_image(400, 300, image=filename)
C.create_image(400, 290, image=proj_logo)

C.create_text(390, 100, text="WELCOME TO TYPING SPEED TEST", font=f, fill="white")
btn_login=Button(welcome,text="Login",width=10,font=fa,bg="pink2",command=f1)
btn_signup=Button(welcome,text="Sign-Up",width=10,font=fa,bg="pink2",command=f3)
btn_admin=Button(welcome,text="Admin",width=7,height=1,font=fa,bg="pink2",command=admin)

C.pack(expand=True)
btn_login.place(x=150,y=450)
btn_signup.place(x=450,y=450)
btn_admin.place(x=650,y=7)
welcome.mainloop()