# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

# Item C da Questão 1 do grupo “Cálculos Algébricos”do Laboratório 2.

# Função que retorna o valor de desconto, que é 20% do valor total da compra (lab1)
# float , float -> float
def Desconto(porcentagem,valortotal):
    return porcentagem*valortotal


# Questão 1
# Função que calcula o valor da compra dados os preços de 3 peças, o valor de desconto é dado pela peça de maior valor sobre 100
# float,float,float ->float
def ValorCompra(item1,item2,item3):
    valor_max = max(item1,item2,item3)
    valor_total = item1+item2+item3
    return Desconto(valor_max/100, valor_total)
    

# Questão 2
# Retorna a concatenação de duas strings a e b no formato abba.
# string,string -> string
def Concatenacao(a,b):
    return a+b+b+a


# Questão 3
# Retorna a palavra Feliz Natal, com o último 'a' repetido I vezes
# int-> string
def FelizNatal(I):
    concat = "Feliz Nat" + (I * 'a') + 'l'
    return concat

# Questão 4
# Função que adiciona uma string i em um local x de uma string  s
# string,int,string -> string
def Substitui(s, x, i):
    texto = s[0:x] + i + s[x:]
    return texto

# Questão 5
# Função que recebe uma tupla cm 3 dados (nome,salário fixo e vendas efetuadas) e calcula salário do mês 
# tuple(string,float,float) -> tuple
def Salario(dados):
    nome = dados[0]
    salario_fixo = dados[1]
    vendas_efetuadas = dados[2]
    salario_mes = salario_fixo + (vendas_efetuadas * 0.15)
    return (nome, "TOTAL= R$" + str(salario_mes))  # to-do -> duas casas decimais

# Questão 6
# Função que recebe uma tupla com quatro valores int, checa quais valores são pares e retorna uma nova tupla com eles
# tuple(int,int,int,int) -> tuple
def FiltraPares(tupla):
    pares = ()

    if(tupla[0]%2 == 0):
        pares = pares + (tupla[0],)
    if(tupla[1]%2 == 0):
        pares = pares + (tupla[1],)
    if(tupla[2]%2 == 0):
        pares = pares + (tupla[2],)
    if(tupla[3]%2 == 0):
        pares = pares + (tupla[3],)
    return pares

# Questão 7
# Função retorna o vencedor ou empate de uma batalha dados ataque, defesa e nível de cada jogador. 
# Golpe = (ataque + defesa)/2 + Bonus, sendo o bonus calculado por (ataque/defesa) * nível
# string, int, int, int, string, int, int, int -> string
def Batalhar(nome1, ai, di, li,nome2, ai2, di2, li2):

    Bonus1, Bonus2 = (0,0)

    # bonus = ataque/ defesa vezes nível
    if(li%2==0):
        Bonus1 = (ai/di) * li 
    if(li%2==0):
        Bonus2 = (ai2/di2) * li2

    ValorGolpe1 = ((ai + di)/2)+ Bonus1
    ValorGolpe2 = ((ai + di)/2)+ Bonus2

    if(ValorGolpe1 == ValorGolpe2):
        return "Empate"
    elif(ValorGolpe1>ValorGolpe2):
        return nome1
    elif(ValorGolpe1<ValorGolpe2):
        return nome2

# Questão 8
# Função que calcula imposto de renda dado um salário
# 0 <= salário <=2000 -> isento
# 2000.01 <= salário <= 3000 ->8%
# 3000.01 <= salário <= 4500 ->18%
# salário <= 4500.01 -> 28% 
# float -> float
def IR(salario):
    if(salario>=0 and salario<= 2000):
        return "Isento"
    elif(salario>=2000.01 and salario<= 3000):
        return salario * (8/100)
    elif(salario>=3000.01 and salario<= 4500):
        return salario * (18/100)
    else:
        return salario * (28/100)

