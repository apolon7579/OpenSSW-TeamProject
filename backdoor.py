from tkinter import *
from math import *
import tkinter.font
import tkinter.ttk

root = Tk()
root.geometry("1920x1080")
font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

#프레임 설정
title=tkinter.Frame(root, relief="solid", bd=2)
title.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
main=tkinter.Frame(root, relief="solid", bd=2, pady = 100)
main.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
ip=tkinter.Frame(main, relief="solid", bd=2)
ip.pack(side="top", fill="both", pady = 50)
loading=tkinter.Frame(main, relief="solid", bd=2)
loading.pack(side="top", fill="both", expand=True, pady = 50)
button=tkinter.Frame(root, padx = 70, pady = 30, relief="solid", bd=2)
button.pack(side="bottom", fill="x")

#title
labelTitle=tkinter.Label(title, text="BACKDOOR", height=1, width=12, font=font, bg="#564898", fg="white")
labelTitle.pack(side = "left", expand = YES, fill = BOTH)
labelWhite=tkinter.Label(title, text="", height=1, font=font)
labelWhite.pack(side = "left", expand = YES, fill = BOTH)
labelTultip=tkinter.Label(title, text="INSTALL A BACKDOOR TO ANOTHER FIREWALL", height=1, width=46, font=font, bg="#564898", fg="#cac4e2")
labelTultip.pack(side = "left", expand = YES, fill = BOTH)

#ip 입력창
entry = Entry(ip, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
entry.pack(side = "right", expand = YES, fill = X)

labelIp=tkinter.Label(ip, text="IP: ", font=font)
labelIp.pack(side = "right")

#프로그레스 바
labelFin=tkinter.Label(loading, text="INSTALLATION COMPLETE!")
labelFin.pack(side="top", anchor = "e")
pb = tkinter.ttk.Progressbar(loading, maximum=100, mode="determinate")
pb.pack(expand = YES, fill = BOTH)                       # 프로그래스 바 배치
label0=tkinter.Label(loading, text="0%", font=font)
label0.pack(side="left")
label100=tkinter.Label(loading, text="100%", font=font)
label100.pack(side="right")

#버튼 입력창
options = Button(button, text="INITIALIZE /\nACTIVATE", height=1, width=10, fg="black",bg="#ec6818", font=font, relief="flat")
options.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

unzip = Button(button, text="PAUSE", height=1, width=10, fg="black",bg="#e71b69", font=font, relief="flat")
unzip.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

backdoor = Button(button, text="RESUME", height=1, width=10, fg="black",bg="#ebda1d", font=font, relief="flat")
backdoor.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

ddos = Button(button, text="EXIT /\nTERMINATE", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat")
ddos.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

root.mainloop()