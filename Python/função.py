# Funções já usadas anteriormente

"""
print() imprime uma imagem (int, float, str) no console (terminal, cmd)
input() retorna dado informado por usuário
len() recebe uma lista e retorna o tamanho da lista
max() recebe uma lista e retorna o maior valor da lista
"""

# função inicial
def Saudações(nome, site="PORNÔ GAY"):
    print(site)
    print(f"BEM VINDO AO SITE DE {site}")
    print(f"AOOOOHN OOOOHN OOOOOOHN {nome}-SENPAIIII")
nome = input("Defina seu nome ")
Saudações(nome)

def soma (n1, n2):
    return n1 + n2
resultado = soma(5, 7)
print("O resultado da soma é", resultado)

def calculadora(n1, n2, operação="+"):
    if operação == "+":
        return n1 + n2
    elif operação == "-":
        return n1 - n2
    elif operação == "/":
        return n1 / n2
    elif operação == "*":
        return n1 * n2
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
resultado = calculadora(n1, n2, "*")
print(resultado)