from __future__ import print_function
import optparse
from socket import *
from threading import *
screenLock = Semaphore(value=1)                                                                              #세마포어 객체를 screenLock에 저장 세마포어란 공유자원을 의미하는데 여기서는 공유자원을 1개로 설정함 공유자원이란 멀티스레드 프로그래밍에서 사용되는
def connScan(tgtHost, tgtPort):                                                                              #용어인데 여러개의 스레드가 한 메모리에 접근하려고 할 경우 스레드끼리 동시에 접근이 가능하면 문제가 생기기때문에 한 스레드가 메모리를 점유하고 있는
    try:                                                                                                     #경우 다른 스레드는 그 스레드가 메모리 사용이 끝날 떄 까지 대기하도록 해야함 이를 구현하기 위해서 세마포어 객체를 사용함
        connSkt = socket(AF_INET, SOCK_STREAM)                                                               #원격 주소(서버)에 연결하기위한 소켓 객체 생성 AF_INET은 ipv4 주소체계를 사용하겠다는 의미, SOCK_STREAM은 TCP를 사용해 연결하겠다는 의미
        connSkt.connect((tgtHost, tgtPort))                                                                  #지정한 ip와 port를 사용해 서버와 연결 시도
        connSkt.send("hackerman")                                                                            #연결이 되었다면 hackerman이라는 메세지를 보냄
        results = connSkt.recv(1024)                                                                         #1024바이트의 버퍼를 선언해서 서버에서 보내주는 응답 메세지를 받음
        screenLock.acquire()                                                                                 #다른 스레드가 접근 못하도록 lock을 걸음 출력같은 경우 출력하기 위한 모니터가 일종의 공유자원이기떄문
        print("[+] %d/tcp open" % (tgtPort))                                                                 #port가 오픈 되있다는 메세지를 출력
        print("[+] " + str(results))                                                                         #서버에서 받은 응답 메세지를 받음
    except:
        screenLock.acquire()                                                                                 #에러 또는 접속이 안되는경우 출력을 위해 lock을 걸고
        print("[-] %d/tcp closed" % tgtPort)                                                                 #연결이 닫혀있다는 메세지를 내보냄                                                                                         
    finally: 
        screenLock.release()                                                                                 #출력이 끝났으면 lock을 해제해 다른 스레드가 모니터를 사용할 수 있게 설정
        connSkt.close()                                                                                      #연결에 사용되었던 소켓 객체 역시 닫아줌
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)                                                                       #호스트 이름으로 아이피를 알려줌 ex) www.naver.com으로 ip를 입력했을 경우 네이버의 ip를 알려줌
    except:
        print("[-] Cannot resolve '%s': Unknown Host" % tgtHost)                                             #호스트 이름으로 아이피 알아내는게 불가능 할 경우 에러메세지 출력
        return
    try:
        tgtName = gethostbyaddr(tgtIP)                                                                       #반대로 ip 이름으로 host 이름을 가져옴
        print("\n[+] Scan Results for: " + tgtName[0])
    except:
        print("\n[+] Scan Results for: " + tgtIP)                                                            #불가능 할 경우 그냥 ip 출력
    setdefaulttimeout(1)                                                                                     #소켓의 응답시간을 설정함 만약 소켓에 있는 ip로 1초가 넘게 연결했을경우 연결할수 없는것으로 판단하고 연결을 끊음
    for tgtPort in tgtPorts:                                                                                 #인자로 입력받은 port 개수만큼 스레드를 생성해서 connScan 함수를 실행함
       t = Thread(target=connScan, args=(tgtHost, int(tgtPort.strip())))
       t.start()
def main():
    parser = optparse.OptionParser(('usage %prog -H <target host> -p <target port(s) separated by space>'))   #프로그램 실행시에 적절한 인자값을 넣지 않으면 인자값을 넣는 방법의 설명문이 나오도록 설정함 -H <ip번호> -p <포트번호> 형식으로 인자값 입력
    parser.add_option("-H", dest="tgtHost", type="string", help="specify tarhet host")                        #-H 뒤에 적히는 인자값은 string type의 tgtHost라는 변수로 저장하도록 설정
    parser.add_option("-p", dest="tgtPort", type="string", help="specify target port(s) separated by space")  #-p 뒤에 적히는 인자값은 string type의 tgtPort라는 변수로 저장하도록 설정
    (options, args) = parser.parse_args()                                                                     #tgtHost, tgtPort를 options, args를 조작해서 값을 가져올 수 있도록 설정
    tgtHost = str(options.tgtHost).strip()                                                                    #tgtHost값을 가져와서 tgtHost에 저장
    tgtPorts = [s.strip() for s in str(options.tgtPort).split(',')]                                           #tgtPorts값을 가져와서 tgtPort에 저장
    if (tgtHost == 'None') | (tgtPorts[0] == 'None'):                                                             #만약에 -H, -p 인자값중 하나라도 없다면 프로그램 설명을 출력하고 프로그램을 종료
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)                                                                               #tgtPorts안에 있는 port번호값을 모두 포트스캔시킴
if __name__ == "__main__":
    main()