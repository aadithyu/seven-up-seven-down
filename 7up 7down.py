import tkinter as tk
import random
from tkinter import Frame

#Game Variables
HEIGHT=500
WIDTH=500

#function
def test(entry):
    print("Button Clicked")
    print("This is the Entry " + entry)
def place_bet(entry):
    if entry > "12":
        label["text"] = "Invalid Entry Choose a proper number between 1 to 12"
    else:
        heading = random.randint(2, 12)
        label["text"]= heading

#Make the root
root = tk.Tk()

#canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH )
canvas.pack()

#make the Frame
frame = tk.Frame(root, bg='blue', bd=5)
frame.place(relheight=0.15, relwidth=0.9, relx=0.05, rely=0.05)

#make the entry
entry = tk.Entry(frame, font=40)
entry.place(relheight=0.9, relwidth= 0.6, rely=0.05)

#make the button
button = tk.Button(frame, text='Place Bet' , command=lambda:place_bet(entry.get()))
button.place(relheight=0.9, relwidth=0.35, relx=0.63, rely=0.05)

#lower fame
lower_frame = tk.Frame(root, bg='blue', bd=5)
lower_frame.place(relheight=0.63, relwidth=0.9, relx=0.05, rely=0.3)

#label
label= tk.Label(lower_frame)
label.place(relheight=1, relwidth=1)
#mak the mainloop
root.title("Seven up Seven down")
root.mainloop()