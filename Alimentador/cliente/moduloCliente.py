#coding: utf-8

import time
import hashlib
import socket
import json
host = '192.168.0.103'
porta = 19199
serverPort = 19197


def testeTcp():
    try:
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.settimeout(2)
        tcp.connect((host,porta))
        tcp.close()
        return True
    except:
        print ('Erro TCP')

def sendMsg(cmd):
    global host, serverPort
    try:
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.sendto(str(cmd).encode("utf-8"), (host, serverPort))
        udp.close()

        udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp2.bind(('', serverPort))
        udp2.settimeout(5)
        resultado, serv = udp2.recvfrom(2048)
        udp2.close()
        

        return resultado.decode('utf-8')
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
           
def listar():
    if(testeTcp()):
        myJson = MsgJson("listar", "00/00/00", 0, 0, ["00:00", "00:00"])
        return sendMsg(json.dumps(myJson))

def adicionar(dia, tanque, quantidade, horarios):
    if(testeTcp()):
        myJson = MsgJson("adicionar", dia, tanque, quantidade, horarios)
        return sendMsg(json.dumps(myJson))

def remover(dia, tanque, quantidade, horarios):
    if(testeTcp()):
        myJson = MsgJson("remover", dia, tanque, quantidade, horarios)
        return sendMsg(json.dumps(myJson))

