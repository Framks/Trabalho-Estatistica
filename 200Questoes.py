import math
import statistics as estatistica

# aqui é a função que ira retornar um fatorial do numero N passado por parametro
def fatorial(n):
    if (n <= 1):
        return 1
    else :
        return n*fatorial(n-1)

# aqui se faz o calco da combinação simples de n! / p!*(n-p)!
def combinacao(n,p):
    return (fatorial(n)/(fatorial(p)*fatorial(n-p)))

# aqui se faz a permutação com nem todos elementos destintos com  formula: n! /(p1!*p2!*p3!*...*pk!)
def permutacaoComRepeticao(n,p):
    divisor = 1
    dividendo = fatorial(n)
    for a in p:
        divisor *= fatorial(a)
    return dividendo/divisor

# Função para calcular a probabilidade condicional
def probabilidade_condicional(p_a, p_b_dado_a):
    return p_a * p_b_dado_a

# combinação completa formula: Combinação onde o N = (n+p-1), e o P é o P;
def combinacaoCompleta(n,p):
    return combinacao((n+p-1),p)

def permutacaoCaotica(n):
    fracoes = 0
    for a in range(2,(n+1)):
        if(a%2 == 0):
            fracoes += (1/fatorial(a))
        else:
            fracoes -= (1/fatorial(a))
    return fracoes*fatorial(n)

# Cálculo da probabilidade de que ao menos uma peça na amostra seja defeituosa
def probabilidade_ao_menos_uma_defeituosa(total_boas, total_mas, amostra):
    # Número total de peças
    total_pecas = total_boas + total_mas
    
    # Número total de maneiras de escolher a amostra de 10 peças entre todas as 35 peças
    total_combinacoes = combinacao(total_pecas, amostra)
    
    # Número de maneiras de escolher 10 peças apenas entre as 20 boas (nenhuma defeituosa na amostra)
    boas_combinacoes = combinacao(total_boas, amostra)
    
    # Probabilidade de que todas as peças na amostra sejam boas
    probabilidade_todas_boas = boas_combinacoes / total_combinacoes
    
    # Probabilidade de que ao menos uma peça seja defeituosa é o complemento da probabilidade de que todas sejam boas
    return 1 - probabilidade_todas_boas

# Função para calcular permutação caótica (números de derangements)
def permutacaoCaotica(n):
    fracoes = 0
    for a in range(2, n + 1):
        if a % 2 == 0:
            fracoes += 1 / fatorial(a)
        else:
            fracoes -= 1 / fatorial(a)
    return round(fatorial(n) * (1 - fracoes))

def probabilidade_ao_menos_um_evento(total_eventos, eventos_sucesso, amostra):
    total_combinacoes = combinacao(total_eventos, amostra)
    combinacoes_sucesso = combinacao(eventos_sucesso, amostra)
    return 1 - (combinacoes_sucesso / total_combinacoes)

