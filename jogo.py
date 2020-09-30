# EP - Design de Software
# Renato Laffranchi Falcão
# Data: DD/MM/2020

import random
from baralhos import *

#Função que define a quantidade de baralhos que serão usados no jogo

definindo_baralhos = True

def define_baralhos():
    while definindo_baralhos = True:
        numero_de_baralhos = int(input("Com quantos baralhos deseja jogar?(1,6 ou 8) "))
        if numero_de_baralhos == 1 or numero_de_baralhos == 6 or numero_de_baralhos == 8:
            definindo_baralhos = False
            return numero_de_baralhos
        else:
            print("Esse número de baralhos é inválido")

#Função principal
def jogar():

    numero_baralhos = define_baralhos()

    if numero_baralhos == 1:
        baralho_de_jogo = um_baralho
        valores_baralho = valores_um_baralho
    elif numero_baralhos == 6:
        baralho_de_jogo = seis_baralhos
        valores_baralho = valores_seis_baralhos
    else:
        baralho_de_jogo = oito_baralhos
        valores_baralho = valores_oito_baralhos





    cartas_jogador = []
    cartas_jogador.append()

