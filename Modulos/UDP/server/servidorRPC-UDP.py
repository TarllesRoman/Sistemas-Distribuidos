#coding: utf-8

from socket import *
import hashlib
import server_modulo as modulo

TCP_port = 19199
UDP_port = 19198

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
	print ('Server pronto para aceitar conexao')
	
	try:
		conexao, cliente = TCPSocket.accept()
		print ('Conexao aceita')
		conexao.close()
	except:
		conexao.close()
	
	try:
		message, client = receiver_socket.recvfrom(2048)

		message = message.decode("utf-8")
						
		print ('Mensagem recebida: '+message)
		msg_split = message.split("#")
		msg_hash = msg_split[0]
		operacao = msg_split[1]
		num1 = int(msg_split[2])
		num2 = int(msg_split[3])
		msg_completa = operacao + '#' + str(num1) + '#' + str(num2)
		if(msg_hash == hashlib.md5(msg_completa.encode('utf-8')).hexdigest()):
			resultado = dic_operacoes[operacao](num1,num2)
			dest = (client[0],UDP_port)
			sender_socket.sendto(str(resultado).encode("utf-8"),dest)
		else:
			sender_socket.sendto("MSG ERRADA".encode("utf-8"),dest)
	except Exception as e:
		print(e)
		receiver_socket.close()
		conexao.close()
		sender_socket.close()
