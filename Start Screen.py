from tkinter import *

root = Tk()
root.geometry("1920x1080")

def resize(e):
     
    size = e.width/10
    intro.config(font = ("Malgun Gothic", 40))
    start.config(font = ("Malgun Gothic", 40))
    exit_b.config(font = ("Malgun Gothic", 40))


intro = Button(root, text = "PY-CURITY", height = 1, width=10, fg = "white",bg = "#8551fe")
intro.place(x=580, y = 190)

start = Button(root, text = "START", height = 1, width=10, fg = "black",bg = "#ec681a")
start.place(x=335, y = 470)

exit_b = Button(root, text = "EXIT", height = 1, width=10, fg = "black",bg = "#5db134")
exit_b.place(x=825, y = 470)

root.bind('<Configure>', resize)

root.mainloop()