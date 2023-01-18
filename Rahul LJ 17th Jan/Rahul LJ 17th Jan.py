from tkinter import *

root =Tk()
root.geometry("1254x472")
root.resizable(False,False)
root.title("Stone, Paper, Scissors!")

bg_image =PhotoImage(file="C://songs//from desktop//PCV//ICT and Python Classes//Python Classes//Class XI- Python Programs//Fun and Games//Rock Paper Scissors//Rahul LJ 17th Jan//bgimage (1).png")
bg_label =Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label =Label(root, text="Stone, Paper, Scissors!", font=("Kyomadoka", 40,'bold italic'),fg='white',bg='#000126')
title_label.place(x=640, y=50, anchor="center")

name_label =Label(root, text="Enter your name:", font=("Consolas", 18),fg='white',bg='#000126')
name_label.place(x=640, y=250, anchor="center")

name_var = StringVar()
name_entry = Entry(root, textvariable=name_var, font=("Helvetica", 18,"bold"),borderwidth=4)
name_entry.place(x=640,y=300, anchor="center")

play_button =Button(root, text="Play", font=("Helvetica", 18), bg="#00b300", activebackground='yellow',cursor='hand2',fg="white", width=5, height=1,borderwidth=0)
play_button.place(x=640,y=375, anchor="center")

photo = PhotoImage(file ='rock-emoji.png')
root.iconphoto(False, photo)

root.mainloop()



