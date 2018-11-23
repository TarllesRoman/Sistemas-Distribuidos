#coding utf-8

import servidor, controlServidor, threading, json

controle = controlServidor.Control()

def job_receiver():
    while True:
        if(servidor.testeTCP()):
            message,client = servidor.receiveUDP()
            if(message):
                controle.ler = True
                controle.mensagem = message
                controle.cliente = client

def efetuar_leitura():
    mensagem = json.loads(controle.mensagem)
    alm = mensagem['alimentacao'] #alimentação
    resultado = controle.dic_operacoes[mensagem['operacao']](alm)
    servidor.send(json.dumps(resultado),(controle.cliente[0],servidor.UDP_port))
    controle.mensagem = ""
    controle.cliente = []

if __name__ == "__main__":
    th_receiver =  threading.Thread(target=job_receiver, args=())
    th_receiver.start()
    while(True):
        if(controle.ler):
            controle.ler = False
            efetuar_leitura()


