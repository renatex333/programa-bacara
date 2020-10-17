# EP - Design de Software
# Feito por: Renato Laffranchi Falcão
# Data: 16/10/2020

import random
from baralhos import *
import math
import time

# Função para checar se a resposta do usuário é um número inteiro

def checa_numero(numero):
    if numero.isdigit():
        return True
    else:
        return False

# Função para definir a quantidade de apostadores que vão entrar no jogo
def entrada_de_apostadores():
    lista_apostadores = []
    entrando_apostadores = True

# Enquanto houver jogadores desejando entrar, o loop continuará
    while entrando_apostadores:
        resposta = input("Você deseja participar do jogo? (1-Sim e 2-Não) ")

        if checa_numero(resposta):
            resposta = int(resposta)
        else:
            pass
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
        numero_de_baralhos = input("Com quantos baralhos deseja jogar?(1,6 ou 8) ")

        if checa_numero(numero_de_baralhos):
            numero_de_baralhos = int(numero_de_baralhos)
        else:
            pass

        if numero_de_baralhos == 1 or numero_de_baralhos == 6 or numero_de_baralhos == 8:
            definindo_baralhos = False
            return numero_de_baralhos
        else:
            print("Resposta inválida. ")

# Função para inicializar uma aposta
def apostas(jogadores, fichas_jogadores):
    aposta_vencedor = []
    apostas_fichas = []
    i = 0
    while i < len(jogadores):
        quem_vence = input("{}, quem você acha que vai ganhar? (1 - Jogador, 2 - Banco, 3 - Empate) ".format(jogadores[i]))

        if checa_numero(quem_vence):
            quem_vence = int(quem_vence)
        else:
            pass

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
        numero_fichas = input("{}, quantas fichas você deseja apostar no {}? (Você tem {} fichas) ".format(jogadores[i], aposta_vencedor[i], fichas_jogadores[i]))

        if checa_numero(numero_fichas):
            numero_fichas = int(numero_fichas)

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

        else:
            print("Resposta inválida. ")

    conjunto_apostas = [apostas_fichas, aposta_vencedor]

    return conjunto_apostas

# Função para a distribuição de cartas e checa o vencedor
def jogar():
    cartas_jogador = []
    cartas_banco = []
    # randint para randomizar uma carta do baralho
    indice_1_jogador = random.randint(0, len(baralho_de_jogo))
    indice_2_jogador = random.randint(0, len(baralho_de_jogo))
    indice_1_banco = random.randint(0, len(baralho_de_jogo))
    indice_2_banco = random.randint(0, len(baralho_de_jogo))
    # coloca as cartas nas respectivas listas
    cartas_jogador.append(baralho_de_jogo[indice_1_jogador])
    cartas_jogador.append(baralho_de_jogo[indice_2_jogador])
    cartas_banco.append(baralho_de_jogo[indice_1_banco])
    cartas_banco.append(baralho_de_jogo[indice_2_banco])

    # usei a função time.sleep() para deixar o jogo mais apresentável
    # e mais fácil para que o usuário entenda o que está acontecendo
    print("As cartas do jogador são {}".format(cartas_jogador))
    time.sleep(1.5)
    print("As cartas do banco são {}".format(cartas_banco))
    time.sleep(1.5)

    soma_jogador = valores_baralho[indice_1_jogador] + valores_baralho[indice_2_jogador]
    soma_banco = valores_baralho[indice_1_banco] + valores_baralho[indice_2_banco]

    if soma_jogador == 10 or soma_jogador > 10:
        soma_jogador -= 10
    else:
        pass
    if soma_banco == 10 or soma_banco > 10:
        soma_banco -= 10
    else:
        pass

    # checa a soma das cartas e distribui uma terceira nos casos específicos
    if soma_jogador == 8 or soma_jogador == 9:
        pass

    elif soma_banco == 8 or soma_banco == 9:
        pass

    elif soma_jogador == 6 or soma_jogador == 7:
        if soma_banco == 6 or soma_banco == 7:
            pass

        elif soma_banco == 5 or soma_banco < 5:
            print("Dá mais uma carta para o Banco")
            novo_indice = random.randint(0, len(baralho_de_jogo))
            cartas_banco.append(baralho_de_jogo[novo_indice])
            time.sleep(1.5)
            print("As cartas do banco são {}".format(cartas_banco))
            soma_banco += valores_baralho[novo_indice]
            if soma_banco == 10 or soma_banco > 10:
                soma_banco -= 10
            else:
                pass

    elif soma_banco == 6 or soma_banco == 7:
        print("Dá mais uma carta para o Jogador")
        novo_indice = random.randint(0, len(baralho_de_jogo))
        cartas_jogador.append(baralho_de_jogo[novo_indice])
        time.sleep(1.5)
        print("As cartas do jogador são {}".format(cartas_jogador))
        soma_jogador += valores_baralho[novo_indice]
        if soma_jogador == 10 or soma_jogador > 10:
            soma_jogador -= 10
        else:
            pass

    else:
        print("Dá mais uma carta para o Jogador")
        novo_indice = random.randint(0, len(baralho_de_jogo))
        cartas_jogador.append(baralho_de_jogo[novo_indice])
        time.sleep(1.5)
        print("As cartas do jogador são {}".format(cartas_jogador))
        soma_jogador += valores_baralho[novo_indice]
        if soma_jogador == 10 or soma_jogador > 10:
            soma_jogador -= 10
        else:
            pass

        print("Dá mais uma carta para o Banco")
        novo_indice = random.randint(0, len(baralho_de_jogo))
        cartas_banco.append(baralho_de_jogo[novo_indice])
        time.sleep(1.5)
        print("As cartas do banco são {}".format(cartas_banco))
        soma_banco += valores_baralho[novo_indice]
        if soma_banco == 10 or soma_banco > 10:
            soma_banco -= 10
        else:
            pass

    print("O Jogador teve uma soma de {} pontos e o Banco teve uma soma de {} pontos.".format(soma_jogador, soma_banco))

    # checa quem teve a maior soma depois da distribuição correta das cartas

    if soma_jogador == soma_banco:
        resultado = "Empate"
    elif soma_jogador > soma_banco:
        resultado = "Jogador Venceu"
    elif soma_jogador < soma_banco:
        resultado = "Banco Venceu"
    return resultado

