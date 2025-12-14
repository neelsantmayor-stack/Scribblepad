# Original standalone script for quick scribbling

from tkinter import *

# function definition

def get_x_and_y(event):
    global lasx, lasy # makes this available to other functions
    lasx, lasy = event.x, event.y

# function definition

def draw(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), fill = 'yellow', width = 5)
    lasx, lasy = event.x, event.y # if commented old point won't change

root= Tk()
root.geometry("400x400") # "widthxheight"
root.title("Scribble Pad") # title of the window
canvas = Canvas(root, bg = 'brown')
canvas.pack(anchor = 'nw', fill = 'both', expand = 1)
canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw)
root.mainloop()
