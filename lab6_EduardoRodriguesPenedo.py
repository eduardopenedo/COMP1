# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

# Questão 1
# Se palavra existe na string frase, retorna frase com palavra com a primeira letra em maiúsculo, caso contrário, insere a palavra na frase na posição indicada
# string,string, int -> string 
def altera_frase(frase, palavra, posicao): 
    palavras = list(frase.split(" "))
    if(palavra in frase):
        palavras[palavras.index(palavra)] = str.capitalize(palavra)
    else:
        palavras.insert(posicao,palavra)
    
    resultado = str.join(' ',palavras)
    return resultado
# Questão 2
# Retorna média aritmética de um campeonato
# list -> float
def faltas(jogos):
    nfaltas = (sum(jogos[0][2]) + sum(jogos[1][2]) +  sum(jogos[2][2]))/3
    return nfaltas

# Questão 3
# Insere um elemento n em uma lista e a ordena
# list, int -> list
def insere(lista_numero,n):
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero

# Questão 4
# Remove os elementos de uma lista que são menores que um numero n (não tenho ideia de como fazer sem o while pois o exercício não cita que o elemento n está presente na lista)
# list, int -> list
def maiores(lista,n):
    maiores = list()
    i=0
    while(i<len(lista)):
        if(lista[i]>n):
            maiores.append(lista[i])
        i+=1
    return maiores

# Questão 5
# Retorna as médias aritméticas de listas que são maiores que 7 (Não há como percorrer todos os elementos da lista sem o while, o tamanho da lista não foi citado no enunciado)
# list -> list
def acima_da_media(notas):
    i=0
    medias = list()
    while i<len(notas):
        medias.append(sum(notas[i])/ len(notas[i]))
        i+=1
    return maiores(medias,7)

# Questão 6
# Recebe uma lista como parâmetro e devolve uma tupla cujo primeiro elemento é True se for uma lista ordenada, caso não seja, retorna Falso. O segundo elemento da tupla é "Crescente" para listas crescentes, "Decrescente" para listas decrescentes ou "Desordenada" quando não é nenhum dos dois tipos de lista  
# list -> tuple
def eh_ordenada(lista):
    lista_sort = lista[:]
    lista_reverse = lista[:]
    lista_sort.sort()
    lista_reverse.reverse
    if(lista == lista_sort):
        return (True, "Crescente")
    if(lista == lista_reverse):
        return (True, "Decrescente")
    else:
        return (False, "Desordenada")

# Questão 7 a
# Adiciona strings nome, telefone, email e instagram em uma lista, caso ele consiga adicionar retorna True, caso não, retorna False. O argumento nome é obrigatório, enquanto telefone, instagram e email são opcionais
# string,string,string,string -> bool 
def criar_contato(nome='', telefone='', email='', instagram=''):
    contatos = list()
    if nome!='':
        contato = [nome, [(telefone[0:3], telefone[3:] )], email, instagram]
        contatos.append(contato)
        return True
    else: 
        return False

# Questão 7 b
# Recebe uma lista(contato) um int(index) e uma string(data) como parâmetros 
# se index>= tamanho da lista retorna false
# se index é igual a 0,2 ou 3 -> atribui a string a posição index do contato e retorna True
# se a index for 1 retorna true, se a data existir no contato remove do contato, caso não, o adiciona a data na lista contato            
# list, int, string -> bool
def atualizar_contato(contato, index, data):
    # contato = [nome, [(telefone[0:3], telefone[3:] )], email, instagram]
    if(index>=len(contato)):
        return False
    elif(index == 0 or index == 2 or index == 3):
        contato[index] = data
        return True
    elif(index==1):
        if data in contato[index]:
            list.remove(contato[index], data)
        else:
            list.append(contato[index],data)
        return True

# Testes 

# Questão 1
# Teste 1 -> Deve retornar "Meu nome é Anna" pois anna existe na string frase
altera_frase("Meu nome é anna","anna",1)

# Teste 2 -> Deve retornar "Meu primeiro nome é anna" pois anna não existe na string frase
altera_frase("Meu nome é anna","primeiro",1)

# Questão 2
# Teste 1 -> Deve retornar 15.333333333333334 => ((10+9) + (5+7) + (7+8))/3
faltas([['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]])

# Questão 3
# Teste 1 -> Deve retornar [2,4,5,6,8,10]
insere([2,4,6,8,10], 5)

# Questão 4
# Teste 1 -> Deve retornar os elementos maiores que 5, [6,7,8,9,10]
maiores([0,1,2,3,4,5,6,7,8,9,10],5 )

# Questão 5
# Teste 1 -> Deve retornar 8, única média maior que 7
acima_da_media([[2,3],[6,10],[4,9]])

# Questão 6
# Teste 1 -> Deve retornar (True,"Crescente") pois é uma lista ordenada e crescente
eh_ordenada([2,3,4,5])

# Teste 2 -> Deve retornar (True,"Decrescente") pois é uma lista ordenada e decrescente
eh_ordenada([6,4,1])

# Teste 3 -> Deve retornar (False,"Desordenada") pois é uma lista desordenada, não sendo decrescente e nem crescente
eh_ordenada([2,3,2,1,0])

# Questão 7a
# Teste 1 -> Deve retornar True pois todos os dados são válidos
criar_contato('Bruno Campos', '2192112-1331', 'brunoc91@emailquente.com.br','@bruninho')

# Teste 2 -> Deve retornar False pois o nome está vazio
criar_contato()

# Questão 7b
# Teste 1 -> Deve retornar True e atualizar o nome do contato
atualizar_contato( ['Bruno Campos', [('21','99112233'), ('21','33992211')],
'brunoc91@emailquente.com.br', '@brunocampos91'],0, 'Bruno Rodrigues Campos')
# Teste 2 -> Deve retornar True e remover o telefone do contato
atualizar_contato( ['Bruno Campos', [('21','99112233'), ('21','33992211')],
'brunoc91@emailquente.com.br', '@brunocampos91'],1, ('21','99112233'))
# Teste 3 -> Deve retornar True e adicionar o telefone do contato
atualizar_contato( ['Bruno Campos', [('21','99112233'), ('21','33992211')],
'brunoc91@emailquente.com.br', '@brunocampos91'],1, ('21','99999-9999'))
