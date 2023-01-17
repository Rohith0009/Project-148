from tkinter import *
import random

global RandomNumber

root = Tk()
root.title("Project 148")
root.geometry("1600x1600")
root.configure(background="pale green")

Title = Label(
    root, text="Random Number Generator", font=("Arial", "30"), fg="blue", bg="pale green"
)
ItemListLabel = Label(root, text="Listed Items: ['Bottle', 'Tiffin', 'ID Card', 'Chocolates', 'Chips', 'Tickets', 'Hanky']", fg="blue", bg="pale green", font=("Arial", "15"))
RandomNumberLabel = Label(root, text="Click On the Above Button", fg="blue", bg="pale green", font=("Arial", "15"))

RandomNumber = []


def MainFunction():
    RandomNumber.append(random.sample(range(7),1))
    RandomNumberLabel['text'] = f"Put Item Number {RandomNumber} in your bag"

PickItemBtn = Button(root, text="Pick Item", command=MainFunction, fg="blue", font=("Arial", "15"))

Title.place(relx=0.5, rely=0.07, anchor=CENTER)
ItemListLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
PickItemBtn.place(relx=0.5, rely=0.27, anchor=CENTER)
RandomNumberLabel.place(relx=0.5, rely=0.34, anchor=CENTER)

root.mainloop()
