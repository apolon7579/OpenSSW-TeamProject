from tkinter import *
from math import *
import tkinter.font
import tkinter.ttk

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.geometry("1920x1080")
        self.switch_frame(UnZipper)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class UnZipper(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        titleUZ=tkinter.Frame(self)
        titleUZ.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        mainUZ=tkinter.Frame(self, pady = 80)
        mainUZ.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        fileLocation=tkinter.Frame(mainUZ, pady = 10)
        fileLocation.pack(side="top", fill="both")
        passwordFile=tkinter.Frame(mainUZ, pady = 10)
        passwordFile.pack(side="top", fill="both")
        loading=tkinter.Frame(mainUZ)
        loading.pack(side="top", fill="both", expand=True, pady = 20)
        button=tkinter.Frame(self, padx = 70, pady = 30)
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
        init = Button(button, text="INITIALIZE /\nACTIVATE", height=2, width=10, fg="black",bg="#ec6818", font=font, relief="flat")
        init.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        pause = Button(button, text="PAUSE /\nBACKDOOR", height=2, width=10, fg="black",bg="#e71b69", font=font, relief="flat", command=lambda: master.switch_frame(PortScan))
        pause.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        resume = Button(button, text="RESUME", height=2, width=10, fg="black",bg="#ebda1d", font=font, relief="flat")
        resume.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        exit = Button(button, text="EXIT /\nTERMINATE", height=2, width=10, fg="black",bg="#5bb137", font=font, relief="flat")
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

class Backdoor(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        titleBD=tkinter.Frame(self, relief="solid", bd=2)
        titleBD.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        mainBD=tkinter.Frame(self, relief="solid", bd=2, pady = 100)
        mainBD.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        ip=tkinter.Frame(mainBD, relief="solid", bd=2)
        ip.pack(side="top", fill="both", pady = 50)
        loading=tkinter.Frame(mainBD, relief="solid", bd=2)
        loading.pack(side="top", fill="both", expand=True, pady = 50)
        button=tkinter.Frame(self, padx = 70, pady = 30, relief="solid", bd=2)
        button.pack(side="bottom", fill="x")

        #title
        labelTitle=tkinter.Label(titleBD, text="BACKDOOR", height=1, width=12, font=font, bg="#564898", fg="white")
        labelTitle.pack(side = "left", expand = YES, fill = BOTH)
        labelWhite=tkinter.Label(titleBD, text="", height=1, font=font)
        labelWhite.pack(side = "left", expand = YES, fill = BOTH)
        labelTultip=tkinter.Label(titleBD, text="INSTALL A BACKDOOR TO ANOTHER FIREWALL", height=1, width=46, font=font, bg="#564898", fg="#cac4e2")
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
        init = Button(button, text="INITIALIZE /\nACTIVATE", height=1, width=10, fg="black",bg="#ec6818", font=font, relief="flat")
        init.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        pause = Button(button, text="PAUSE", height=1, width=10, fg="black",bg="#e71b69", font=font, relief="flat")
        pause.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        resume = Button(button, text="RESUME", height=1, width=10, fg="black",bg="#ebda1d", font=font, relief="flat")
        resume.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        exit = Button(button, text="EXIT /\nTERMINATE", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat")
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

class DDos(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        title=tkinter.Frame(self, relief="solid", bd=2)
        title.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        main=tkinter.Frame(self, relief="solid", bd=2, pady = 100)
        main.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        ip=tkinter.Frame(main, relief="solid", bd=2)
        ip.pack(side="top", fill="both", pady = 50)
        loading=tkinter.Frame(main, relief="solid", bd=2)
        loading.pack(side="top", fill="both", expand=True, pady = 50)
        button=tkinter.Frame(self, padx = 70, pady = 30, relief="solid", bd=2)
        button.pack(side="bottom", fill="x")

        #title
        labelTitle=tkinter.Label(title, text="D-DOS", height=1, width=12, font=font, bg="#564898", fg="white")
        labelTitle.pack(side = "left", expand = YES, fill = BOTH)
        labelWhite=tkinter.Label(title, text="", height=1, font=font)
        labelWhite.pack(side = "left", expand = YES, fill = BOTH)
        labelTultip=tkinter.Label(title, text="INITIATE D-DOS PROTOCOL", height=1, width=46, font=font, bg="#564898", fg="#cac4e2")
        labelTultip.pack(side = "left", expand = YES, fill = BOTH)

        #ip 입력창
        entry = Entry(ip, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
        entry.pack(side = "right", expand = YES, fill = X)

        labelIp=tkinter.Label(ip, text="IP: ", font=font)
        labelIp.pack(side = "right")

        #프로그레스 바
        labelFin=tkinter.Label(loading, text="INITIATING COMPLETE!")
        labelFin.pack(side="top", anchor = "e")
        pb = tkinter.ttk.Progressbar(loading, maximum=100, mode="determinate")
        pb.pack(expand = YES, fill = BOTH)                       # 프로그래스 바 배치
        label0=tkinter.Label(loading, text="0%", font=font)
        label0.pack(side="left")
        label100=tkinter.Label(loading, text="100%", font=font)
        label100.pack(side="right")

        #버튼 입력창
        init = Button(button, text="INITIALIZE /\nACTIVATE", height=1, width=10, fg="black",bg="#ec6818", font=font, relief="flat")
        init.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        pause = Button(button, text="PAUSE", height=1, width=10, fg="black",bg="#e71b69", font=font, relief="flat")
        pause.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        resume = Button(button, text="RESUME", height=1, width=10, fg="black",bg="#ebda1d", font=font, relief="flat")
        resume.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        exit = Button(button, text="EXIT /\nTERMINATE", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat")
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

class SSH(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        titleSSH=tkinter.Frame(self, relief="solid", bd=2)
        titleSSH.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        mainSSH=tkinter.Frame(self, relief="solid", bd=2, pady = 100)
        mainSSH.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        ip=tkinter.Frame(mainSSH, relief="solid", bd=2)
        ip.pack(side="top", fill="both", pady = 50)
        loading=tkinter.Frame(mainSSH, relief="solid", bd=2)
        loading.pack(side="top", fill="both", expand=True, pady = 50)
        button=tkinter.Frame(self, padx = 70, pady = 30, relief="solid", bd=2)
        button.pack(side="bottom", fill="x")

        #title
        labelTitle=tkinter.Label(titleSSH, text="SSH", height=1, width=12, font=font, bg="#564898", fg="white")
        labelTitle.pack(side = "left", expand = YES, fill = BOTH)
        labelWhite=tkinter.Label(titleSSH, text="", height=1, font=font)
        labelWhite.pack(side = "left", expand = YES, fill = BOTH)
        labelTultip=tkinter.Label(titleSSH, text="INITIATE SSH BRUTE FORCE PROTOCOL", height=1, width=46, font=font, bg="#564898", fg="#cac4e2")
        labelTultip.pack(side = "left", expand = YES, fill = BOTH)

        #ip 입력창
        entry = Entry(ip, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
        entry.pack(side = "right", expand = YES, fill = X)

        labelIp=tkinter.Label(ip, text="IP: ", font=font)
        labelIp.pack(side = "right")

        #프로그레스 바
        labelFin=tkinter.Label(loading, text="INITIATING COMPLETE!")
        labelFin.pack(side="top", anchor = "e")
        pb = tkinter.ttk.Progressbar(loading, maximum=100, mode="determinate")
        pb.pack(expand = YES, fill = BOTH)                       # 프로그래스 바 배치
        label0=tkinter.Label(loading, text="0%", font=font)
        label0.pack(side="left")
        label100=tkinter.Label(loading, text="100%", font=font)
        label100.pack(side="right")

        #버튼 입력창
        init = Button(button, text="INITIALIZE /\nACTIVATE", height=1, width=10, fg="black",bg="#ec6818", font=font, relief="flat")
        init.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        pause = Button(button, text="PAUSE", height=1, width=10, fg="black",bg="#e71b69", font=font, relief="flat")
        pause.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        resume = Button(button, text="RESUME", height=1, width=10, fg="black",bg="#ebda1d", font=font, relief="flat")
        resume.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        exit = Button(button, text="EXIT /\nTERMINATE", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat")
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

class PortScan(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        titlePS=tkinter.Frame(self, relief="solid", bd=2)
        titlePS.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        mainPS=tkinter.Frame(self, relief="solid", bd=2, pady = 100)
        mainPS.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        ip=tkinter.Frame(mainPS, relief="solid", bd=2)
        ip.pack(side="top", fill="both", pady = 50)
        loading=tkinter.Frame(mainPS, relief="solid", bd=2)
        loading.pack(side="top", fill="both", expand=True, pady = 50)
        button=tkinter.Frame(self, padx = 70, pady = 30, relief="solid", bd=2)
        button.pack(side="bottom", fill="x")

        #title
        labelTitle=tkinter.Label(titlePS, text="PORT SCAN", height=1, width=12, font=font, bg="#564898", fg="white")
        labelTitle.pack(side = "left", expand = YES, fill = BOTH)
        labelWhite=tkinter.Label(titlePS, text="", height=1, font=font)
        labelWhite.pack(side = "left", expand = YES, fill = BOTH)
        labelTultip=tkinter.Label(titlePS, text="SCANNING IF THERE'S ANY OPEN PORT", height=1, width=46, font=font, bg="#564898", fg="#cac4e2")
        labelTultip.pack(side = "left", expand = YES, fill = BOTH)

        #ip 입력창
        entry = Entry(ip, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
        entry.pack(side = "right", expand = YES, fill = X)

        labelIp=tkinter.Label(ip, text="IP: ", font=font)
        labelIp.pack(side = "right")

        #프로그레스 바
        labelFin=tkinter.Label(loading, text="SCANNING COMPLETE!")
        labelFin.pack(side="top", anchor = "e")
        pb = tkinter.ttk.Progressbar(loading, maximum=100, mode="determinate")
        pb.pack(expand = YES, fill = BOTH)                       # 프로그래스 바 배치
        label0=tkinter.Label(loading, text="0%", font=font)
        label0.pack(side="left")
        label100=tkinter.Label(loading, text="100%", font=font)
        label100.pack(side="right")
        labelResult=tkinter.Label(loading, text="VULNERABLE/OPEN PORT NO.:", font=font, fg="red") #결과값 출력(변수 부분은 비워두었습니다.)
        labelResult.pack(side="bottom", anchor = "n")

        #버튼 입력창
        init = Button(button, text="INITIALIZE /\nACTIVATE", height=1, width=10, fg="black",bg="#ec6818", font=font, relief="flat")
        init.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        pause = Button(button, text="PAUSE", height=1, width=10, fg="black",bg="#e71b69", font=font, relief="flat")
        pause.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        resume = Button(button, text="RESUME", height=1, width=10, fg="black",bg="#ebda1d", font=font, relief="flat")
        resume.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        exit = Button(button, text="EXIT /\nTERMINATE", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat")
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()