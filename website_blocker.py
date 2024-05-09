#importing required liberary
from tkinter import *
#creating a window
window = Tk()
window.geometry('650x400')
window.minsize(650,400)
window.maxsize(650,400)
window.title("Website Blocker")

heading=Label(window, text ='Website Blocker' , font ='arial')
heading.pack()

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

label1=Label(window, text ='Enter Website :' , font ='arial 13 bold')
label1.place(x=5 ,y=60)

enter_Website = Text(window,font = 'arial',height='2', width = '40')
enter_Website.place(x= 140,y = 60)

window.mainloop()
