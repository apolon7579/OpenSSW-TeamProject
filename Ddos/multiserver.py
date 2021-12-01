from socket import *
import threading

t = []
index = 0

class Cserver(threading.Thread):
  def __init__(self, socket):
    super().__init__()
    self.s_socket = socket

  def run(self):
    global index
    self.c_socket, addr = self.s_socket.accept()
    print(addr[0], addr[1], "이 연결되었습니다")
    index = index + 1
    creat_thread(self.s_socket)
    t=threading.Thread(target=self.c_recv)
    t.daemon=True
    t.start()

  def c_recv(self):
    
    while True:
      get_data=self.c_socket.recv(1024)
      print(get_data.decode('utf-8'))
  
  def c_send(self,put_data):
    self.c_socket.send(put_data.encode('utf-8'))

def creat_thread(s_socket):
  global index
  t.append(Cserver(s_socket))
  t[index].daemon=True
  t[index].start()

def start_server():
  s_socket = socket(AF_INET, SOCK_STREAM)
  ufsize=1024
  host='182.230.134.78'
  port=12345
  s_socket.bind((host,port))
  s_socket.listen(1)
  creat_thread(s_socket)

  while True:
    put_data = input("서버 입력 : ")
    if put_data=='1':
      break

    try:
      for i in t:
        i.c_send(put_data)
    except Exception as e:
      pass

  for j in t:
    try:
      j.c_socket.close()
    except Exception as e:
      pass
  s_socket.close()

if __name__ == '__main__':
  start_server()



