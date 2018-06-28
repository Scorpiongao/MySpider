from Crypto.Cipher import AES
import os
import json
import base64
import codecs


class Cracker():
	def __init__(self):
		self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
		self.nonce = '0CoJUm6Qyw8W8jud'
		self.pubKey = '010001'

	def get(self, text):
		text = json.dumps(text)
		secKey = self.createSecretKey(16)
		encText = self.aesEncrypt(self.aesEncrypt(text, self.nonce), secKey)
		encSecKey = self.rsaEncrypt(secKey, self.pubKey, self.modulus)
		post_data = {
					'params': encText,
					'encSecKey': encSecKey
					}
		print('[INFO]:Get params successfully...',post_data )
		return post_data

	def aesEncrypt(self, text, secKey):
		pad = 16 - len(text) % 16
		if isinstance(text, bytes):
			text = text.decode('utf-8')
		text = text + str(pad * chr(pad))
		encryptor = AES.new(secKey, 2, '0102030405060708')
		ciphertext = encryptor.encrypt(text)
		ciphertext = base64.b64encode(ciphertext)
		return ciphertext

	def rsaEncrypt(self, text, pubKey, modulus):
		text = text[::-1]
		rs = int(codecs.encode(text.encode('utf-8'), 'hex_codec'), 16) ** int(pubKey, 16) % int(modulus, 16)
		return format(rs, 'x').zfill(256)

	def createSecretKey(self, size):
		return (''.join(map(lambda xx: (hex(ord(xx))[2:]), str(os.urandom(size)))))[0:16]


if __name__ =="__main__":
    keyword='当你'
    search_type=1
    limit=10
    params = {
        's': keyword,
        'type': search_type,
        'offset': 0,
        'sub': 'false',
        'limit': limit
    }
    cracker=Cracker ()
    cracker.get(params)