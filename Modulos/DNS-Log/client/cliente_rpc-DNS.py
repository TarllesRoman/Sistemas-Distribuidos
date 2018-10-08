#coding :utf-8

import modulo_rpc_DNS as modulo

msg = ""
		
def detectSinal(cmd):
	if '+' in msg:
		return modulo.soma(msg.split('+')[0],msg.split('+')[1],'+')
	elif '-' in msg:
		return modulo.subtracao(msg.split('-')[0],msg.split('-')[1],'-')
	elif '*' in msg:
		return modulo.soma(msg.split('*')[0],msg.split('*')[1],'*')
	elif '/' in msg:
		return modulo.soma(msg.split('/')[0],msg.split('/')[1],'/')


while True:
	msg = input("Digite uma operação: ")
	detectSinal(msg)
