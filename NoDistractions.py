#importing required liberary
import webbrowser 
import os
import time
from selenium import webdriver
from tkinter import *
#creating a window
window = Tk()
window.geometry('1024x400')
window.minsize(1024,400)
window.maxsize(1024,400)
window.title("NOD")

heading=Label(window, text ='No Distractions' , font ='arial')
heading.pack()

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

label1=Label(window, text ='Enter Website :' , font ='arial 13 bold')
label1.place(x=5 ,y=60)
label1_height = label1.winfo_width()
hor_spacing = 10 
label2_y = 60 + label1_height + hor_spacing

enter_Website = Text(window,font = 'arial',height='2', width = '40')
enter_Website.place(x= 140,y = 60)

label2=Label(window, text ='Enter Time :' , font ='arial 13 bold')
label2.place(x=5,y=120)

enter_time = Text(window,font = 'arial',height='2', width = '40')
enter_time.place(x= 140,y = 120)



def Blocker():
    website_lists = enter_Website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            if web in file_content:
                display=Label(window, text = 'Already Blocked' , font = 'arial')
                display.place(x=500,y=200)
                pass
            else:
                host_file.write(ip_address + " " + web + '\n')
                Label(window, text = "Blocked", font = 'arial').place(x=230,y =200)

def Unblock():
    website_lists = enter_Website.get(1.0, END)
    Website = list(website_lists.split(","))
    with open(host_path, "r") as host_file:
        file_content = host_file.readlines()
    with open(host_path, "w") as f:
        for line in file_content:
            if not any(web in line for web in Website):
                f.write(line)
                display = Label(window, text="Unblocked Successfully", font='arial')
                display.place(x=500, y=200)




def SetTimer():
    text = enter_time.get(1.0, END).rstrip()  # Get text and strip trailing whitespace
    if text:  # Check if text is not empty after stripping
        duration = int(text)
        webbrowser.open(enter_Website.get(1.0, END).rstrip())  # Open website URL
        time.sleep(duration)  # Use the sleep function from the time module
        os.system("taskkill /f /im msedge.exe")  # Close browser after the timer expires
    else:
        print("No time input")  # Handle case where there's no input or only whitespace






block_button = Button(window, text = 'Block',font = 'arial',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'grey')
block_button.place(x = 230, y = 200)

unblock_button = Button(window, text = 'UnBlock',font = 'arial',pady = 5,command = Unblock ,width = 8, bg = 'royal blue1', activebackground = 'grey')
unblock_button.place(x = 350, y = 200)

set_timer = Button(window, text = 'Set Time',font = 'arial',pady = 5,command = SetTimer ,width = 10, bg = 'royal blue1', activebackground = 'grey')
set_timer.place(x = 470, y = 200)


window.mainloop()
