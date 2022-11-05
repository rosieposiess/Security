
import sys
from zipfile import * 


def unzipfile(filename,pw): #압축푸는 함수
    try: 
        filename.extractall(pwd=pw)
        #print(pw)
        return 1 #압축 풀기에 성공하면 1 반환
    except: #압축풀기에 실패하면 그냥 패스
        pass

#zip 파일 받기
try:
    zip_file=ZipFile(sys.argv[1]) #zip 파일 이름 받기
except:
    print("bad")
 

pwfile=["dict1.lst","dict2.lst","dict3.lst","dict4.lst","dict5.lst","dict6.lst","dict7.lst","dict8.lst","dict9.lst","dict10.lst","dict11.lst","dict12.lst"]
for name in pwfile: #반복문으로 하나하나 딕셔너리 파일 받음
    #dictionary 파일 받기   
    try:
        dict=open(name,'r')
    except FileNotFoundError:
        print("File doesn't exist!")  
    lines=dict.readlines() #파일 안의 줄들을 원소로 갖는 lines 생성
    for line in lines: #각 줄마다 반복문 돌리기
        pw=bytes(line.strip(), 'UTF-8') #string을 바이트로 바꿈
        result=unzipfile(zip_file,pw)
        #dictionary file의 각 줄의 내용을 엔터 지우고 하나하나 대입해봄
        if result==1: 
            print("pw:"+str(pw,'utf-8'))
            dict.close()
            break
        else:
            print(str(pw,'utf-8'))
            continue

