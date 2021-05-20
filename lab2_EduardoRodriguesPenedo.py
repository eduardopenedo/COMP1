# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

## Cálculos Algébricos

# Questão 1 Letra B -> Retorna valor total de uma compra descartando o menor valor
# float, float, float -> float
# int, int, int -> int
def ValorTotal(valor1, valor2, valor3):
    return (valor1+valor2+valor3)- min(valor1,valor2,valor3)

# Questão 1 Letra C 

# Função que retorna o valor de desconto, que é 20% do valor total da compra (lab1)
# float , float -> float
def Desconto(porcentagem,valortotal):
    return porcentagem*valortotal

# Função que calcula o valor da compra dados os preços de 3 peças, o valor de desconto é dado pela peça de maior valor sobre 100
# float, float -> float

def ValorCompra(item1,item2,item3):
    return Desconto(max(item1,item2,item3)/100,item1+item2+item3)

# Questão 2 Letra a
# Calcula valor do discriminante dados os valores de a, b e c de uma equação do segundo grau
# int,int,int -> int 
def Discriminante(a,b,c):   
    return (b**2)-(4*a*c)

# Questão 2 Letra b
# Calcula a primeira raiz real de uma equação do segundo grau
# int,int,int -> float   ----------------> Assumindo que o usuário só vai passar valores que tornem o discriminante positivo
def X1(a,b,c):
    return (-b + math.sqrt(Discriminante(a,b,c)))/(2*a)

# Questão 2 Letra c
# Calcula a segunda raiz real de uma equação do segundo grau
# int,int,int -> float   ----------------> Assumindo que o usuário só vai passar valores que tornem o discriminante positivo
def X2(a,b,c):
    return (-b - math.sqrt(Discriminante(a,b,c)))/2*a

# Questão 3 Letra a
# Calcula a aceleração média de um movimento retilíneo uniformemente variado dados velocidade inicial, velocidade final e tempo final
# int, int, int -> float
def AceleracaoMediaMRUV(velocidade_inicial,velocidade_final,tempo_final):
    return (velocidade_final-velocidade_inicial)/(tempo_final - 0)

# Questão 3 Letra b
# Calcula Posição final de um movimento retilíneo uniformemente variado dados posição inicial, velocidade inicial, velocidade final e tempo final
# int, int,int int -> float
def PosicaoFinal(posicao_inicial,velocidade_inicial,velocidade_final, tempo_final):
    return (posicao_inicial+velocidade_inicial*tempo_final)+(AceleracaoMediaMRUV(velocidade_inicial,velocidade_final,tempo_final) *tempo_final**2)/2

## Cálculos Geométricos 
import math

# Questão 1 Letra a
# Calcula a hipotenusa de um triângulo
# int, int -> float
def Hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1**2+cateto2**2)

# Questão 1 Letra b
# Calcula a distância entre dois pontos no plano cartesiano
# int,int,int,int -> float
def DistDoisPontos(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


# Questão 1 Letra c

# Função calcular área triângulo lab1
# int, int -> float
def AreaTriangulo(base, altura):
    return (base * altura)/2

# Calcula área de um hexágono regular
# int -> float
def AreaHexagono(lado):
    return 6*AreaTriangulo(lado, (lado* math.sqrt(3))/2)

# Questão 1 Letra d
# Calcula o comprimento de um circulo através de seu raio
# int -> float
def ComprimentoCirculo(raio):
    return 2 * math.pi * raio

# Questão 2
# Calcula a área de um setor do círculo
# float, float -> float
def AreaSetorCircular(raio, angulo=2):
    return (raio**2) * (angulo * math.pi)
