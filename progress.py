from tkinter import *    
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter import ttk
from sqlite3 import *
import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

#-----------------------------------------------------------------------------------------------
def f12():
	progress.destroy()
	os.system('python option.py')

def f18():
	progress.destroy()
	os.system('python profile.py')
	
def f19():
	progress.destroy()
	os.system('python Test.py')

def f27():
	progress.destroy()
	os.system('python practice.py')
	
def f11():
	con = None
	name = usrnm
	C5.itemconfig(prog_name, text=name)
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql1= "select max(test_no) from '%s'"
		cursor.execute(sql1 % (name))
		tnum=cursor.fetchone()[0]
		sql2 = "select speed from '%s' where test_no='%d'"
		cursor.execute(sql2 % (name,tnum))
		spd=cursor.fetchone()[0]
		prg_spd = str(spd) + " words/min"
		sql3 = "select accuracy from '%s' where test_no='%d'"
		cursor.execute(sql3 % (name,tnum))
		acc=cursor.fetchone()[0]
		prg_acc = str(acc) + "%"
		sql4 = "select rank from ranked where user_id='%s'"
		cursor.execute(sql4 % (name))
		prg_rank=cursor.fetchone()[0]
		sql5 = "Select * from '%s'"
		cursor.execute(sql5 % (name))
		rows = cursor.fetchall()
		for i in rows:
			if i[0]%2==0:
				prog_tree.insert('','end',values=i,tags=("yess",))
			else:
				prog_tree.insert('','end',values=i,tags=("noo",))
		prog_tree.tag_configure("yess",foreground="black",background="thistle1")
		C5.itemconfig(prog_speed, text=prg_spd)
		C5.itemconfig(prog_accuracy, text=prg_acc)
		C5.itemconfig(prog_rank, text=prg_rank)
	except Exception as e:
		#showerror("Issue",e)
		C5.itemconfig(prog_speed, text="NA")
		C5.itemconfig(prog_accuracy, text="NA")
		C5.itemconfig(prog_rank, text="NA")
	finally:
		if con is not None:
			con.close()

def graph():
	name = usrnm
	con = None
	try:
		con = connect("TST.db")
		cursor= con.cursor()
		sql = "select test_no from '%s'"
		cursor.execute(sql % (name))
		attempts = cursor.fetchall()
		x = attempts
		sql1 = "select speed from '%s'"
		cursor.execute(sql1 % (name))
		speedd = cursor.fetchall()
		y = speedd
		plt.plot(x,y,marker="o",label=name, color="red")
		plt.xlabel("Number of attempts")
		plt.ylabel("Speed")
		plt.title(name + "'s Performance")
		plt.legend()
		plt.grid()
		plt.show()
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()

def pie():
	name = usrnm
	acc = []
	att = []
	spd = []
	con = None
	try:
		con = connect("TST.db")
		cursor= con.cursor()
		sql = "select test_no from '%s'"
		cursor.execute(sql % (name))
		attempts = cursor.fetchall()
		for t in attempts:
			att.append(float(str(t[0])))
		sql1 = "select accuracy from '%s'"
		cursor.execute(sql1 % (name))
		accuracy = cursor.fetchall()
		for a in accuracy:
			acc.append(float(str(a[0])))
		sql2 = "select speed from '%s'"
		cursor.execute(sql2 % (name))
		speed = cursor.fetchall()
		for s in speed:
			spd.append(float(str(s[0])))
		x = np.arange(len(att))
		plt.bar(x, spd, width=0.25, label="Speed")
		plt.bar(x+0.25, acc, width=0.25, label="Accuracy")
		plt.xticks(x, att)
		plt.xlabel("No. of Attempts")
		plt.ylabel("Speed and Accuracy")
		plt.title(name + "'s Performance Analysis")
		plt.legend()
		plt.grid()
		plt.show()
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()


#-------------------------------------------------------------------------------------------------

