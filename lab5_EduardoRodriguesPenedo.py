# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

# Questão 1
# Retorna o número de palavras em uma string
# string -> int
def NumeroPalavras(frase):
    frase = frase.strip()           
    lista_palavras = frase.split(" ")
    qtd_palavras = len(lista_palavras)
    return qtd_palavras

# Questão 2
# Retorna o número de frases em uma string. Uma frase é identificada por terminar com ... , . , ? ou !
# String -> int
def NumeroDeFrases(texto):
    numero_de_frases = texto.count("?") + texto.count("!")
    if texto.count("...") >0:
        numero_de_frases += (texto.count(".") - (3 * texto.count("..."))) + texto.count("...")
    else:
        numero_de_frases += texto.count(".")
    return numero_de_frases

# Questão 3
# Retorna a concatenação de duas listas de três elementos [a,c,e] e [b,d,f] na forma [a,b,c,d,e,f] 
# list -> list
def AddListas(l1,l2):
    res = l1+l2
    res = res[0::3] +res[1::3] + res[2::3]
    return res
    
# Questão 4 
# Verifica se uma string possui ponto, reticências, exclamação ou interrogação no final da frase, caso sim retorna "Completa", caso não "Mal Elaborada"
# string -> string
def FraseCompleta(frase):
    if((frase[len(frase)-1] == ".") or (frase[len(frase)-1] == "...") or (frase[len(frase)-1] == "!") or (frase[len(frase)-1] == "?") ):
        return "Completa"
    else:
        return "Mal Elaborada"

# Questão 5
# Retira pontuações como '-', ',', ':', '?', '!', '...', '.' de uma string
# string -> string
def TirarPontuacao(texto):
    resultado = texto
    resultado = resultado.replace('-',' ')
    resultado = resultado.replace(',',' ')
    resultado = resultado.replace(':',' ')
    resultado = resultado.replace(';',' ')
    resultado = resultado.replace('!',' ')
    resultado = resultado.replace('?',' ')
    resultado = resultado.replace('...',' ')
    resultado = resultado.replace('.',' ')
    return resultado

# Questão 6
# Retorna um texto com as palavras na ordem inversa
# string -> string
def FraseInvertida(texto):
    texto = TirarPontuacao(texto)
    lista_palavras = texto.split(" ")
    lista_palavras =  lista_palavras[::-1]
    resultado = str.join(" ", lista_palavras)
    resultado = resultado.strip()
    return resultado


## Testes

# Questão 1
# Teste 1 - Deve retornar 10 com uma frase de dez palavras
NumeroPalavras("Nulla lorem nunc, luctus at molestie ac, fringilla in dui.")

# Teste 2 - Deve retornar 5 com uma frase de cinco palavras
NumeroPalavras("In tristique dui in odio.")

# Questão 2
# Teste 1 - Deve retornar 4 com uma frase com 4 pontuações dentre (., ..., ?, !)
NumeroDeFrases("Preciso tirar um cochilo. Meus Deus! Que horas são? Vou perder a minha aula...")

# Teste 2 - Deve retornar 3 com uma frase com 3 pontuações dentre (., ..., ?, !)
NumeroDeFrases("Vestibulum rhoncus imperdiet turpis. et vulputate nunc viverra vitae. Curabitur.")

# Questão 3
# Teste 1 - Deverá retornar uma lista com preenchida com os elementos 1,2,3,4,5,6 nessa ordem ao passarmos as listas [1,3,5] e [2,4,6]
AddListas([1,3,5], [2,4,6])

# Teste 2 - Deverá retornar uma lista com preenchida com os elementos 'a','b','c','d','e','f' nessa ordem ao passarmos as listas ["a","c","e"] e ["b","d","f"]
AddListas(["a","c","e"], ["b","d","f"])

# Questão 4
# Teste 1 - Deverá retornar "Mal Elaborada" pois não possui ponto, reticências, exclamação ou interrogação no final da frase
FraseCompleta("ola, como voce esta hoje")

# Teste 2 - Deverá retornar "Completa" pois possui ponto, reticências, exclamação ou interrogação no final da frase
FraseCompleta("hoje fui na feira, e comprei banana, melao e abacates.")

# Questão 5
# Teste 1 - Deverá retornar a string "Lorem-ipsum?dolor...sit!amet." com espaço no lugar da pontuação ('-', ',', ':', '?', '!', '...', '.')
TirarPontuacao("Lorem-ipsum?dolor...sit!amet.") # => "Lorem ipsum dolor sit amet. "

# Teste 2 - Deverá retornar a string "Vestibulum rhoncus imperdiet turpis, et vulputate nunc viverra vitae. Curabitur." com espaço no lugar da pontuação ('-', ',', ':', '?', '!', '...', '.')
TirarPontuacao("Vestibulum rhoncus imperdiet turpis, et vulputate nunc viverra vitae. Curabitur.") # => "Vestibulum rhoncus imperdiet turpis  et vulputate nunc viverra vitae  Curabitur "

# Questão 6
# Teste 1 - Deverá retornar a frase "Nossa,como eu gosto de chocolate!“ com as palavras na ordem inversa 
FraseInvertida("Nossa,como eu gosto de chocolate!") # => "chocolate de gosto eu como Nossa”

# Teste 2 - Deverá retornar a frase "Donec eleifend est accumsan lacus.“ com as palavras na ordem inversa 
FraseInvertida("Donec eleifend est accumsan lacus.") # => "'lacus accumsan est eleifend Donec'”