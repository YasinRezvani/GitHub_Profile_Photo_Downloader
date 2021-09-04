from tkinter import * 
import os
from tkinter import messagebox
from tkinter import ttk
import requests 
from bs4 import BeautifulSoup as bs

root= Tk()

root.title("GitHub_Profile_Photo_Downloader")
root.geometry("500x160")
root.resizable(False, False)

label=Label(root, text="Enter GitHub Username: ", font=("Arial 18 bold"))
label.pack()

entry= Entry(root, width= 40)
entry.pack()


def download():
    lbl.configure(text="Download Link")
    res = entry.get()
    url = "https://github.com/" + res
    req = requests.get(url)
    scrab = bs(req.content, "html.parser")
    data = scrab.find("img" , {"alt" : "Avatar"})['src']
    get.configure(text=data)
    command = 'echo ' + data.strip() + '| clip'
    os.system(command)
    messagebox.showinfo('Successfully', 'Download Link Copy in Clipboard Successfully')

ttk.Button(root, text= "Download",width= 20,command=download).pack(pady=10)
lbl = Label(root, font=("Arial 15"))
lbl.pack()
get = Label(root , font=("Arial 15") ,bg ="blue" , fg="white")
get.pack()

root.mainloop()

# Made By Yasin Rezvani
