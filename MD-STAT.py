import tkinter as tk
import tkinter.font as tkFont
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from pandas import DataFrame
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import math
from math import *

count = 0
li = list()
companynames = list()
il = list()

varmean = list()
varmeansquare = list()


class Window1:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master


        fontStyle = tkFont.Font(family="Lucida Grande", size=25)

        self.btn1 = tk.Button(self.master, text ="DESCRIPTIVE STATISTICS", font = fontStyle, command = self.load_new1)
        self.btn1.place(relx = 0.5, rely = 0.10, anchor = CENTER)

        self.btn2 = tk.Button(self.master, text ="PIE-CHART", font = fontStyle, command = self.load_new2)
        self.btn2.place(relx = 0.5, rely = 0.25, anchor = CENTER)

        self.btn3 = tk.Button(self.master, text ="BAR-CHART", font = fontStyle, command = self.load_new3)
        self.btn3.place(relx = 0.5, rely = 0.40, anchor = CENTER)

    def load_new1(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()

        # use `root` with another class
        self.another = Descriptive(self.master)
        
    def load_new2(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()

        # use `root` with another class
        self.another = Piechart(self.master)
    def load_new3(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()

        # use `root` with another class
        self.another = Barchart(self.master)


class Descriptive:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master
        
        fontStyle = tkFont.Font(family="Lucida Grande", size=25)
        fontStyle1 = tkFont.Font(family="Lucida Grande", size=13)
        
        self.btn1 = tk.Button(self.master, text ="MEASURE OF CENTRAL TENDENCY", font = fontStyle, command = self.load_measureofcentraltendency)
        self.btn1.place(relx = 0.5, rely = 0.10, anchor = CENTER)

        self.btn2 = tk.Button(self.master, text ="MEASURE OF DISPERSION", font = fontStyle, command = self.load_measureofdispersion)
        self.btn2.place(relx = 0.5, rely = 0.25, anchor = CENTER)

        self.btn3=tk.Button(self.master, text="HOME", font= fontStyle1, command= self.load_home)
        self.btn3.place(relx = 0.90, rely = 0.90, anchor = CENTER)

        self.btn4 = tk.Button(self.master, text ="BACK", font = fontStyle1, command = self.load_back)
        self.btn4.place(relx = 0.90, rely = 0.84, anchor = CENTER)


    def load_measureofcentraltendency(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.another = Measureofcentraltendency(self.master)
    def load_measureofdispersion(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.another = Measureofdispersion(self.master)
    def load_home(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.another = Window1(self.master)
    def load_back(self):
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        self.btn4.destroy()
        self.another = Window1(self.master)
    
class Measureofdispersion:
    
    def __init__(self, master):
           

        # keep `root` in `self.master`
        self.master = master

        variance = tk.StringVar()
        standarddeviation = tk.StringVar()
        ranGe = tk.StringVar()

        fontStyle = tkFont.Font(family="Lucida Grande", size=13)
        fontStyle1 = tkFont.Font(family="Lucida Grande", size=13)

        
        
        self.label1 = Label(self.master, text="Company", font = fontStyle)
        self.label1.grid(column=0, row = 0, )
        self.label2 = Label(self.master, text="Sales(Naira)", font = fontStyle)
        self.label2.grid(column=1, row = 0)
        self.label3 = Label(self.master, text="Variance:", font = fontStyle)
        self.label3.grid(row=4, column = 3)
        self.label4= Label(self.master, text="", textvariable=variance, font = fontStyle)
        self.label4.grid(row=4, column=4)
        self.label5= Label(self.master, text="Standard Deviation:", font = fontStyle)
        self.label5.grid(row=5, column = 3)
        self.label6= Label(self.master, text="", textvariable=standarddeviation, font = fontStyle)
        self.label6.grid(row=5, column=4)

        self.label7= Label(self.master, text="Range:", font = fontStyle)
        self.label7.grid(row=6, column = 3)
        self.label8= Label(self.master, text="", textvariable=ranGe, font = fontStyle)
        self.label8.grid(row=6, column=4)
        

        def clearFunc():
            li.clear()
            companynames.clear()
            varmean.clear()
            varmeansquare.clear()
            
            variance.set("")
            standarddeviation.set("")
            ranGe.set("")

        self.Reset=tk.Button(self.master, text="Reset",command=clearFunc, font = fontStyle)
        self.Reset.grid(row=9, column=2, columnspan=2, rowspan=9,padx=80)



        self.entry_1 = Entry(self.master)
        self.entry_2 = Entry(self.master)
        self.entry_3 = Entry(self.master)
        self.entry_4 = Entry(self.master)
        self.entry_5 = Entry(self.master)
        self.entry_6 = Entry(self.master)
        self.entry_7 = Entry(self.master)
        self.entry_8 = Entry(self.master)
        self.entry_9 = Entry(self.master)
        self.entry_10 = Entry(self.master)
        self.entry_11 = Entry(self.master)
        self.entry_12 = Entry(self.master)
        self.entry_13 = Entry(self.master)
        self.entry_14 = Entry(self.master)
        self.entry_15 = Entry(self.master)
        self.entry_16 = Entry(self.master)
        self.entry_17 = Entry(self.master)
        self.entry_18 = Entry(self.master)
        self.entry_19 = Entry(self.master)
        self.entry_20 = Entry(self.master)
        self.entry_21 = Entry(self.master)
        self.entry_22 = Entry(self.master)
        self.entry_23 = Entry(self.master)
        self.entry_24 = Entry(self.master)
        self.entry_25 = Entry(self.master)
        self.entry_26 = Entry(self.master)
        self.entry_27 = Entry(self.master)
        self.entry_28 = Entry(self.master)
        self.entry_29 = Entry(self.master)
        self.entry_30 = Entry(self.master)
        self.entry_31 = Entry(self.master)
        self.entry_32 = Entry(self.master)
        self.entry_33 = Entry(self.master)
        self.entry_34 = Entry(self.master)
        self.entry_35 = Entry(self.master)
        self.entry_36 = Entry(self.master)
        self.entry_37 = Entry(self.master)
        self.entry_38 = Entry(self.master)
        self.entry_39 = Entry(self.master)
        self.entry_40 = Entry(self.master)

        self.entry_1.grid(row=1, column=0, ipady=5, ipadx=10)
        self.entry_2.grid(row=1, column=1, ipady=5, ipadx=10)
        self.entry_3.grid(row=2, column=0, ipady=5, ipadx=10)
        self.entry_4.grid(row=2, column=1, ipady=5, ipadx=10)
        self.entry_5.grid(row=3, column=0, ipady=5, ipadx=10)
        self.entry_6.grid(row=3, column=1, ipady=5, ipadx=10)
        self.entry_7.grid(row=4, column=0, ipady=5, ipadx=10)
        self.entry_8.grid(row=4, column=1, ipady=5, ipadx=10)
        self.entry_9.grid(row=5, column=0, ipady=5, ipadx=10)
        self.entry_10.grid(row=5, column=1, ipady=5, ipadx=10)
        self.entry_11.grid(row=6, column=0, ipady=5, ipadx=10)
        self.entry_12.grid(row=6, column=1, ipady=5, ipadx=10)
        self.entry_13.grid(row=7, column=0, ipady=5, ipadx=10)
        self.entry_14.grid(row=7, column=1, ipady=5, ipadx=10)
        self.entry_15.grid(row=8, column=0, ipady=5, ipadx=10)
        self.entry_16.grid(row=8, column=1, ipady=5, ipadx=10)
        self.entry_17.grid(row=9, column=0, ipady=5, ipadx=10)
        self.entry_18.grid(row=9, column=1, ipady=5, ipadx=10)
        self.entry_19.grid(row=10, column=0, ipady=5, ipadx=10)
        self.entry_20.grid(row=10, column=1, ipady=5, ipadx=10)
        self.entry_21.grid(row=11, column=0, ipady=5, ipadx=10)
        self.entry_22.grid(row=11, column=1, ipady=5, ipadx=10)
        self.entry_23.grid(row=12, column=0, ipady=5, ipadx=10)
        self.entry_24.grid(row=12, column=1, ipady=5, ipadx=10)
        self.entry_25.grid(row=13, column=0, ipady=5, ipadx=10)
        self.entry_26.grid(row=13, column=1, ipady=5, ipadx=10)
        self.entry_27.grid(row=14, column=0, ipady=5, ipadx=10)
        self.entry_28.grid(row=14, column=1, ipady=5, ipadx=10)
        self.entry_29.grid(row=15, column=0, ipady=5, ipadx=10)
        self.entry_30.grid(row=15, column=1, ipady=5, ipadx=10)
        self.entry_31.grid(row=16, column=0, ipady=5, ipadx=10)
        self.entry_32.grid(row=16, column=1, ipady=5, ipadx=10)
        self.entry_33.grid(row=17, column=0, ipady=5, ipadx=10)
        self.entry_34.grid(row=17, column=1, ipady=5, ipadx=10)
        self.entry_35.grid(row=18, column=0, ipady=5, ipadx=10)
        self.entry_36.grid(row=18, column=1, ipady=5, ipadx=10)
        self.entry_37.grid(row=19, column=0, ipady=5, ipadx=10)
        self.entry_38.grid(row=19, column=1, ipady=5, ipadx=10)
        self.entry_39.grid(row=20, column=0, ipady=5, ipadx=10)
        self.entry_40.grid(row=20, column=1, ipady=5, ipadx=10)
        def add():
            no1 = (self.entry_1.get())
            companynames.append(no1)
            no2 = (self.entry_2.get())
            try:
                two = float(no2)
                li.append(two)
            except:
                il.append(no2)
            no3 = (self.entry_3.get())
            companynames.append(no3)
            no4 = (self.entry_4.get())
            try:
                four = float(no4)
                li.append(four)
            except:
                il.append(no4)
            no5 = (self.entry_5.get())
            companynames.append(no5)
            no6 = (self.entry_6.get())
            try:
                six = float(no6)
                li.append(six)
            except:
                il.append(no6)
            no7 = (self.entry_7.get())
            companynames.append(no7)
            no8 = (self.entry_8.get())
            try:
                eight = float(no8)
                li.append(eight)
            except:
                il.append(no8)
            no9 = (self.entry_9.get())
            companynames.append(no9)
            no10 = (self.entry_10.get())
            try:
                ten = float(no10)
                li.append(ten)
            except:
                il.append(no10)
            no11 = (self.entry_11.get())
            companynames.append(no11)
            no12 = (self.entry_12.get())
            try:
                twelve = float(no12)
                li.append(twelve)
            except:
                il.append(no12)
            no13 = (self.entry_13.get())
            companynames.append(no13)
            no14 = (self.entry_14.get())
            try:
                fourteen = float(no14)
                li.append(fourteen)
            except:
                il.append(no14)
            no15 = (self.entry_15.get())
            companynames.append(no15)
            no16 = (self.entry_16.get())
            try:
                sixteen = float(no16)
                li.append(sixteen)
            except:
                il.append(no16)
            no17 = (self.entry_17.get())
            companynames.append(no17)
            no18 = (self.entry_18.get())
            try:
                eighteen = float(no18)
                li.append(eighteen)
            except:
                il.append(no18)
            no19 = (self.entry_19.get())
            companynames.append(no19)
            no20 = (self.entry_20.get())
            try:
                twenty = float(no20)
                li.append(twenty)
            except:
                il.append(no20)
            no21 = (self.entry_21.get())
            companynames.append(no21)
            no22 = (self.entry_22.get())
            try:
                two2 = float(no22)
                li.append(two2)
            except:
                il.append(no22)
            no23 = (self.entry_23.get())
            companynames.append(no23)
            no24 = (self.entry_24.get())
            try:
                four2 = float(no24)
                li.append(four2)
            except:
                il.append(no24)
            no25 = (self.entry_25.get())
            companynames.append(no25)
            no26 = (self.entry_26.get())
            try:
                six2 = float(no26)
                li.append(six2)
            except:
                il.append(no26)
            no27 = (self.entry_27.get())
            companynames.append(no27)
            no28 = (self.entry_28.get())
            try:
                eight2 = float(no28)
                li.append(eight2)
            except:
                il.append(no28)
            no29 = (self.entry_29.get())
            companynames.append(no29)
            no30 = (self.entry_30.get())
            try:
                ten3 = float(no30)
                li.append(ten3)
            except:
                il.append(no30)
            no31 = (self.entry_31.get())
            companynames.append(no31)
            no32 = (self.entry_32.get())
            try:
                twelve3 = float(no32)
                li.append(twelve3)
            except:
                il.append(no32)
            no33 = (self.entry_33.get())
            companynames.append(no33)
            no34 = (self.entry_34.get())
            try:
                fourteen3 = float(no34)
                li.append(fourteen3)
            except:
                il.append(no34)
            no35 = (self.entry_35.get())
            companynames.append(no35)
            no36 = (self.entry_36.get())
            try:
                sixteen3 = float(no36)
                li.append(sixteen3)
            except:
                il.append(no36)
            no37 = (self.entry_37.get())
            companynames.append(no37)
            no38 = (self.entry_38.get())
            try:
                eighteen3 = float(no38)
                li.append(eighteen3)
            except:
                il.append(no38)
            no39 = (self.entry_39.get())
            companynames.append(no39)
            no40 = (self.entry_40.get())
            try:
                twenty4 = float(no40)
                li.append(twenty4)
            except:
                il.append(no40)

            count = 0
            for i in li:
                count = count + i
            mean = count/len(li)

            for o in li:
                s = o - mean
                varmean.append(s)
                k = sum(varmean)

            for w in varmean:
                q = w * w
                varmeansquare.append(q)
            print(mean)
            m = sum(varmeansquare)
            n = len(li)

            variancee = m/(n - 1)
            std = round(math.sqrt(variancee), 4)

            rangee = max(li) - min(li)

            variance.set(variancee)
            standarddeviation.set(std)
            ranGe.set(rangee)
            print("var:", variancee)
            print("Stdev: ", std)
            print("Range: ", rangee)

        self.btn1=tk.Button(self.master, text="Analyse", command=add, font = fontStyle)
        self.btn1.grid(row=8, column=2, columnspan=2, rowspan=8,padx=80)

        self.btn2=tk.Button(self.master, text="HOME", font= fontStyle1, command= self.load_home)
        self.btn2.place(relx = 0.90, rely = 0.90, anchor = CENTER)

        self.btn3 = tk.Button(self.master, text ="BACK", font = fontStyle1, command = self.load_back)
        self.btn3.place(relx = 0.90, rely = 0.84, anchor = CENTER)

    def load_home(self):
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.label6.destroy()
        self.label7.destroy()
        self.label8.destroy()
        self.Reset.destroy()
        self.entry_1.destroy()
        self.entry_2.destroy()
        self.entry_3.destroy()
        self.entry_4.destroy()
        self.entry_5.destroy()
        self.entry_6.destroy()
        self.entry_7.destroy()
        self.entry_8.destroy()
        self.entry_9.destroy()
        self.entry_10.destroy()
        self.entry_11.destroy()
        self.entry_12.destroy()
        self.entry_13.destroy()
        self.entry_14.destroy()
        self.entry_15.destroy()
        self.entry_16.destroy()
        self.entry_17.destroy()
        self.entry_18.destroy()
        self.entry_19.destroy()
        self.entry_20.destroy()
        self.entry_21.destroy()
        self.entry_22.destroy()
        self.entry_23.destroy()
        self.entry_24.destroy()
        self.entry_25.destroy()
        self.entry_26.destroy()
        self.entry_27.destroy()
        self.entry_28.destroy()
        self.entry_29.destroy()
        self.entry_30.destroy()
        self.entry_31.destroy()
        self.entry_32.destroy()
        self.entry_33.destroy()
        self.entry_34.destroy()
        self.entry_35.destroy()
        self.entry_36.destroy()
        self.entry_37.destroy()
        self.entry_38.destroy()
        self.entry_39.destroy()
        self.entry_40.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()

        self.another = Window1(self.master)
    def load_back(self):
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.label6.destroy()
        self.label7.destroy()
        self.label8.destroy()
        self.Reset.destroy()
        self.entry_1.destroy()
        self.entry_2.destroy()
        self.entry_3.destroy()
        self.entry_4.destroy()
        self.entry_5.destroy()
        self.entry_6.destroy()
        self.entry_7.destroy()
        self.entry_8.destroy()
        self.entry_9.destroy()
        self.entry_10.destroy()
        self.entry_11.destroy()
        self.entry_12.destroy()
        self.entry_13.destroy()
        self.entry_14.destroy()
        self.entry_15.destroy()
        self.entry_16.destroy()
        self.entry_17.destroy()
        self.entry_18.destroy()
        self.entry_19.destroy()
        self.entry_20.destroy()
        self.entry_21.destroy()
        self.entry_22.destroy()
        self.entry_23.destroy()
        self.entry_24.destroy()
        self.entry_25.destroy()
        self.entry_26.destroy()
        self.entry_27.destroy()
        self.entry_28.destroy()
        self.entry_29.destroy()
        self.entry_30.destroy()
        self.entry_31.destroy()
        self.entry_32.destroy()
        self.entry_33.destroy()
        self.entry_34.destroy()
        self.entry_35.destroy()
        self.entry_36.destroy()
        self.entry_37.destroy()
        self.entry_38.destroy()
        self.entry_39.destroy()
        self.entry_40.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        
        self.another = Descriptive(self.master)

        

class Measureofcentraltendency:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master
        fontStyle = tkFont.Font(family="Lucida Grande", size=13)
        fontStyle1 = tkFont.Font(family="Lucida Grande", size=13)

        total = tk.StringVar()
        mean = tk.StringVar()
        median = tk.StringVar()
        mode = tk.StringVar()
        
        self.label1 = Label(self.master, text="Company", font = fontStyle)
        self.label1.grid(column=0, row = 0)
        self.label2 = Label(self.master, text="Sales(Naira)", font = fontStyle)
        self.label2.grid(column=1, row = 0)

        self.label3 = Label(self.master, text="Total:", font = fontStyle)
        self.label3.grid(row=4, column = 3)
        self.label4= Label(self.master, text="", textvariable=total, font = fontStyle)
        self.label4.grid(row=4, column=4)

        self.label5 = Label(self.master, text="Mean:", font = fontStyle)
        self.label5.grid(row=5, column = 3)
        self.label6 = Label(self.master, text="", textvariable=mean, font = fontStyle)
        self.label6.grid(row=5, column=4)

        self.label7 = Label(self.master, text="Median:", font = fontStyle)
        self.label7.grid(row=6, column = 3)
        self.label8 = Label(self.master, text="", textvariable=median, font = fontStyle)
        self.label8.grid(row=6, column=4)

        self.label9 = Label(self.master, text="Mode:", font = fontStyle)
        self.label9.grid(row=7, column = 3)
        self.label10 = Label(self.master, text="", textvariable=mode, font = fontStyle)
        self.label10.grid(row=7, column=4)


        
        def clearFunc():
            li.clear()
            companynames.clear()
            total.set("")
            mean.set("")
            median.set("")
            mode.set("")

        self.Reset=tk.Button(self.master, text="Reset",command=clearFunc, font = fontStyle)
        self.Reset.grid(row=9, column=2, columnspan=2, rowspan=9,padx=80)


        self.entry_1 = Entry(self.master)
        self.entry_2 = Entry(self.master)
        self.entry_3 = Entry(self.master)
        self.entry_4 = Entry(self.master)
        self.entry_5 = Entry(self.master)
        self.entry_6 = Entry(self.master)
        self.entry_7 = Entry(self.master)
        self.entry_8 = Entry(self.master)
        self.entry_9 = Entry(self.master)
        self.entry_10 = Entry(self.master)
        self.entry_11 = Entry(self.master)
        self.entry_12 = Entry(self.master)
        self.entry_13 = Entry(self.master)
        self.entry_14 = Entry(self.master)
        self.entry_15 = Entry(self.master)
        self.entry_16 = Entry(self.master)
        self.entry_17 = Entry(self.master)
        self.entry_18 = Entry(self.master)
        self.entry_19 = Entry(self.master)
        self.entry_20 = Entry(self.master)
        self.entry_21 = Entry(self.master)
        self.entry_22 = Entry(self.master)
        self.entry_23 = Entry(self.master)
        self.entry_24 = Entry(self.master)
        self.entry_25 = Entry(self.master)
        self.entry_26 = Entry(self.master)
        self.entry_27 = Entry(self.master)
        self.entry_28 = Entry(self.master)
        self.entry_29 = Entry(self.master)
        self.entry_30 = Entry(self.master)
        self.entry_31 = Entry(self.master)
        self.entry_32 = Entry(self.master)
        self.entry_33 = Entry(self.master)
        self.entry_34 = Entry(self.master)
        self.entry_35 = Entry(self.master)
        self.entry_36 = Entry(self.master)
        self.entry_37 = Entry(self.master)
        self.entry_38 = Entry(self.master)
        self.entry_39 = Entry(self.master)
        self.entry_40 = Entry(self.master)

        self.entry_1.grid(row=1, column=0, ipady=5, ipadx=10)
        self.entry_2.grid(row=1, column=1, ipady=5, ipadx=10)
        self.entry_3.grid(row=2, column=0, ipady=5, ipadx=10)
        self.entry_4.grid(row=2, column=1, ipady=5, ipadx=10)
        self.entry_5.grid(row=3, column=0, ipady=5, ipadx=10)
        self.entry_6.grid(row=3, column=1, ipady=5, ipadx=10)
        self.entry_7.grid(row=4, column=0, ipady=5, ipadx=10)
        self.entry_8.grid(row=4, column=1, ipady=5, ipadx=10)
        self.entry_9.grid(row=5, column=0, ipady=5, ipadx=10)
        self.entry_10.grid(row=5, column=1, ipady=5, ipadx=10)
        self.entry_11.grid(row=6, column=0, ipady=5, ipadx=10)
        self.entry_12.grid(row=6, column=1, ipady=5, ipadx=10)
        self.entry_13.grid(row=7, column=0, ipady=5, ipadx=10)
        self.entry_14.grid(row=7, column=1, ipady=5, ipadx=10)
        self.entry_15.grid(row=8, column=0, ipady=5, ipadx=10)
        self.entry_16.grid(row=8, column=1, ipady=5, ipadx=10)
        self.entry_17.grid(row=9, column=0, ipady=5, ipadx=10)
        self.entry_18.grid(row=9, column=1, ipady=5, ipadx=10)
        self.entry_19.grid(row=10, column=0, ipady=5, ipadx=10)
        self.entry_20.grid(row=10, column=1, ipady=5, ipadx=10)
        self.entry_21.grid(row=11, column=0, ipady=5, ipadx=10)
        self.entry_22.grid(row=11, column=1, ipady=5, ipadx=10)
        self.entry_23.grid(row=12, column=0, ipady=5, ipadx=10)
        self.entry_24.grid(row=12, column=1, ipady=5, ipadx=10)
        self.entry_25.grid(row=13, column=0, ipady=5, ipadx=10)
        self.entry_26.grid(row=13, column=1, ipady=5, ipadx=10)
        self.entry_27.grid(row=14, column=0, ipady=5, ipadx=10)
        self.entry_28.grid(row=14, column=1, ipady=5, ipadx=10)
        self.entry_29.grid(row=15, column=0, ipady=5, ipadx=10)
        self.entry_30.grid(row=15, column=1, ipady=5, ipadx=10)
        self.entry_31.grid(row=16, column=0, ipady=5, ipadx=10)
        self.entry_32.grid(row=16, column=1, ipady=5, ipadx=10)
        self.entry_33.grid(row=17, column=0, ipady=5, ipadx=10)
        self.entry_34.grid(row=17, column=1, ipady=5, ipadx=10)
        self.entry_35.grid(row=18, column=0, ipady=5, ipadx=10)
        self.entry_36.grid(row=18, column=1, ipady=5, ipadx=10)
        self.entry_37.grid(row=19, column=0, ipady=5, ipadx=10)
        self.entry_38.grid(row=19, column=1, ipady=5, ipadx=10)
        self.entry_39.grid(row=20, column=0, ipady=5, ipadx=10)
        self.entry_40.grid(row=20, column=1, ipady=5, ipadx=10)
        def add():
            no1 = (self.entry_1.get())
            companynames.append(no1)
            no2 = (self.entry_2.get())
            try:
                two = float(no2)
                li.append(two)
            except:
                il.append(no2)
            no3 = (self.entry_3.get())
            companynames.append(no3)
            no4 = (self.entry_4.get())
            try:
                four = float(no4)
                li.append(four)
            except:
                il.append(no4)
            no5 = (self.entry_5.get())
            companynames.append(no5)
            no6 = (self.entry_6.get())
            try:
                six = float(no6)
                li.append(six)
            except:
                il.append(no6)
            no7 = (self.entry_7.get())
            companynames.append(no7)
            no8 = (self.entry_8.get())
            try:
                eight = float(no8)
                li.append(eight)
            except:
                il.append(no8)
            no9 = (self.entry_9.get())
            companynames.append(no9)
            no10 = (self.entry_10.get())
            try:
                ten = float(no10)
                li.append(ten)
            except:
                il.append(no10)
            no11 = (self.entry_11.get())
            companynames.append(no11)
            no12 = (self.entry_12.get())
            try:
                twelve = float(no12)
                li.append(twelve)
            except:
                il.append(no12)
            no13 = (self.entry_13.get())
            companynames.append(no13)
            no14 = (self.entry_14.get())
            try:
                fourteen = float(no14)
                li.append(fourteen)
            except:
                il.append(no14)
            no15 = (self.entry_15.get())
            companynames.append(no15)
            no16 = (self.entry_16.get())
            try:
                sixteen = float(no16)
                li.append(sixteen)
            except:
                il.append(no16)
            no17 = (self.entry_17.get())
            companynames.append(no17)
            no18 = (self.entry_18.get())
            try:
                eighteen = float(no18)
                li.append(eighteen)
            except:
                il.append(no18)
            no19 = (self.entry_19.get())
            companynames.append(no19)
            no20 = (self.entry_20.get())
            try:
                twenty = float(no20)
                li.append(twenty)
            except:
                il.append(no20)
            no21 = (self.entry_21.get())
            companynames.append(no21)
            no22 = (self.entry_22.get())
            try:
                two2 = float(no22)
                li.append(two2)
            except:
                il.append(no22)
            no23 = (self.entry_23.get())
            companynames.append(no23)
            no24 = (self.entry_24.get())
            try:
                four2 = float(no24)
                li.append(four2)
            except:
                il.append(no24)
            no25 = (self.entry_25.get())
            companynames.append(no25)
            no26 = (self.entry_26.get())
            try:
                six2 = float(no26)
                li.append(six2)
            except:
                il.append(no26)
            no27 = (self.entry_27.get())
            companynames.append(no27)
            no28 = (self.entry_28.get())
            try:
                eight2 = float(no28)
                li.append(eight2)
            except:
                il.append(no28)
            no29 = (self.entry_29.get())
            companynames.append(no29)
            no30 = (self.entry_30.get())
            try:
                ten3 = float(no30)
                li.append(ten3)
            except:
                il.append(no30)
            no31 = (self.entry_31.get())
            companynames.append(no31)
            no32 = (self.entry_32.get())
            try:
                twelve3 = float(no32)
                li.append(twelve3)
            except:
                il.append(no32)
            no33 = (self.entry_33.get())
            companynames.append(no33)
            no34 = (self.entry_34.get())
            try:
                fourteen3 = float(no34)
                li.append(fourteen3)
            except:
                il.append(no34)
            no35 = (self.entry_35.get())
            companynames.append(no35)
            no36 = (self.entry_36.get())
            try:
                sixteen3 = float(no36)
                li.append(sixteen3)
            except:
                il.append(no36)
            no37 = (self.entry_37.get())
            companynames.append(no37)
            no38 = (self.entry_38.get())
            try:
                eighteen3 = float(no38)
                li.append(eighteen3)
            except:
                il.append(no38)
            no39 = (self.entry_39.get())
            companynames.append(no39)
            no40 = (self.entry_40.get())
            try:
                twenty4 = float(no40)
                li.append(twenty4)
            except:
                il.append(no40)

            sorted_li = sorted(li)
            print(sorted_li)
            print(li)
            print(companynames)
            print(len(li))
            print(il)

            count = 0
            for re in li:
                count = count + re
                modecount = li.count(re)
                if modecount != 1:
                    modee = re
                    mode.set(modee)
                else:
                    modee2 = "No mode for the given data, each data appears once"
                    mode.set(modee2)
            mea = count/(len(li))
            median1 = ((len(li)) + 1) / 2
            median2 = int(median1)
            median4 = str(median2)
            if median1 >1.0 and median1<2.0:
                medianreal1 = ((sorted_li[0] + sorted_li[1]) / 2)
                median.set(medianreal1)
            elif median1 == 1.0:
                medianreal11 = int(sorted_li[0])
                median.set(medianreal11)
            elif median1 >2.0 and median1<3.0:
                medianreal2 = ((sorted_li[1] + sorted_li[2]) / 2)
                median.set(medianreal2)
            elif median1 == 2.0:
                medianreal22 = int(sorted_li[1])
                median.set(medianreal22)
            elif median1>3.0 and median1<4.0:
                medianreal3 = ((sorted_li[2] + sorted_li[3]) / 2)
                median.set(medianreal3)
            elif median1 == 3.0:
                medianreal33 = int(sorted_li[2])
                median.set(medianreal33)
            elif median1 > 4.0 and median1<5.0:
                medianreal4 = ((sorted_li[3] + sorted_li[4]) / 2)
                median.set(medianreal4)
            elif median1 == 4.0:
                medianreal44 = int(sorted_li[3])
                median.set(medianreal44)
            elif median1 >5.0 and median1<6.0:
                medianreal5 = ((sorted_li[4] + sorted_li[5]) / 2)
                median.set(medianreal5)
            elif median1 == 5.0:
                medianreal55 = int(sorted_li[4])
                median.set(medianreal55)
            elif median1 >6.0 and median1<7.0:
                medianreal6 = ((sorted_li[5] + sorted_li[6]) / 2)
                median.set(medianreal6)
            elif median1 == 6.0:
                medianreal66 = int(sorted_li[5])
                median.set(medianreal66)
            elif median1 >7.0 and median1<8.0:
                medianreal7 = ((sorted_li[6] + sorted_li[7]) / 2)
                median.set(medianreal7)
            elif median1 == 7.0:
                medianreal77 = int(sorted_li[6])
                median.set(medianreal77)
            elif median1>8.0 and median1<9.0:
                medianreal8 = ((sorted_li[7] + sorted_li[8]) / 2)
                median.set(medianreal8)
            elif median1 == 8.0:
                medianreal88 = int(sorted_li[7])
                median.set(medianreal88)
            elif median1 > 9.0 and median1<10.0:
                medianreal9 = ((sorted_li[8] + sorted_li[9]) / 2)
                median.set(medianreal9)
            elif median1 == 9.0:
                medianreal99 = int(sorted_li[8])
                median.set(medianreal99)
            elif median1 >10.0 and median1<11.0:
                medianreal10 = ((sorted_li[9] + sorted_li[10]) / 2)
                median.set(medianreal10)
            elif median1 == 10.0:
                medianreal1010 = int(sorted_li[9])
                median.set(medianreal1010)

            total.set(count)
            mean.set(mea)
            
        self.btn1=tk.Button(self.master, text="Analyse", command=add, font = fontStyle)
        self.btn1.grid(row=8, column=2, columnspan=2, rowspan=8,padx=80)

        self.btn2=tk.Button(self.master, text="HOME", font= fontStyle1, command= self.load_home)
        self.btn2.place(relx = 0.90, rely = 0.90, anchor = CENTER)

        self.btn3 = tk.Button(self.master, text ="BACK", font = fontStyle1, command = self.load_back)
        self.btn3.place(relx = 0.90, rely = 0.84, anchor = CENTER)

    def load_home(self):
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.label6.destroy()
        self.label7.destroy()
        self.label8.destroy()
        self.label9.destroy()
        self.label10.destroy()
        self.Reset.destroy()
        self.entry_1.destroy()
        self.entry_2.destroy()
        self.entry_3.destroy()
        self.entry_4.destroy()
        self.entry_5.destroy()
        self.entry_6.destroy()
        self.entry_7.destroy()
        self.entry_8.destroy()
        self.entry_9.destroy()
        self.entry_10.destroy()
        self.entry_11.destroy()
        self.entry_12.destroy()
        self.entry_13.destroy()
        self.entry_14.destroy()
        self.entry_15.destroy()
        self.entry_16.destroy()
        self.entry_17.destroy()
        self.entry_18.destroy()
        self.entry_19.destroy()
        self.entry_20.destroy()
        self.entry_21.destroy()
        self.entry_22.destroy()
        self.entry_23.destroy()
        self.entry_24.destroy()
        self.entry_25.destroy()
        self.entry_26.destroy()
        self.entry_27.destroy()
        self.entry_28.destroy()
        self.entry_29.destroy()
        self.entry_30.destroy()
        self.entry_31.destroy()
        self.entry_32.destroy()
        self.entry_33.destroy()
        self.entry_34.destroy()
        self.entry_35.destroy()
        self.entry_36.destroy()
        self.entry_37.destroy()
        self.entry_38.destroy()
        self.entry_39.destroy()
        self.entry_40.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()

        self.another = Window1(self.master)
    def load_back(self):
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.label4.destroy()
        self.label5.destroy()
        self.label6.destroy()
        self.label7.destroy()
        self.label8.destroy()
        self.label9.destroy()
        self.label10.destroy()
        self.Reset.destroy()
        self.entry_1.destroy()
        self.entry_2.destroy()
        self.entry_3.destroy()
        self.entry_4.destroy()
        self.entry_5.destroy()
        self.entry_6.destroy()
        self.entry_7.destroy()
        self.entry_8.destroy()
        self.entry_9.destroy()
        self.entry_10.destroy()
        self.entry_11.destroy()
        self.entry_12.destroy()
        self.entry_13.destroy()
        self.entry_14.destroy()
        self.entry_15.destroy()
        self.entry_16.destroy()
        self.entry_17.destroy()
        self.entry_18.destroy()
        self.entry_19.destroy()
        self.entry_20.destroy()
        self.entry_21.destroy()
        self.entry_22.destroy()
        self.entry_23.destroy()
        self.entry_24.destroy()
        self.entry_25.destroy()
        self.entry_26.destroy()
        self.entry_27.destroy()
        self.entry_28.destroy()
        self.entry_29.destroy()
        self.entry_30.destroy()
        self.entry_31.destroy()
        self.entry_32.destroy()
        self.entry_33.destroy()
        self.entry_34.destroy()
        self.entry_35.destroy()
        self.entry_36.destroy()
        self.entry_37.destroy()
        self.entry_38.destroy()
        self.entry_39.destroy()
        self.entry_40.destroy()
        self.btn1.destroy()
        self.btn2.destroy()
        self.btn3.destroy()
        
        self.another = Descriptive(self.master)


        

class Piechart:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master

        fontStyle = tkFont.Font(family="Lucida Grande", size=13)
        self.label = Label(self.master, text="Company", font = fontStyle).grid(column=0, row = 0, )
        self.label = Label(self.master, text="Sales(Naira)", font = fontStyle).grid(column=1, row = 0)


        def clearFunc():
            li.clear()
            companynames.clear()
           

        Reset=tk.Button(self.master, text="Reset",command=clearFunc, font = fontStyle)
        Reset.grid(row=9, column=2, columnspan=2, rowspan=9,padx=80)

        Home=tk.Button(self.master, text="Home", command=lambda: controller.show_frame(StartPage), font= fontStyle)
        Home.grid(row=10, column=2, columnspan=2, rowspan=10,padx=80)


        self.entry_1 = Entry(self.master)
        self.entry_2 = Entry(self.master)
        self.entry_3 = Entry(self.master)
        self.entry_4 = Entry(self.master)
        self.entry_5 = Entry(self.master)
        self.entry_6 = Entry(self.master)
        self.entry_7 = Entry(self.master)
        self.entry_8 = Entry(self.master)
        self.entry_9 = Entry(self.master)
        self.entry_10 = Entry(self.master)
        self.entry_11 = Entry(self.master)
        self.entry_12 = Entry(self.master)
        self.entry_13 = Entry(self.master)
        self.entry_14 = Entry(self.master)
        self.entry_15 = Entry(self.master)
        self.entry_16 = Entry(self.master)
        self.entry_17 = Entry(self.master)
        self.entry_18 = Entry(self.master)
        self.entry_19 = Entry(self.master)
        self.entry_20 = Entry(self.master)
        self.entry_21 = Entry(self.master)
        self.entry_22 = Entry(self.master)
        self.entry_23 = Entry(self.master)
        self.entry_24 = Entry(self.master)
        self.entry_25 = Entry(self.master)
        self.entry_26 = Entry(self.master)
        self.entry_27 = Entry(self.master)
        self.entry_28 = Entry(self.master)
        self.entry_29 = Entry(self.master)
        self.entry_30 = Entry(self.master)
        self.entry_31 = Entry(self.master)
        self.entry_32 = Entry(self.master)
        self.entry_33 = Entry(self.master)
        self.entry_34 = Entry(self.master)
        self.entry_35 = Entry(self.master)
        self.entry_36 = Entry(self.master)
        self.entry_37 = Entry(self.master)
        self.entry_38 = Entry(self.master)
        self.entry_39 = Entry(self.master)
        self.entry_40 = Entry(self.master)

        self.entry_1.grid(row=1, column=0, ipady=5, ipadx=10)
        self.entry_2.grid(row=1, column=1, ipady=5, ipadx=10)
        self.entry_3.grid(row=2, column=0, ipady=5, ipadx=10)
        self.entry_4.grid(row=2, column=1, ipady=5, ipadx=10)
        self.entry_5.grid(row=3, column=0, ipady=5, ipadx=10)
        self.entry_6.grid(row=3, column=1, ipady=5, ipadx=10)
        self.entry_7.grid(row=4, column=0, ipady=5, ipadx=10)
        self.entry_8.grid(row=4, column=1, ipady=5, ipadx=10)
        self.entry_9.grid(row=5, column=0, ipady=5, ipadx=10)
        self.entry_10.grid(row=5, column=1, ipady=5, ipadx=10)
        self.entry_11.grid(row=6, column=0, ipady=5, ipadx=10)
        self.entry_12.grid(row=6, column=1, ipady=5, ipadx=10)
        self.entry_13.grid(row=7, column=0, ipady=5, ipadx=10)
        self.entry_14.grid(row=7, column=1, ipady=5, ipadx=10)
        self.entry_15.grid(row=8, column=0, ipady=5, ipadx=10)
        self.entry_16.grid(row=8, column=1, ipady=5, ipadx=10)
        self.entry_17.grid(row=9, column=0, ipady=5, ipadx=10)
        self.entry_18.grid(row=9, column=1, ipady=5, ipadx=10)
        self.entry_19.grid(row=10, column=0, ipady=5, ipadx=10)
        self.entry_20.grid(row=10, column=1, ipady=5, ipadx=10)
        self.entry_21.grid(row=11, column=0, ipady=5, ipadx=10)
        self.entry_22.grid(row=11, column=1, ipady=5, ipadx=10)
        self.entry_23.grid(row=12, column=0, ipady=5, ipadx=10)
        self.entry_24.grid(row=12, column=1, ipady=5, ipadx=10)
        self.entry_25.grid(row=13, column=0, ipady=5, ipadx=10)
        self.entry_26.grid(row=13, column=1, ipady=5, ipadx=10)
        self.entry_27.grid(row=14, column=0, ipady=5, ipadx=10)
        self.entry_28.grid(row=14, column=1, ipady=5, ipadx=10)
        self.entry_29.grid(row=15, column=0, ipady=5, ipadx=10)
        self.entry_30.grid(row=15, column=1, ipady=5, ipadx=10)
        self.entry_31.grid(row=16, column=0, ipady=5, ipadx=10)
        self.entry_32.grid(row=16, column=1, ipady=5, ipadx=10)
        self.entry_33.grid(row=17, column=0, ipady=5, ipadx=10)
        self.entry_34.grid(row=17, column=1, ipady=5, ipadx=10)
        self.entry_35.grid(row=18, column=0, ipady=5, ipadx=10)
        self.entry_36.grid(row=18, column=1, ipady=5, ipadx=10)
        self.entry_37.grid(row=19, column=0, ipady=5, ipadx=10)
        self.entry_38.grid(row=19, column=1, ipady=5, ipadx=10)
        self.entry_39.grid(row=20, column=0, ipady=5, ipadx=10)
        self.entry_40.grid(row=20, column=1, ipady=5, ipadx=10)
        def piechart():
            no1 = (self.entry_1.get())
            companynames.append(no1)
            no2 = (self.entry_2.get())
            try:
                two = float(no2)
                li.append(two)
            except:
                il.append(no2)
            no3 = (self.entry_3.get())
            companynames.append(no3)
            no4 = (self.entry_4.get())
            try:
                four = float(no4)
                li.append(four)
            except:
                il.append(no4)
            no5 = (self.entry_5.get())
            companynames.append(no5)
            no6 = (self.entry_6.get())
            try:
                six = float(no6)
                li.append(six)
            except:
                il.append(no6)
            no7 = (self.entry_7.get())
            companynames.append(no7)
            no8 = (self.entry_8.get())
            try:
                eight = float(no8)
                li.append(eight)
            except:
                il.append(no8)
            no9 = (self.entry_9.get())
            companynames.append(no9)
            no10 = (self.entry_10.get())
            try:
                ten = float(no10)
                li.append(ten)
            except:
                il.append(no10)
            no11 = (self.entry_11.get())
            companynames.append(no11)
            no12 = (self.entry_12.get())
            try:
                twelve = float(no12)
                li.append(twelve)
            except:
                il.append(no12)
            no13 = (self.entry_13.get())
            companynames.append(no13)
            no14 = (self.entry_14.get())
            try:
                fourteen = float(no14)
                li.append(fourteen)
            except:
                il.append(no14)
            no15 = (self.entry_15.get())
            companynames.append(no15)
            no16 = (self.entry_16.get())
            try:
                sixteen = float(no16)
                li.append(sixteen)
            except:
                il.append(no16)
            no17 = (self.entry_17.get())
            companynames.append(no17)
            no18 = (self.entry_18.get())
            try:
                eighteen = float(no18)
                li.append(eighteen)
            except:
                il.append(no18)
            no19 = (self.entry_19.get())
            companynames.append(no19)
            no20 = (self.entry_20.get())
            try:
                twenty = float(no20)
                li.append(twenty)
            except:
                il.append(no20)
            no21 = (self.entry_21.get())
            companynames.append(no21)
            no22 = (self.entry_22.get())
            try:
                two2 = float(no22)
                li.append(two2)
            except:
                il.append(no22)
            no23 = (self.entry_23.get())
            companynames.append(no23)
            no24 = (self.entry_24.get())
            try:
                four2 = float(no24)
                li.append(four2)
            except:
                il.append(no24)
            no25 = (self.entry_25.get())
            companynames.append(no25)
            no26 = (self.entry_26.get())
            try:
                six2 = float(no26)
                li.append(six2)
            except:
                il.append(no26)
            no27 = (self.entry_27.get())
            companynames.append(no27)
            no28 = (self.entry_28.get())
            try:
                eight2 = float(no28)
                li.append(eight2)
            except:
                il.append(no28)
            no29 = (self.entry_29.get())
            companynames.append(no29)
            no30 = (self.entry_30.get())
            try:
                ten3 = float(no30)
                li.append(ten3)
            except:
                il.append(no30)
            no31 = (self.entry_31.get())
            companynames.append(no31)
            no32 = (self.entry_32.get())
            try:
                twelve3 = float(no32)
                li.append(twelve3)
            except:
                il.append(no32)
            no33 = (self.entry_33.get())
            companynames.append(no33)
            no34 = (self.entry_34.get())
            try:
                fourteen3 = float(no34)
                li.append(fourteen3)
            except:
                il.append(no34)
            no35 = (self.entry_35.get())
            companynames.append(no35)
            no36 = (self.entry_36.get())
            try:
                sixteen3 = float(no36)
                li.append(sixteen3)
            except:
                il.append(no36)
            no37 = (self.entry_37.get())
            companynames.append(no37)
            no38 = (self.entry_38.get())
            try:
                eighteen3 = float(no38)
                li.append(eighteen3)
            except:
                il.append(no38)
            no39 = (self.entry_39.get())
            companynames.append(no39)
            no40 = (self.entry_40.get())
            try:
                twenty4 = float(no40)
                li.append(twenty4)
            except:
                il.append(no40)

            y = np.array(li)
            plt.pie(y, labels = companynames)
            plt.legend()
            o = plt.show()
        
        Pie=tk.Button(self.master, text="Get Pie-Chart",command=piechart, font = fontStyle)
        Pie.grid(row=8, column=2, columnspan=2, rowspan=8,padx=120)


class Barchart:

    def __init__(self, master):

        # keep `root` in `self.master`
        self.master = master
        fontStyle = tkFont.Font(family="Lucida Grande", size=13)

        def clearFunc():
            li.clear()
            companynames.clear()
           

        Reset=tk.Button(self.master, text="Reset",command=clearFunc, font = fontStyle)
        Reset.grid(row=9, column=2, columnspan=2, rowspan=9,padx=80)

        Home=tk.Button(self.master, text="Home", command=lambda: controller.show_frame(StartPage), font= fontStyle)
        Home.grid(row=10, column=2, columnspan=2, rowspan=10,padx=80)

        self.entry_1 = Entry(self.master)
        self.entry_2 = Entry(self.master)
        self.entry_3 = Entry(self.master)
        self.entry_4 = Entry(self.master)
        self.entry_5 = Entry(self.master)
        self.entry_6 = Entry(self.master)
        self.entry_7 = Entry(self.master)
        self.entry_8 = Entry(self.master)
        self.entry_9 = Entry(self.master)
        self.entry_10 = Entry(self.master)
        self.entry_11 = Entry(self.master)
        self.entry_12 = Entry(self.master)
        self.entry_13 = Entry(self.master)
        self.entry_14 = Entry(self.master)
        self.entry_15 = Entry(self.master)
        self.entry_16 = Entry(self.master)
        self.entry_17 = Entry(self.master)
        self.entry_18 = Entry(self.master)
        self.entry_19 = Entry(self.master)
        self.entry_20 = Entry(self.master)
        self.entry_21 = Entry(self.master)
        self.entry_22 = Entry(self.master)
        self.entry_23 = Entry(self.master)
        self.entry_24 = Entry(self.master)
        self.entry_25 = Entry(self.master)
        self.entry_26 = Entry(self.master)
        self.entry_27 = Entry(self.master)
        self.entry_28 = Entry(self.master)
        self.entry_29 = Entry(self.master)
        self.entry_30 = Entry(self.master)
        self.entry_31 = Entry(self.master)
        self.entry_32 = Entry(self.master)
        self.entry_33 = Entry(self.master)
        self.entry_34 = Entry(self.master)
        self.entry_35 = Entry(self.master)
        self.entry_36 = Entry(self.master)
        self.entry_37 = Entry(self.master)
        self.entry_38 = Entry(self.master)
        self.entry_39 = Entry(self.master)
        self.entry_40 = Entry(self.master)

        self.entry_1.grid(row=1, column=0, ipady=5, ipadx=10)
        self.entry_2.grid(row=1, column=1, ipady=5, ipadx=10)
        self.entry_3.grid(row=2, column=0, ipady=5, ipadx=10)
        self.entry_4.grid(row=2, column=1, ipady=5, ipadx=10)
        self.entry_5.grid(row=3, column=0, ipady=5, ipadx=10)
        self.entry_6.grid(row=3, column=1, ipady=5, ipadx=10)
        self.entry_7.grid(row=4, column=0, ipady=5, ipadx=10)
        self.entry_8.grid(row=4, column=1, ipady=5, ipadx=10)
        self.entry_9.grid(row=5, column=0, ipady=5, ipadx=10)
        self.entry_10.grid(row=5, column=1, ipady=5, ipadx=10)
        self.entry_11.grid(row=6, column=0, ipady=5, ipadx=10)
        self.entry_12.grid(row=6, column=1, ipady=5, ipadx=10)
        self.entry_13.grid(row=7, column=0, ipady=5, ipadx=10)
        self.entry_14.grid(row=7, column=1, ipady=5, ipadx=10)
        self.entry_15.grid(row=8, column=0, ipady=5, ipadx=10)
        self.entry_16.grid(row=8, column=1, ipady=5, ipadx=10)
        self.entry_17.grid(row=9, column=0, ipady=5, ipadx=10)
        self.entry_18.grid(row=9, column=1, ipady=5, ipadx=10)
        self.entry_19.grid(row=10, column=0, ipady=5, ipadx=10)
        self.entry_20.grid(row=10, column=1, ipady=5, ipadx=10)
        self.entry_21.grid(row=11, column=0, ipady=5, ipadx=10)
        self.entry_22.grid(row=11, column=1, ipady=5, ipadx=10)
        self.entry_23.grid(row=12, column=0, ipady=5, ipadx=10)
        self.entry_24.grid(row=12, column=1, ipady=5, ipadx=10)
        self.entry_25.grid(row=13, column=0, ipady=5, ipadx=10)
        self.entry_26.grid(row=13, column=1, ipady=5, ipadx=10)
        self.entry_27.grid(row=14, column=0, ipady=5, ipadx=10)
        self.entry_28.grid(row=14, column=1, ipady=5, ipadx=10)
        self.entry_29.grid(row=15, column=0, ipady=5, ipadx=10)
        self.entry_30.grid(row=15, column=1, ipady=5, ipadx=10)
        self.entry_31.grid(row=16, column=0, ipady=5, ipadx=10)
        self.entry_32.grid(row=16, column=1, ipady=5, ipadx=10)
        self.entry_33.grid(row=17, column=0, ipady=5, ipadx=10)
        self.entry_34.grid(row=17, column=1, ipady=5, ipadx=10)
        self.entry_35.grid(row=18, column=0, ipady=5, ipadx=10)
        self.entry_36.grid(row=18, column=1, ipady=5, ipadx=10)
        self.entry_37.grid(row=19, column=0, ipady=5, ipadx=10)
        self.entry_38.grid(row=19, column=1, ipady=5, ipadx=10)
        self.entry_39.grid(row=20, column=0, ipady=5, ipadx=10)
        self.entry_40.grid(row=20, column=1, ipady=5, ipadx=10)
        def barchart():
            no1 = (self.entry_1.get())
            companynames.append(no1)
            no2 = (self.entry_2.get())
            try:
                two = float(no2)
                li.append(two)
            except:
                il.append(no2)
            no3 = (self.entry_3.get())
            companynames.append(no3)
            no4 = (self.entry_4.get())
            try:
                four = float(no4)
                li.append(four)
            except:
                il.append(no4)
            no5 = (self.entry_5.get())
            companynames.append(no5)
            no6 = (self.entry_6.get())
            try:
                six = float(no6)
                li.append(six)
            except:
                il.append(no6)
            no7 = (self.entry_7.get())
            companynames.append(no7)
            no8 = (self.entry_8.get())
            try:
                eight = float(no8)
                li.append(eight)
            except:
                il.append(no8)
            no9 = (self.entry_9.get())
            companynames.append(no9)
            no10 = (self.entry_10.get())
            try:
                ten = float(no10)
                li.append(ten)
            except:
                il.append(no10)
            no11 = (self.entry_11.get())
            companynames.append(no11)
            no12 = (self.entry_12.get())
            try:
                twelve = float(no12)
                li.append(twelve)
            except:
                il.append(no12)
            no13 = (self.entry_13.get())
            companynames.append(no13)
            no14 = (self.entry_14.get())
            try:
                fourteen = float(no14)
                li.append(fourteen)
            except:
                il.append(no14)
            no15 = (self.entry_15.get())
            companynames.append(no15)
            no16 = (self.entry_16.get())
            try:
                sixteen = float(no16)
                li.append(sixteen)
            except:
                il.append(no16)
            no17 = (self.entry_17.get())
            companynames.append(no17)
            no18 = (self.entry_18.get())
            try:
                eighteen = float(no18)
                li.append(eighteen)
            except:
                il.append(no18)
            no19 = (self.entry_19.get())
            companynames.append(no19)
            no20 = (self.entry_20.get())
            try:
                twenty = float(no20)
                li.append(twenty)
            except:
                il.append(no20)
            no21 = (self.entry_21.get())
            companynames.append(no21)
            no22 = (self.entry_22.get())
            try:
                two2 = float(no22)
                li.append(two2)
            except:
                il.append(no22)
            no23 = (self.entry_23.get())
            companynames.append(no23)
            no24 = (self.entry_24.get())
            try:
                four2 = float(no24)
                li.append(four2)
            except:
                il.append(no24)
            no25 = (self.entry_25.get())
            companynames.append(no25)
            no26 = (self.entry_26.get())
            try:
                six2 = float(no26)
                li.append(six2)
            except:
                il.append(no26)
            no27 = (self.entry_27.get())
            companynames.append(no27)
            no28 = (self.entry_28.get())
            try:
                eight2 = float(no28)
                li.append(eight2)
            except:
                il.append(no28)
            no29 = (self.entry_29.get())
            companynames.append(no29)
            no30 = (self.entry_30.get())
            try:
                ten3 = float(no30)
                li.append(ten3)
            except:
                il.append(no30)
            no31 = (self.entry_31.get())
            companynames.append(no31)
            no32 = (self.entry_32.get())
            try:
                twelve3 = float(no32)
                li.append(twelve3)
            except:
                il.append(no32)
            no33 = (self.entry_33.get())
            companynames.append(no33)
            no34 = (self.entry_34.get())
            try:
                fourteen3 = float(no34)
                li.append(fourteen3)
            except:
                il.append(no34)
            no35 = (self.entry_35.get())
            companynames.append(no35)
            no36 = (self.entry_36.get())
            try:
                sixteen3 = float(no36)
                li.append(sixteen3)
            except:
                il.append(no36)
            no37 = (self.entry_37.get())
            companynames.append(no37)
            no38 = (self.entry_38.get())
            try:
                eighteen3 = float(no38)
                li.append(eighteen3)
            except:
                il.append(no38)
            no39 = (self.entry_39.get())
            companynames.append(no39)
            no40 = (self.entry_40.get())
            try:
                twenty4 = float(no40)
                li.append(twenty4)
            except:
                il.append(no40)

            yy = np.array(li)

            plt.bar(companynames, yy)
            plt.ylabel("Sales(Naira)")
            # Show plot
            plt.show()
        
        Bar=tk.Button(self.master, text="Get Bar-Chart",command=barchart, font = fontStyle)
        Bar.grid(row=8, column=2, columnspan=2, rowspan=8,padx=120)


root = Tk()
root.configure(width=1000, height=900)
run = Window1(root)
root.mainloop()
