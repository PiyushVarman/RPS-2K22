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
        exitscreen()
def quitbox():
    if messagebox.askyesno("Warning!","Are you sure you want to\nquit the game?")==True:
        root.destroy()                                        

bg_image=PhotoImage(file="G://Piyush Chandra Varman 11D//RPS//PCV Work//Work+Assets//bgimage (1).png")
def exitscreen():
    global rps
    global exitscrn
    global bg_image
    global playscore
    global cpuscore
    rps.destroy()
    exitscrn=Toplevel(root)
    exitscrn.geometry("1254x472")
    exitscrn.title("Results")
    exitscrn.resizable(False,False)
    bg_label=Label(exitscrn,image=bg_image).place(x=0,y=0)
    

    user_name = Label(exitscrn,text = "Results",anchor='nw',font=('Kyomadoka',50,'bold italic'),fg='white',bg='#000123')
    user_name.place(x=627,y=50, anchor="center")

    ps="Your score: "+str(playscore)+" "
    cs="CPU score: "+str(cpuscore)+" "
    ds="Delta score: "+str(playscore-cpuscore)+" "
    
    playerscore = Label(exitscrn,text = ps,anchor='w',font=('Broadway',35,'bold italic'),fg='white',bg='#000123')
    playerscore.place(x=610,y=150, anchor="center")

    cpulab = Label(exitscrn,text = cs,anchor='w',font=('Broadway',35,'bold italic'),fg='white',bg='#000123')
    cpulab.place(x=610,y=230, anchor="center")

    deltascore = Label(exitscrn,text = ds,anchor='w',font=('Broadway',35,'bold italic'),fg='white',bg='#000123')
    deltascore.place(x=610,y=310, anchor="center")

    quitbutton = Button(exitscrn, text="Quit", command=quitbox,font=("Consolas", 14,'bold'),cursor='hand2',fg='white',bg='#FF0000',activebackground='yellow',borderwidth=2)
    quitbutton.place(x=1150,y=390, anchor="center")

    if int(playscore-cpuscore)>0:
        result=Label(exitscrn,text="You Win! ",font=('Broadway',35,'bold italic'),fg='#FFD700',bg='#000123')
        result.place(x=610,y=410,anchor="center")
        ##############

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
        else:
            resultlabel=Label(rps,text="The CPU Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.place(x=640,y=425,anchor='center')
            cpuscore+=1
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
        else:
            resultlabel=Label(rps,text="The CPU Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.place(x=640,y=425,anchor='center')
            cpuscore+=1
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
    resultlabel=Label(text='')
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
        else:
            resultlabel=Label(rps,text="The CPU Won!",bg='cyan',font=('Open Sans',14))
            resultlabel.place(x=640,y=425,anchor='center')
            cpuscore+=1
    else:
        resultlabel=Label(rps,text="It's a tie!Equal points awarded!",bg='cyan',font=('Open Sans',14))
        resultlabel.place(x=640,y=425,anchor='center')
        playscore+=1
        cpuscore+=1
    
photorock=PhotoImage(file="Play Rock.png")
photopap=PhotoImage(file="Play Paper.png")
photosci=PhotoImage(file="Play Scissors.png")

image1=Image.open('G://Piyush Chandra Varman 11D//RPS//PCV Work//Work+Assets//solid-color-image (1).png')
bg1=ImageTk.PhotoImage(image1)
def gamewindow():
    if name_entry.get().isalnum():
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
        lb2=Label(rps,text=hello,font=('KyoMadoka',25,'bold'),fg='white',bg='#000126',borderwidth=2,relief="solid")
        lb2.place(x=640, y=25, anchor="center")
        exitbtn=Button(rps,text='Quit',command=box,bg='#FFD700',activebackground='red',activeforeground='pink',fg='black',font=("Consolas",12),cursor='hand2').place(x=1185,y=430)
        rock=Button(rps,image=photorock,borderwidth=0,command=rock,bg='#000126',activebackground='#23F900').place(x=50,y=50)
        pap=Button(rps,image=photopap,borderwidth=0,bg='#000126',command=paper,activebackground='#23F900').place(x=450,y=50)
        sci=Button(rps,image=photosci,borderwidth=0,bg="#000126",command=scissors,activebackground='#23F900').place(x=850,y=50)
    else:
        messagebox.showerror('Wrong Username!', 'Usernames must include\neither alphabets,numbers or both')
    



bg_image =PhotoImage(file="G://Piyush Chandra Varman 11D//RPS//Rahul LJ 17th Jan//bgimage (1).png")
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