print("QUESTÃO 1\n\tQuantas palavras contendo 3 letras diferentes podem ser formadas com um alfabeto de 26 letras?\n\tResposta: 26*25*24 :",26*25*24,", pois para a primeira à 26 possibilidades para asegunda 25 pois a primeira ja foi escolhida poir fim a 3 com 24 possibilidade\n")
print("QUESTÃO 2\n\tQuantos são os gabaritos possíveis de um teste de 10 questões de múltiplaescolha, com cinco alternativas por questão?\n\tResposta: 5^10 :", pow(5,10),", pois em cada questão é 5 posibilidades e são 10 questões assim é 5 elevado a 10\n")
print("QUESTÃO 3\n\tQuantos inteiros há entre 1000 e 9999 cujos algarismos são distintos?\n\tResposta: 9*9*8*7 :",(9*9*8*7),", pois 9 para a primeira posição tirando o 0 9 para a segunda, 8 para a terceira e 7 para a quarta\n")
print("QUESTÃO 4\n\tDe quantos modos diferentes podem ser escolhidos um presidente e um secretário de um conselho que tem 12 membros?\n\tResposta: 11*12 =",11*12,", pois é 12 para a primeira possição e 11 para a segunda\n")
print("QUESTÃO 5\n\tDe quantos modos 3 pessoas podem sentar-se em 5 cadeiras em fila?\n\tResposta: 5*4*3 :",5*4*3,", pois o primeiro teria 5 possiveis cadeiras o segndo 4 e o terceiro 3\n")
print("QUESTÃO 6\n\tQuantos números de quatro dígitos são maiores que 2400 e têm todos os dígitos diferentes.\n\tResposta: (7*9*8*7)+(1*6*8*7)=",(7*9*8*7)+(6*8*7),"\n")
print("QUESTÃO 7\n\tQuantos são os anagramas da palavra CAPÍTULO que começam por consoante e terminam por vogal\n\tResposta: (4*4*6!) =",4*4*fatorial(6),"Pois 4*4 são as possibilidades da primeira e da ultima letra, as letras restantes são 6!\n")
print("QUESTÃO 8\n\tQuantos são os anagramas da palavra CAPÍTULO que têm as letras C, A, P juntas nessa ordem?\n\tResposta: (6!)=",fatorial(6),", tendo cap como uma unica litra o resultado é 6! \n")
print("QUESTÃO 9\n\tUm cubo de madeira tem uma face de cada cor. Quantos dados diferentes podemos formar gravando números de 1 a 6 sobre essas faces?\n\tResposta: (6!) =",fatorial(6),", pois temos que ordenar 6 numero em 6 posissoes diferentes \n")
print("QUESTÃO 10\n\tQuantos dados diferentes podemos formar gravando números de 1 a 6 sobre as faces indistinguíveis de um cubo de madeira?\n\tResposta: (6!/24) = ",fatorial(6)/24,", como as faces são indistinguíveis então o mesmo dado é contado varias vezes assim nós temos que dividir pela quantidade de vezes que eles se repetem\n")
print("QUESTÃO 11\n\tResolva o problema anterior para: a) números de 1 a 4, tetraedro regular\n\tResposta: (4X3) = ",4*3,", O número de posições para um tetraedro regular é 4 x 3 = 12, pois há 4 modos de escolher a face de apoio e 4 de escolher, nessa face, o lado que fica de frente. \n")
print("QUESTÃO 12\n\tUm campeonato é disputado por 12 clubes em rodadas de 6 jogos cada. De quantos modos é possível selecionar osjogos de primeira rodada?\n\tResposta: (12!/6! * (2!)^6) = ",(fatorial(12)/(fatorial(6)*pow(2,6))),", pois assim dividiremos a combinação dos 12 times por grupos de 2 times\n")
print("QUESTÃO 13\n\tUma comissão formada por 3 homens e 3 mulheres deve ser escolhida em um grupo de 8 homens e 5 mulheres.\n\tResposta: (C(3,5) * C(3,8 )) = ",combinacao(5,3)*combinacao(8,3),", Para formar uma comissão devemos selecionar 3 homens, o que pode ser feito de combinação de 3 em 8 56 modos, e 3 mulheres, o que pode ser feito de combinação de 3 em 5 = 10 modos, depois é so ultiplicar\n")
print("QUESTÃO 14\n\tPara a seleção brasileira foram convocados dois goleiros, 6 zagueiros, 7 meios de campo e 4 atacantes. De quantos modos é possível escalar a seleção com 1 goleiro, 4 zagueiros, 4 meios de campo e 2 atacantes?\n\tResposta: (2 x C(4,6) x C(4,7) x C(2,4) ) = ",(2*combinacao(4,2)*combinacao(7,4)*combinacao(6,4)),", O goleiro pode serselecionado de 2 modos; os zagueiros de C(4,6)= 15 modos; os meios-de-campo, de C(4,7) = 35 modos e os atacantes, de C(2,4)\n")
print("QUESTÃO 15\n\tQuantas diagonais possui um polígono de n lados?\n\t Resposta = n(n-3)/2, Vamos contar as diagonais que incidem em cada vértice do polígono. Em cada um dos n vértices do polígono incidem n — 3 diagonais (que ligam esse vértice a todos os vértices à exceção de si mesmo e dos dois vértices que lhe são adjacentes). Logo, o resultado da contagem é n(n — 3). Como cada diagonal incide em dois vértices, cada diagonal foi contada duas vezes. \n")
print("QUESTÃO 16\n\tTem-se 5 pontos sobre uma reta R e 8 pontos sobre uma reta R' paralela a R. Quantos quadriláteros convexos com vértices em 4 desses 13 pontos existem?\n\tResposta: (C(2,5) * C(2,8)) = ",combinacao(5,2) * combinacao(8,2),", Para formar um quadrilátero convexo, basta selecionar dois pontos em R e dois pontos em R’ \n")
print("QUESTÃO 17\n\tQuantos são os anagramas da palavra CARAGUATATUBA? Quantos começam por vogal?\n\tResposta ((C(4,12) x C(2,8) x C(2,6) x 4!) + (C(5,12) x C(2,7) x 5!)) = ",(combinacao(12,4)*combinacao(8,2)*combinacao(6,2)*fatorial(4))+(combinacao(12,5)*combinacao(7,2)*fatorial(5)),", Em CARAGUATATUBA a letra A aparece 5 vezes, U aparece 2 vezes, T aparece 2 vezes e as letras C, R, G e B aparecem 1 vez cada uma, havendo, portanto, 13 letras na palavra.  Há C(4,12) x C(2,8) x C(2,6) x 4! anagramas que começam por A e C(5,12) x C(2,7) x 5! que começam por U.\n")
print("QUESTÃO 18\n\tConsidere um polígono convexo de n lados e suponha que não há duas de suas diagonais que sejam paralelas nem três que concorram em um mesmo ponto que não seja vértice. Quantos desses pontos de interseção são interiores ao polígono?\n\tResposta: (n(n-1)*(n-2)*(n-3))/24, Cada ponto de interseção é proveniente da interseção de duas diagonais, as quais foram geradas por 4 dos pontos dados. Cada grupo de 4 pontos dados, A, B, C e D, gera um quadrilátero convexo cujas duas diagonais se intersectam no interior do polígono.\n")
print("QUESTÃO 19\n\tUma fila de cadeiras no cinema tem 20 poltronas. De quantos modos 6 casais podem se sentar nessas poltronas de modo que nenhum marido se sente separado de sua mulher?\n\tResposta: ((2^6)*C(8,14)*6!)=",(pow(2,6)*combinacao(14,8)*fatorial(6)),", Escolhida a ordem de cada casal, o que pode ser feito de 26 modos temos que arrumar em fila 8 espaços vazios e 6 casais, o que pode ser feito de C(8,14) modos (escolha dos espaços vazios) vezes 6! (colocação dos 6 casais nos 6 lugares restantes). \n")

# Definição dos parâmetros
total_boas = 20
total_mas = 15
amostra = 10

print("QUESTÃO 20\n\tUma caixa contém 20 peças em boas condições e 15 em más condições. "
      "Uma amostra de 10 peças é extraída. Calcular a probabilidade de que ao menos uma peça na amostra seja defeituosa.\n"
      "\tResposta: ", probabilidade_ao_menos_uma_defeituosa(total_boas, total_mas, amostra), "\n")
