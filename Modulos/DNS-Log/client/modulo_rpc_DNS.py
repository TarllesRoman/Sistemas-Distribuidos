#coding: utf-8

import hashlib
import socket
import json

DNS_ip = 'localhost'
DNS_port = 19197

TCP_port = 19199
UDP_port = 19198

dic_ops = {'+' : 'som',
		  '-' : 'sub',
		  '*' : 'mul',
		  '/' : 'div'
}

def connec_tcp(ip, porta):
	try:
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp.settimeout(2)
		tcp.connect((ip, porta))
		tcp.close()
		return True
	except:
		print ('Erro ao conectar TCP')
		return False

def send_msg(msg, ip, porta):
	try:
		udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp.sendto(bytes(msg, 'utf-8'), (ip, porta))
		udp.close()
		return True
	except:
		print ('Erro ao enviar msg')
		return False

'''
	Retorna uma lista contendo a (resposta, origem) ou None
'''
def receive_msg(porta):
	try:
		udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp.bind(('', porta))
		udp.settimeout(3)
		resultado, serv = udp.recvfrom(2048)
		udp.close()
		return (resultado.decode('utf-8'), serv)
	except:
		print ('Timeout de recebimento')
		return None

'''
	Executa uma ponte com determinado servidor, retorna true caso a operaçao tenha sido executada corretamente ou false
	em caso de algum erro na comunicação
'''
def bridge_server(cmd, ip):
	if connec_tcp(ip, TCP_port):
		send_msg(cmd, ip, UDP_port)
		response = receive_msg(UDP_port)
		if(not response == None):
			print ('\033[0;31;40mO servidor: \033[m'+str(response[1])+'\033[0;31;40m respondeu \033[m'+ str(response[0]))
			return True
		else:
			return False
	else:
		print('Sem conexao no servidor: '+ip)
		return False

def dns_request(operacao):
	tentativas = 5
	while(tentativas > 0):
		if(send_msg(operacao, DNS_ip, DNS_port)):
			result = receive_msg(UDP_port)
			if(not (result == None)):
				return str(result[0])
		tentativas -= 1
	return None

def find_server(num1, num2, op):
	cmd = dic_ops[op]+'#'+num1+'#'+num2
	cmd = hashlib.md5(cmd.encode('utf8')).hexdigest()+'#'+cmd
	dns_response = dns_request(dic_ops[op])
	if(dns_response == None):
		print ('\033[0;31;40mServidor DNS não encontrado\033[m')
		return None
	jso = json.loads(dns_response)
	for servidor in jso['servidores']:
		if(bridge_server(cmd, servidor)):
			break

def soma(num1, num2, op):
	find_server(num1, num2, op)


def divisao(num1, num2, op):
	find_server(num1, num2, op)


def multiplicao(num1, num2, op):
	find_server(num1, num2, op)
	
	
def subtracao(num1, num2, op):
	find_server(num1, num2, op)
