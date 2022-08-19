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

trial=Tk()
trial.title("Login Page")
trial.geometry("800x600+300+50")

C1 = Canvas(trial, width=800, height=600)

C1.create_text(420, 110, text="LOGIN", font=("Bradley hand ITC",29,"bold"), fill="black")
C1.create_text(420, 310, text="LOGIN1", font=("Arial Rounded MT Bold",29,"bold"), fill="black")

C1.pack(expand=True)
trial.mainloop()