from tkinter import *
from math import *
import tkinter.font
import tkinter.ttk
from tkinter import filedialog
from zipfile import ZipFile
from port_scan import port_scanner
from unzip import unzip
from Ddos import multiserver
import threading
import time

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
        titleMm=tkinter.Frame(self, padx=500, pady=100)
        titleMm.pack(side="top", fill="x", expand=True, anchor="n", ipady=70)
        buttonMm=tkinter.Frame(self, padx=100, pady=100)
        buttonMm.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady=10)
        warning=tkinter.Frame(self)
        warning.pack(side="top", fill="both", expand=True, pady = 100)

        #버튼 입력창
        options = Button(titleMm, text="OPTIONS", height=1, width=10, fg="black",bg="white", font=font, relief="flat", command=lambda: master.switch_frame(Sscreen))
        options.pack(side = "left", anchor = "center", padx = 50, expand = YES, fill = X)

        unzip = Button(buttonMm, text="UNZIP", height=1, width=10, fg="#564898",bg="white", font=font, relief="flat", command=lambda: master.switch_frame(UnZipper))
        unzip.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        ddos = Button(buttonMm, text="D-DOS", height=1, width=10, fg="#564898",bg="white", font=font, relief="flat", command=lambda: master.switch_frame(DDos))
        ddos.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        portscan = Button(buttonMm, text="PORT SCAN", height=1, width=10, fg="#564898",bg="white", font=font, relief="flat", command=lambda: master.switch_frame(PortScan))
        portscan.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

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
        mainUZ.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 40)
        fileLocation=tkinter.Frame(mainUZ, pady = 10)
        fileLocation.pack(side="top", fill="both")
        passwordFile=tkinter.Frame(mainUZ, pady = 10)
        passwordFile.pack(side="top", fill="both")
        result=tkinter.Frame(mainUZ, pady = 40)
        result.pack(side="top", fill="both", expand=True)
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
        self.labelFL = tkinter.Label(fileLocation, text="", relief="solid", width=15, bg="white", font=tkinter.font.Font(family="Malgun Gothic", size=20))
        self.labelFL.pack(side = "right", expand = YES, fill = X)

        buttonFL=Button(fileLocation, text="FILE LOCATION: ", font=font, command=self.findFL)
        buttonFL.pack(side = "right")

        #PASSWORD FILE 입력창
        self.labelPF = tkinter.Label(passwordFile, text="", relief="solid", width=15, bg="white", font=tkinter.font.Font(family="Malgun Gothic", size=20))
        self.labelPF.pack(side = "right", expand = YES, fill = X)

        buttonPF=Button(passwordFile, text="PASSWORD FILE: ", font=font, command=self.findPF)
        buttonPF.pack(side = "right")

        #압축파일 비밀번호 라벨
        self.labelResult=tkinter.Label(result, text="PASSWORD IS: ", font=font, fg="red")
        self.labelResult.pack(side = "bottom")

        #버튼 입력창
        init = Button(button, text="START", height=2, width=10, fg="black",bg="#ec6818", font=font, relief="flat", command=self.unzip_attack)
        init.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        exit = Button(button, text="EXIT", height=2, width=10, fg="black",bg="#5bb137", font=font, relief="flat", command=lambda: master.switch_frame(Mmenu))
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        self.zipfile_path = ""
        self.passfile_path = ""
    def findFL(self):
        fname = filedialog.askopenfile(mode='r', filetypes=[('Zip Files', '*.zip')])
        self.labelFL.configure(text=format(fname.name))
        self.zipfile_path = fname.name
        fname.close()

    def findPF(self):
        fname = filedialog.askopenfile(mode='r', filetypes=[('Txt Files', '*.txt')])
        self.labelPF.configure(text=format(fname.name))
        self.passfile_path = fname.name
        fname.close()

    def unzip_attack(self):
        zip_path = self.zipfile_path
        pass_path = self.passfile_path

        zip_path = zip_path.replace("\\", "/", 10)
        pass_path = pass_path.replace("\\", "/", 10)

        zfile = ZipFile(zip_path)
        passFile = open(pass_path)
        unzip.zipdict_attack(zfile, passFile)
        passFile.close()
        
        text_pwd = "PASSWORD IS : " + unzip.passwd
        self.labelResult.configure(text=text_pwd)

