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

def ok():
	admininfo.destroy()
	os.system('python admin.py')

def f11():
	con = None
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql5 = "Select user_name from users"
		cursor.execute(sql5)
		rows = cursor.fetchall()
		for i in rows:
			prog_tree.insert('','end',values=i,tags=("yess",))

	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()



admininfo=Tk()
admininfo.title("Admin's Information Page")
admininfo.geometry("800x600+300+50")


AdminInfo=PhotoImage(file="Images/adminheader.png")
Adminicon=PhotoImage(file="Images/adminicon.png")
#Back=PhotoImage(file="Images/back.png")
small_logo1 = PhotoImage(file="Images/medium_logo.png")
p=Canvas(admininfo,width=800,height=600)
p.create_image(400,24,image=AdminInfo)
p.create_image(50,100,image=Adminicon)
p.create_text(400, 100, text="User's Information", font=("Bahnschrift SemiBold SemiConden",25,"normal"), fill="navy blue")
p.create_text(390, 150, text="_________________________________________________________________________________________________________________",fill="navy blue")

'''
scrol=ScrolledText(admininfo,height=18,width=87)
scrol.place(x=50,y=190)'''

prog_wrap = Frame(admininfo)
prog_wrap.place(x=80, y=190)

prstyle = ttk.Style()

prog_tree_scrl = Scrollbar(prog_wrap,orient="vertical")
prog_tree_scrl.pack(side = RIGHT, fill=Y)
prog_tree = ttk.Treeview(prog_wrap, columns=(1), show="headings", height="12",yscrollcommand=prog_tree_scrl.set, style="mystyle1.Treeview")
prstyle.theme_use("clam")
prstyle.configure("mystyle1.Treeview.Heading", font=("Calibri", 13, "bold"),background="navy blue", foreground="white")
prstyle.configure("Treeview", font=("Calibri", 12))
prog_tree.pack()
prog_tree_scrl.config(command=prog_tree.yview)
prog_tree.column(1,width=620,anchor=CENTER)
prog_tree.heading(1, text="Users")

btn_ok=Button(admininfo, text="OK", width=10, bg="navy blue",font=("Bahnschrift SemiBold SemiConden", 17, "bold"),foreground="white",command=ok)
#btn_back=Button(admininfo,image=Back,borderwidth=0,bg="navy blue")



btn_ok.place(x=340,y=500)
#btn_back.place(x=6,y=10)


p.pack()

f11()







admininfo.mainloop()


