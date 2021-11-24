from tkinter import *

root = Tk()
root.geometry("1920x1080")

def resize(e):
     
    size = e.width/10
    options.config(font = ("Malgun Gothic", 40))
    unzip.config(font = ("Malgun Gothic", 40))
    backdoor.config(font = ("Malgun Gothic", 40))
    ddos.config(font = ("Malgun Gothic", 40))
    pscan.config(font = ("Malgun Gothic", 40))
    ssh.config(font = ("Malgun Gothic", 40))

options = Button(root, text = "OPTIONS", height = 1, width=17, fg = "black",bg = "white")
options.place(x=490, y = 50)

unzip = Button(root, text = "UNZIP", height = 1, width=10, fg = "#8551fe",bg = "white")
unzip.place(x=340, y = 270)

backdoor = Button(root, text = "BACKDOOR", height = 1, width=10, fg = "#8551fe",bg = "white")
backdoor.place(x=840, y = 270)

ddos = Button(root, text = "D-DOS", height = 1, width=10, fg = "#8551fe",bg = "white")
ddos.place(x=125, y = 500)

pscan = Button(root, text = "PORT SCAN", height = 1, width=10, fg = "#8551fe",bg = "white")
pscan.place(x=605, y = 500)

ssh = Button(root, text = "SSH", height = 1, width=10, fg = "#8551fe",bg = "white")
ssh.place(x=1075, y = 500)

root.bind('<Configure>', resize)

root.mainloop()