print("QUESTÃO 21\n\tDez pessoas são separadas em dois grupos de 5 pessoas cada um. Qual é a probabilidade de que duas pessoas determinadas A e B façam parte do mesmo grupo?\n\tResposta",4/9,"Colocada a pessoa A, há 9 posições possíveis para B, das quais 4 são favoráveis. \n")
print("QUESTÃO 22\n\tUm número entre 1 e 200 é escolhido aleatoriamente. Calcular a probabilidade de que seja divisível por 5 ou por 7\n\tResposta: ",63/200," Sendo A e B os eventos “o número é divisível por 5” e “o número é divisível por 7”, respectivamente, A n B é o evento “o número é divisível por 35”\n")
print("QUESTÃO 23\n\tUma moeda foi cunhada de tal forma que é 4 vezes mais provável dar cara do que coroa. Calcular as probabilidades de cara e coroa.\n\t Se P(coroa) = p, então P(cara) = Ap. Mas p + Ap = 1; logo, P = l/5 As probabilidades são P(coroa) = 1/5 e P(cara) — 4/5.\n")
print("QUESTÃO 24\n\tDois dados são jogados simultaneamente. Calcular a probabilidade de obter 7 como soma dos resultados.\n\t",1,"Há 6 x 6 = 36 resultados possíveis igualmente prováveis, em 6 dos quais a soma vale 7. a resposta é 1/6\n")
print("QUESTÃO 25\n\tUma urna contém 10 bolas vermelhas e 15 bolas azuis. Qual é a probabilidade de que ao menos uma bola vermelha seja retirada em uma amostra de 5 bolas?\n\tResposta: ", probabilidade_ao_menos_um_evento(25, 15, 5), "\n")
print("QUESTÃO 26\n\tLançando dois dados, qual é a probabilidade de a soma dos números ser igual a 7?\n\tResposta: ", 6/36, "\n")
print("QUESTÃO 27\n\tQual é a probabilidade de tirar uma carta de copas de um baralho padrão?\n\tResposta: ", 13/52, "\n")
print("QUESTÃO 28\n\tQual é a probabilidade de tirar uma carta de ás de um baralho padrão?\n\tResposta: ", 4/52, "\n")
print("QUESTÃO 29\n\tQual é a probabilidade de tirar uma carta de ás de copas de um baralho padrão?\n\tResposta: ", 1/52, "\n")
print("QUESTÃO 30\n\tLançando três moedas, qual é a probabilidade de obter pelo menos uma cara?\n\tResposta: ", 1 - (1/8), "\n")
print("QUESTÃO 31\n\tQual é a probabilidade de obter um número primo ao lançar um dado de 6 faces?\n\tResposta: ", 3/6, "\n")
print("QUESTÃO 32\n\tQual é a probabilidade de obter um número par ao lançar um dado de 6 faces?\n\tResposta: ", 3/6, "\n")
print("QUESTÃO 33\n\tQual é a probabilidade de obter um número menor que 4 ao lançar um dado de 6 faces?\n\tResposta: ", 3/6, "\n")
print("QUESTÃO 34\n\tQual é a probabilidade de obter uma sequência específica de 3 cartas de um baralho padrão?\n\tResposta: ", 1/(52*51*50), "\n")
print("QUESTÃO 35\n\tLançando duas moedas, qual é a probabilidade de obter duas caras?\n\tResposta: ", 1/4, "\n")
print("QUESTÃO 36\n\tLançando dois dados, qual é a probabilidade de a soma dos números ser maior que 8?\n\tResposta: ", 10/36, "\n")
print("QUESTÃO 37\n\tQual é a probabilidade de tirar uma carta de copas ou de ás de um baralho padrão?\n\tResposta: ", (13 + 3) / 52, "\n")
print("QUESTÃO 38\n\tQual é a probabilidade de tirar uma carta de copas e de ás de um baralho padrão?\n\tResposta: ", 1/52, "\n")
print("QUESTÃO 39\n\tQual é a probabilidade de obter uma sequência específica de 4 cartas de um baralho padrão?\n\tResposta: ", 1/(52*51*50*49), "\n")
print("QUESTÃO 40\n\tLançando três dados, qual é a probabilidade de obter pelo menos um 6?\n\tResposta: ", 1 - (125/216), "\n")
print("QUESTÃO 41\n\tQual é a probabilidade de obter um número ímpar ao lançar um dado de 6 faces?\n\tResposta: ", 3/6, "\n")
print("QUESTÃO 42\n\tQual é a probabilidade de obter um número maior que 4 ao lançar um dado de 6 faces?\n\tResposta: ", 2/6, "\n")
print("QUESTÃO 43\n\tQual é a probabilidade de obter um número primo e par ao lançar um dado de 6 faces?\n\tResposta: ", 1/6, "\n")
print("QUESTÃO 44\n\tQual é a probabilidade de obter uma sequência específica de 5 cartas de um baralho padrão?\n\tResposta: ", 1/(52*51*50*49*48), "\n")
print("QUESTÃO 45\n\tDez pessoas são separadas em dois grupos de 5 pessoas cada um. Qual é a probabilidade de que duas pessoas determinadas A e B façam parte do mesmo grupo?\n\tResposta: ", 4/9, "\n")
print("QUESTÃO 46\n\tQual é a probabilidade de obter um número par ou um número menor que 4 ao lançar um dado de 6 faces?\n\tResposta: ", 4/6, "\n")
print("QUESTÃO 47\n\tLançando duas moedas, qual é a probabilidade de obter pelo menos uma cara?\n\tResposta: ", 3/4, "\n")
print("QUESTÃO 48\n\tQual é a probabilidade de tirar uma carta de figura (valete, dama ou rei) de um baralho padrão?\n\tResposta: ", 12/52, "\n")
print("QUESTÃO 49\n\tQual é a probabilidade de tirar uma carta de figura ou de ás de um baralho padrão?\n\tResposta: ", 16/52, "\n")
print("QUESTÃO 50\n\tLançando três dados, qual é a probabilidade de obter uma soma igual a 10?\n\tResposta: ", 27/216, "\n")
print("QUESTÃO 51\n\tQual é a probabilidade de obter um número menor que 5 ao lançar um dado de 6 faces?\n\tResposta: ", 4/6, "\n")
print("QUESTÃO 52\n\tQual é a probabilidade de obter um número par e maior que 3 ao lançar um dado de 6 faces?\n\tResposta: ", 2/6, "\n")
print("QUESTÃO 53\n\tQual é a probabilidade de obter um número primo ou ímpar ao lançar um dado de 6 faces?\n\tResposta: ", 4/6, "\n")
print("QUESTÃO 54\n\tQual é a probabilidade de obter uma sequência específica de 6 cartas de um baralho padrão?\n\tResposta: ", 1/(52*51*50*49*48*47), "\n")
print("QUESTÃO 55\n\tLançando quatro moedas, qual é a probabilidade de obter exatamente duas caras?\n\tResposta: ", combinacao(4, 2) * (1/2)**4, "\n")
print("QUESTÃO 56\n\tQual é a probabilidade de tirar uma carta de copas ou de figura de um baralho padrão?\n\tResposta: ", (13 + 9) / 52, "\n")
print("QUESTÃO 57\n\tQual é a probabilidade de tirar uma carta de copas e de figura de um baralho padrão?\n\tResposta: ", 3/52, "\n")
print("QUESTÃO 58\n\tQual é a probabilidade de obter uma sequência específica de 7 cartas de um baralho padrão?\n\tResposta: ", 1/(52*51*50*49*48*47*46), "\n")
print("QUESTÃO 59\n\tQual é a probabilidade de obter um número menor que 3 ou maior que 4 ao lançar um dado de 6 faces?\n\tResposta: ", 4/6, "\n")
print("QUESTÃO 60\n\tLançando três moedas, qual é a probabilidade de obter exatamente duas caras?\n\tResposta: ", combinacao(3, 2) * (1/2)**3, "\n")
print("QUESTÃO 61\n\tQual é a probabilidade de tirar uma carta de ás ou de figura de um baralho padrão?\n\tResposta: ", (4 + 12) / 52, "\n")
print("QUESTÃO 62\n\tQual é a probabilidade de tirar uma carta de ás e de figura de um baralho padrão?\n\tResposta: ", 0/52, "\n")
print("QUESTÃO 63\n\tQual é a probabilidade de obter uma sequência específica de 8 cartas de um baralho padrão?\n\tResposta: ", 1/(52*51*50*49*48*47*46*45), "\n")
print("QUESTÃO 64\n\tQual é a probabilidade de obter um número maior que 2 e menor que 5 ao lançar um dado de 6 faces?\n\tResposta: ", 2/6, "\n")
print("QUESTÃO 65\n\tLançando quatro moedas, qual é a probabilidade de obter exatamente três caras?\n\tResposta: ", combinacao(4, 3) * (1/2)**4, "\n")
print("QUESTÃO 66\n\tEm uma urna com 5 bolas vermelhas e 7 bolas azuis, duas bolas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda bola seja azul, dado que a primeira bola foi vermelha?\n\tResposta: ", (5/12) * (7/11), "\n")
print("QUESTÃO 67\n\tEm um baralho padrão de 52 cartas, qual é a probabilidade de tirar uma carta de copas, dado que a carta é vermelha?\n\tResposta: ", 13/26, "\n")
print("QUESTÃO 68\n\tEm uma família com duas crianças, qual é a probabilidade de ambas serem meninas, dado que pelo menos uma é menina?\n\tResposta: ", 1/3, "\n")
print("QUESTÃO 69\n\tEm um baralho padrão de 52 cartas, qual é a probabilidade de tirar um ás, dado que a carta é de espadas?\n\tResposta: ", 1/13, "\n")
print("QUESTÃO 70\n\tEm uma urna com 4 bolas vermelhas e 6 bolas verdes, duas bolas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda bola seja verde, dado que a primeira bola foi verde?\n\tResposta: ", (6/10) * (5/9), "\n")
print("QUESTÃO 71\n\tEm uma caixa com 8 canetas azuis e 5 canetas vermelhas, duas canetas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda caneta seja vermelha, dado que a primeira caneta foi azul?\n\tResposta: ", (8/13) * (5/12), "\n")
print("QUESTÃO 72\n\tEm uma urna com 7 bolas pretas e 3 bolas brancas, duas bolas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda bola seja branca, dado que a primeira bola foi preta?\n\tResposta: ", (7/10) * (3/9), "\n")
print("QUESTÃO 73\n\tEm um baralho padrão de 52 cartas, qual é a probabilidade de tirar um rei, dado que a carta é de copas?\n\tResposta: ", 1/13, "\n")
print("QUESTÃO 74\n\tEm uma caixa com 10 bolas amarelas e 5 bolas verdes, duas bolas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda bola seja verde, dado que a primeira bola foi amarela?\n\tResposta: ", (10/15) * (5/14), "\n")
print("QUESTÃO 75\n\tEm uma família com três crianças, qual é a probabilidade de todas serem meninos, dado que pelo menos um é menino?\n\tResposta: ", 1/7, "\n")
print("QUESTÃO 76\n\tEm uma urna com 6 bolas azuis e 4 bolas vermelhas, duas bolas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda bola seja vermelha, dado que a primeira bola foi azul?\n\tResposta: ", (6/10) * (4/9), "\n")
print("QUESTÃO 77\n\tEm uma caixa com 9 canetas pretas e 6 canetas brancas, duas canetas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda caneta seja branca, dado que a primeira caneta foi preta?\n\tResposta: ", (9/15) * (6/14), "\n")
print("QUESTÃO 78\n\tEm uma urna com 8 bolas verdes e 5 bolas amarelas, duas bolas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda bola seja amarela, dado que a primeira bola foi verde?\n\tResposta: ", (8/13) * (5/12), "\n")
print("QUESTÃO 79\n\tEm um baralho padrão de 52 cartas, qual é a probabilidade de tirar uma dama, dado que a carta é de ouros?\n\tResposta: ", 1/13, "\n")
print("QUESTÃO 80\n\tEm uma caixa com 7 bolas azuis e 3 bolas vermelhas, duas bolas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda bola seja vermelha, dado que a primeira bola foi azul?\n\tResposta: ", (7/10) * (3/9), "\n")
print("QUESTÃO 81\n\tEm uma urna com 5 bolas pretas e 4 bolas brancas, duas bolas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda bola seja branca, dado que a primeira bola foi preta?\n\tResposta: ", (5/9) * (4/8), "\n")
print("QUESTÃO 82\n\tEm uma caixa com 8 canetas pretas e 5 canetas brancas, duas canetas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda caneta seja branca, dado que a primeira caneta foi preta?\n\tResposta: ", (8/13) * (5/12), "\n")
print("QUESTÃO 83\n\tEm uma urna com 7 bolas azuis e 3 bolas vermelhas, duas bolas são retiradas sucessivamente sem reposição. Qual é a probabilidade de que a segunda bola seja vermelha, dado que a primeira bola foi azul?\n\tResposta: ", (7/10) * (3/9), "\n")
print("QUESTÃO 84\n\tEm uma família com quatro crianças, qual é a probabilidade de todas serem meninas, dado que pelo menos uma é menina?\n\tResposta: ", 1/15, "\n")
print("QUESTÃO 85\n\tEm um baralho padrão de 52 cartas, qual é a probabilidade de tirar um valete, dado que a carta é de espadas?\n\tResposta: ", 1/13, "\n")
print("QUESTÃO 86\n\tEm uma sala de aula, 15 alunos gostam de Matemática, 12 gostam de Física e 8 gostam de ambas as matérias. Quantos alunos gostam de pelo menos uma dessas matérias?\n\tResposta: ", 15 + 12 - 8, "\n")
print("QUESTÃO 87\n\tEm um grupo de 30 pessoas, 18 gostam de futebol, 15 gostam de basquete e 10 gostam de ambos. Quantas pessoas gostam de pelo menos um desses esportes?\n\tResposta: ", 18 + 15 - 10, "\n")
print("QUESTÃO 88\n\tEm uma pesquisa, 70 pessoas assistem filmes de ação, 50 assistem filmes de comédia e 30 assistem ambos. Quantas pessoas assistem pelo menos um desses tipos de filme?\n\tResposta: ", 70 + 50 - 30, "\n")
print("QUESTÃO 89\n\tEm uma escola, 25 alunos fazem curso de Inglês, 20 fazem curso de Espanhol e 10 fazem ambos. Quantos alunos fazem pelo menos um desses cursos?\n\tResposta: ", 25 + 20 - 10, "\n")
print("QUESTÃO 90\n\tEm uma biblioteca, 60 livros são de ficção, 40 são de não-ficção e 20 são de ambos os gêneros. Quantos livros são de pelo menos um desses gêneros?\n\tResposta: ", 60 + 40 - 20, "\n")
print("QUESTÃO 91\n\tEm um clube, 100 membros jogam tênis, 80 jogam vôlei e 30 jogam ambos. Quantos membros jogam pelo menos um desses esportes?\n\tResposta: ", 100 + 80 - 30, "\n")
print("QUESTÃO 92\n\tEm uma cidade, 200 pessoas têm carro, 150 têm moto e 50 têm ambos. Quantas pessoas têm pelo menos um desses veículos?\n\tResposta: ", 200 + 150 - 50, "\n")
print("QUESTÃO 93\n\tEm um grupo de 50 estudantes, 30 estudam Matemática, 25 estudam Ciência da Computação e 10 estudam ambos. Quantos estudantes estudam pelo menos uma dessas matérias?\n\tResposta: ", 30 + 25 - 10, "\n")
print("QUESTÃO 94\n\tEm uma conferência, 120 participantes são de TI, 80 são de Engenharia e 40 são de ambas as áreas. Quantos participantes são de pelo menos uma dessas áreas?\n\tResposta: ", 120 + 80 - 40, "\n")
print("QUESTÃO 95\n\tEm uma empresa, 40 funcionários trabalham no departamento de Marketing, 30 trabalham no departamento de Vendas e 20 trabalham em ambos. Quantos funcionários trabalham em pelo menos um desses departamentos?\n\tResposta: ", 40 + 30 - 20, "\n")
print("QUESTÃO 96\n\tEm um evento, 90 pessoas assistem palestras sobre Saúde, 70 assistem palestras sobre Tecnologia e 30 assistem ambas. Quantas pessoas assistem pelo menos uma dessas palestras?\n\tResposta: ", 90 + 70 - 30, "\n")
print("QUESTÃO 97\n\tEm um grupo de 40 amigos, 25 gostam de ler, 20 gostam de assistir filmes e 10 gostam de ambas as atividades. Quantos amigos gostam de pelo menos uma dessas atividades?\n\tResposta: ", 25 + 20 - 10, "\n")
print("QUESTÃO 98\n\tEm uma festa, 80 convidados bebem suco, 60 bebem refrigerante e 20 bebem ambos. Quantos convidados bebem pelo menos uma dessas bebidas?\n\tResposta: ", 80 + 60 - 20, "\n")
print("QUESTÃO 99\n\tEm uma escola, 50 alunos jogam futebol, 40 jogam basquete e 15 jogam ambos. Quantos alunos jogam pelo menos um desses esportes?\n\tResposta: ", 50 + 40 - 15, "\n")
print("QUESTÃO 100\n\tEm uma turma, 35 alunos gostam de ciências, 25 gostam de história e 10 gostam de ambas as matérias. Quantos alunos gostam de pelo menos uma dessas matérias?\n\tResposta: ", 35 + 25 - 10, "\n")
print("QUESTÃO 101\n\tEm um clube, 60 membros praticam natação, 50 praticam tênis e 20 praticam ambos. Quantos membros praticam pelo menos um desses esportes?\n\tResposta: ", 60 + 50 - 20, "\n")
print("QUESTÃO 102\n\tEm uma empresa, 100 funcionários têm certificação em TI, 70 têm certificação em Gestão e 30 têm ambas. Quantos funcionários têm pelo menos uma dessas certificações?\n\tResposta: ", 100 + 70 - 30, "\n")
print("QUESTÃO 103\n\tEm uma pesquisa, 120 pessoas assistem a séries de drama, 90 assistem a séries de comédia e 40 assistem a ambos os tipos de séries. Quantas pessoas assistem a pelo menos um desses tipos de série?\n\tResposta: ", 120 + 90 - 40, "\n")
print("QUESTÃO 104\n\tEm uma comunidade, 200 pessoas fazem caminhadas, 150 fazem corridas e 50 fazem ambas as atividades. Quantas pessoas fazem pelo menos uma dessas atividades?\n\tResposta: ", 200 + 150 - 50, "\n")
print("QUESTÃO 105\n\tEm uma escola, 80 alunos participam do clube de ciências, 60 participam do clube de matemática e 30 participam de ambos. Quantos alunos participam de pelo menos um desses clubes?\n\tResposta: ", 80 + 60 - 30, "\n")
print("QUESTÃO 106\n\tEm uma biblioteca, 70 livros são de mistério, 50 são de romance e 20 são de ambos os gêneros. Quantos livros são de pelo menos um desses gêneros?\n\tResposta: ", 70 + 50 - 20, "\n")
print("QUESTÃO 107\n\tEm um clube de leitura, 40 membros leem ficção, 30 leem não-ficção e 10 leem ambos. Quantos membros leem pelo menos um desses gêneros?\n\tResposta: ", 40 + 30 - 10, "\n")
print("QUESTÃO 108\n\tEm um evento esportivo, 90 pessoas jogam tênis, 70 jogam vôlei e 30 jogam ambos. Quantas pessoas jogam pelo menos um desses esportes?\n\tResposta: ", 90 + 70 - 30, "\n")
print("QUESTÃO 109\n\tEm uma escola, 100 alunos participam do clube de teatro, 80 participam do clube de música e 50 participam de ambos. Quantos alunos participam de pelo menos um desses clubes?\n\tResposta: ", 100 + 80 - 50, "\n")
print("QUESTÃO 110\n\tEm uma empresa, 60 funcionários têm certificação em marketing, 40 têm certificação em finanças e 20 têm ambas. Quantos funcionários têm pelo menos uma dessas certificações?\n\tResposta: ", 60 + 40 - 20, "\n")
print("QUESTÃO 111\n\tEm uma escola, 90 alunos praticam basquete, 70 praticam vôlei e 40 praticam ambos. Quantos alunos praticam pelo menos um desses esportes?\n\tResposta: ", 90 + 70 - 40, "\n")
print("QUESTÃO 112\n\tEm um grupo de amigos, 50 gostam de ler, 30 gostam de escrever e 20 gostam de ambas as atividades. Quantos amigos gostam de pelo menos uma dessas atividades?\n\tResposta: ", 50 + 30 - 20, "\n")
print("QUESTÃO 113\n\tEm um evento, 70 participantes assistem a palestras sobre economia, 50 assistem a palestras sobre política e 20 assistem a ambas. Quantos participantes assistem a pelo menos uma dessas palestras?\n\tResposta: ", 70 + 50 - 20, "\n")
print("QUESTÃO 114\n\tEm uma pesquisa, 80 pessoas leem jornais, 60 leem revistas e 30 leem ambos. Quantas pessoas leem pelo menos um desses tipos de publicação?\n\tResposta: ", 80 + 60 - 30, "\n")
print("QUESTÃO 115\n\tEm uma empresa, 50 funcionários são treinados em vendas, 40 são treinados em atendimento ao cliente e 20 são treinados em ambos. Quantos funcionários são treinados em pelo menos uma dessas áreas?\n\tResposta: ", 50 + 40 - 20, "\n")
print("QUESTÃO 116\n\tQuantas permutações caóticas existem para um conjunto de 4 elementos?\n\tResposta: ", permutacaoCaotica(4), "\n")
print("QUESTÃO 117\n\tEm quantas maneiras diferentes podemos distribuir 5 bolinhas em 3 caixas, permitindo caixas vazias?\n\tResposta: ", combinacaoCompleta(3, 5), "\n")
print("QUESTÃO 118\n\tDe quantas maneiras diferentes podemos distribuir 7 doces em 4 crianças, permitindo que uma criança receba nenhum doce?\n\tResposta: ", combinacaoCompleta(4, 7), "\n")
print("QUESTÃO 120\n\tQuantas maneiras diferentes existem para distribuir 10 maçãs em 6 cestos, permitindo cestos vazios?\n\tResposta: ", combinacaoCompleta(6, 10), "\n")
print("QUESTÃO 121\n\tDe quantas maneiras diferentes podemos distribuir 8 livros em 5 prateleiras, permitindo prateleiras vazias?\n\tResposta: ", combinacaoCompleta(5, 8), "\n")
print("QUESTÃO 122\n\tQuantas maneiras diferentes existem para distribuir 12 bolas de gude em 4 potes, permitindo potes vazios?\n\tResposta: ", combinacaoCompleta(4, 12), "\n")
print("QUESTÃO 123\n\tEm quantas maneiras diferentes podemos distribuir 15 cartões em 6 caixas, permitindo caixas vazias?\n\tResposta: ", combinacaoCompleta(6, 15), "\n")
print("QUESTÃO 124\n\tQuantas maneiras diferentes existem para distribuir 20 balas em 5 saquinhos, permitindo saquinhos vazios?\n\tResposta: ", combinacaoCompleta(5, 20), "\n")
print("QUESTÃO 125\n\tDe quantas maneiras diferentes podemos distribuir 25 chocolates em 8 crianças, permitindo que uma criança receba nenhum chocolate?\n\tResposta: ", combinacaoCompleta(8, 25), "\n")
print("QUESTÃO 126\n\tQuantas maneiras diferentes existem para distribuir 30 presentes em 10 caixas, permitindo caixas vazias?\n\tResposta: ", combinacaoCompleta(10, 30), "\n")
print("QUESTÃO 127\n\tEm quantas maneiras diferentes podemos distribuir 50 figurinhas em 20 álbuns, permitindo álbuns vazios?\n\tResposta: ", combinacaoCompleta(20, 50), "\n")
print(" \n\t EXERCICIOS SOBRE ESTATÍSTICA \n")
print("QUESTÃO 128\n\t Dado o seguinte conjunto de dados: {7, 8, 6, 10, 5, 9, 4, 12, 7, 8}, calcule a média\n\tResposta:",estatistica.mean([7,8,6,10,5,9,4,12,7,8]),", Somando os elementos e dividindo pela quantidade se tem o resultado\n")
print("QUESTÃO 129\n\t Dado o seguinte conjunto de dados: {7, 8, 6, 10, 5, 9, 4, 12, 7, 8}, calcule o desvio padrão.\n\tResposta",estatistica.stdev([7,8,6,10,5,9,4,12,7,8]),",  é uma medida de dispersão que indica o quanto os elementos de um conjunto de dados estão afastados da média.\n")

