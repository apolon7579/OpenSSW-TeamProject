from tkinter import *
from math import *
import tkinter.font
import tkinter.ttk
from tkinter import filedialog
import os

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.geometry("1920x1080")
        self.switch_frame(Sscreen)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Sscreen(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        titleSs=tkinter.Frame(self)
        titleSs.pack(side="top", anchor="center", ipady=170, expand = YES, fill = BOTH)
        buttonSs=tkinter.Frame(self, padx = 70, pady = 30)
        buttonSs.pack(side="bottom", anchor="s", ipady=150, expand = YES, fill = BOTH)

        #버튼 입력창
        pycurity = Button(titleSs, text="PY-CURITY", height=1, width=10, fg="white",bg="#564898", font=font, relief="flat")
        pycurity.pack(side = "left", anchor = "center", padx = 600, expand = YES, fill = X)

        start = Button(buttonSs, text="START", height=1, width=10, fg="black",bg="#ec681a", font=font, relief="flat", command=lambda: master.switch_frame(Mmenu))
        start.pack(side = "left", anchor = "s", padx = 200, expand = YES, fill = X)

        exit = Button(buttonSs, text="EXIT", height=1, width=10, fg="black",bg="#5db134", font=font, relief="flat")
        exit.pack(side = "left", anchor = "s", padx = 200, expand = YES, fill = X)

class Mmenu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")
        font2 = tkinter.font.Font(family="Malgun Gothic", size=22, weight="bold", slant="italic")

        #프레임 설정
        titleMm=tkinter.Frame(self, padx=500)
        titleMm.pack(side="top", fill="x", expand=True, anchor="n", ipady=70)
        buttonMm1=tkinter.Frame(self, padx=100, pady=50)
        buttonMm1.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady=10)
        buttonMm2=tkinter.Frame(self, pady=50)
        buttonMm2.pack(side="top", fill="both", pady=10)
        warning=tkinter.Frame(self)
        warning.pack(side="top", fill="both", expand=True, pady = 100)

        #버튼 입력창
        options = Button(titleMm, text="OPTIONS", height=1, width=10, fg="black",bg="white", font=font, relief="flat")
        options.pack(side = "left", anchor = "center", padx = 50, expand = YES, fill = X)

        unzip = Button(buttonMm1, text="UNZIP", height=1, width=10, fg="#564898",bg="white", font=font, relief="flat", command=lambda: master.switch_frame(UnZipper))
        unzip.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        backdoor = Button(buttonMm1, text="BACKDOOR", height=1, width=10, fg="#564898",bg="white", font=font, relief="flat", command=lambda: master.switch_frame(Backdoor))
        backdoor.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        ddos = Button(buttonMm2, text="D-DOS", height=1, width=10, fg="#564898",bg="white", font=font, relief="flat", command=lambda: master.switch_frame(DDos))
        ddos.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        portscan = Button(buttonMm2, text="PORT SCAN", height=1, width=10, fg="#564898",bg="white", font=font, relief="flat", command=lambda: master.switch_frame(PortScan))
        portscan.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        ssh = Button(buttonMm2, text="SSH", height=1, width=10, fg="#564898",bg="white", font=font, relief="flat", command=lambda: master.switch_frame(SSH))
        ssh.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        #워닝소리
        labelWarn=tkinter.Label(warning, text="!WARNING:\nUNAUTHORIZED ATTEMPT OF THESE PROTOCOLS MAY CAUSE LEGAL ISSUES DEPENDING ON YOUR COUNTRY'S REGULATIONS.", font=font2, fg="#e9511c")
        labelWarn.pack(side = "bottom", expand = YES, fill = BOTH)

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
        self.labelFL = tkinter.Label(fileLocation, text="", relief="solid", width=10, font=tkinter.font.Font(family="Malgun Gothic", size=20))
        self.labelFL.pack(side = "right", expand = YES, fill = X)

        buttonFL=Button(fileLocation, text="FILE LOCATION: ", font=font, command=self.findFL)
        buttonFL.pack(side = "right")

        #PASSWORD FILE 입력창
        self.labelPF = tkinter.Label(passwordFile, text="", relief="solid", width=10, font=tkinter.font.Font(family="Malgun Gothic", size=20))
        self.labelPF.pack(side = "right", expand = YES, fill = X)

        buttonPF=Button(passwordFile, text="PASSWORD FILE: ", font=font, command=self.findPF)
        buttonPF.pack(side = "right")

        #버튼 입력창
        init = Button(button, text="INITIALIZE /\nACTIVATE", height=2, width=10, fg="black",bg="#ec6818", font=font, relief="flat")
        init.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        exit = Button(button, text="EXIT /\nTERMINATE", height=2, width=10, fg="black",bg="#5bb137", font=font, relief="flat", command=lambda: master.switch_frame(Mmenu))
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

    def findFL(self):
        fname = filedialog.askopenfile(mode='w', filetypes=[('Zip Files', '*.zip')])
        self.labelFL.configure(text=format(fname))
    def findPF(self):
        fname = filedialog.askopenfile(mode='w', filetypes=[('Txt Files', '*.txt')])
        self.labelPF.configure(text=format(fname))

class Backdoor(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        titleBD=tkinter.Frame(self)
        titleBD.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        mainBD=tkinter.Frame(self, pady = 100)
        mainBD.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        ip=tkinter.Frame(mainBD)
        ip.pack(side="top", fill="both", pady = 50)
        loading=tkinter.Frame(mainBD)
        loading.pack(side="top", fill="both", expand=True, pady = 50)
        button=tkinter.Frame(self, padx = 70, pady = 30)
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

        exit = Button(button, text="EXIT /\nTERMINATE", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat", command=lambda: master.switch_frame(Mmenu))
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

class DDos(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        title=tkinter.Frame(self)
        title.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        main=tkinter.Frame(self, pady = 100)
        main.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        ip=tkinter.Frame(main)
        ip.pack(side="top", fill="both", pady = 50)
        loading=tkinter.Frame(main)
        loading.pack(side="top", fill="both", expand=True, pady = 50)
        button=tkinter.Frame(self, padx = 70, pady = 30)
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

        exit = Button(button, text="EXIT /\nTERMINATE", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat", command=lambda: master.switch_frame(Mmenu))
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

class SSH(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        titleSSH=tkinter.Frame(self)
        titleSSH.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        mainSSH=tkinter.Frame(self, pady = 100)
        mainSSH.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        ip=tkinter.Frame(mainSSH)
        ip.pack(side="top", fill="both", pady = 50)
        loading=tkinter.Frame(mainSSH)
        loading.pack(side="top", fill="both", expand=True, pady = 50)
        button=tkinter.Frame(self, padx = 70, pady = 30)
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

        exit = Button(button, text="EXIT /\nTERMINATE", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat", command=lambda: master.switch_frame(Mmenu))
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

class PortScan(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        titlePS=tkinter.Frame(self)
        titlePS.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        mainPS=tkinter.Frame(self, pady = 100)
        mainPS.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        ip=tkinter.Frame(mainPS)
        ip.pack(side="top", fill="both", pady = 50)
        loading=tkinter.Frame(mainPS)
        loading.pack(side="top", fill="both", expand=True, pady = 50)
        button=tkinter.Frame(self, padx = 70, pady = 30)
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

        exit = Button(button, text="EXIT /\nTERMINATE", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat", command=lambda: master.switch_frame(Mmenu))
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()