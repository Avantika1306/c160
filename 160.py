from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox 
import os
root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title("Notepad")
open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
close_img=ImageTk.PhotoImage(Image.open("close.png"))
label_file=Label(root,text="file name")
label_file.place(relx=0.28,rely=0.03)
input_filename=Entry(root)
input_filename.place(relx=0.45,rely=0.03)

def openfile():
    print("hi")

def savefile():
    print("hi")

def closefile():
    print("hi")

        

button_open=Button(root,image=open_img,command=openfile)
button_open.place(relx=0.05,rely=0.03)
button_save=Button(root,image=save_img,command=savefile)
button_save.place(relx=0.11,rely=0.03)
button_close=Button(root,image=close_img,command=closefile)
button_close.place(relx=0.17,rely=0.03)
textarea=Text(root,height=35,width=80)
textarea.place(relx=0.5,rely=0.55)
root.mainloop()