# Dados
num_ocorencia = [0, 1, 2, 3, 4]
frequencias = [30, 25, 10, 5, 2]

# Calculando a média ponderada
def calcular_media_ponderada(valores, frequencias):
    soma_ponderada = sum(v * f for v, f in zip(valores, frequencias))
    soma_frequencias = sum(frequencias)
    return soma_ponderada / soma_frequencias

# Calculando o desvio padrão
def calcular_desvio_padrao(valores, frequencias, media):
    variancia_ponderada = sum(f * (v - media) ** 2 for v, f in zip(valores, frequencias)) / sum(frequencias)
    return math.sqrt(variancia_ponderada)

media = calcular_media_ponderada(num_ocorencia, frequencias)
print("QUESTÃO 131\n\t Calcule a média e o desvio padrão da seguinte distribuição de frequências:\nNúmero de ocorência , Frequência\n\t 0\t\t30\n\t1\t\t25\n\t2\t\t10\n\t3\t\t5\n\t4\t\t2 \n\tResposta: ",media," \n")
print("QUESTÃO 132\n\t Calcule o desvio padrão da seguinte distribuição de frequências:\nNúmero de ocorência , Frequência \n\t 0\t\t30\n\t1\t\t25\n\t2\t\t10\n\t3\t\t5\n\t4\t\t2\n\tResposta: ",calcular_desvio_padrao(num_ocorencia, frequencias, media)," \n")
print("QUESTÃO 133\n\t Em um lançamento de uma moeda honesta e observação da face voltada para cima. Apresente os espaços amostrais levando em consideração o experimento aleatório:\n\t Resposta: Q = {cara, coroa} \n")
print("QUESTÃO 134\n\t Retira-se, ao acaso, uma carta de um baralho de 52 cartas. Calcule a probabilidade de a carta não ser de ouro:  \n\tResposta: ",39/52,", Em um baralho de 52 cartas, há 4 naipes. Cada naipe tem 13 cartas. Portanto, há 13 cartas de ouro e 52 − 13 = 39 cartas que não são de ouro. \n")
print("QUESTÃO 135\n\t Depois de um longo período de testes, verificou-se que o procedimento A de recuperação de informação corre um risco de 2% de não oferecer resposta satisfatória. No procedimento £, o risco cai para 1%. O risco de ambos os procedimentos apresentarem resposta insatisfatória é de 0,5%. Qual é a probabilidade de pelo menos um dos procedimentos apresentar respos ta insatisfatória? \n\tResposta: ",0.02+0.01-0.005,",A regra da adição para a união de dois eventos é: P(A∪B)=P(A)+P(B)−P(A∩B)\n")
print("QUESTÃO 136\n\t Certo tipo de conserva tem peso líquido médio de 900 g, com desvio padrão de 10 g. A embalagem tem peso médio de 100 g, com desvio padrão de 4 g. Suponha que o processo de enchimento das embalagens controla o peso líquido, de tal forma que se possa supor independência entre o peso líquido e o peso da embalagem. Qual é a média e o desvio padrão do peso bruto? \n\tResposta: 1000g, ",math.sqrt((math.pow(10,2)+math.pow(4,2)))," \n")
print("QUESTÃO 137\n\t Dados históricos mostram que 5% dos itens provindos de um fornecedor apresentam algum tipo de defeito. Considerando um lote com 20 itens, calcular a probabilidade de haver algum item com defeito\n\tResposta: ",0.06415," \n")
print("QUESTÃO 138\n\t Mensagens chegam a um servidor de acordo com uma distribuição de Poisson, com taxa média de cinco chegadas por minuto. Qual é a probabilidade de que duas chegadas ocorram em um minuto?\n\tResposta: ",0.0843," \n")
print("QUESTÃO 139\n\t Em um canal de comunicação digital, a probabilidade de se receber um bit com erro é de 0,0002. Se 10.000 bits forem transmitidos por esse canal, qual é a probabilidade de que mais de quatro bits sejam recebidos com erro? \n\tResposta: ",0.0527," \n")
print("QUESTÃO 140\n\t Um piso cerâmico tem, em média, 0,01 defeito por m2. Em uma área de 10 m x 10 m desse piso, calcule a probabilidade de ocorrer algum defeito. \n\tResposta: ",0.6321," \n")
print("QUESTÃO 141\n\t Suponha que as requisições a um sistema ocorram de forma independente e que a taxa média de ocorrências é três requisições por minuto, constante no período em estudo. Calcule a probabilidade de: ocorrer mais que uma requisição no próximo minuto; \n\tResposta: ",0.8009 ," \n")
print("QUESTÃO 142\n\t Dados históricos mostram que 5% dos itens provindos de um fornecedor apresentam algum tipo de defeito. Considerando um lote com 20 itens, calcular a probabilidade de haver mais de dois itens defeituosos\n\t Resposta: ",0.0754," \n")
print("QUESTÃO 143\n\t texto \n\t",1," \n")
print("QUESTÃO 144\n\t texto \n\t",1," \n")
print("QUESTÃO 145\n\t texto \n\t",1," \n")
print("QUESTÃO 146\n\t texto \n\t",1," \n")
print("QUESTÃO 147\n\t texto \n\t",1," \n")
print("QUESTÃO 148\n\t texto \n\t",1," \n")
print("QUESTÃO 149\n\t texto \n\t",1," \n")
print("QUESTÃO 150\n\t texto \n\t",1," \n")
print("QUESTÃO 151\n\t texto \n\t",1," \n")
print("QUESTÃO 152\n\t texto \n\t",1," \n")
print("QUESTÃO 153\n\t texto \n\t",1," \n")
print("QUESTÃO 154\n\t texto \n\t",1," \n")
print("QUESTÃO 155\n\t texto \n\t",1," \n")
print("QUESTÃO 156\n\t texto \n\t",1," \n")
print("QUESTÃO 157\n\t texto \n\t",1," \n")
print("QUESTÃO 158\n\t texto \n\t",1," \n")
print("QUESTÃO 159\n\t texto \n\t",1," \n")
print("QUESTÃO 160\n\t texto \n\t",1," \n")
print("QUESTÃO 161\n\t texto \n\t",1," \n")
print("QUESTÃO 162\n\t texto \n\t",1," \n")
print("QUESTÃO 163\n\t texto \n\t",1," \n")
print("QUESTÃO 164\n\t texto \n\t",1," \n")
print("QUESTÃO 165\n\t texto \n\t",1," \n")
print("QUESTÃO 166\n\t texto \n\t",1," \n")
print("QUESTÃO 167\n\t texto \n\t",1," \n")
print("QUESTÃO 168\n\t texto \n\t",1," \n")
print("QUESTÃO 169\n\t texto \n\t",1," \n")
print("QUESTÃO 170\n\t texto \n\t",1," \n")
print("QUESTÃO 171\n\t texto \n\t",1," \n")
print("QUESTÃO 172\n\t texto \n\t",1," \n")
print("QUESTÃO 173\n\t texto \n\t",1," \n")
print("QUESTÃO 174\n\t texto \n\t",1," \n")
print("QUESTÃO 175\n\t texto \n\t",1," \n")
print("QUESTÃO 176\n\t texto \n\t",1," \n")
print("QUESTÃO 177\n\t texto \n\t",1," \n")
print("QUESTÃO 178\n\t texto \n\t",1," \n")
print("QUESTÃO 179\n\t texto \n\t",1," \n")
print("QUESTÃO 180\n\t texto \n\t",1," \n")
print("QUESTÃO 181\n\t texto \n\t",1," \n")
print("QUESTÃO 182\n\t texto \n\t",1," \n")
print("QUESTÃO 183\n\t texto \n\t",1," \n")
print("QUESTÃO 184\n\t texto \n\t",1," \n")
print("QUESTÃO 185\n\t texto \n\t",1," \n")
print("QUESTÃO 186\n\t texto \n\t",1," \n")
print("QUESTÃO 187\n\t texto \n\t",1," \n")
print("QUESTÃO 188\n\t texto \n\t",1," \n")
print("QUESTÃO 189\n\t texto \n\t",1," \n")
print("QUESTÃO 190\n\t texto \n\t",1," \n")
print("QUESTÃO 191\n\t texto \n\t",1," \n")
print("QUESTÃO 192\n\t texto \n\t",1," \n")
print("QUESTÃO 193\n\t texto \n\t",1," \n")
print("QUESTÃO 194\n\t texto \n\t",1," \n")
print("QUESTÃO 195\n\t texto \n\t",1," \n")
print("QUESTÃO 196\n\t texto \n\t",1," \n")
print("QUESTÃO 197\n\t texto \n\t",1," \n")
print("QUESTÃO 198\n\t texto \n\t",1," \n")
print("QUESTÃO 199\n\t texto \n\t",1," \n")
print("QUESTÃO 200\n\t texto \n\t",1," \n")
