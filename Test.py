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

def f13():
	msg_quit = askquestion("Quit","Test will be terminated. Are you sure?")
	if msg_quit == "yes":
		taketest.destroy()
		os.system('python option.py')
	else:
		pass

def f17():
	taketest.destroy()
	os.system('python option.py')

def f23():
	taketest.destroy()
	os.system('python progress.py')

def f22():
	taketest.destroy()
	os.system('python profile.py')

def f29():
	taketest.destroy()
	os.system('python practice.py')

def shut():
	rftt.withdraw()
	

def test_para():
	usrnm1 = usrnm
	num = 0
	msg_start = askquestion("Get Ready!","Are you ready to start test?")
	if msg_start == "yes":
		showinfo("Instructions","You will be provided 5 minutes within which you need to type the given paragraph")
		btn_home.configure(state=DISABLED)
		btn_profile.configure(state=DISABLED)
		btn_progress.configure(state=DISABLED)
		btn_practice.configure(state=DISABLED)
		con=None
		try:
			con=connect("TST.db")
			cursor=con.cursor()
			sql="select test_no from users where user_name='%s'"
			cursor.execute(sql % (usrnm1))
			test_no=cursor.fetchall()
			sql1="select max(id) from practice"
			cursor.execute(sql1)
			max_para=cursor.fetchone()[0]
			for t in test_no:
				num=int(t[0])
				num=num+1
			sql2="select paragraph from practice where id='%d'"
			cursor.execute(sql2 % (num))
			data=cursor.fetchall()
			for d in data:
				info=str(d[0])
				para1.insert(INSERT, info)
			if num==max_para:
				max_para=0
				sql3="Update users set test_no ='%d' where user_name ='%s'"
				cursor.execute(sql3 % (max_para,usrnm1))
				con.commit()
			else:
				sql3="Update users set test_no ='%d' where user_name ='%s'"
				cursor.execute(sql3 % (num,usrnm1))
				con.commit()
			start()
			
		except Exception as e:
			showerror("Issue",e)
		finally:
			if con is not None:
				con.close()
		para1.config(state=DISABLED)
	else:
		import option
		taketest.destroy()


def start():
	try:
		temp = int(minute.get())*60 + int(second.get())
	except:
		print("Please input the right value")
	while temp >-1:
		mins,secs = divmod(temp,60)
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))
		taketest.update()
		time.sleep(1)
		if (temp == 0):
			showinfo("Time Countdown", "Time's up ")
		temp -= 1



def tcap_time():
	btn_home.configure(state=NORMAL)
	btn_profile.configure(state=NORMAL)
	btn_progress.configure(state=NORMAL)
	btn_practice.configure(state=NORMAL)
	min = int(minuteentry.get())
	sec = int(secondentry.get())
	minuteentry.destroy()
	secondentry.destroy()
	min = 5-min
	sec = 60-sec
	msec = sec/60
	con = None
	name = usrnm
	ttime = min+msec
	ttime = round(ttime, 2)
	tcap_time.totaltime = ttime 
	timetaken = str(min) + " min " + str(sec) + " sec"
	C9.itemconfig(tcanvas_id, text=name)
	C9.itemconfig(ttime_id, text=timetaken)
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql1="select max(test_no) from '%s'"
		cursor.execute(sql1 % (name))
		testnum=cursor.fetchone()[0]
		print(testnum)
		C9.itemconfig(ttest_no, text=testnum)
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
	
	rftt.deiconify()

def tcal_acc():
	p=para1.get("1.0",END)
	tot_char=len(p)
	tb=text_box1.get("1.0",END)
	count=0
	for i,j in zip(p,tb):
		if i==j:
			count=count+1
		else:
			pass
	corr_char=count
	accurate = (corr_char * 100)/tot_char
	accurate = round(accurate,2)
	accurr = str(accurate) + "%"
	C9.itemconfig(taccuracy_id, text=accurr)
	tcal_acc.acc = accurate

