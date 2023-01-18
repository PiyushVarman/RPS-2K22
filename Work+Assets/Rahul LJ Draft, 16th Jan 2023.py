import tkinter as tk
from tkinter import PhotoImage

def on_start_button_click():
    name = name_entry.get()
root = tk.Tk()
root.geometry("1280x720")
canvas = tk.Canvas(root, bg="cyan", height=720, width=1280)
canvas.pack()
heading_label = tk.Label(root, text="STONE PAPER SCISSORS", font=("Kyomadoka", 18))
heading_label.place(relx=0.5, rely=0.1, anchor="center")
name_label = tk.Label(root, text="Enter your name:",font=("Consolas", 14))
name_label.place(relx=0.5, rely=0.3, anchor="center")
name_entry = tk.Entry(root)
name_entry.place(relx=0.5, rely=0.4, anchor="center")
start_button = tk.Button(root, text="Start", command=on_start_button_click,font=("Consolas", 14),cursor='hand2')
start_button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
