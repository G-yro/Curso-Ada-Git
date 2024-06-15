nsorteado = 6
nescolhido = int( input("Quanto é 3 * 2? ") )
while nescolhido != nsorteado:
    print("Você errou :( Tente novamente!")
    nescolhido = int( input("Quanto é 3 * 2? ") )
if nescolhido == nsorteado:
    print("Parabéns!")

contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1