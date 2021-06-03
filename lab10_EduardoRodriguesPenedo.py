# DRE: 120043223
# Nome: Eduardo Rodrigues Penedo

# Questão 1
def faces():
    sequencia = str.split(input("Digite uma sequência de numeros\n> "), " ")
    ultimo_num = 0
    ultimo_num_repetido = 0
    num_faces = 0
    for i in range(len(sequencia)):
        if i != 0:
            if sequencia[i] == ultimo_num and sequencia[i] != ultimo_num_repetido:
                ultimo_num_repetido = sequencia[i]
                num_faces+=1
        ultimo_num = sequencia[i]
    print(num_faces)
# Questão 2
def calculos():
    i = int(input("Digite o valor de i (1-4)\n> "))
    a = int(input("Digite o valor de a\n> "))
    b = int(input("Digite o valor de b\n> "))
    c = int(input("Digite o valor de c\n> "))
    if i == 1:
        print(str.format("Área do Trapézio = {}", ((a*b)*c)/2))
    if i == 2:
        print(str.format("a({}) * a({}) = {}", a, a, a * a))
        print(str.format("b({}) * b({}) = {}", b, b, b * b))
        print(str.format("c({}) * c({}) = {}", c, c, c * c))
    if i == 3:
        print(str.format("M.A = {}", (a+b+c)/3))
    if i == 4:
        numeros = list((range(a, b + 1, c)))
        numeros_str = list()
        for t in range(len(numeros)):
            numeros_str.append(str(numeros[t]))
        soma_str = " + ".join(numeros_str)
        print(str.format("{} = {}", soma_str, sum(numeros)))
# Questão 3

#       Questão 6 - Laboratório 9
#       Função que recebe os dados e percorre cada funcionario de uma lista "data" retornando os elementos que possuem na possuem na posição 2 um dado igual ao parãmetro passado como setor
#       string, list
def busca(setor):
    data = list()
    inserindo_data = True
    while(inserindo_data):
        funcionario = list()
        funcionario.append(input("Insira o nome do funcionário\n> "))
        funcionario.append(int( input("Insira o registro do funcionário\n> ")))
        funcionario.append(input("Insira o setor do funcionário\n> "))
        funcionario.append(input("Insira o telefone do funcionário\n> "))

        if(len(funcionario)>=0 ):
            data.append(funcionario)
            print("Registro inserido com sucesso")
            again_sn = input("Deseja inserir outro funcionário? [S/N]")
            if again_sn == 'N' or again_sn == 'n':
                inserindo_data = False
        else:
            print("Error: Tente novamente")
    resultado = list()
    for i in range(len(data)):
        if data[i][2] == setor:
            resultado.append(data[i])
    print(resultado)

# Testes

# Questão 1
# Deve retornar 2 para a sequencia 4 5 4 2 1 4 4 1 1 3 5 1 2 3 1
faces()
# Deve retornar 2 para a sequencia 3 5 4 3 3 1 3 1 1 1 1 2 5 1 6
faces()

# Questão 2

# Com i = 1, a = 5, b = 17 e c = 3 deve retornar "Área do Trapézio = 127.5" => ((5*17)*3)/2
calculos()
# Com i = 2, a = 5, b = 17 e c = 3 deve retornar:
# "a(5) * a(5) = 25
# b(17) * b(17) = 289
# c(3) * c(3) = 9"
calculos()
# Com i = 3, a = 5, b = 17 e c = 3 deve retornar "M.A = 8.333333333333334"
calculos()
# Com i = 4, a = 5, b = 17 e c = 3 deve retornar "5 + 8 + 11 + 14 + 17 = 55"
calculos()


# Questão 3
# Inserindo os dados abaixo, deve retornar apenas o funcionário do setor "Contabilidade"
# AdalbertoFerreira [ENTER] 1091982 [ENTER] Contabilidade [ENTER] (21)90281-9983 [ENTER] S [ENTER]
# Juliana Vasconcelos [ENTER] 11722 [ENTER] Recursos Humanos [ENTER] 21)998-181902 [ENTER] N [ENTER]
busca("Contabilidade")
