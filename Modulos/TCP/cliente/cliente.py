#coding :utf-8

import modulo

msg = ""
		
def detectSinal(cmd):
	if '+' in msg:
		return modulo.soma(msg.split('+')[0],msg.split('+')[1],'+')
	if '-' in msg:
		return modulo.subtracao(msg.split('-')[0],msg.split('-')[1],'-')
	if '*' in msg:
		return modulo.soma(msg.split('*')[0],msg.split('*')[1],'*')
	if '/' in msg:
		return modulo.soma(msg.split('/')[0],msg.split('/')[1],'/')


while True:
	msg = input("Digite uma operação: ")
	detectSinal(msg)
