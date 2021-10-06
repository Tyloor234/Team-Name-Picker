import random
from tkinter import *
from tkinter import ttk

# Define lists of words
prefix = ["Wet", "Sticky", "Smooth", "Hideous", "Sexy", "Rude", "Strange", "Creamy", "Wavy", "Running", "Chunky",
          "Stormy", "Desolate", "Crisp"]
noun = ["Bikers", "Hands", "Witches", "Blenders", "Maids", "Streamers", "Eggs", "Fishes", "Dustbunnies",
        "Pieces", "Chunks", "Bushes", "Mushrooms"]


# Create the actual window
root = Tk()
root.title("Team Name Generator")
root.iconbitmap("turtle.ico")
root.resizable(False, False)
root.geometry("440x150")

# Set up the grid
mainframe = ttk.Frame(root, width=300, height=200)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.pack(fill="both", expand=True, padx=10, pady=10)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Pulls a random assortment of words from the above lists
def getWords():
    prefixes = random.sample(prefix, k=3)
    nouns = random.sample(noun, k=3)

    global p1, p2, p3, n1, n2, n3

    p1 = prefixes[0]
    p2 = prefixes[1]
    p3 = prefixes[2]

    n1 = nouns[0]
    n2 = nouns[1]
    n3 = nouns[2]


# Creates the buttons, when clicked the buttons add the word that's on them to the bottom "Team name" row
getWords()


def doButtons():

    global btn1, btn2, btn3, btn4, btn5, btn6, space1, space2

    labelThe = ttk.Label(mainframe, text="The")
    labelThe.grid(column=1, row=3)

    btnReroll = ttk.Button(mainframe, text="Reroll!", command=lambda: reRoll())
    btnReroll.grid(column=2, row=4)

    space1 = ttk.Label(mainframe, text="")
    space1.grid(column=2, row=3)

    space2 = ttk.Label(mainframe, text="")
    space2.grid(column=3, row=3)

    btn1 = ttk.Button(mainframe, width=20, text=p1, command=lambda: space1.config(text=p1))
    btn1.grid(column=1, row=1)
    btn2 = ttk.Button(mainframe, width=20, text=p2, command=lambda: space1.config(text=p2))
    btn2.grid(column=2, row=1)
    btn3 = ttk.Button(mainframe, width=20, text=p3, command=lambda: space1.config(text=p3))
    btn3.grid(column=3, row=1)

    btn4 = ttk.Button(mainframe, width=20, text=n1, command=lambda: space2.config(text=n1))
    btn4.grid(column=1, row=2)
    btn5 = ttk.Button(mainframe, width=20, text=n2, command=lambda: space2.config(text=n2))
    btn5.grid(column=2, row=2)
    btn6 = ttk.Button(mainframe, width=20, text=n3, command=lambda: space2.config(text=n3))
    btn6.grid(column=3, row=2)

    # Adds padding to the buttons to make it look nicer
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)


doButtons()


def reRoll():

    getWords()

    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn6.destroy()

    space1.destroy()
    space2.destroy()

    doButtons()


root.mainloop()
