#coding utf-8

import controlServidor, servidor, threading, json, time
import modulo_hora

controle = controlServidor.Control()

def job_receiver():
    while True:
        try:
            if(servidor.testeTCP()):
                message,client = servidor.receiveUDP()
                if(message):
                    controle.ler = True
                    controle.mensagem = message
                    controle.cliente = client
        except Exception as e:
            print("Tentativa de comunicação com chave invalida"+str(e))

def efetuar_leitura():
    mensagem = json.loads(controle.mensagem)
    alm = mensagem['alimentacao'] #alimentação
    resultado = controle.dic_operacoes[mensagem['operacao']](alm)
    servidor.send(json.dumps(resultado),(controle.cliente[0],servidor.UDP_port))
    controle.mensagem = ""
    controle.cliente = []

def job_alimentar():
    while True: 
        try:
            controle.update_proxima()
            print("\nPROXIMA   : "+str(controle.proxima))
            while(controle.proxima["timestamp"] > (modulo_hora.get_timestamp(modulo_hora.request_utc()) - 7200)):
                print("\nPA: " + str(controle.proxima["timestamp"]) + "     NOW: "+str(modulo_hora.get_timestamp(modulo_hora.request_utc()) - 7200))
                time.sleep(5)
            print("\n\nRealizando a alimentação: "+str(controle.proxima))
            controle.food_now()
        except:
            print("\nNada para alimentar! Posso descançar por enquanto")
            return None


if __name__ == "__main__":
    th_receiver =  threading.Thread(target=job_receiver, args=())
    th_receiver.start()
    th_alimentar = threading.Thread(target=job_alimentar, args=())
    th_alimentar.start()
    while(True):
        if(controle.ler):
            controle.ler = False
            efetuar_leitura()
        if(("timestamp" in controle.proxima) and (not th_alimentar.is_alive())):
            print("\nTenho bocas para alimentar!")
            th_alimentar = threading.Thread(target=job_alimentar, args=())
            th_alimentar.start()



