# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

import math
## Cálculos Algébricos

# Questão 1 Letra A -> Retorna valor máximo ou mínimo de um conjunto de valores

# Teste 1 -> Deve retornar 3.9 quando os parâmetros forem 3,2.8 e 3.9
# float,float,float->float
max(3,2.8,3.9)

# Teste 1 -> Deve retornar 0 quando os parâmetros forem 7,2,4,1 e 0
# int,int,int->int
min(7,2,4,1,0)

# Questão 1 Letra B -> Retorna valor total de uma compra descartando o menor valor

# Teste 1 -> Passando os valores 5, 10 e 15 como parâmetros, deverá retornar 25
# float, float, float -> float
ValorTotal(5,10,15)
# (5+10+15)- min(5,10,15)
# (30) - (5) = 25 

# Teste 2 -> Passando os valores 5, 10 e 15 como parâmetros,deverá retornar 90.99
# int, int, int -> int
ValorTotal(39.99,50.99,9.99)
# (39.99+50.99+9.99)- min(39.99,50.99,9.99)
# (100.97) - 9.99 = 90.98

# Questão 1 Letra C 
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

# Questão 2 Letra a
# Calcula valor do discriminante dados os valores de a, b e c de uma equação do segundo grau


# Teste 1 -> Passando os valores 2, 3 e -4 como parâmetros,deverá retornar 41
# int,int,int -> int 
Discriminante(2,3,-4)
# (3*3)-(4*2*-4)
# (9) - (-32) = 41


# Teste 2 -> Passando os valores 2, 3 e 4 como parâmetros,deverá retornar -23
# int,int,int -> int 
Discriminante(2,3,4)
# (3*3)-(4*2*4)
# (9) - (32) = -23

# Questão 2 Letra b
# Calcula a primeira raiz real de uma equação do segundo grau

# Teste 1 -> Passando os valores 1, -1 e -20 como parâmetros,deverá retornar 5
# int,int,int -> float   ----------------> Assumindo que o usuário só vai passar valores que tornem o discriminante positivo
X1(1,-1,-20)
# Δ => Discriminante(1,-1,-20)
# Δ => -1 * -1 - 4 * 1 * -20
# Δ => 1 + 80 
# Δ = 81

# (-(-1) + math.sqrt(Δ))/2*1
# (1 + 9)/2
# 10/2 = 5

# Teste 2 -> Passando os valores 1, -1 e 20 como parâmetros,deverá retornar erro
# int,int,int -> erro (raiz negativa)
X1(1,-1,20)
# Δ => Discriminante(1,-1,20)
# Δ => -1 * -1 - 4 * 1 * 20
# Δ => 1 - 80 
# Δ = -79

# (-(-1) + math.sqrt(Δ))/2*1
# ValueError: math domain error

# Questão 2 Letra c
# Calcula a segunda raiz real de uma equação do segundo grau


# Teste 1 -> Passando os valores 1, -1 e -20 como parâmetros,deverá retornar -4
# int,int,int -> float   ----------------> Assumindo que o usuário só vai passar valores que tornem o discriminante positivo
X2(1,-1,-20)
# Δ => Discriminante(1,-1,-20)
# Δ => -1 * -1 - 4 * 1 * -20
# Δ => 1 + 80 
# Δ = 81

# (-(-1) - math.sqrt(Δ))/2*1
# (1 - 9)/2
# -8/2 = -4

# Questão 3 Letra a
# Calcula a aceleração média de um movimento retilíneo uniformemente variado dados velocidade inicial, velocidade final e tempo final

# Teste 1 -> Passando os valores 30, 0 e 15 como parâmetros,deverá retornar -2.0m/s
# int, int, int -> float
AceleracaoMediaMRUV(30,0,15)
# (0-30)/(15 - 0)
# -30/15 = -2.0m/s


