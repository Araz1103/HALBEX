# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:27:15 2020

@author: Araz Sharma
"""

#Importing Stuff

import tkinter as tk
from PIL import ImageTk,Image
#from functools import partial

# Methods to Display Text & Image in another window
# If button is clicked with no input - error shown but program doesn't halt
def createtext():
    print("Displaying Image from",file_txt.get())
    window_txt = tk.Toplevel(app)
    window_txt.title("Text File is being Displayed")
    txt_file = open(file_txt.get(), 'r')
    text_area = tk.Text(window_txt)
    text_area.insert(tk.INSERT,txt_file.read())
    text_area.pack(fill = tk.BOTH, expand = True)
    

def createNewWindow():
    print("Displaying Image from",file.get())
    newWindow = tk.Toplevel(app)
    newWindow.title("Image Displayed")
    img = Image.open(file.get())
    #img = img.resize((200,200), Image.ANTIALIAS) # Can be used to resize the image
    img = ImageTk.PhotoImage(img)  
    
    #icon = tk.PhotoImage(file = "bats.jpg")
    label = tk.Label(newWindow,image = img)
    label.image = img
    label.pack()
    

#Creating Main Window

app = tk.Tk()
app.title("Command Window")
file = tk.StringVar()
file_txt = tk.StringVar()
#Image Labels & Buttons
Image_tab = tk.Label(text="Enter Address for Image File", #Shows error on console if address not found, but program doesn't halt
                    fg ="purple", #foreground
                    bg ="yellow",  #background
                    width = 25, # wid & hgt are mesured by size of character 0 - width of character 0 & height of 0
                    height = 5) 
Image_tab.pack()
entry_1 = tk.Entry(textvariable = file)
entry_1.pack()  
print(file.get())
#file = entry_1.get()
#createNewWindow = partial(createNewWindow, file.get())


button_img = tk.Button(app, 
              text="Click to Display Image from the address you have given",
              command=createNewWindow)
button_img.pack()
#Txt File Labels & Buttons
File_tab = tk.Label(text="Enter Address for Text File", #Error if not found, but program doesn't halt
                    fg ="purple", #foreground
                    bg ="yellow",  #background
                    width = 25, # wid & hgt are mesured by size of character 0 - width of character 0 & height of 0
                    height = 5) 
File_tab.pack()
entry_2 = tk.Entry(textvariable = file_txt)
entry_2.pack()  
print(file_txt.get())

button_txt = tk.Button(app, 
              text="Click to Display Text file from the address you have given",
              command=createtext)
button_txt.pack()

app.mainloop()