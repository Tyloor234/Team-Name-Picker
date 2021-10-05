import random
from tkinter import *
from tkinter import ttk

# Define lists of words
prefix = ["Wet", "Sticky", "Smooth", "Hideous", "Sexy", "Rude", "Strange", "Creamy", "Wavy", "Running", "Chunky",
          "Stormy", "Desolate", "Crisp"]
noun = ["Bikers", "Hands", "Witches", "Blenders", "Housekeepers", "Streamers", "Eggs", "Fishes", "Dustbunnies",
        "Pieces", "Chunks", "Bushes", "Mushrooms"]


# Create the actual window
root = Tk()
root.title("Team Name Generator")
root.iconbitmap("turtle.ico")
root.resizable(False, False)
root.geometry("300x180")

# Set up the grid
mainframe = ttk.Frame(root, width=300, height=200)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.pack(fill="both", expand=True, padx=20, pady=20)
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
def doButtons():

    getWords()

    ttk.Button(mainframe, text=p1, command=lambda: ttk.Label(mainframe, text=p1).grid(column=2, row=3)).grid(column=1, row=1)
    ttk.Button(mainframe, text=p2, command=lambda: ttk.Label(mainframe, text=p2).grid(column=2, row=3)).grid(column=2, row=1)
    ttk.Button(mainframe, text=p3, command=lambda: ttk.Label(mainframe, text=p3).grid(column=2, row=3)).grid(column=3, row=1)

    ttk.Button(mainframe, text=n1, command=lambda: ttk.Label(mainframe, text=n1).grid(column=3, row=3)).grid(column=1, row=2)
    ttk.Button(mainframe, text=n2, command=lambda: ttk.Label(mainframe, text=n2).grid(column=3, row=3)).grid(column=2, row=2)
    ttk.Button(mainframe, text=n3, command=lambda: ttk.Label(mainframe, text=n3).grid(column=3, row=3)).grid(column=3, row=2)


doButtons()


ttk.Label(mainframe, text="The").grid(column=1, row=3)
ttk.Button(mainframe, text="Reroll!", command=lambda: doButtons()).grid(column=2, row=4)

# Adds padding to the buttons to make it look nicer
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