def tcal_spd():
	con = None
	name = usrnm
	accurate = tcal_acc.acc
	typed=text_box1.get("1.0",END)
	ttl_words = len(typed.split())
	total_time = tcap_time.totaltime
	words = ttl_words/total_time
	words = round(words, 2)
	WPM = str(words) + " per minute"
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql = "insert into '%s'(speed, accuracy) values('%f','%f')"
		cursor.execute(sql % (name, words, accurate))
		con.commit()
		sql2 = "update rank set curr_speed='%f' where user_id='%s'"
		cursor.execute(sql2 % (words, name))
		con.commit()
		sql3="select max(test_no) from '%s'"
		cursor.execute(sql3 % (name))
		testnum=cursor.fetchone()[0]
		C9.itemconfig(ttest_no, text=testnum)
	except Exception as e:
		con.rollback()
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
	C9.itemconfig(tspeed_id, text=WPM)

def trankers():
	name = usrnm
	con = None
	try:
		con = connect("TST.db")
		cursor= con.cursor()
		sq3 = "delete from ranked;"
		cursor.execute(sq3)
		con.commit()
		sq4 = "DELETE FROM SQLITE_SEQUENCE WHERE name='ranked';"
		cursor.execute(sq4)
		con.commit()
		sql = "Insert into ranked(user_id, speed) select user_id,curr_speed FROM rank order by curr_speed desc"
		cursor.execute(sql)
		con.commit()
		sql1 = "Select * from ranked"
		cursor.execute(sql1)
		rows = cursor.fetchall()
		for i in rows:
			if i[1] == name:
				trv.insert('','end',values=i,tags=("yess",))
			else:
				trv.insert('','end',values=i,tags=("noo",))
		trv.tag_configure("yess",foreground="white",background="DeepPink4")

	except Exception as e:
		showerror("Issue",e)
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

taketest=Tk()
taketest.title("Take Test")
taketest.geometry("800x600+300+50")

# Declaration of variables
minute=StringVar()
second=StringVar()
# setting the default value as 0
minute.set("05")
second.set("00")

name = StringVar()
name.set(usrnm)
header_bg = PhotoImage(file="Images/head.png")
wallp = PhotoImage(file="Images/w7.png")
small_logo = PhotoImage(file="Images/small_logo.png")
C7 = Canvas(taketest, width=800, height=600, bg="white")
C7.create_image(400, 24, image=header_bg)
C7.create_image(743, 24, image=small_logo)
C7.create_image(400, 325, image=wallp)
C7.create_rectangle(535, 2, 668, 48, fill='plum1', stipple="gray50")
C7.create_rectangle(50, 105, 750, 330, fill='white', width=2)
C7.create_text(550, 87, text="Timer : ", font=("Monotype Corsiva",16,"italic"), fill="black")

