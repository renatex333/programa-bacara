# Baralhos usados no Bacará

um_baralho = ["A-Paus", "2-Paus", "3-Paus", "4-Paus", "5-Paus", "6-Paus", "7-Paus", "8-Paus", "9-Paus", "10-Paus", "J-Paus", "Q-Paus", "K-Paus",
 "A-Copas", "2-Copas", "3-Copas", "4-Copas", "5-Copas", "6-Copas", "7-Copas", "8-Copas", "9-Copas", "10-Copas", "J-Copas", "Q-Copas", "K-Copas", 
 "A-Espadas", "2-Espadas", "3-Espadas", "4-Espadas", "5-Espadas", "6-Espadas", "7-Espadas", "8-Espadas", "9-Espadas", "10-Espadas", "J-Espadas", "Q-Espadas", "K-Espadas", 
 "A-Ouros", "2-Ouros", "3-Ouros", "4-Ouros", "5-Ouros", "6-Ouros", "7-Ouros", "8-Ouros", "9-Ouros", "10-Ouros", "J-Ouros", "Q-Ouros", "K-Ouros"]
seis_baralhos = um_baralho * 6
oito_baralhos = um_baralho * 8

# Valores das cartas

valores_um_baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0,
1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]

valores_seis_baralhos = valores_um_baralho * 6
valores_oito_baralhos = valores_um_baralho * 8

# Valores das comissões do banco dependendo
# da quantidade de baralhos e do vencedor da rodada

comissao_um_baralho = [1.29/100 , 1.01/100 , 15.75/100]
comissao_seis_baralhos = [1.24/100 , 1.06/100 , 14.44/100]
comissao_oito_baralhos = [1.24/100 , 1.06/100 , 14.36/100]

# comissao_um_baralho[0] para quando o jogador vence
# comissao_um_baralho[1] para quando o banco vence
# comissao_um_baralho[2] para quando dá empate

# comissao_seis_baralhos[0] para quando o jogador vence
# comissao_seis_baralhos[1] para quando o banco vence
# comissao_seis_baralhos[2] para quando dá empate

# comissao_oito_baralhos[0] para quando o jogador vence
# comissao_oito_baralhos[1] para quando o banco vence
# comissao_oito_baralhos[2] para quando dá empate 