from tkinter import *
import pyttsx3
import PIL,ImageTk,Image
from tkinter import messagebox
count=0
size=20
def speak():
    if entry.get()=="":
        messagebox.showerror("ERROR","PLEASE ENTER TEXT")
    else:
        engine=pyttsx3.init()
        engine.setProperty('rate',125)
        engine.say(entry.get())
        engine.runAndWait()
def dell():
    entry.delete(0,END)

def change():
    ans=messagebox.askyesno("Confirm","ARE YOU SURE!\nCHANGE BACKGROUND")
    if (ans):
        root.config(bg="magenta")
def defa():
    root.config(bg="#003e53")

def ex():
    ans=messagebox.askyesno('Confirm',"ARE YOU SURE TO EXIT?")
    if ans==1:
        root.destroy()
def doc():
    messagebox.showinfo('PYTTSX3','SORRY! THIS IS NOT CURRENTLY WORKING')
root=Tk()
root.title("Text To Speech | CREATOR: ENG-CJ")
root.geometry('600x700')
root.config(bg="#003e53")
Label(root,text="TEXT TO SPEECH",bg="#003e53",fg="white",
      font=("Verdana",40,"bold")).pack(pady=20)
Label(root,text="DEVELOPED BY: ENG-CJ",bg="#003e53",fg="white",
      font=('Verdana',19,"bold")).place(x=130,y=80)
global entry
entry=StringVar()
entry=Entry(root,textvariable=entry,width=50,bd=5,relief='sunken',font=('Verdana',14,"bold"))
entry.pack(pady=10)
Label(root,text="ENTER TEXT TO CONVERT SPEECH",bg="#003e53",fg="cyan",
      font=("times new roman",17,"bold")).place(x=96,y=190)

b1=Button(root,text="SPEAK",bg="red",fg="white",command=speak,font=("times new roman",15,"bold"),
          bd=7,relief="groove",width=6).place(x=120,y=260)

b2=Button(root,text="DELETE",bg="blue",fg="white",font=("times new roman",15,"bold"),
          bd=7,relief="groove",width=6,command=dell).place(x=240,y=260)

Button(root,text="CHANGE BG",bg="white",command=change,fg="black",font=("Verdana",14,"bold"),
       bd=9,relief="groove").place(x=370,y=260)

Button(root,text="DEFAULT",command=defa,bg="magenta",fg="black",font=("Verdana",14,"bold"),
       bd=9,relief="groove",width=10).place(x=370,y=340)

Button(root,text="PYTTSX3",command=doc,bg="black",fg="white",font=("Verdana",14,"bold"),
       bd=9,relief="groove").place(x=220,y=340)
Button(root,text="EXIT",command=ex,bg="red",fg="white",font=("Verdana",14,"bold"),
       bd=9,relief="groove",width=5).place(x=120,y=340)
IM=Image.open("LOGO.png")
res=IM.resize((300,300),Image.ANTIALIAS)
new=ImageTk.PhotoImage(res)
Label(root,image=new,bd=0,bg="#003e53").place(x=200,y=400)

mainloop()
