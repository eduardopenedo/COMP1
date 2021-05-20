# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

################ Grupo I ################

# Questão 1
# Função que recebe horas, minutos e segundos como parâmetros e os retorna no formato hora:minutos:segundos
# int, int, int -> string

def Horas(horas, minutos, segundos):
    return str(horas) +":"+str(minutos)+":"+ str(segundos)


# Questão 2
# Retorna número de raízes reais
# int, int, int -> int

import lab2_EduardoRodriguesPenedo

def NRaizes(a,b,c):
    if lab2_EduardoRodriguesPenedo.Discriminante(a,b,c)<0:
        return 0
    else:
        if lab2_EduardoRodriguesPenedo.Discriminante(a,b,c)==0:
            return 1
        else:
            if lab2_EduardoRodriguesPenedo.Discriminante(a,b,c)>0:
                return 2

################ Grupo II ################

# Questão 1
# Função que retorna fala de personagem, baseada em sua quantidade de energia. Se quantidade <= 8000 retorna "Inseto!", se quantidade>8000 retorna 'Mais de 8000!'
# int -> string

def Energia(qtd_energia):
    if qtd_energia<=8000:
        return 'Inseto!'
    else:
        if qtd_energia>8000:
            return 'Mais de 8000!'

# Questão 2
# Função que calcula se duende Ed fabricará presentes ou deixará para o dia seguinte
# int, int, int -> string

def VaiFabricar(min_ir_embora,min_presente_A,min_presente_B):
    if (min_presente_A + min_presente_B) > min_ir_embora:
        return 'Deixa para amanha!'
    else:
        if (min_presente_A + min_presente_B) <= min_ir_embora:
            return 'Farei hoje!'

################ Grupo III ################

# Questão 1
# Função que retorna repetição de texto através do texto a ser repetido e o número de vezes de repetição como argumentos 
# string, int -> string 

def RepetirTexto(texto,n_vezes):
    return n_vezes * texto

# Questão 3
# Função que retorna se uma árvore está dentro dos padrôes especificados por Roberto
#Padôes: 
# -> 200 <= altura <=300
# -> espessura >= 50 
# -> galhos >= 150
# int, int int -> bool
def ArvoreAceita(altura, espessura, galhos):
    return (altura <=300) and (altura>=200) and (espessura >= 50 ) and (galhos >= 150) 
