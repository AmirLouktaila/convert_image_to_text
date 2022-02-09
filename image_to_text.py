from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pywhatkit,os
root = Tk()
root.title('image_to_text')
root.geometry("400x50")
root.resizable(0,0)
label_path=ttk.Label(root,text='input path image : ')
label_path.place(x=10,y=12)
Entry_path=ttk.Entry(root,width=30)
Entry_path.place(x=120,y=12)
button_convert=ttk.Button(root,text='Convert')
button_convert.place(x=310,y=10)


def convert():
	getpath="C:\\Users\\salahlkt\\Desktop\\app python tkinter\\{}".format(Entry_path.get()+".png")
	getpathedit="C:\\Users\\salahlkt\\Desktop\\app python tkinter\\{}".format(Entry_path.get())
	pywhatkit.image_to_ascii_art(getpath,getpathedit)
	messagebox.showinfo(title="convert", message="Done convert")
button_convert.configure(command=convert)
root.mainloop()