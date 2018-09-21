#coding: utf-8

import time
import hashlib
import socket
host = '10.3.1.69'
porta = 19199
serverPort = 19198


dicops = {'+' : 'som',
		  '-' : 'sub',
		  '*' : 'mul',
		  '/' : 'div'
}

def connecTcp():
	try:
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp.settimeout(2)
		tcp.connect((host,porta))
		tcp.close()
		return True
	except:
		print ('ERRO')

def sendmsg(cmd):
	global host, serverPort
	try:
		udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp.sendto(bytes(cmd, 'utf-8'), (host, serverPort))
		udp.close()
		udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp.bind(('', serverPort))
		udp.settimeout(3)
		resultado, serv = udp.recvfrom(2048)
		udp.close()
		print ('\033[0;31;40mExecutado do servidor!!!!\033[m')
		print (resultado.decode('utf-8'))
	except Exception as e:
		print ('\033[0;31;40mNao conectado no servidor\033[m')
		print ('Exception: ',e)


def soma(num1, num2, op):
	cmd = dicops[op]+'#'+num1+'#'+num2
	cmd = hashlib.md5(cmd.encode('utf8')).hexdigest()+'#'+cmd
	if connecTcp():
		sendmsg(cmd)
	else:
		print('Sem conexao no servidor')


def divisao(num1, num2, op):
	cmd = dicops[op]+'#'+num1+'#'+num2
	cmd = hashlib.md5(cmd.encode('utf8')).hexdigest()+'#'+cmd
	if connecTcp():
		sendmsg(cmd)
	else:
		print('Sem conexao no servidor')


def multiplicao(num1, num2, op):
	cmd = dicops[op]+'#'+num1+'#'+num2
	cmd = hashlib.md5(cmd.encode('utf8')).hexdigest()+'#'+cmd
	if connecTcp():
		sendmsg(cmd)
	else:
		print('Sem conexao no servidor')
	
	
def subtracao(num1, num2, op):
	cmd = dicops[op]+'#'+num1+'#'+num2
	cmd = hashlib.md5(cmd.encode('utf8')).hexdigest()+'#'+cmd
	if connecTcp():
		sendmsg(cmd)
	else:
		print('Sem conexao no servidor')
