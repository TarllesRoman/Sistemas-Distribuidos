#coding: utf-8

import time, hashlib, socket, json, Cryptpy

porta = 19199
serverPort = 19197

class Host:
    def __init__(self, ip, senha):
        self.ip = ip
        self.crypto = Cryptpy.Cryptpy(senha)

def testeTcp(hostip):
    try:
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.settimeout(2)
        tcp.connect((hostip,porta))
        tcp.close()
        return True
    except:
        print ('Erro TCP')

def sendMsg(cmd, host):
    global serverPort
    try:
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        msg = str(cmd).encode("utf-8")
        udp.sendto(host.crypto.crypt(msg), (host.ip, serverPort))
        udp.close()

        udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp2.bind(('', serverPort))
        udp2.settimeout(5)
        resultado, serv = udp2.recvfrom(2048)
        udp2.close()
	result = host.crypto.decrypt(resultado)
        return result.encode("utf-8")
    except Exception as e:
        print ('Nao conectado no servidor')
        print ('Exception: ',e)


def MsgJson(operacao, dia, tanque, quantidade, horarios):
    msgJson = {
        "operacao" : operacao,
        "alimentacao" : {
            "dia" : dia,
            "tanque" : tanque,
            "quantidade" : quantidade,
            "horarios" : horarios
            }
        }
    return msgJson
           
def listar(host):
    if(testeTcp(host.ip)):
        myJson = MsgJson("listar", "00/00/00", 0, 0, ["00:00", "00:00"])
        return sendMsg(json.dumps(myJson), host)

def adicionar(host, dia, tanque, quantidade, horarios):
    if(testeTcp(host.ip)):
        myJson = MsgJson("adicionar", dia, tanque, quantidade, horarios)
        return sendMsg(json.dumps(myJson), host)

def remover(host, dia, tanque, quantidade, horarios):
    if(testeTcp(host.ip)):
        myJson = MsgJson("remover", dia, tanque, quantidade, horarios)
        return sendMsg(json.dumps(myJson), host)

