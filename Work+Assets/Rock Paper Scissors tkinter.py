from tkinter import *
import random
from tkinter import messagebox
from PIL import ImageTk, Image
root=Tk()

playscore=0
cpuscore=0

def box():
    if messagebox.askyesno("Warning!","Are you sure you want to\nquit and view your results?")==True:
        hi()

def hi():
    rps.destroy()
    exitscrn=Toplevel(root)
    exitscrn.geometry("1280x320")
    exitscrn.title("Results")
    exitscrn.resizable(False,False)
    lb3=Label(exitscrn,text="Venkat Window").pack()



def rock():
    global play
    global rps
    global playscore
    global cpuscore
    resultlabel=Label(text='')
    play='rock'
    cpu=random.choice(['rock','paper','scissors'])
    cputext="The Computer chose "+cpu
    cpulabel=Label(rps,text=cputext,font=('Open Sans',14))
    cpulabel.grid(row=3,column=1)
    if play!=cpu:
        if cpu!='paper':
            resultlabel=Label(rps,text="You Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.grid(row=4,column=1)
            playscore+=1    
            print("Player",playscore)
        else:
            resultlabel=Label(rps,text="The CPU Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.grid(row=4,column=1)
            cpuscore+=1
            print("computer:",cpuscore)
    else:
        resultlabel=Label(rps,text="It's a tie!Equal points awarded!",bg='cyan',font=('Open Sans',14))
        resultlabel.grid(row=4,column=1)
        playscore+=1
        cpuscore+=1
    


photo=PhotoImage(file='Poké_Ball_icon.svg.png')
root.iconphoto(False,photo)

photorock=PhotoImage(file="Play Rock.png")
photopap=PhotoImage(file="Play Paper.png")
photosci=PhotoImage(file="Play Scissors.png")

image=Image.open('C://songs//from desktop//PCV//ICT and Python Classes//Python Classes//Class XI- Python Programs//Fun and Games//Rock Paper Scissors//journeys.jpeg')
bg=ImageTk.PhotoImage(image)
def gamewindow():
    #Text Part
    global rps
    global rock
    global image
    root.iconify()
    hello='Hello '+e.get()+". Let's Begin!"
    rps=Toplevel(root)
    lbl=Label(rps,image=bg)
    lbl.place(x=0,y=0)
    rps.geometry("1254x472")
    rps.resizable(False,False)
    rps.title("Rock, Paper, Scissors!")

    #Game Part
    lb2=Label(rps,text=hello,font=('KyoMadoka',25,'bold'),bg='#FFD700',borderwidth=2,relief="solid")
    lb2.place(x=640, y=20, anchor="center")
    exitbtn=Button(rps,text='QUIT☻',command=box,bg='#FFD700',activebackground='red',activeforeground='pink',fg='black',font=("Consolas",12),cursor='hand2').place(x=1185,y=430)
    rock=Button(rps,image=photorock,borderwidth=0,command=rock,bg='#fd0889',activebackground='yellow').place(x=50,y=50)
    pap=Button(rps,image=photopap,borderwidth=0,bg='#fd0889').place(x=450,y=50)
    sci=Button(rps,image=photosci,borderwidth=0,bg="#fe2b8c").place(x=850,y=50)
    
    



image=Image.open('C://songs//from desktop//PCV//ICT and Python Classes//Python Classes//Class XI- Python Programs//Fun and Games//Rock Paper Scissors//journeys.jfif')
background=ImageTk.PhotoImage(image)
root.geometry("1000x667")
lbl=Label(root,image=background)
lbl.place(x=0,y=0)
labe=Label(text="Hello World!",bg="#FFD700",cursor='dotbox').pack()
e=Entry(root)
e.pack()

root.title("Welcome!")
btn=Button(root,text='Enter',command=gamewindow,cursor='hand2').pack()




