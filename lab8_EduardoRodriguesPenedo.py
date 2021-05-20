# -*- coding: utf-8 -*-
# DRE: 120043223
# Nome: Eduardo Rodrigues Penedo

# Questão 1
#
# list, string ->list
def PesquisarContatinhos(lista_contatinhos, search):
    search_capitalize = search.capitalize()
    search_minuscula = search.upper()
    search_maiuscula = search.lower()

    resposta = list()
    for i in range(len(lista_contatinhos)):
        if search_capitalize in lista_contatinhos[i][0] or search_maiuscula in lista_contatinhos[i][0] or search_minuscula in lista_contatinhos[i][0]:
            resposta.append(lista_contatinhos[i])
    return  resposta

# Questão 2
# Retorna o fatorial de um número, número inserido multiplicado pelos seus numeros antecessores
# int -> int
def fatorial(numero):

    resultado =1

    for i in range(numero):
        resultado = resultado * numero
        numero-=1

    return resultado

# Questão 3
#
#
def soma_fatorial(n_vezes):
    sum_fat = 0
    numero = n_vezes
    for i in range(n_vezes + 1):
        sum_fat+= fatorial(numero)
        numero-=1
    return sum_fat

# Questão 4
# Verifica se um numero é primo, se ele for divisível por um ou mais números anteriores maiores 2 e por ele mesmo a função retorma False, se o número for divisível apenas por ele mesmo, retorna-se True
# int -> bool
def primo(numero):
    eh_divisivel = 0
    divisor = numero
    for i in range(numero):
        if divisor < 2:
            break
        elif numero%divisor == 0:
            eh_divisivel+=1
        divisor-=1
    return eh_divisivel == 1

# Questão 5
#
# int -> int
def soma_quadrados(numero):
    sum_quadrados = 0
    if numero < 5 or numero > 2000:
        return -1
    else:
        for i in range(numero):
            if numero%2 == 0:
                sum_quadrados+=(numero*numero)
            numero-=1
    return sum_quadrados

# Questão 6
# Retorna uma lista com o número inserido multiplicado por cada número presente no intervalo [0,10]
# int -> list
def tabuada(numero):
    tabuada = list()
    if numero < 2 or numero > 1000:
        return -1
    else:
        for i in range(11):
            list.append(tabuada,numero*i)
    return tabuada

# Questão 7
# Recebe uma lista de números, cada número é a posição de uma letra em uma lista chamada alfabeto, esses elementos da lista são adicionados em outra lista chamada letras e é devolvida uma string das letras que tinham posições na lista inserida como parâmetro da função
# list -> string
def RPG(numeros_letras):
    letras = list()
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    for i in range(len(numeros_letras)):
        numeros_letras[i] -= 1

    for i in range(len(numeros_letras)):
        list.append(letras,alfabeto[numeros_letras[i]])
    resultado = ""
    return resultado.join(letras)

# Questão 8
# Recebe uma string como parâmetro e a cada vogal adiciona 0.01 ao tempo total, o tempo total é o valor retornado
# string -> float
def tempo_vogais(palavra):
    vogais =["a","e","i","o","u"]
    tempo_total = 0
    for i in range(len(palavra)):
        if palavra[i] in vogais:
            tempo_total+=0.01
    return tempo_total

# Questão 9
# Recebe uma lista com duas outras listas, uma de notas e outra de carga horárias. O cálculo da ira é dado por pelo somatório das notas vezes a respectiva carga horária dividido pela soma das cargas horárias vezes 100
# lista -> float
def calcula_ira(notas_ch):
    # [ [n1,n2,n3],[c1,c2,c3] ]
    sum_notas_ch = 0
    sum_ch = 0

    for i in range(len(notas_ch)+1):
        sum_notas_ch += notas_ch[0][i] * notas_ch[1][i]
        print(str(notas_ch[0][i]) + " " + str( notas_ch[1][i]))
    return sum_notas_ch/(sum(notas_ch[1])*100)

# Questão 10
# Verifica quantas letras A,E e X existem em uma lista e retorna e uma tupla (num_elementos_a,num_elementos_e,num_elementos_x )
# list -> tuple
def elfos(lista):
    elfos, anoes, hobbits = (0,0,0)
    for i in range(len(lista)):
        if lista[i] == "A":
            anoes+=1
        if lista[i] == "E":
            elfos+=1
        if lista[i] == "X":
            hobbits+=1
    return (anoes,elfos,hobbits)
# Testes
# 1
# Deve retornar os nomes que contenham fields em uma lista com os elementos "Fieldsnei Campos Jr", "Jão Matheus" e "Julia Fields"
print(PesquisarContatinhos([ ["Fieldsnei Campos Jr"],["Jão Matheus"],["Julia Fields"], ["Afieldstones Shzenheger"] ],"fields"))

# 2
# Deve retornar o fatorial de 5 = 5*4*3*2*1 = 120
print(fatorial(5))

# 3
# Deve retornar 154 = 5! + 4! + 3! +2! + 1! + 0!= 120 + 24 + 6 + 2 + 1 + 1
print(soma_fatorial(5))

# 4
# Deve retornar False pois é divisível sem restos por ele mesmo e os números anteriores maiores ou iguais a 2 14, 7, 4 e 2
print(primo(28))

# Deve retornar True pois é divisível sem restos apenas por ele mesmo
print(primo(29))

# 5
# Deve retornar a soma dos quadrados dos números pares anteriores. 36(6^2) + 16(4^2) + 4(2^2) => 56
print(soma_quadrados(6))

# 6
# Deve retornar a tabuada de 9 em uma lista [9*0,9*1,9*2,9*3,9*4,9*5,9*6,9*7,9*8,9*9,9*10] => [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
print(tabuada(9))

# 7
# Deve retornar a palavra HELP
print(RPG([8,5,12,16]))

# 8 Deve retornar 0.05 pois há 5 vogais na palavra
print(tempo_vogais("galopeira"))

# 9
# Deve retornar o valor resultante de ((1*3)+(2*5)+(3*7))/((3+5+7)*100) = 0.02266666666666667
print(calcula_ira([[1,2,3], [3,5,7]]))

# 10
# Deve retornar (3,3,3) passando 3 elementos de cada(A,E e X) em uma lista como parâmetro
print(elfos(["A","A","A","E","E","E","X","X","X",]))