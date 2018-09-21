#coding: utf-8

TCP_port = 19199
UDP_port = 19198

from socket import *
import subprocess
import commands
import modulo

TCPSocket = socket(AF_INET,SOCK_STREAM)
TCPSocket.bind(('', TCP_port))
TCPSocket.listen(1)

receiver_socket = socket(AF_INET, SOCK_DGRAM)
receiver_socket.bind(('', UDP_port))

sender_socket = socket(AF_INET, SOCK_DGRAM)

tm_buffer = 2048

dic_operacoes = { 
	'som':modulo.soma,
	'sub':modulo.subtracao,
	'div':modulo.divisao,
	'mul':modulo.multiplicacao
}

while True:
	print "Server pronto para aceitar conexao"
	
	try:
		conexao, cliente = TCPSocket.accept()
		print "Conexao aceita"
		conexao.close()
	except:
		conexao.close()
	
	try:
		message, client = receiver_socket.recvfrom(2048)
						
		print "Mensagem recebida: ",message.decode("utf-8")
		msg_split = message.split('#') 
		operacao = msg_split[0]
		num1 = int(msg_split[1])
		num2 = int(msg_split[2])
		
		resultado = dic_operacoes[operacao](num1,num2)
		dest = (client[0],UDP_port)
		sender_socket.sendto(str(resultado),dest)
		print "dest",dest
		
	except:
		receiver_socket.close()
		conexao.close()
		sender_socket.close()
