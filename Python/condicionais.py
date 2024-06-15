idade = int( input('Quantos anos você tem? ') )

if idade >= 18:
    print("Você é maior de idade!!! :D")
else:
    print("Você é menor de idade! >:(")

"""media = float(input('Informe a média do estudante: '))
if media >= 7:
    print("Você foi aprovado(a)")
elif media >= 5:
    print("Recuperação")
else:
    print("Você foi reprovado(a)")"""

media = float(input('Informe a média do estudante: '))
presença = int(input('Informe a presença do estudante: '))
if media >= 7 and presença >= 70:
    print("Aprovado(a)")
    print("Parabéns!!!")
elif media >= 5 and presença >= 50:
    print("Recuperação")
    print("Você consegue!!")
else:
    print("Reprovado")
    print("Não se desanime!")