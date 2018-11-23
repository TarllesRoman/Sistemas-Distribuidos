#coding: utf-8
import moduloCliente as cliente

while True:
    msg = input("Digite: ")
    if(cliente.testTcp()):
        cliente.sendmsg(msg)

