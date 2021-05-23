# Nome: Eduardo Rodrigues Penedo
# DRE: 120043223

import lab3_EduardoRodriguesPenedo

################ Grupo I ################

# Questão 1
# int, int, int -> string

# Teste 1 -> Deve retornar '22:45:55' com os parâmetros 22,45,55
lab3_EduardoRodriguesPenedo.Horas(22,45,55)

# Teste 2 -> Deve retornar '12:15:25' com os parâmetros 22,45,55
lab3_EduardoRodriguesPenedo.Horas(12,15,25)

# Questão 2
# int, int, int -> int 

# Teste 1 -> Discriminante negativo deve retornar 0
# ∆ = b² - 4ac
# ∆ = (-4)² - 4*1*5
# ∆ = 16 – 20
# ∆ = - 4
lab3_EduardoRodriguesPenedo.NRaizes(1,4,5)

# Teste 2 -> Discriminante nulo deve retornar 1
# ∆ = b² - 4ac
# ∆ = (-4)² - 4*4*1
# ∆ = 16 – 16
# ∆ = 0
lab3_EduardoRodriguesPenedo.NRaizes(4,4,1)

# Teste 3 -> Discriminante positivo deve retornar 2
# ∆ = b² - 4ac
# ∆ = (-5)² - 4*1*6
# ∆ = 25 - 24
# ∆ = 1
lab3_EduardoRodriguesPenedo.NRaizes(1,5,6)


################ Grupo II ################

# Questão 1
# int -> string

# Teste 1 -> Quantidade <8000 deve retornar 'Inseto!'
lab3_EduardoRodriguesPenedo.Energia(5000)

# Teste 2 -> Quantidade =8000 deve retornar 'Inseto!'
lab3_EduardoRodriguesPenedo.Energia(8000)

# Teste 3 -> Quantidade >8000 deve retornar 'Mais de 8000!'
lab3_EduardoRodriguesPenedo.Energia(999999999999999999999999999999) # 😨


# Questão 2
# int -> string

# Teste 1 -> Tempos de presente A somado com presente B MAIOR que os minutos restantes para ir embora deverá retornar 'Deixa para amanha!'
lab3_EduardoRodriguesPenedo.VaiFabricar(10,20,30)

# Teste 2 -> Tempos de presente A somado com presente B MENOR que os minutos restantes para ir embora deverá retornar 'Farei hoje!'
lab3_EduardoRodriguesPenedo.VaiFabricar(50,20,30)


################ Grupo III ################
# Questão 1 
# string, num_vezes -> string  

# Teste 1 -> Deverá retornar 'Feliz Aniversário!!Feliz Aniversário!!Feliz Aniversário!!' quando "Feliz Aniversário!!" e 3 forem passados com parâmetro 
lab3_EduardoRodriguesPenedo.RepetirTexto("Feliz Aniversário!!",3)

# Teste 2 -> Deverá retornar 'kkk' quando "k" e 3 forem passados com parâmetro 
lab3_EduardoRodriguesPenedo.RepetirTexto("k",3)


# Questão 3
# int, int, int -> bool

# Teste 1 -> Deverá retornar true quando todos os requisitos forem atendidos 
# -> 200 <= altura <=300    ✅
# -> espessura >= 50        ✅
# -> galhos >= 150          ✅
lab3_EduardoRodriguesPenedo.ArvoreAceita(200,60,160)


# Teste 2 -> Deverá retornar false quando algum dos requisitos não for atendido
# -> 200 <= altura <=300    ❌
# -> espessura >= 50        ✅
# -> galhos >= 150          ✅
lab3_EduardoRodriguesPenedo.ArvoreAceita(150,50,200)