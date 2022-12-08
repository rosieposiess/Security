"""
file-recovery program 은 사용자가 암호화된 파일을 복호화 하기 위해 사용되어야
하며, step 2)에서 생성된 “.enc” 형태의 암호화된 파일을 step 5)에서 복호화 된 키를
사용하여 복호화 해야 한다.
"""

from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import glob,os
from ransomware import iv

#공격자가 key.txt(b64꼴 string) 보내주면
#그 키로.enc로 끝나는 파일을 사용자는 가지고 AES복호화

key_file=open('key.txt','rt') #ransome을 주고 공격자에게 받은 key.txt 파일
enc_list=glob.glob("./*.enc")
key = key_file.read()
aes_key = b64decode(key.encode('utf-8'))

for file in enc_list:
    try:
        enc=open(file,'rt')
        dec=open(file[2:-4]+".txt","wt")
        # ct=평문->utf인코딩->b64인코딩->utf디코딩
        enc_txt=enc.read().encode('utf-8') # base64 타입으로 다시 바꿔주기 위해서는 utf-8으로 인코딩 먼저해줘야함
        ct = b64decode(enc_txt)

        cipher = AES.new(aes_key, AES.MODE_CBC, iv=iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        pt = pt.decode('utf-8')
        dec.write(pt) #pt를 다시 써준다
        enc.close()
        dec.close()
        os.remove(file)
    except ValueError:
          print("Incorrect decryption")
    except KeyError:
            print("Incorrect Key")

key_file.close()
os.remove("key.txt") #key.txt는 지운다


