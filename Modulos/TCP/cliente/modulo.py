#coding: utf-8

import socket

host = '127.0.0.1'
porta = 19198

dicops = {'+' : 'som',
		  '-' : 'sub',
		  '*' : 'mul',
		  '/' : 'div'
}


def sendmsg(cmd):
	try:
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp.connect((host,porta))
		print(cmd)
		tcp.sendall(bytes(cmd, 'utf-8'))
		resultado = tcp.recv(1024)
		tcp.close()
		print ('\033[0;31;40mExecutado do servidor!!!!\033[m')
		print (resultado.decode('utf-8'))
	except:
		print ('\033[0;31;40mNao conectado no servidor\033[m')


def soma(num1, num2, op):
	cmd = dicops[op]+'#'+num1+'#'+num2
	sendmsg(cmd)


def divisao(num1, num2, op):
	cmd = dicops[op]+'#'+num1+'#'+num2
	sendmsg(cmd)


def multiplicao(num1, num2, op):
	cmd = dicops[op]+'#'+num1+'#'+num2
	sendmsg(cmd)
	
	
def subtracao(num1, num2, op):
	cmd = dicops[op]+'#'+num1+'#'+num2
	sendmsg(cmd)
