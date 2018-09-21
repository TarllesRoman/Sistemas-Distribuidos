#coding :utf-8

import moduloRPCUDP

msg = ""
		
def detectSinal(cmd):
	if '+' in msg:
		return moduloRPCUDP.soma(msg.split('+')[0],msg.split('+')[1],'+')
	if '-' in msg:
		return moduloRPCUDP.subtracao(msg.split('-')[0],msg.split('-')[1],'-')
	if '*' in msg:
		return moduloRPCUDP.soma(msg.split('*')[0],msg.split('*')[1],'*')
	if '/' in msg:
		return moduloRPCUDP.soma(msg.split('/')[0],msg.split('/')[1],'/')


while True:
	msg = input("Digite uma operação: ")
	detectSinal(msg)