# Variáveis globais fora de qualquer função

jogadores = entrada_de_apostadores()
fichas_jogadores = [10000] * len(jogadores)

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

jogando = True

while jogando:
    apostas_jogadores = apostas(jogadores, fichas_jogadores)
    fichas_apostadas = apostas_jogadores[0]
    aposta_vencedor = apostas_jogadores[1]


    resultado = jogar()

    time.sleep(1.5)

    if resultado == "Jogador Venceu":
        print("O Jogador venceu!")
        i = 0
        for aposta in aposta_vencedor:
            if aposta == "Jogador":
                recebimento = fichas_apostadas[i] * 2
            else:
                recebimento = 0
            if recebimento == 0:
                pass
            else:
                fichas_jogadores[i] += recebimento - math.floor(recebimento * valor_comissao[0])
            i += 1

    elif resultado == "Banco Venceu":
        print("O Banco venceu!")
        i = 0
        for aposta in aposta_vencedor:
            if aposta == "Banco":
                recebimento = math.floor(fichas_apostadas[i] * 1.95)
            else:
                recebimento = 0
            if recebimento == 0:
                pass
            else:
                fichas_jogadores[i] += recebimento - math.floor(recebimento * valor_comissao[1])
            i += 1

    else:
        print("Foi Empate!")
        i = 0
        for aposta in aposta_vencedor:
            if aposta == "Empate":
                recebimento = fichas_apostadas[i] * 8
            else:
                recebimento = 0
            if recebimento == 0:
                pass
            else:
                fichas_jogadores[i] += recebimento - math.floor(recebimento * valor_comissao[2])
            i += 1

    i = 0
    while i < len(fichas_jogadores):
        if fichas_jogadores[i] == 0:
            print("Desculpe {}, mas você ficou sem fichas. Você está fora do jogo.".format(jogadores[i]))
            del jogadores[i]
            del fichas_jogadores[i]
        else:
            print("{}, você está agora com {} fichas.".format(jogadores[i], fichas_jogadores[i]))
            parou = input("Deseja parar agora? (1 - Sim e 2 - Não)")

            parou = checa_numero(parou)

            if parou == 1:
                print("Obrigado por jogar!")
                del jogadores[i]
                del fichas_jogadores[i]
            elif parou == 2:
                print("Então vamos para mais uma rodada!")
                i += 1

            else:
                print("Resposta inválida. ")


    if not jogadores:
        print("O jogo acabou. Não tem mais jogadores jogando.")
        jogando = False
    else:
        pass