
import sys
from zipfile import * 


def unzipfile(filename,pw):
    try:
        filename.extractall(pwd=pw)
        #print(pw)
        return 1 #압축 풀기에 성공하면 1 반환
    except:
        pass

#zip 파일 받기
try:
    zip_file=ZipFile(sys.argv[1]) #zip 파일 이름 받기
except:
    print("bad")
 

name=sys.argv[2]
    #dictionary 파일 받기   
try:
        dict=open(name,'r')
except FileNotFoundError:
        print("File doesn't exist!")  
lines=dict.readlines()
for line in lines:
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

