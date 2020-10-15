## Exercício programa
## Jogo simplificado de Bacará

O jogo está contido no arquivo **jogo.py**.

Para começar o jogo, inicialize o arquivo **jogo.py**.

## Instruções gerais:

### 1) Entrada de apostadores

- Ao iniciar o programa, várias pessoas poderão apostar.
- Para isso, digite **1** caso algum apostador deseje participar e insira o nome do apostador no campo designado ou digite **2** caso **não haja mais apostadores** desejando entrar.
- Todos os apostadores recebem **10.000 fichas** iniciais.

### 2) Definindo a quantidade de baralhos

- Após a entrada de apostadores, você precisará decidir a quantidade de baralhos que serão utilizados no jogo.
- Você pode escolher entre 1, 6 e 9 baralhos, e para cada quantidade de baralhos, há um valor diferente para a comissão cobrada.

### 3) Fazendo apostas

- Você poderá escolher entre apostar no **Jogador**, no **Banco** ou no **Empate**.
- Você só pode apostar uma quantidade igual ou menor que a quantidade de fichas que você possui.

### 4) Distribuição das cartas

- O programa simula a distribuição das cartas seguindo as seguintes regras:

1.  Se a soma das cartas do jogador ou do banco for igual a 8 ou 9 o jogo termina e as apostas são pagas.
2.  Se a soma das cartas tanto do jogador quanto do banco forem diferentes de 8 ou 9, a mesa decide se distribuirá uma terceira carta a cada um de acordo com as regras a seguir, começando pelo jogador e depois distribuindo a carta do banco:

- Se a soma das cartas for 6 ou 7, não distribui mais uma carta.
- Se a soma das cartas for 5 ou menos, distribui mais uma carta e a soma é recalculada.

### 5) Pagamento das apostas

- O jogo é simulado e as apostas são pagas da forma devida a cada apostador, com os descontos de comissão já aplicados.

### 6) Fim do jogo

- A cada rodada o apostador decide se deseja continuar jogando ou se deseja parar.
- Quando as fichas de um jogador acaba, ele é eliminado automaticamente.
- Quando todos os jogadores ficam sem fichas, o jogo termina.