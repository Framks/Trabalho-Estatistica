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

print("QUESTÃO 10\n\t texto \n\t",1," \n")

print("QUESTÃO 11\n\t texto \n\t",1," \n")

print("QUESTÃO 12\n\t texto \n\t",1," \n")

print("QUESTÃO 13\n\t texto \n\t",1," \n")

print("QUESTÃO 14\n\t texto \n\t",1," \n")

print("QUESTÃO 15\n\t texto \n\t",1," \n")

print("QUESTÃO 16\n\t texto \n\t",1," \n")

print("QUESTÃO 17\n\t texto \n\t",1," \n")

print("QUESTÃO 18\n\t texto \n\t",1," \n")

print("QUESTÃO 19\n\t texto \n\t",1," \n")

print("QUESTÃO 20\n\t texto \n\t",1," \n")

print("QUESTÃO 21\n\t texto \n\t",1," \n")

print("QUESTÃO 22\n\t texto \n\t",1," \n")

print("QUESTÃO 23\n\t texto \n\t",1," \n")

print("QUESTÃO 24\n\t texto \n\t",1," \n")

print("QUESTÃO 24\n\t texto \n\t",1," \n")
