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

def f17():
	profile.destroy()
	os.system('python option.py')

def f23():
	profile.destroy()
	os.system('python progress.py')

def f22():
	profile.destroy()
	os.system('python Test.py')

def f29():
	profile.destroy()
	os.system('python practice.py')

def f26():
	profile.destroy()
	os.system('python login.py')

def change():
	C6.coords(ab, 90, 360)
	C6.coords(cd, 90, 400)
	C6.coords(ef, 90, 440)
	C6.coords(prof_perfm, 370, 360)
	C6.coords(prof_rank, 370, 400)
	btn_delete.place(x=370, y=430)
	C6.itemconfig(gh, state='normal')
	btn_change.place_forget()
	ent_change.place(x=370, y=310)
	btn_update.place(x=570, y=306)

def updte():
	name = usrnm
	new_pass = ent_change.get()
	con = None
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql1= "update users set user_pass='%s' where user_name='%s'"
		cursor.execute(sql1 % (new_pass, name))
		con.commit()
		showinfo("Changed", "Your password has been successfully updated!")
		C6.itemconfig(prof_pass, text=new_pass)
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()


def delete():
	name = usrnm
	con = None
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql1= "delete from users where user_name='%s'"
		cursor.execute(sql1 % (name))
		con.commit()
		sql2= "delete from rank where user_id='%s'"
		cursor.execute(sql2 % (name))
		con.commit()
		sql3= "delete from ranked where user_id='%s'"
		cursor.execute(sql3 % (name))
		con.commit()
		sql4= "drop table '%s'"
		cursor.execute(sql4 % (name))
		con.commit()
		showinfo("Deleted", "Your account has been successfully deleted!")
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
		profile.destroy()
		os.system('python welcome.py')
	

def f14():
	name = usrnm
	prf_perf = ""
	prf_spd = 3.94
	prf_acc = 5.04
	C6.itemconfig(prof_name, text=name)
	con = None
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql1= "select user_pass from users where user_name='%s'"
		cursor.execute(sql1 % (name))
		usrpass=cursor.fetchone()[0]
		sql2 = "select max(speed+accuracy) from '%s'"
		cursor.execute(sql2 % (name))
		perf=cursor.fetchone()[0]
		perf=round(perf, 2)
		print(perf)
		sql3 = "select speed,accuracy from '%s' where speed+accuracy=%f"
		cursor.execute(sql3 % (name,perf))
		data=cursor.fetchall()
		con.commit()
		print(data)
		for d in data:
			prf_spd = d[0]
			prf_acc = d[1]
		prf_perf = "Speed of " + str(prf_spd) + " WPM with " + str(prf_acc) + "%"
		sql4 = "select rank from ranked where user_id='%s'"
		cursor.execute(sql4 % (name))
		prf_rank=cursor.fetchone()[0]
		C6.itemconfig(prof_pass, text=usrpass)
		C6.itemconfig(prof_perfm, text=prf_perf)
		C6.itemconfig(prof_rank, text="Rank " + str(prf_rank))
	except Exception as e:
		#showerror("Issue",e)
		C6.itemconfig(prof_pass, text="None")
		C6.itemconfig(prof_perfm, text="None")
		C6.itemconfig(prof_rank, text="None")
	finally:
		if con is not None:
			con.close()


try:
	con = connect("TST.db")
	cursor = con.cursor()
	sql1="select curr_user from logged where No=1"
	cursor.execute(sql1)
	usrnm=cursor.fetchone()[0]
except Exception as e:
	showerror("Issue",e)
finally:
	if con is not None:
		con.close()

profile=Tk()
profile.title("Profile page")
profile.geometry("800x600+300+50")

header_bg = PhotoImage(file="Images/head.png")
wallp = PhotoImage(file="Images/w7.png")
prof_icon = PhotoImage(file="Images/profile.png")
small_logo = PhotoImage(file="Images/small_logo.png")
C6 = Canvas(profile, width=800, height=600, bg="white")
C6.create_image(400, 24, image=header_bg)
C6.create_image(743, 24, image=small_logo)
C6.create_image(400, 325, image=wallp)
C6.create_image(150, 148, image=prof_icon)
C6.create_rectangle(269, 2, 402, 48, fill='plum1', stipple="gray50")

btn_home=Button(profile,text="Home",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4",foreground="White",command=f17)
btn_profile=Button(profile,text="Profile",width=13,font=("Times New Roman",12,"bold"),bg="plum1")
btn_ttest=Button(profile,text="Take Test",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4",foreground="White",command=f22)
btn_progress=Button(profile,text="Progress",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4",foreground="White",command=f23)
btn_practice=Button(profile,text="Practice",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4",foreground="White",command=f29)
btn_logout=Button(profile,text="Logout",width=13,font=("Calibri",16,"bold"),bg="plum1",command=f26)

C6.create_text(260, 170, text=usrnm, font=("Segoe UI Semibold",23,"normal"), anchor="w")
C6.create_text(400, 200, text="______________________________________________________________", font=("Calibri",17,"bold"), fill="DeepPink4")
C6.create_text(90, 240, text="User-ID                           :", font=("Segoe UI Semibold",17,"normal"), anchor="w")
C6.create_text(90, 280, text="Password                        :", font=("Segoe UI Semibold",17,"normal"), anchor="w")
gh = C6.create_text(90, 320, text="New Password                 :", font=("Segoe UI Semibold",17,"normal"),anchor="w",state='hidden')
ab = C6.create_text(90, 320, text="Best performance          :", font=("Segoe UI Semibold",17,"normal"), anchor="w")
cd = C6.create_text(90, 360, text="Ranking in Last 24 Hrs  :", font=("Segoe UI Semibold",17,"normal"), anchor="w")
ef = C6.create_text(90, 400, text="Remove Account           :", font=("Segoe UI Semibold",17,"normal"), anchor="w")
C6.create_text(400, 480, text="______________________________________________________________", font=("Calibri",17,"bold"), fill="DeepPink4")
btn_delete=Button(profile,text="DELETE",width=13,font=("Calibri",12,"bold"),bg="Cyan",command=delete)
btn_change=Button(profile,text="CHANGE PASSWORD",font=("Calibri",12,"bold"),bg="Cyan",command=change)

ent_change=Entry(profile,font=("Calibri",15,"bold"),width=17)
btn_update=Button(profile,text="CHANGE",font=("Calibri",12,"bold"),bg="Cyan",command=updte)

prof_name = C6.create_text(370, 240, font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
prof_pass = C6.create_text(370, 280, font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
prof_perfm = C6.create_text(370, 320, font=("Arial Rounded MT Bold",17,"normal"), anchor="w")
prof_rank = C6.create_text(370, 360, font=("Arial Rounded MT Bold",17,"normal"), anchor="w")

btn_home.place(x=7,y=7)
btn_practice.place(x=140,y=7)  
btn_profile.place(x=273,y=7)
btn_progress.place(x=406,y=7)
btn_ttest.place(x=539,y=7)
btn_delete.place(x=370, y=390)
btn_change.place(x=500, y=268)
btn_update.place_forget()
ent_change.place_forget()

btn_logout.place(x=560,y=520)
C6.pack()
f14()
profile.mainloop()