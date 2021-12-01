from __future__ import print_function
import zipfile
import optparse
import itertools
from threading import Thread

def extractFile(zFile, password):                                                                           # zip파일이랑 패스워드를 인자로 받아서 압축을 해제하는 함수
    try:
        zFile.extractall(pwd=password)
        print('[+] Password = ' + password + "\n")
    except:                                                                                                 # 에러가 나면 그냥 끝냄
        pass    
    
def main():
    chars = '0123456789abcdefghijklmnopqustuvwxyz'
    
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile>")                          # 프로그램 메인 실행 로직 zip파일이랑 dictinoary를 인자로 받아야 된다는걸 알림
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")                           # f 옵션은 zname 변수로 저장되며 zipfile 의미

    (options, args) = parser.parse_args()                                                                   # f 인자로 받은걸 options.zname에 저장
    if (options.zname == None):                                                   # 인자를 입력하지 않았다면 프로그램 사용법을 출력하고 프로그램 끝냄
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
    zFile = zipfile.ZipFile(zname)                               
    for length in range(4,5):                                                       #4자리수                                     
        for password in itertools.product(chars,repeat=length):                     #product는 for와 동일 repeat = 4 -> 4자릿수로 뽑아낸다.
            print(password)
            print(''.join(password))                                                #튜플값이기 때문에 join으로 합쳐줌 
            t = Thread(target=extractFile, args=(zFile, password))
            t.start()
        
if __name__ == '__main__':                                                                                  # 본인이 메인함수 일 경우에만 실행
    main()
