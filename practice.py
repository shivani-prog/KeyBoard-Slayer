from tkinter import *    
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import os
import random
from PIL import Image,ImageTk

def f9():
	practice.destroy()
	os.system('python option.py')

def f13():
	practice.destroy()
	os.system('python progress.py')

def f24():
	practice.destroy()
	os.system('python profile.py')

def f25():
	practice.destroy()
	os.system('python Test.py')
	
def shut():
	rfp.withdraw()

def start2():
	try:
		temp = int(minute1.get())*60 + int(second1.get())
		text_box.configure(state=NORMAL)
		minuteentry1.configure(state=DISABLED)
		secondentry1.configure(state=DISABLED)
	except:
		print("Please input the right value")
	while temp >-1:
		mins,secs = divmod(temp,60)
		hours=0
		minute1.set("{0:2d}".format(mins))
		second1.set("{0:2d}".format(secs))
		practice.update()
		time.sleep(1)
		temp += 1

def f8():
	con=None
	try:
		con=connect("TST.db")
		cursor=con.cursor()
		sql="select paragraph from practice where id='%d'"
		x=random.randint(1,10)
		cursor.execute(sql % (x))
		data=cursor.fetchall()
		for d in data:
			info=str(d[0])
		return info
	except Exception as e:
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
def cap_time():
	min = int(minuteentry1.get())
	sec = int(secondentry1.get())
	msec = sec/60
	minuteentry1.destroy()
	secondentry1.destroy()
	userid = usrnm
	ptime = min+msec
	ptime = round(ptime, 2)
	cap_time.totaltime = ptime 
	timetaken = str(min) + " min " + str(sec) + " sec"
	C8.itemconfig(canvas_id, text=userid)
	C8.itemconfig(time_id, text=timetaken)
	rfp.deiconify()

def cal_acc():
	p=para.get("1.0",END)
	tot_char=len(p)
	tb=text_box.get("1.0",END)
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
	C8.itemconfig(accuracy_id, text=accurr)

def cal_spd():
	con = None
	name = usrnm
	typed=text_box.get("1.0",END)
	ttl_words = len(typed.split())
	total_time = cap_time.totaltime
	words = ttl_words/total_time
	words = round(words, 2)
	WPM = str(words) + " per minute"
	try:
		con = connect("TST.db")
		cursor = con.cursor()
		sql = "update rank set prac_no=prac_no+1 where user_id='%s'"
		cursor.execute(sql % (name))
		con.commit()
		sql2 = "select prac_no from rank where user_id='%s'"
		cursor.execute(sql2 % (name))
		pracno = cursor.fetchone()[0]
		C8.itemconfig(ptest_no, text=pracno)
	except Exception as e:
		con.rollback()
		showerror("Issue",e)
	finally:
		if con is not None:
			con.close()
	C8.itemconfig(speed_id, text=WPM)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Practice page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

practice=Tk()
practice.title("Practice")
practice.geometry("800x600+300+50")

minute1=StringVar()
second1=StringVar()
minute1.set("00")
second1.set("00")

header_bg = PhotoImage(file="Images/head.png")
wallp = PhotoImage(file="Images/w7.png")
small_logo = PhotoImage(file="Images/small_logo.png")
C4 = Canvas(practice, width=800, height=600, bg="white")
C4.create_image(400, 24, image=header_bg)
C4.create_image(400, 325, image=wallp)
C4.create_image(743, 24, image=small_logo)
C4.create_rectangle(136, 2, 269, 48, fill='plum1', stipple="gray50")
C4.create_rectangle(50, 105, 750, 330, fill='white', width=2)
C4.create_text(550, 87, text="Timer : ", font=("Monotype Corsiva",16,"italic"), fill="black")

