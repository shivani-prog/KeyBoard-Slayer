from tkinter import *    
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import random
import os
import sys

fb=("Arial Rounded MT Bold",29,"normal")
fc=("Arial", 18, "normal")
fd=("Arial Rounded MT", 20, "bold")

def f6():
	option.destroy()
	os.system('python login.py')

def f8():
	option.destroy()
	os.system('python practice.py')

def f11():
	option.destroy()
	os.system('python progress.py')

def f14():
	option.destroy()
	os.system('python profile.py')

def f16():
	option.destroy()
	os.system('python Test.py')


option=Tk()
option.title("Option page")
option.geometry("800x600+300+50")

wall = PhotoImage(file="Images/option.png")
wall2 = PhotoImage(file="Images/grey.png")
C3 = Canvas(option,bg="White",width=800, height=600)
C3.create_image(535, 300, image=wall2)
C3.create_image(130, 300, image=wall)
C3.create_text(535, 60, text="~~~ INSTRUCTIONS ~~~", font=("Monotype Corsiva",20,"bold"), fill="magenta4")

btn_progress=Button(option,text="Progress",width=10,font=fd,command=f11)
btn_profile=Button(option,text="Profile",width=10,font=fd, command=f14)
btn_ttest=Button(option,text="Take Test",width=10,font=fd,command=f16)
btn_ptest=Button(option,text="Practice",width=10,font=fd,command=f8)
scrol=ScrolledText(option,width=46,height=20,font=("Times New Roman",15),wrap=WORD)

scrol.insert("insert",'''USER’S  NOTE:-
Dear User, KEYBOARD SLAYER is a platform where you can increase your Typing Speed. We have tried our best to create a proper interface between you and the platform. Before you move ahead please read the following instructions this might be useful for you:-
Important points:-
1) The test would be only for 60 sec, if user fails to submit the typed text then it will would be submitted automatically.\n
2) Whatever you have typed during test session would be examined by the platform and user would be provided with the speed , accuracy and rank.\n
3) The paragraph for typing would be randomly allotted to user , the paragraph would differ from test to test.\n
4) There are two options provided to the user one is to Take test and the second is for practice test, If chooses Take Test , then user would be ranked otherwise in practice test user is not ranked he/she can practice as mush they want.\n
5) There is dashboard available for the user to see his/her rank as well as other user’s ranks.\n
6) A progress bar is available for the user where user can see his/her day to day progress in his typing speed as well as a proper pictorial graph would make easier for the user to evaluate his /her performance.
______________________________________________\n
"PRACTICE MAKES PERFECT.AFTER LONG TIME OF PRACTICE OUR PERFORMANCE WOULD BECOME NATURAL, SKILLFULL, SWIFT AND STEAD"\n\t -----BRUCE LEE-----
______________________________________________\n

Thank you, for selecting this platform for increasing your keyboard typing speed, hopefully this platform helps you to achieve your goals.
  
Yours  Sincerely
Team KeyboardSlayer\n''')

scrol.config(state=DISABLED)
btn_back=Button(option,text="Back",width=10,font=fd,command=f6)
btn_profile.place(x=40,y=80)
btn_ptest.place(x=40,y=180)
btn_ttest.place(x=40,y=280)
btn_progress.place(x=40,y=380)
btn_back.place(x=40,y=480)

scrol.place(x=300,y=90)
C3.pack(expand=True)
option.mainloop()
