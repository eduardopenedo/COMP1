# DRE: 120043223
# Nome: Eduardo Rodrigues Penedo

# Questão 1
# Função que retorna True se lista é vazia ou se a linha tem o mesmo tamanho da coluna da matriz, caso contrário, retorna False
# list -> bool

def eh_quadrarda(matriz):
    if matriz == [] or  len(matriz) == len(matriz[0]):
        return True
    else:
        return False

# Questão 2
# Função que retorna a quantidade de elementos em uma lista que são maiores que um int "numero" em uma matriz
# int, list
def conta_numero(numero, matriz):
    maiores =0
    for i in range(len(matriz)):
        for x in range(len(matriz[i])):
            if matriz[i][x] > numero:
                maiores+=1
    return maiores

# Questão 3
# Função que retorna uma matriz com todos seus elementos multiplicas por um int "num"
# int, list -> list
def multiplica_matriz(num, matriz):
    multiplicacao = list()
    for i in range(len(matriz)):
        multiplicacao.append([])
        for x in range(len(matriz[i])):
            multiplicacao[i].append(num* matriz[i][x])
    return multiplicacao


# Questão 4
# Função que percorre uma matriz m1, subtraindo o elemento da matriz m1 por um elemento de m2 na mesma posição e retorna uma nova matriz com os resultados das subtrações
# list, list -> list
def subtrai_matriz(m1, m2):
    subtracao = list()
    for i in range(len(m1)):
        subtracao.append([])
        for x in range(len(m1[i])):
            op = m1[i][x] - m2[i][x]
            subtracao[i].append(op)
    return subtracao

# Questão 5
# Função que percorre uma matriz contatos verificando se na posição 1 de cada elemento dessa matriz é igual a uma tupla "num_telefone"
# tuple, list -> list
def quem_ligou(num_telefone, contatos):
    for i in range(len(contatos)):
        if contatos[i][1] == num_telefone:
            return contatos[i]
    return []

# Questão 6
# Função que percorre cada elemento de uma lista "data" retornando os elementos que possuem na possuem na posição 2 um dado igual a "setor"
# string, list
def busca(setor, data):
    resultado = list()
    for i in range(len(data)):
        if data[i][2] == setor:
            resultado.append(data[i])
    return resultado

# Questão 7
# Função que retorna a quantidade de elementos 1 nas listas passadas dentro de uma lista "lampadas_esquina" passada como parametro
# list -> int
def lampadas_acesas(lampadas_esquina):
    acesas = 0
    for i in range(len(lampadas_esquina)):
        for x in range(len(lampadas_esquina[i])):
            if lampadas_esquina[i][x] == 1:
                acesas+=1
    return acesas

# Testes
# 1
# Teste 1 -> deve retornar True em uma matriz 2x2
print(eh_quadrarda([[1,2],[3,4]]))
# Teste 2 -> deve retornar False em uma matriz 2x3
print(eh_quadrarda([[1,2],[3,4],[3,4]]))
# Teste 3 -> deve retornar True em uma matriz vazia
print(eh_quadrarda([]))

# 2
# Teste 1 -> Deve retornar 2, a quantidade de números maior que 2 (3,4)
print(conta_numero(2,[[1,2],[3,4]]))

# 3
# Teste 1 -> Deve retornar [[2, 16, -6], [8, -4, 10]] => [[2*1,2*8,2*-3],[2*4,2*-2,2*5]]
print(multiplica_matriz(2,[[1,8,-3],[4,-2,5]]))

# 4
# Teste 1 -> Deve retornar [[-1, 1], [-5, 0], [0, -4]] => [ [1-2, 2-1], [3-8,4-4], [5-5,6-10] ]
print(subtrai_matriz([[1,2],[3,4],[5,6] ],[[2,1], [8,4], [5,10]]))

# 5
# Teste 1 -> Deve retornar ['Bruno Campos 4', ('21', '3399225411'),'brunoc91@emailquente.com.br', '@brunocampos91', 1] => os dados do contato que possui o número ('21', '3399225411')
print(quem_ligou(('21', '3399225411'),
    [
        ['Bruno Campos', ('21','33992211'), 'brunoc91@emailquente.com.br', '@brunocampos91',1],
        ['Bruno Campos 3', ('21', '99112233'),'brunoc91@emailquente.com.br', '@brunocampos91', 1],
        ['Bruno Campos 4', ('21', '3399225411'),'brunoc91@emailquente.com.br', '@brunocampos91', 1]
    ]
))

# 6
# Teste 1 -> Deve retornar [["AdalbertoFerreira", "1091982", "Contabilidade", "(21)90281-9983"],["Flavia Amorim", "128938", "Contabilidade", "(22)99273-9404"]]],
# elementos que possuem "Contabilidade" na posição 2 da lista
P = [["AdalbertoFerreira", "1091982", "Contabilidade", "(21)90281-9983"],
    ["Juliana Vasconcelos", "111722", "Recursos Humanos", "(21)998-181902" ],
    ["Flavia Amorim", "128938", "Contabilidade", "(22)99273-9404"]]
print(busca("Contabilidade", P))

# 7
# Teste 1 -> Deve retornar 8 => quantidade somada de elementos igual a 1 em cada lista (4 + 4)
print(lampadas_acesas([[0,1,1,1,0,1],[1,0,0,1,1,1]]))