btn_home=Button(practice,text="Home",width=13,font=("Times new Roman",12,"bold"),bg="DeepPink4", foreground="White", command=f9)
btn_prac=Button(practice,text="Practice",width=13,font=("Times New Roman",12,"bold"),bg="plum1", activebackground="plum1")
btn_profile=Button(practice,text="Profile",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4", foreground="White",command=f24)
btn_progress=Button(practice,text="Progress",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4", foreground="White",command=f13)
btn_ttest=Button(practice,text="Take Test",width=13,font=("Times New Roman",12,"bold"),bg="DeepPink4", foreground="White",command=f25)
btn_submit=Button(practice,text="Submit",height=2,width=20,font=("Times New Roman",12,"bold"),command=lambda:[pbtn_start.place_forget(),cap_time(),cal_acc(),cal_spd()])
btn_clear=Button(practice,text="Clear",height=2,width=20,font=("Times New Roman",12,"bold"))
btn_quit=Button(practice,text="Quit",height=2,width=20,font=("Times New Roman",12,"bold"))
pbtn_start=Button(practice,text="Start",height=1,width=11,font=("Times New Roman",12,"bold"),bg="DeepPink4",foreground="White",command=start2)

minuteentry1= Entry(practice, width=3, font=("Arial",18,"bold"),textvariable=minute1)
minuteentry1.place(x=650,y=70)
secondentry1= Entry(practice, width=3, font=("Arial",18,"bold"),textvariable=second1)
secondentry1.place(x=700,y=70)

usrname = Label(practice, text=usrnm ,font=("Monotype Corsiva",17,"italic"), width=20,anchor="w", bg="white")
para = Text(practice, height=9, width=69, font=("Times New Roman",15), wrap=WORD, bd=0)
text_box = Text(practice, height=6, width=69, font=("Times New Roman",15), wrap=WORD, bd=5)

para.bind('<Control-x>', lambda e: 'break')
para.bind('<Control-c>', lambda e: 'break')
para.bind('<Control-v>', lambda e: 'break')
text_box.bind('<Control-x>', lambda e: 'break')
text_box.bind('<Control-c>', lambda e: 'break')
text_box.bind('<Control-v>', lambda e: 'break')
pbtn_start.place(x=320,y=65)
btn_home.place(x=7,y=7)
btn_prac.place(x=140,y=7)
btn_profile.place(x=273,y=7)
btn_progress.place(x=406,y=7)
btn_ttest.place(x=539,y=7)
btn_submit.place(x=10,y=530)
btn_clear.place(x=300,y=530)
btn_quit.place(x=590,y=530)
usrname.place(x=52, y=71)
para.place(x=55, y=110)
text_box.place(x=50, y=350)

'''
#*****************************************************
text_box.insert(INSERT, "START TYPING HERE...")
text_box.configure(state=DISABLED)
def on_click(event):
        text_box.configure(state=NORMAL)
        text_box.delete(1.0,END)
        text_box.unbind('<Button-1>', on_click_id)
on_click_id = text_box.bind('<Button-1>', on_click)
#*****************************************************
'''
para.delete(1.0, END)
info = f8()
para.insert(INSERT, info)
para.config(state=DISABLED)

C4.pack()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~result page for practice(rfp)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rfp=Toplevel(practice)
rfp.title("Result page")
#rfp.overrideredirect(True)
rfp.geometry("520x400+450+170")
acc=StringVar()
timetook=StringVar()
wpm=StringVar()
usid=StringVar()
result = PhotoImage(file="Images/result.png")
res_icon = PhotoImage(file="Images/res_icon.png")
C8 = Canvas(rfp, width=5200, height=400, bg="white")
C8.create_image(260, 200, image=result)
C8.create_image(410, 300, image=res_icon)
C8.create_text(100, 25, text="User Id:", font=("Arial Rounded MT Bold",17,"normal"), fill="White", anchor="e")
canvas_id = C8.create_text(225, 25, font=("Arial Rounded MT Bold",17,"italic"), fill="White", anchor="e")
ptest_no = C8.create_text(460, 25,font=("Arial Rounded MT Bold",17,"normal"), fill="White", anchor="w")
C8.create_text(360, 25, text="Prac no:", font=("Arial Rounded MT Bold",17,"normal"), fill="White", anchor="w")
C8.create_text(260, 85,text="PERFORMANCE", font=("Arial Rounded MT Bold",20,"normal"), fill="White")
C8.create_text(260, 73, text="_____                            _____", font=("Arial Rounded MT",20,"normal"), fill="White")
C8.create_text(20, 145, text="TIME TAKEN  :", font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
C8.create_text(20, 195, text="SPEED             :", font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
C8.create_text(20, 245, text="ACCURACY    :", font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")

time_id = C8.create_text(235, 145, font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
speed_id = C8.create_text(235, 195, font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")
accuracy_id = C8.create_text(235, 245, font=("Arial Rounded MT Bold",18,"normal"), fill="White", anchor="w")

btn_ok=Button(rfp,text="OK",width=10,font=("Arial Rounded MT Bold",15,"normal"),bg="LightCyan2",command=shut)

btn_ok.place(x=110,y=300)
C8.pack()
rfp.withdraw()
practice.mainloop()