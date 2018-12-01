#coding: utf-8

from socket import *

TCP_port = 19199
UDP_port = 19197

TCPSocket = socket(AF_INET,SOCK_STREAM)
TCPSocket.bind(('', TCP_port))
TCPSocket.listen(1)

def testeTCP():
	try:
		print("Aguardando confirmação TCP")
		conexao, cliente = TCPSocket.accept()
		print ('Conexao aceita'+str(cliente))
		conexao.close()
		return True
	except:
		conexao.close()
		return False

receiver_socket = socket(AF_INET, SOCK_DGRAM)
receiver_socket.bind(('', UDP_port))

def receiveUDP():
	try:
		print("Aguardando mensagem UDP")
		message, client = receiver_socket.recvfrom(2048)
		message = message.decode("utf-8")
		print ('Mensagem recebida: '+message)
		return [message, client]
	except:
		return ""

sender_socket = socket(AF_INET, SOCK_DGRAM)
def send(msg,dest):
	print("Respondendo "+str(msg)+" para "+str(dest))
	sender_socket.sendto(str(msg).encode("utf-8"),dest)

def close():
	receiver_socket.close()
	sender_socket.close()
	

"""
tm_buffer = 2048

dic_operacoes = { 
	'listar':modulo.listar,
	'adicionar':modulo.adicionar,
	'remover':modulo.remover
}

while True:
	print ('Server pronto para aceitar conexao')
	
	try:
		message, client = receiver_socket.recvfrom(2048)

		message = message.decode("utf-8")
						
		print ('Mensagem recebida: '+message)
		msg_split = message.split("#")
		msg_hash = msg_split[0]
		operacao = msg_split[1]
		args = msg_split[2]
		msg_completa = operacao + '#' + args
		if(msg_hash == hashlib.md5(msg_completa.encode('utf-8')).hexdigest()):
			resultado = dic_operacoes[operacao](args)
			dest = (client[0],UDP_port)
			sender_socket.sendto(str(resultado).encode("utf-8"),dest)
		else:
			sender_socket.sendto("MSG ERRADA".encode("utf-8"),dest)

	except Exception as e:
		print(e)
		receiver_socket.close()
		conexao.close()
sender_socket.close()
"""
