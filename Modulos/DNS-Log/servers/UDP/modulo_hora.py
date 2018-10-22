#coding:'utf-8'

from datetime import datetime, timedelta
import json
import requests
import time

url = 'http://www.worldclockapi.com/api/json/utc/now'

'''Time delta com o modulo da diferença de horarios'''
n = datetime.now()
diff = n - n
'''Indica se a diferença é positiva ou negativa'''
diff_signal = True

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

'''Obtem a hora atual ja sincoroniza'''
def sinchronized():
    global diff, diff_signal
    l_now = now()

    return somar_h(l_now,diff) if diff_signal else sub_h(l_now, diff)

def start_sync(delay):
    th_sync = threading.Thread(target=loop_sync,args=(delay))
    th_sync.start()

def loop_sync(delay):
    while True:
        sync()
        time.sleep(delay)

def sync():
    global diff, diff_signal
	
    try:
        r_utc = request_utc()
        n_utc = utc_now()

        if(r_utc > n_utc):
            diff_signal = True
        else:
            diff_signal = False
        diff = diferenca(r_utc,n_utc)
    except:
        print("Erro ao atualizar time delta")
