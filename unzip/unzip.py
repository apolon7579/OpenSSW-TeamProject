from __future__ import print_function
import zipfile
import optparse
import os
from threading import Thread
def extractFile(zFile, password):                                                                           # zip파일이랑 패스워드를 인자로 받아서 압축을 해제하는 함수
    try:
        zFile.extractall(pwd=password.encode())
        print('[+] Password = ' + password + "\n")
    except Exception as e:                                                                                       # 에러가 나면 그냥 끝냄
        pass

def zipdict_attack(zFile, passFile):
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")                          # 프로그램 메인 실행 로직 zip파일이랑 dictinoary를 인자로 받아야 된다는걸 알림
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")                           # f 옵션은 zname 변수로 저장되며 zipfile 의미
    parser.add_option("-d", dest="dname", type="string", help="specify dictionary file")                    # d 옵션은 dname 변수로 지정되며 dictinary file 의미
    (options, args) = parser.parse_args()                                                                   # f와 d 인자로 받은걸 options.zname, options.dname에 저장
    if (options.zname == None) | (options.dname == None):                                                   # 인자를 입력하지 않았다면 프로그램 사용법을 출력하고 프로그램 끝냄
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)                                 
    passFile = open(dname)                                                                                  # dictionary 파일을 열어서 공백을 제거한 후 extractfile 함수를 실행하는 스레드에 각각 넣고 돌림 
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
if __name__ == '__main__':                                                                                  # 본인이 메인함수 일 경우에만 실행
    main()

