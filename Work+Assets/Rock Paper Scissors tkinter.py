from tkinter import *
import random
from tkinter import messagebox
from PIL import ImageTk, Image
root =Tk()
root.geometry("1254x472")
root.resizable(False,False)
root.title("Stone, Paper, Scissors!")

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
    cpulabel.place(x=640,y=400,anchor='center')
    if play!=cpu:
        if cpu!='paper':
            resultlabel=Label(rps,text="You Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.place(x=640,y=425,anchor='center')
            playscore+=1    
            print("Player",playscore)
        else:
            resultlabel=Label(rps,text="The CPU Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.place(x=640,y=425,anchor='center')
            cpuscore+=1
            print("computer:",cpuscore)
    else:
        resultlabel=Label(rps,text="It's a tie!Equal points awarded!",bg='cyan',font=('Open Sans',14))
        resultlabel.place(x=640,y=425,anchor='center')
        playscore+=1
        cpuscore+=1

def paper():
    global play
    global rps
    global playscore
    global cpuscore
    resultlabel=Label(text='')
    play='paper'
    cpu=random.choice(['rock','paper','scissors'])
    cputext="The Computer chose "+cpu
    cpulabel=Label(rps,text=cputext,font=('Open Sans',14))
    cpulabel.place(x=640,y=400,anchor='center')
    if play!=cpu:
        if cpu!='scissors':
            resultlabel=Label(rps,text="You Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.place(x=640,y=425,anchor='center')
            playscore+=1    
            print("Player",playscore)
        else:
            resultlabel=Label(rps,text="The CPU Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.place(x=640,y=425,anchor='center')
            cpuscore+=1
            print("computer:",cpuscore)
    else:
        resultlabel=Label(rps,text="It's a tie!Equal points awarded!",bg='cyan',font=('Open Sans',14))
        resultlabel.place(x=640,y=425,anchor='center')
        playscore+=1
        cpuscore+=1


def scissors():
    global play
    global rps
    global playscore
    global cpuscore
    play='scissors'
    cpu=random.choice(['rock','paper','scissors'])
    cputext="The Computer chose "+cpu
    cpulabel=Label(rps,text=cputext,font=('Open Sans',14))
    cpulabel.place(x=640,y=400,anchor='center')
    if play!=cpu:
        if cpu!='rock':
            resultlabel=Label(rps,text="You Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.place(x=640,y=425,anchor='center')
            playscore+=1    
            print("Player",playscore)
        else:
            resultlabel=Label(rps,text="The CPU Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.place(x=640,y=425,anchor='center')
            cpuscore+=1
            print("computer:",cpuscore)
    else:
        resultlabel=Label(rps,text="It's a tie!Equal points awarded!",bg='cyan',font=('Open Sans',14))
        resultlabel.place(x=640,y=425,anchor='center')
        playscore+=1
        cpuscore+=1
    


photorock=PhotoImage(file="Play Rock.png")
photopap=PhotoImage(file="Play Paper.png")
photosci=PhotoImage(file="Play Scissors.png")

image1=Image.open('C://songs//from desktop//PCV//ICT and Python Classes//Python Classes//Class XI- Python Programs//Fun and Games//Rock Paper Scissors//solid-color-image (1).png')
bg1=ImageTk.PhotoImage(image1)
def gamewindow():
    #Text Part
    global rps
    global rock
    global image
    root.iconify()
    hello='Hello '+name_entry.get()+". Let's Begin!"
    rps=Toplevel(root)
    lbl=Label(rps,image=bg1)
    lbl.place(x=0,y=0)
    rps.geometry("1254x472")
    rps.resizable(False,False)
    rps.title("Stone, Paper, Scissors!")

    #Game Part
    lb2=Label(rps,text=hello,font=('KyoMadoka',25,'bold'),fg='white',bg='#000126',borderwidth=0,relief="solid")
    lb2.place(x=640, y=25, anchor="center")
    exitbtn=Button(rps,text='Quit',command=box,bg='#FFD700',activebackground='red',activeforeground='pink',fg='black',font=("Consolas",12),cursor='hand2').place(x=1185,y=430)
    rock=Button(rps,image=photorock,borderwidth=0,command=rock,bg='#000126',activebackground='#23F900').place(x=50,y=50)
    pap=Button(rps,image=photopap,borderwidth=0,bg='#000126',command=paper).place(x=450,y=50)
    sci=Button(rps,image=photosci,borderwidth=0,bg="#000126",command=scissors).place(x=850,y=50)
    
    



bg_image =PhotoImage(file="C://songs//from desktop//PCV//ICT and Python Classes//Python Classes//Class XI- Python Programs//Fun and Games//Rock Paper Scissors//Rahul LJ 17th Jan//bgimage (1).png")
bg_label =Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label =Label(root, text="Stone, Paper, Scissors!", font=("Kyomadoka",40,'bold italic'),fg='white',bg='#000126')
title_label.place(x=640, y=50, anchor="center")

name_label =Label(root, text="Enter your name:", font=("Consolas",18),fg='white',bg='#000126')
name_label.place(x=640, y=250, anchor="center")

name_var = StringVar()
name_entry = Entry(root, textvariable=name_var, font=("Helvetica", 18,"bold"),borderwidth=4)
name_entry.place(x=640,y=300, anchor="center")

play_button =Button(root, text="Play", font=("Helvetica", 18), command=gamewindow, bg="#00b300", activebackground='yellow',cursor='hand2',fg="white", width=5, height=1,borderwidth=0)
play_button.place(x=640,y=375, anchor="center")

photo = PhotoImage(file ='rock-emoji.png')
root.iconphoto(False, photo)

root.mainloop()
