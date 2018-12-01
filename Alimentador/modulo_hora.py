#coding:'utf-8'

from datetime import datetime, timedelta
import json
import requests
import time
import threading

url = 'http://www.worldclockapi.com/api/json/utc/now'

'''Time delta com o modulo da diferença de horarios'''
diff = 0
'''Indica se a diferença é positiva ou negativa'''
diff_signal = True

'''Retorna um datetime com a data e a hora fornecida'''
def str_time(data, hora):
    return datetime.strptime(data+' '+hora,'%d/%m/%Y %H:%M')

'''Retorna o timestamp do objeto datetime fornecido'''
def get_timestamp(date):
    return time.mktime(date.timetuple())

def from_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)


'''Realiza uma requisição HTTP para pegar a hora em UTC'''
def request_utc():
    r = requests.get(url)
    jso = r.json()
    time = jso['currentDateTime']

    return datetime.strptime(time, '%Y-%m-%dT%H:%MZ')

'''Pega a hora do sistema em UTC'''
def utc_now():
    return datetime.utcnow()

'''Pega a hora do sistema'''
def now():
    return datetime.now()

'''Calcula o modulo da diferença entre dois horários'''
def diferenca(dt1, dt2):
    if(dt2 > dt1):
        return dt2 - dt1
    else:
        return dt1 - dt2

'''Soma os dois horarios'''
def somar_h(dt1, dt2):
    return dt1 + dt2

'''Subtrai os dois horarios'''
def sub_h(dt1, dt2):
    return dt1 - dt2

'''Obtem a hora atual sincoroniza, É necessário ter utilizado o método start_sync'''
def sinchronized():
    global diff, diff_signal
    l_now = now()

    return somar_h(l_now,diff) if diff_signal else sub_h(l_now, diff)

'''Inicia a sincronização com um delay. 
    Esse delay é o tempo em que o modulo ficará ocioso antes de
    buscar uma nova atualização no servidor
'''
def start_sync(delay):
    th_sync = threading.Thread(target=loop_sync,args=(delay))
    th_sync.start()

'''loop para a sincronização. while True'''
def loop_sync(delay):
    while True:
        sync()
        time.sleep(delay)

'''realiza a sincronização da diferença do tempo consultado
    e do relógio do computador'''
def sync():
    global diff, diff_signal

    r_utc = request_utc()
    n_utc = utc_now()

    if(r_utc > n_utc):
        diff_signal = True
    else:
        diff_signal = False

    diff = diferenca(r_utc,n_utc)
