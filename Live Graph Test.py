# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 06:07:26 2020

@author: Araz Sharma
"""
import random
import numpy as np
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk




LARGE_FONT= ("Verdana", 12)
style.use("ggplot")
'''
matplotlib.pyplot.xlim(0,5)
matplotlib.pyplot.ylim(0,1000)
xmin, xmax = matplotlib.pyplot.xlim()
print(xmin,xmax)
ymin, ymax = matplotlib.pyplot.ylim()
print(ymin,ymax)
'''
#Initial set of Figure/ Plot Properties
f = Figure(figsize=(6,6), dpi=100)
a = f.add_subplot(111)
a.set_xlim([0,6])
a.set_ylim([0,1000])
a.set_xticks(np.arange(0, 6.0, 0.5))
a.set_ylabel('Value')
a.set_xlabel('Time in Milliseconds')
b_mark = 0
t_val = 0
def animate(i):
    
    # Code to Plot the points from a random value btwn 1-1000
    # This function is called every 0.5 seconds, and adds a point
    
    global b_mark
    global t_val
    # Checks when 10 points are there - clears graph
    
    if(b_mark == 10):
        b_mark = 0
        t_val = 0
        a.clear()
        # Needs to reset the graph properties every time it clears
        a.set_xlim([0,6])
        a.set_ylim([0,1000])
        a.set_xticks(np.arange(0, 6.0, 0.5))
        a.set_ylabel('Value')
        a.set_xlabel('Time in Milliseconds')
        
    
    b_mark+=1
    r_val = random.randrange(1,1001)
    t_val+=0.5
    #Using to plot the point
    a.scatter(t_val,r_val)
    
    #time.sleep(0.5) - Not using as gives lag in displaying/ tkinter hangs
    
    
    #Code if we want to fetch datapoints from a text file
     
    '''
    pullData = open("sampleText.txt","r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    
    #a.clear()
    a.plot(xList, yList)

    '''
            

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
     
        tk.Tk.iconbitmap(self,"Bat3.ico")
        tk.Tk.wm_title(self, "Batman")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

#Basic Tkinter Codes for Making 3 Pages & Linking them up
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


#Tkinter Code for Graph Page

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
#Calling Animate function every 0.5 seconds
ani = animation.FuncAnimation(f, animate, interval=500)
app.mainloop()
