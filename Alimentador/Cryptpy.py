from Crypto.Cipher import AES

"""Classe para cryptografar mensagens utilizando o metodo AES"""
class Cryptpy:
    def __init__(self,key):
        self.key = self.fill_text(key)
        self.aes = AES.new(self.key, AES.MODE_ECB)

    def crypt(self, text):
        t = self.fill_text(text)
        return self.aes.encrypt(str(t))
    
    def decrypt(self, text):
        d = self.aes.decrypt(text)
        return d.decode("utf-8").replace("#","")

    def fill_text(self, text):
        return str(text)+'#'*(16-len(str(text))%16)

"""
c = Cryptpy("bananabanabofana")
tc = c.crypt("")
td = c.decrypt(tc)
print("\nCRYPTED: "+str(tc))
print("\nDECRYPTED: "+str(td))
"""