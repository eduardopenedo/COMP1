# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223


##Cálculos Geométricos

# Questão 1 -> Calcula área de um retângulo dados base e altura, a função retorna o 
def AreaTriangulo(base, altura):
    return (base * altura)/2

# Questão 2 -> Calcula a área de uma circunferência através de um raio
def AreaCircunferencia(raio):
    return 3.1415 * raio * raio

##Cálculos Algébricos

# Questão 1 -> Calcula a média aritmética de três números
def MediaAritmetica(numero1,numero2,numero3):
    return (numero1+numero2+numero3)/3

# Questão 2 -> Calcula resultado da expressão abaixo através de um valor
# passado como parâmetro     
#          1
#---------------------
#   1      +       1
#           ---------------
#            1   +     1
#                  ---------
#                  1 + valor
def CalculaExpresao(valor):
    return 1/(1+(1/(1+1/(1+valor))))

##Cálculos Aplicados

# Questão 1 -> Calcula a notafinal de um aluno através de suas notas de teste1,
# teste2 e prova passados como parâmetro

def NotaFinal(prova, teste1, teste2):
    return (0.8* prova) +(0.2* ((teste1+teste2)/2))

# Questão 2 -> Função que retorna o valor de desconto, que é 20% do valor total
# da compra
def CalcularDesconto(valortotal):
    return 0.2*valortotal