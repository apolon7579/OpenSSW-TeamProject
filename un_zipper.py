from tkinter import *
from math import *
import tkinter.font
import tkinter.ttk

def switch_frame(self, frame_class):
  new_frame = frame_class(self)
  if self._frame is not None:
    self._frame.destroy()
  self._frame = new_frame
  self._frame.pack()

root = Tk()
root.geometry("1920x1080")
font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

#프레임 설정
titleUZ=tkinter.Frame(root)
titleUZ.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
mainUZ=tkinter.Frame(root, pady = 80)
mainUZ.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
fileLocation=tkinter.Frame(mainUZ, pady = 10)
fileLocation.pack(side="top", fill="both")
passwordFile=tkinter.Frame(mainUZ, pady = 10)
passwordFile.pack(side="top", fill="both")
loading=tkinter.Frame(mainUZ)
loading.pack(side="top", fill="both", expand=True, pady = 20)
button=tkinter.Frame(root, padx = 70, pady = 30)
button.pack(side="bottom", fill="x")

#title
labelTitle=tkinter.Label(titleUZ, text="UN-ZIPPER", height=1, width=12, font=font, bg="#564898", fg="white")
labelTitle.pack(side = "left", expand = YES, fill = BOTH)
labelWhite=tkinter.Label(titleUZ, text="", height=1, width=0, font=font)
labelWhite.pack(side = "left", expand = YES, fill = BOTH)
labelTultip=tkinter.Label(titleUZ, text="UN-ZIPPING COMPRESSED FILES WITH PASSCODES", height=1, width=46, font=font, bg="#564898", fg="#cac4e2")
labelTultip.pack(side = "left", expand = YES, fill = BOTH)

#FILE LOCATION 입력창
entryLocation = Entry(fileLocation, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
entryLocation.pack(side = "right", expand = YES, fill = X)

labelFL=tkinter.Label(fileLocation, text="FILE LOCATION: ", font=font)
labelFL.pack(side = "right")

#PASSWORD FILE 입력창
entryFile = Entry(passwordFile, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
entryFile.pack(side = "right", expand = YES, fill = X)

labelPF=tkinter.Label(passwordFile, text="PASSWORD FILE: ", font=font)
labelPF.pack(side = "right")

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
options = Button(button, text="INITIALIZE /\nACTIVATE", height=2, width=10, fg="black",bg="#ec6818", font=font, relief="flat")
options.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

unzip = Button(button, text="PAUSE", height=2, width=10, fg="black",bg="#e71b69", font=font, relief="flat")
unzip.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

backdoor = Button(button, text="RESUME", height=2, width=10, fg="black",bg="#ebda1d", font=font, relief="flat")
backdoor.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

ddos = Button(button, text="EXIT /\nTERMINATE", height=2, width=10, fg="black",bg="#5bb137", font=font, relief="flat")
ddos.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

root.mainloop()