try:
	con = connect("TST.db")
	cursor = con.cursor()
	sql1="select curr_user from logged where No=1"
	cursor.execute(sql1)
	usrnm=cursor.fetchone()[0]
	print(usrnm)
except Exception as e:
	showerror("Issue",e)
finally:
	if con is not None:
		con.close()

progress=Tk()
progress.title("Progress")
progress.geometry("800x600+300+50")
graph_wall = PhotoImage(file="Images/g4.png")
small_logo = PhotoImage(file="Images/small_logo.png")
prog_logo = PhotoImage(file="Images/prog_logo.png")
header_bg = PhotoImage(file="Images/head.png")
C5 = Canvas(progress, width=800, height=600, bg="white")
C5.create_image(400, 24, image=header_bg)
C5.create_image(743, 24, image=small_logo)
C5.create_image(400, 325, image=graph_wall)
C5.create_image(640, 170, image=prog_logo)
C5.create_rectangle(402, 2, 535, 48, fill='plum1', stipple="gray50")

btn_home=Button(progress,text="Home",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4", foreground="White",command=f12)
btn_profile=Button(progress,text="Profile",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4", foreground="White",command=f18)
btn_prac=Button(progress,text="Practice",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4", foreground="White",command=f27)
btn_ttest=Button(progress,text="Take Test",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4", foreground="White",command=f19)
btn_progress=Button(progress,text="Progress",width=13,font=("Times New Roman",12,"bold"),bg="plum1")

C5.create_text(50, 100, text="User-ID                              :", font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
C5.create_text(50, 130, text="Current Typing Speed   :", font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
C5.create_text(50, 160, text="Accuracy                          :", font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
C5.create_text(50, 190, text="Ranking in Last 24 Hrs  :", font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
C5.create_text(400, 250, text="Test Records", font=("Arial Rounded MT Bold",19,"normal"))
C5.create_text(400, 240, text="______                         ______", font=("Arial Rounded MT",19,"normal"))

prog_name = C5.create_text(350, 100, font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
prog_speed = C5.create_text(350, 130, font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
prog_accuracy = C5.create_text(350, 160, font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
prog_rank = C5.create_text(350, 190, font=("Arial Rounded MT Bold",17,"normal"), anchor="w")

prog_wrap = Frame(progress)
prog_wrap.place(x=80, y=280)

prstyle = ttk.Style()

prog_tree_scrl = Scrollbar(prog_wrap,orient="vertical")
prog_tree_scrl.pack(side = RIGHT, fill=Y)
prog_tree = ttk.Treeview(prog_wrap, columns=(1,2,3), show="headings", height="7",yscrollcommand=prog_tree_scrl.set, style="mystyle1.Treeview")
prstyle.theme_use("clam")
prstyle.configure("mystyle1.Treeview.Heading", font=("Calibri", 13, "bold"),background="pale violet red", foreground="white")
prstyle.configure("Treeview", font=("Calibri", 12))
prog_tree.pack()
prog_tree_scrl.config(command=prog_tree.yview)
prog_tree.column(1,width=210,anchor=CENTER)
prog_tree.column(2,width=210,anchor=CENTER)
prog_tree.column(3,width=210,anchor=CENTER)
prog_tree.heading(1, text="Attemps")
prog_tree.heading(2, text="Speed")
prog_tree.heading(3, text="Accuracy")

btn_graph=Button(progress,text="View speed progress",width=28,bg="pink",font=("Calibri",16,"bold"),command=graph)
btn_acc=Button(progress,text="Overall Performance",width=28,bg="pink",font=("Calibri",16,"bold"),command=pie)
btn_home.place(x=7,y=7)
btn_prac.place(x=140,y=7)
btn_profile.place(x=273,y=7)
btn_progress.place(x=406,y=7)
btn_ttest.place(x=539,y=7)
btn_graph.place(x=70,y=490)
btn_acc.place(x=400,y=490)
C5.pack()
f11()
progress.mainloop()

