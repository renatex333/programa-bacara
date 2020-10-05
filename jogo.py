# EP - Design de Software
# Renato Laffranchi Falcão
# Data: DD/MM/2020

import random
from baralhos import *

# Função para definir a quantidade de apostadores que vão entrar no jogo
def entrada_de_apostadores():
    lista_apostadores = []
    entrando_apostadores = True

# Enquanto houver jogadores desejando entrar, o loop continuará
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


# Função que define a quantidade de baralhos que serão usados no jogo
def define_baralhos():
    definindo_baralhos = True
    while definindo_baralhos == True:
        numero_de_baralhos = int(input("Com quantos baralhos deseja jogar?(1,6 ou 8) "))
        if numero_de_baralhos == 1 or numero_de_baralhos == 6 or numero_de_baralhos == 8:
            definindo_baralhos = False
            return numero_de_baralhos
        else:
            print("Esse número de baralhos é inválido")

# Função para inicializar uma aposta
def apostas(jogadores, fichas_jogadores):
    aposta_vencedor = []
    apostas_fichas = []
    i = 0
    while i < len(jogadores):
        quem_vence = int(input("{}, quem você acha que vai ganhar? (1 - Jogador, 2 - Banco, 3 - Empate) ".format(jogadores[i])))

        if quem_vence == 1:
            aposta_vencedor.append("Jogador")
            i += 1
        elif quem_vence == 2:
            aposta_vencedor.append("Banco")
            i += 1
        elif quem_vence == 3:
            aposta_vencedor.append("Empate")
            i += 1
        else:
            print("Resposta inválida.")

    i = 0
    while i < len(jogadores):
        numero_fichas = int(input("{}, quantas fichas você deseja apostar no {}? (Você tem {} fichas) ".format(jogadores[i], aposta_vencedor[i], fichas_jogadores[i])))

        if numero_fichas > fichas_jogadores[i]:
            print("Você não pode apostar mais do que tem. ")
        elif numero_fichas < 0:
            print("Você não pode apostar um número negativo de fichas. ")
        elif numero_fichas == 0:
            print("Você deve apostar no mínimo uma ficha. ")
        else:
            apostas_fichas.append(numero_fichas)
            fichas_jogadores[i] = fichas_jogadores[i] - numero_fichas
            i += 1

    return aposta_vencedor
    return apostas_fichas

# Função para a distribuição de cartas
def distribui_cartas():
    cartas_jogador = []
    cartas_banco = []

    #randint para randomizar uma carta do baralho e retirá-la do monte



# Função principal
# def jogar():




# Variáveis globais fora de qualquer função

jogadores = entrada_de_apostadores()
fichas_jogadores = [200] * len(jogadores)

# Dependendo do número de baralhos escolhido pelo jogador,
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


apostas_jogadores = apostas(jogadores, fichas_jogadores)