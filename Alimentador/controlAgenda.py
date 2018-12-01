#coding: utf-8

import json, modulo_hora

file_name = "agenda.txt"

def get_alimentacoes():
    try:
        file = open(file_name,"r")
        jso = file.read()
        file.close()
        return json.loads(jso)
    except:
        escrever_agenda([])
        return json.loads("[]")

def escrever_agenda(alimentacoes):
    try:
        file = open(file_name,"w")
        file.write(json.dumps(alimentacoes))
        file.close()
        return True
    except:
        return False

def adicionar_alimentacao(agenda, alimentacao):
    for alm in agenda:
        if(alm["dia"] == alimentacao["dia"] and alm["hora"] == alimentacao["hora"]):
            return None
    dt = modulo_hora.str_time(alimentacao["dia"], alimentacao["hora"])
    alimentacao["timestamp"] = modulo_hora.get_timestamp(dt)
    agenda.append(alimentacao)
    return agenda

def adicionar_alimentacoes(alimentacoes):
    agenda = get_alimentacoes()
    if(agenda == None):
        return False
    for hora in alimentacoes["horarios"]:
        alm = {"dia": alimentacoes["dia"],"tanque":alimentacoes["tanque"],"quantidade":alimentacoes["quantidade"],"hora":hora} #Alimentacao
        adicionar_alimentacao(agenda, alm)
    return escrever_agenda(agenda)

def remover(alimentacao):
    agenda = get_alimentacoes()
    agenda.remove(alimentacao)
    escrever_agenda(agenda)

def remover_alimentacao(alimentacao):
    agenda = get_alimentacoes()
    response = False
    if(agenda == None):
        return response
    for alm in agenda:
        if(alm["dia"] == alimentacao["dia"] and alm["hora"] == alimentacao["horarios"][0]):
            agenda.remove(alm)
            response = True
    escrever_agenda(agenda)
    return response
        

