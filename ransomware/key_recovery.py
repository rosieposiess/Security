"""
key-recovery 프로그램은 암호화된 키(key.bin)을 복호화하고 이를 base64
형태로 key.txt 에 저장한다.
"""
#aes 키는 바이트 형태로 저장되어있음 현재 ㅇㅇ
from Crypto.PublicKey import RSA
from base64 import b64encode
from Crypto.Cipher import PKCS1_OAEP

enc_key = open("./key.bin","rb") #RSA로 encypt된 바이트 형태의 키가 저장되어 있는 파일을 rb로 엶
dec_key = open("./key.txt","wt") #encrypt한 키를 decrypt해서 base64꼴로 저장

key_text = enc_key.read()
priv_key = RSA.import_key(open("private.pem").read()) #비밀키 불러옴

cipher=PKCS1_OAEP.new(priv_key)
key=cipher.decrypt(key_text)
dec_key.write(b64encode(key).decode('utf-8'))#b64로 변환 후 string으로 바꿔서 저장

enc_key.close()
dec_key.close()
