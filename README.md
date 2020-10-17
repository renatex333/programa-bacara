## Exercício programa
## Jogo simplificado de Bacará

O jogo está contido no arquivo **jogo.py**.

Para começar o jogo, inicialize o arquivo **jogo.py**.

## Instruções gerais:

### 1) Entrada de apostadores

- Ao iniciar o programa, é possível que mais de um jogador participe das apostas. Cada jogador aposta a quantidade de fichas que quiser em quem acreditar ser o vencedor. As cartas de jogador são as mesmas para todos. Ou seja, é equivalente a ocorrerem diversos jogos ao mesmo tempo, um para cada jogador, mas as cartas sorteadas são as mesmas em todas as mesas. Ao final da partida cada jogador recebe ou paga o resultado das suas apostas.
- Digite **1**, caso algum apostador deseje participar e insira o nome do apostador no campo designado ou digite **2**, caso **não haja mais apostadores** desejando entrar.
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

- O valor das cartas segua a seguinte tabela:

| Cartas | Valor |
|:------:|:-----:|
|    A   |   1   |
|    2   |   2   |
|    3   |   3   |
|    4   |   4   |
|    5   |   5   |
|    6   |   6   |
|    7   |   7   |
|    8   |   8   |
|    9   |   9   |
|   10   |   0   |
|    J   |   0   |
|    Q   |   0   |
|    K   |   0   |

### 5) Pagamento das apostas

- O jogador perde as fichas apostadas se não tiver apostado no vencedor. Caso contrário, a quantidade de fichas recebidas depende de quem foi o vencedor da partida:

- **Jogador**: se o jogador venceu a partida (obteve a soma mais próxima de 9), a mesa paga a mesma quantidade de fichas apostadas. Por exemplo, se o jogador apostou 10 fichas, ele receberá outras 10 fichas.
- **Banco**: se o banco venceu a partida, a mesa paga 95% das fichas apostadas. Por exemplo, se o jogador apostou 20 fichas, ele receberá outras 19. Caso o número não seja inteiro o jogador receberá as fichas sempre arredondando para baixo. Por exemplo, se o jogador apostou 25 fichas, ele vai receber só 23 a mais.
- **Empate**: se ocorreu um empate, e o jogador apostou no empate, a mesa paga 8 vezes a quantidade de fichas apostadas. Por exemplo, se o jogador apostou 10 fichas, ele receberá outras 80.
- Se o jogador perde a aposta ele não paga nada de comissão nessa partida. Entretanto, se ele ganha a aposta, é necessário pagar uma porcentagem do que ele for receber para a casa.
- As taxas de comissão dependem de quem foi o vencedor da partida (jogador, banco ou empate) e da quantidade de baralhos. A tabela a seguir resume as taxas para cada caso:

| Vencedor | 1 Baralho | 6 Baralhos | 8 Baralhos |
|:--------:|:---------:|:----------:|:----------:|
|  Jogador |   1.29%   |    1.24%   |    1.24%   |
|   Banco  |   1.01%   |    1.06%   |    1.06%   |
|  Empate  |   15.75%  |   14.44%   |   14.36%   |

### 6) Fim do jogo

- A cada rodada o apostador decide se deseja continuar jogando ou se deseja parar.
- Quando as fichas de um jogador acaba, ele é eliminado automaticamente.
- Quando todos os jogadores ficam sem fichas, o jogo termina.