class DDos(Frame): #start 버튼을 누르면 공격중이라는 팝업이 떴으면 좋겠음 팝업을 끄면 공격이 중지되는 방식으로 작동
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
        port=tkinter.Frame(main)
        port.pack(side="top", fill="both", expand=True, pady = 50)
        status=tkinter.Frame(main)
        status.pack(side="top", fill="both", expand=True, pady = 10)
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
        self.entry = Entry(ip, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
        self.entry.pack(side = "right", expand = YES, fill = X)

        labelIp=tkinter.Label(ip, text="IP: ", font=font)
        labelIp.pack(side = "right")

        #port 입력창
        self.entry2 = Entry(port, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
        self.entry2.pack(side = "right", expand = YES, fill = X)

        labelPort=tkinter.Label(port, text="PORT: ", font=font)
        labelPort.pack(side = "right")

        self.labelStat=tkinter.Label(status, text="", font=font, fg="red")
        self.labelStat.pack(side = "bottom")

        #버튼 입력창
        init = Button(button, text="START", height=1, width=10, fg="black",bg="#ec6818", font=font, relief="flat", command=self.textAttack)
        init.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        stop = Button(button, text="STOP", height=1, width=10, fg="black",bg="#ec6818", font=font, relief="flat", command=self.textStop)
        stop.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        exit = Button(button, text="EXIT", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat", command=lambda: master.switch_frame(Mmenu))
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

    def textAttack(self):
        ip = self.entry.get()
        port = self.entry2.get()
        self.labelStat.configure(text="ATTACKING...")

        addr = "http://" + ip + ":" + port

        multiserver.put_data = "ddos attack " + addr
        time.sleep(3)
        multiserver.put_data = "wait..."
    def textStop(self):
        self.labelStat.configure(text="")
        multiserver.put_data = "quit"
        
class PortScan(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        font = tkinter.font.Font(family="Malgun Gothic", size=40, weight="bold", slant="italic")

        #프레임 설정
        titlePS=tkinter.Frame(self)
        titlePS.pack(side="top", fill="x", expand=True, anchor="n", ipady=40)
        mainPS=tkinter.Frame(self, pady = 100)
        mainPS.pack(side="top", padx = 100, fill="both", expand=True, anchor="n", pady = 10)
        ipPS=tkinter.Frame(mainPS)
        ipPS.pack(side="top", fill="both", pady = 50)
        portPS=tkinter.Frame(mainPS)
        portPS.pack(side="top", fill="both", expand=True, pady = 50)
        result=tkinter.Frame(mainPS)
        result.pack(side="top", fill="both", expand=True)
        button=tkinter.Frame(self, padx = 70, pady = 30)
        button.pack(side="bottom", fill="x")

        #title
        labelTitle=tkinter.Label(titlePS, text="PORT SCAN", height=1, width=12, font=font, bg="#564898", fg="white")
        labelTitle.pack(side = "left", expand = YES, fill = BOTH)
        labelWhite=tkinter.Label(titlePS, text="", height=1, font=font)
        labelWhite.pack(side = "left", expand = YES, fill = BOTH)
        labelTultip=tkinter.Label(titlePS, text="SCANNING IF THERE'S ANY OPEN PORT", height=1, width=46, font=font, bg="#564898", fg="#cac4e2")
        labelTultip.pack(side = "left", expand = YES, fill = BOTH)

        #ip, port 입력창
        self.entry = Entry(ipPS, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
        self.entry.pack(side = "right", expand = YES, fill = X)

        labelIp=tkinter.Label(ipPS, text="IP: ", font=font)
        labelIp.pack(side = "right")

        self.entry2 = Entry(portPS, relief="flat", font=font, highlightthickness=5, highlightbackground="gray")
        self.entry2.pack(side = "right", expand = YES, fill = X)

        labelPort=tkinter.Label(portPS, text="PORT: ", font=font)
        labelPort.pack(side = "right")

        #PORT 오픈 여부 라벨
        self.labelResult=tkinter.Label(result, text="PORT IS: ", font=font, fg="red")
        self.labelResult.pack(side = "bottom")

        #버튼 입력창
        init = Button(button, text="START", height=1, width=10, fg="black",bg="#ec6818", font=font, relief="flat", command=self.scanPS)
        init.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)

        exit = Button(button, text="EXIT", height=1, width=10, fg="black",bg="#5bb137", font=font, relief="flat", command=lambda: master.switch_frame(Mmenu))
        exit.pack(side = "left", anchor = "s", padx = 50, expand = YES, fill = X)
    
    def scanPS(self): #함수를 command 안에 그냥 넣으면 이상하게 에러가 나서 scanPS 안에 가둬놨습니다
        msg = port_scanner.connScan(self.entry.get(), int(self.entry2.get()))
        self.labelResult.configure(text = msg)

if __name__ == "__main__":
    t = threading.Thread(target=multiserver.start_server)
    t.daemon = True
    t.start()
    app = SampleApp()
    app.mainloop()
