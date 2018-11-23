#coding: utf-8

import json

file_name = "agenda.txt"

def get_alimentacoes():
    try:
        file = open(file_name,"r")
        jso = file.read()
        file.close()
        return json.loads(jso)
    except:
        return None

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
            return False
    agenda.append(alimentacao)
    return True

def adicionar_alimentacoes(alimentacoes):
    agenda = get_alimentacoes()
    if(agenda == None):
        return False
    for hora in alimentacoes["horarios"]:
        alm = {"dia": alimentacoes["dia"],"tanque":alimentacoes["tanque"],"quantidade":alimentacoes["quantidade"],"hora":hora} #Alimentacao
        adicionar_alimentacao(agenda, alm)
    return escrever_agenda(agenda)

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
        