# Questão 9
# Função que recebe uma tupla com elementos string(nome) e float(notas) e calcula a média aritmética, média >=7 -> tupla com nome,'aprovado' e'Parabéns! Aprovação direta!', 5<=média<7 ->tupla com nome  'aprovado'; média<5 -> tupla com nome e 'Você foi reprovado'
# tuple(string, float, float, float) -> string
def SIGA(dados):
    res = (dados[0],)
    media = (dados[1] + dados[2] + dados[3])/3
    if media >=7:
        res = res + (media, 'aprovado','Parabéns! Aprovação direta!')
    elif (media<7 and media>=5):
        res = res + (media, 'aprovado')
    else:
        res = res + (media, 'Você foi reprovado')
    return res

# 10 
# Função que checa se uma string ACGT é parte de uma string. Se sim retorna true, caso não, retornará falso
# string -> bool
def DNA(dna):
    return 'ACGT' in dna

# Testes

# Questão 1
# Função que calcula o valor da compra dados os preços de 3 peças, o valor de desconto é dado pela peça de maior valor sobre 100
# int,int,int -> float

# Teste 1 -> Passando os valores 10, 20 e 30 como parâmetros,deverá retornar 18.0
ValorCompra(10,20,30)
# max(10+20+30)/100 * 10+20 +30
# 0.3 * 60 = 18.0

# Teste 2 -> Passando os valores 13, 47 e 90 como parâmetros,deverá retornar 135.0
ValorCompra(13,47,90)
# max(13+47+90)/100 * 13+47+90
# 0.9 * 150 = 135.0


# Questão 2
# Teste-> Deve retornar 'oiio' com os valores 'o' e 'i' passados como parâmetro. (a,b) => abba
Concatenacao('o','i')

# Questão 3
# Teste-> Deve retornar 'Feliz Nataal' com o valores 2 passado como parâmetro
# Feliz Nat + a + a + l
FelizNatal(2)

# Questão 4
# Teste-> Deve inserir a string 'a' na posição 1 da string 'pizza', retornando 'paizza'
Substitui('pizza', 'a', 1)

# Questão 5
# Teste-> Deve retornar ('joão', "TOTAL= R$ 1015"), ('joão', 1000.0 + (150.0 * 0.15))
Salario(('joão',1000.0,150.0))

# Questão 6
# Deve retornar uma tupla com os valores pares (2,4) contidos na tupla (1,2,3,4) 
FiltraPares((1,2,3,4))

# Questão 8
# Calcula impoosto devido com base no salário
# Teste1 -> Se 0 <= salário <=2000, deve retornar salário (1500.0)
IR(1500)

# Teste2 -> Se 2000.01 <= salário <= 3000, deve retornar salário (2500.0) + (8/100) * salário(2500.0) = 2500.0 + 200.0 = 2700.0
IR(2500)

# Teste3 -> Se 3000.01 <= salário <= 4500, deve retornar salário (3500.0) + (18/100) * salário(3500.0) = 3500.0 + 630.0 = 4130.0
IR(3500)

# Teste3 -> Se salário <= 4500.01, deve retornar salário (5500.0) + (28/100) * salário(5500.0) = 5500.0 + 1.540.0 = 7040.0
IR(5500)

# Questão 9
# Teste1 ->  média >=7 deverá retornar ('Eduardo',8.0, 'aprovado','Parabéns! Aprovação direta!') 
SIGA(('Eduardo',8.0,8.0,8.0))

# Teste2 -> 5<= média <=7 deverá retornar ('Eduardo',6.0, 'aprovado')
SIGA(('Eduardo',6.0,6.0,6.0))

# Teste2 -> média <5 deverá retornar ('Eduardo',4.0, 'Você foi reprovado')
SIGA(('Eduardo',4.0,4.0,4.0))

# Questão 10
# Teste 1 -> Se não houver string 'AGGT' em string retorna false
DNA('acgt')

# Teste 2 -> Se houver string 'AGGT' em string retorna true
DNA('AGGT')
