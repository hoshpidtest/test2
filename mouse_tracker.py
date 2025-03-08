from tkinter import *


def customMouse(e=None):
    x = e.x_root - root.winfo_x() - 10
    y = e.y_root - root.winfo_y() - 40
    print(x, y)
    label.place_configure(x=x, y=y)


root = Tk()
label = Label(master=root, text="^", bg="grey")
label.place(x=0, y=0)

root.bind('<Motion>', customMouse)

root.mainloop()