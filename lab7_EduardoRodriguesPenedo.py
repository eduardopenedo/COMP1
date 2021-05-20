# Eduardo Rodrigues Penedo
# 120043223

import random

# Questão 1
# Gera dois números aleatórios de 1 a 6 e retorna uma tupla com o número de tentativas até sairem iguais e a média das tentativas em cada numero aleatório
# -> int, float, float
import string
from asyncore import socket_map


def JogarDados():
    dado1 = list()
    dado2 = list()
    dado1.append(random.randint(1,6))
    dado2.append(random.randint(1,6))

    i=0
    while(dado1[i]!=dado2[i]):
        dado1.append(random.randint(1, 6))
        dado2.append(random.randint(1, 6))
        i+=1


    media1 = sum(dado1)/len(dado1)
    media2 = sum(dado2)/len(dado2)
    tentativas = len(dado1)
    return (tentativas,media1,media2)


# Questão 2
# Retorna média aritmética de um campeonato
# list -> float
def faltas(jogos):
    # [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7, 8]]]
    i=0
    soma_faltas = 0
    while i<len(jogos):
        soma_faltas = soma_faltas + sum(jogos[i][2])
        i+=1
    media_faltas = soma_faltas/len(jogos)
    return  media_faltas

# Questão 3
# Calcula as diferenças entre o segundo e o primeiro número de todas as tuplas presentes em, uma lista e depois as soma
# tuple -> int
def Virus(virus):
    letalidade = []
    i=0
    while i<len(virus):
        letalidade.append(virus[i][0] - virus[i][1])
        i+=1
    return sum(letalidade)

# Questão 4
# Filtra quais numneros em uma lista possuem resto 0 quando divididos por um número
# list -> list
def Multiplos(lista, numero):
    multiplos = list()
    i=0
    while(i<len(lista)):
        if lista[i] % numero == 0 and lista[i]!=0:
            multiplos.append(lista[i])
        i+=1
    return multiplos

# Questão 5
# Verifica qual o maior valor em uma lista
# list -> float
def MaiorRejeição(rejeicao):
    maior = rejeicao[0]
    i=0
    while i<len(rejeicao):
        if rejeicao[i]> maior:
            maior = rejeicao[i]
        i+=1
    return max(rejeicao)

# Questão 6
# Percorre uma lista contando quantos elementos possuem número anterior igual ao analisado
# list -> int
def repetidos(lista):
    i=0
    repetidos = 0

    while(i<len(lista)-1):
        if((lista[i] == lista[i + 1])):
            repetidos+=1
            i+=1
        else:
            i+=1
    return repetidos

# Questão 7
#
#
def Amarelinha(tupla1, tupla2):
    if tupla1[1] == "PAR":
        if (tupla1[2]+ tupla2[2])%2==0:
            return tupla1[0]
    if tupla1[1] == "IMPAR":
        if(tupla1[2] + tupla2[2]) % 2 != 0:
            return tupla1[0]
    else:
        return tupla2[0]


# Questão 8 a
#
# Pesquisa em uma lisa
def PesquisarContatinhos(lista_contatinhos, search):
    i=0
    search_capitalize = search.capitalize()
    search_minuscula = search.upper()
    search_maiuscula = search.lower()

    resposta = list()
    while i< len(lista_contatinhos):
        if search_capitalize in lista_contatinhos[i][0] or search_maiuscula in lista_contatinhos[i][0] or search_minuscula in lista_contatinhos[i][0]:
            resposta.append(lista_contatinhos[i])
        i+=1
    return  resposta

# Testes

# Questão 1
# Como a função não recebe parametros não dá para prever qual será o resultado da tupla
print(JogarDados())

# Questão 2
# Teste 1 -> Deve retornar 15.25 => ((10+9) + (5+7) + (7+8)+ (7+8))/4
print(faltas([['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]],['Italia', 'Espanha', [7,8]]]))

# Questão 3
# Deverá retornar 38 (9-4)+(43-10)
print(Virus([(9, 4), (43, 10)]))

# Questão 4
# Deve retornar os multiplos de 3 da lista => [3,6,9]
print(Multiplos([0,3,4,5,6,7,8,8,8,9],3 ))

# Questão 5
# Deve retornar o maior valor da lista (0.5)
print(MaiorRejeição([0.1,0.2,0.3,0.4,0.5]))

# Questão 6
# Deve retornar 6 pois há 6 ocorrências onde o número anterior é o mesmo que o que está sendo analisado
print(repetidos([1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7]))
# Deve retornar 4 pois há 4 ocorrências onde o número anterior é o mesmo que o que está sendo analisado
print(repetidos([3,3,3,4,3,3,3]))

# Questão 7
# Deve retornar nome do jogador 1 pois 3 mais 7 é par
print(Amarelinha(("nome1", "PAR", 3),("nome2", "IMPAR", 7)))

# Deve retornar nome do jogador 1 pois 4 mais 7 é impar
print(Amarelinha(("nome1", "IMPAR", 4),("nome2", "PAR", 7)))

# Deve retornar nome do jogador 2 pois 4 mais 7 é impar
print(Amarelinha(("nome1", "PAR", 4),("nome2", "IMPAR", 7)))

# Questão 8
# Deve retornar os nomes que contenham fields em uma lista com os elementos "Fieldsnei Campos Jr", "Jão Matheus" e "Julia Fields"
print(PesquisarContatinhos([ ["Fieldsnei Campos Jr"],["Jão Matheus"],["Julia Fields"], ["Afieldstones Shzenheger"] ],"fields"))