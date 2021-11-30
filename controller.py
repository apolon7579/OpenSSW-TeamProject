from tkinter import *
import tkinter as tk
#from Start_Screen import *
#from Main_Menu import *
#from backdoor import *
#from un_zipper import *

root = tk.Tk()
root.geometry("1920x1080")

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

class SampleApp(tk.Tk):
  def __init__(self):
    tk.Tk.__init__(self)
    self._frame = None
    self.switch_frame(sscreen)

  def switch_frame(self,frame_class):
    new_frame = frame_class(self)
    if self._frame is not None:
      self._frame.destroy()
    self._frame=new_frame
    self._frame.pack()

class sscreen(tk.Frame):
  def __init__(self, master):
    tk.Frame.__init__(self,master)
    tk.Button(self, text = "PY-CURITY", font = ("Malgun Gothic", int(w/40)),height = int(w/800), width = int(w/150), fg = "white",bg = "#8551fe").place(relx=0.5,rely=0.27,anchor=CENTER,)
    tk.Button(self, text = "START",  font = ("Malgun Gothic", int(w/40)), anchor=CENTER, height = int(w/800), width = int(w/150), fg = "black",bg = "#ec681a", command=lambda:master.switch_frame(mmenu)).place(relx=0.33,rely=0.60)
    tk.Button(self, text = "EXIT", font = ("Malgun Gothic", int(w/40)), height = int(w/800), width = int(w/150), fg = "black",bg = "#5db134", command=self.quit).place(relx=0.66,rely=0.60,anchor=CENTER)

class mmenu(tk.Frame):
  def __init__(self, master):
    tk.Frame.__init__(self,master)
    tk.Button(self, text = "OPTIONS", height = int(w/800), width = int(w/100), fg = "black",bg = "white",).place(relx=0.5,rely=0.17,anchor=CENTER)
    tk.Button(self, text = "UNZIP", height = int(w/800), width = int(w/150), fg = "#8551fe",bg = "white").place(relx=0.33,rely=0.42,anchor=CENTER)
    tk.Button(self, text = "BACKDOOR", height = int(w/800), width = int(w/150), fg = "#8551fe",bg = "white").place(relx=0.66,rely=0.42,anchor=CENTER)
    tk.Button(self, text = "D-DOS", height = int(w/800), width = int(w/150), fg = "#8551fe",bg = "white").place(relx=0.25,rely=0.7,anchor=CENTER)
    tk.Button(self, text = "PORT SCAN", height = int(w/800), width = int(w/150), fg = "#8551fe",bg = "white").place(relx=0.5,rely=0.7,anchor=CENTER)
    tk.Button(self, text = "SSH", height = int(w/800), width = int(w/150), fg = "#8551fe",bg = "white").place(relx=0.75,rely=0.7,anchor=CENTER)

app = SampleApp()
app.mainloop()