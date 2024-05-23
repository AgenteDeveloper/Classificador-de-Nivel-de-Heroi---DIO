# Classificador de Nivél de Herói em Python

# Entrada de nome, XP e classe do herói
nome = input("Insira o nome do Herói: ")

xp = float(input("Insira o XP total de seu Herói: "))

classe = str(input("Insira a classe do herói: "))

nivel = ""

mensagem = ""



# Identificador de Nível
if xp <= 1000:
    nivel = "Ferro"

elif xp >= 1001 and xp < 2000:
    nivel = "Bronze"

elif xp >= 2001 and xp <= 5000:
    nivel = "Prata"

elif xp >= 5001 and xp <= 7000:
    nivel = "Ouro"

elif xp >= 7001 and xp <= 8000:
    nivel = "Platina"

elif xp >= 8001 and xp <= 9000:
    nivel = "Ascendente"

elif xp >= 9001 and xp <= 10000:
    nivel = "Imortal"

elif xp >= 10001:
    nivel = "Radiante"



# Mensagem de nível
if nivel == "Ferro":
    mensagem = "Você ainda está começando sua jornada, Herói."

elif nivel == "Bronze":
    mensagem = "Está dando os primeiros passos em sua grande jornada, Herói"

elif nivel == "Prata":
    mensagem = "Parece que está evoluindo, mas ainda há muito a conhecer"

elif nivel == "Ouro":
    mensagem = "Continue nesse ritmo herói!"

elif nivel == "Platina":
    mensagem = "Sua história já é conhecida por todos os cantos, mas ainda há o que fazer Herói!"

elif nivel == "Ascendente":
    mensagem = "Seu poder cresce mais forte a medida que evolui, continue assim!"

elif nivel == "Imortal":
    mensagem = "O seu nivel de poder não parece mais humano! Ainda há o que mostrar?"

elif nivel == "Radiante":
    mensagem = "Você se tornou basicamente uma lenda entre mortais!"

print("O Herói chamado de {} de nível {} possui a classe {}".format(nome, nivel, classe))
print(mensagem)



