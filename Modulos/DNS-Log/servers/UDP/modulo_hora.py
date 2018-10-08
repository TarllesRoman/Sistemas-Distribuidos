#coding:'utf-8'

from datetime import datetime, timedelta
import json
import requests

url = 'http://www.worldclockapi.com/api/json/utc/now'

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

'''Obtem a hora atual e a sincoroniza'''
def sinchronized():
    r_utc = request_utc()
    n_utc = utc_now()
    l_now = now()

    dif = diferenca(r_utc, n_utc)
    if(r_utc > n_utc):
        return somar_h(l_now, dif)
    else:
        return sub_h(l_now, dif)