btn_home=Button(taketest,text="Home",width=13,font=("Times new Roman",12,"bold"),bg="DeepPink4",foreground="White",command=f17)
btn_profile=Button(taketest,text="Profile",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4",foreground="White",command=f22)
btn_progress=Button(taketest,text="Progress",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4",foreground="White",command=f23)
btn_ttest=Button(taketest,text="Take Test",width=13,font=("Times New Roman",12,"bold"),bg="plum1")
btn_practice=Button(taketest,text="Practice",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4",foreground="White",command=f29)
btn_submit=Button(taketest,text="Submit",height=2,width=20,font=("Times New Roman",12,"bold"),command=lambda:[tcap_time(),tcal_acc(),tcal_spd(),trankers()])
btn_clear=Button(taketest,text="Clear",height=2,width=20,font=("Times New Roman",12,"bold"))
btn_quit=Button(taketest,text="Quit",height=2,width=20,font=("Times New Roman",12,"bold"),command=f13)

minuteentry= Entry(taketest, width=3, font=("Arial",18,"bold"),textvariable=minute)
minuteentry.place(x=650,y=70)
secondentry= Entry(taketest, width=3, font=("Arial",18,"bold"),textvariable=second)
secondentry.place(x=700,y=70)

usrname1 = Label(taketest, textvariable=name,font=("Monotype Corsiva",17,"italic"), width=20,anchor="w", bg="white")
para1 = Text(taketest, height=9, width=69, font=("Times New Roman",15), wrap=WORD, bd=0)
text_box1 = Text(taketest, height=6, width=69, font=("Times New Roman",15), wrap=WORD, bd=5)

para1.bind('<Control-x>', lambda e: 'break')
para1.bind('<Control-c>', lambda e: 'break')
para1.bind('<Control-v>', lambda e: 'break')
text_box1.bind('<Control-x>', lambda e: 'break')
text_box1.bind('<Control-c>', lambda e: 'break')
text_box1.bind('<Control-v>', lambda e: 'break')

'''
#*****************************************************
text_box1.insert(INSERT, "START TYPING HERE...")
text_box1.configure(state=DISABLED)
def on_click(event):
	text_box1.configure(state=NORMAL)
	text_box1.delete(1.0,END)
	text_box1.unbind('<Button-1>', on_click_id)
on_click_id = text_box1.bind('<Button-1>', on_click)
#*****************************************************
'''
btn_home.place(x=7,y=7)
btn_practice.place(x=140,y=7)  
btn_profile.place(x=273,y=7)
btn_progress.place(x=406,y=7)
btn_ttest.place(x=539,y=7)
btn_submit.place(x=10,y=530)
btn_clear.place(x=300,y=530)
btn_quit.place(x=590,y=530)
C7.pack()
usrname1.place(x=52, y=71)
para1.place(x=55, y=110)
text_box1.place(x=50, y=350)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rftt=Toplevel(taketest)
rftt.title("Result page")
rftt.geometry("570x470+430+150")
testres = PhotoImage(file="Images/test_res.png")
C9 = Canvas(rftt, width=570, height=470, bg="white")
C9.create_image(285, 235, image=testres)
C9.create_text(100, 25, text="User Id:", font=("Arial Rounded MT Bold",17,"normal"), fill="White", anchor="e")
tcanvas_id = C9.create_text(225, 25, font=("Arial Rounded MT Bold",17,"italic"), fill="White", anchor="e")
ttest_no = C9.create_text(520, 25, font=("Arial Rounded MT Bold",17,"normal"), fill="White", anchor="e")
C9.create_text(390, 25, text="Test no:", font=("Arial Rounded MT Bold",17,"normal"), fill="White", anchor="w")
C9.create_text(285, 85,text="PERFORMANCE", font=("Arial Rounded MT Bold",20,"normal"), fill="White")
C9.create_text(285, 73, text="_____                            _____", font=("Arial Rounded MT",20,"normal"), fill="White")
C9.create_text(20, 130, text="TIME TAKEN  :", font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
C9.create_text(20, 170, text="SPEED             :", font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
C9.create_text(20, 210, text="ACCURACY    :", font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
C9.create_text(285, 260, text="RANK", font=("Arial Rounded MT Bold",20,"normal"), fill="White")
C9.create_text(285, 248, text="_____            _____", font=("Arial Rounded MT",20,"normal"), fill="White")

ttime_id = C9.create_text(235, 130, font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
tspeed_id = C9.create_text(235, 170, font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
taccuracy_id = C9.create_text(235, 210, font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
wrapper1 = Frame(rftt)
wrapper1.place(x=30, y=280)

tree_scroll = Scrollbar(wrapper1,orient="vertical")
tree_scroll.pack(side = RIGHT, fill=Y)
trv = ttk.Treeview(wrapper1, columns=(1,2,3), show="headings", height="4",yscrollcommand=tree_scroll.set)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Calibri", 11, "bold"),background="white")
style.configure("Treeview", font=("Calibri", 11))
trv.pack()
tree_scroll.config(command=trv.yview)
trv.column(1,width=160,anchor=CENTER)
trv.column(2,width=160,anchor=CENTER)
trv.column(3,width=160,anchor=CENTER)
trv.heading(1, text="Rank")
trv.heading(2, text="Name")
trv.heading(3, text="Speed")

btn_ok=Button(rftt,text="OK",width=8,font=("Arial Rounded MT Bold",15,"normal"), bg="LightCyan2",command=shut)
btn_ok.place(x=420,y=410)
C9.pack()
rftt.withdraw()

test_para()

taketest.mainloop()