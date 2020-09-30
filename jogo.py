# EP - Design de Software
# Renato Laffranchi Falcão
# Data: DD/MM/2020

import random
from baralhos import *

#Função para definir a quantidade de apostadores que vão entrar no jogo
def entrada_de_apostadores():
    lista_apostadores = []
    entrando_apostadores = True
#Enquanto houver jogadores desejando entrar, o loop continuará
    while entrando_apostadores:
        resposta = int(input("Você deseja participar do jogo? (1-Sim e 2-Não) "))
        if resposta == 1:
            nome = input("Qual o seu nome? ")
            lista_apostadores.append(nome)
        elif resposta == 2:
            entrando_apostadores = False
            return lista_apostadores
        else:
            print("Resposta inválida. Escolha uma das duas opções")



#Função que define a quantidade de baralhos que serão usados no jogo
def define_baralhos():
    definindo_baralhos = True
    while definindo_baralhos == True:
        numero_de_baralhos = int(input("Com quantos baralhos deseja jogar?(1,6 ou 8) "))
        if numero_de_baralhos == 1 or numero_de_baralhos == 6 or numero_de_baralhos == 8:
            definindo_baralhos = False
            return numero_de_baralhos
        else:
            print("Esse número de baralhos é inválido")


#Função principal
def jogar():

    lista_apostadores = entrada_de_apostadores()

    fichas_dos_apostadores = [150] * len(lista_apostadores)

#Dependendo do número de baralhos escolhido pelo jogador,
# o programa puxa as informações relacionadas àquele número de baralhos

    numero_baralhos = define_baralhos()

    if numero_baralhos == 1:
        baralho_de_jogo = um_baralho
        valores_baralho = valores_um_baralho
        valor_comissao = comissao_um_baralho
    elif numero_baralhos == 6:
        baralho_de_jogo = seis_baralhos
        valores_baralho = valores_seis_baralhos
        valor_comissao = comissao_seis_baralhos
    else:
        baralho_de_jogo = oito_baralhos
        valores_baralho = valores_oito_baralhos
        valor_comissao = comissao_oito_baralhos



    cartas_jogador = []
    cartas_jogador.append()

