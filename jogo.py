# EP - Design de Software
# Renato Laffranchi Falcão
# Data: DD/MM/2020

import random
from baralhos import *

def define_baralhos():
    while definindo_baralhos = True:
        numero_de_baralhos = int(input("Com quantos baralhos deseja jogar?(1,6 ou 8) "))
        if numero_de_baralhos == 1 or numero_de_baralhos == 6 or numero_de_baralhos == 8:
            definindo_baralhos = False
            return numero_de_baralhos
        else:
            print("Esse número de baralhos é inválido")

def jogar():

    define_baralhos()



    cartas_jogador = []
    cartas_jogador.append()

