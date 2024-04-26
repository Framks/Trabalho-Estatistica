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

print("QUESTÃO 20\n\t texto \n\t",1," \n")

print("QUESTÃO 21\n\t texto \n\t",1," \n")

print("QUESTÃO 22\n\t texto \n\t",1," \n")

print("QUESTÃO 23\n\t texto \n\t",1," \n")

print("QUESTÃO 24\n\t texto \n\t",1," \n")

print("QUESTÃO 24\n\t texto \n\t",1," \n")