# Questão 3 Letra b
# Calcula Posição final de um movimento retilíneo uniformemente variado dados posição inicial, velocidade inicial, velocidade final e tempo final


# Teste 1 -> Passando os valores 0, 10, 0 e 30 como parâmetros a função deve retornar 150.0
# int, int,int int -> float
PosicaoFinal(0,10,0, 30)
# A_média = (10 - 0)/(30 - 0)
# A_média = 10/30 = 1/3

# Posição = posicao_inicial + velocidade_inicial * tempo_final + (A_média * t * t)/2
# Posição = 0 + 0 * 30 + (1/3  * 30 *30)/2
# Posição = (300)/2 = 150.0 

## Cálculos Geométricos 

# Questão 1 Letra a
# Calcula a hipotenusa de um triângulo

# Teste 1 - Deve retornar 10.0 quando catetos forem 6 e 8
# int, int -> float
Hipotenusa(6, 8)
#math.sqrt(6**2+8**2)
#math.sqrt(36+64) = 10.0

# Teste 2 - Deve retornar 40.311288741492746 quando catetos forem 20 e 35
# int, int -> float
Hipotenusa(20, 35)
#math.sqrt(20**2+35**2)
#math.sqrt(400 +1225) = 40.311288741492746

# Teste 3 - Deve retornar 25.0 quando catetos forem 20 e 15
# int, int -> float
Hipotenusa(20, 15)
#math.sqrt(20**2+15**2)
#math.sqrt(400 + 225) = 25.0

# Questão 1 Letra b
# Calcula a distância entre dois pontos no plano cartesiano

# Teste 1 - Deve retornar 7.0 quando catetos forem -4,4,3 e 4
# int,int,int,int -> float
DistDoisPontos(-4,4,3,4)
# math.sqrt((3-(-4))**2+(4-4)**2)
# math.sqrt((7)**2+(0)**2)
# math.sqrt(49) = 7.0

# Teste 2 - Deve retornar 2.0 quando catetos forem 2,4,2,2
# int,int,int,int -> float
DistDoisPontos(2,4,2,2)
# math.sqrt((2-2)**2+(2-4)**2)
# math.sqrt((-2)**2)
# math.sqrt(4) = 2.0

# Teste 3 - Deve retornar 3.6055512755 quando catetos forem 2,1,5 e 3
# int,int,int,int -> float
DistDoisPontos(2,1,5,3)
# math.sqrt((5-2)**2+(3-1)**2)
# math.sqrt(9+4) = math.sqrt(13) = 3.6055512755

# Questão 1 Letra c
# Calcula área de um hexágono regular


# Teste 1 - Deve retornar 10.392304845413264 quando o lado for 2
# int -> float
AreaHexagono(2)
# 6*(2 * 2* math.sqrt(3)/2)/2
# 6*(4* 0.8660254037844386)/2 = 10.392304845413264

# Teste 2 - Deve retornar 64.95190528383289 quando o lado for 5
# int -> float
AreaHexagono(5)
# 6*(5 * 5* math.sqrt(3)/2)/2
# 6*(25* 0.8660254037844386)/2 = 64.9519052838329

# Teste 3 - Deve retornar 210.44417311961854 quando o lado for 9
# int -> float
AreaHexagono(9)
# 6*(9 * 9* math.sqrt(3)/2)/2
# 6*(81* 0.8660254037844386)/2 = 210.4441731196186

# Questão 2
# Calcula a área de um setor do círculo

# Teste 1 - Deve retornar 6.283185307179586 quando o raio for 1
# float, float -> float
AreaSetorCircular(1)
# (1**2) * (2 * math.pi)
# 1 * (2 * 3.1415) = 6.283

# Teste 2 - Deve retornar 6.283185307179586 quando o raio for 1 e o angulo for pi/2
# float, float -> float
AreaSetorCircular(1,1/2)
# (1**2) * (0.5 * math.pi)
# 1 * (0.5 * 3.1415) = 1.57075