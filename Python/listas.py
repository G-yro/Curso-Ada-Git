"""nota1 = 7.5
nota2 = 9.3
nota3 = 5.7

notas = [7.9, 9.3, 5.7]
lista = []
lista = list()
lista = [18, "Gustavo", 3.14159, True]
lista_de_listas = [10, [1, 2, 3]]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista [-1])
print(lista [-2])
print(lista [-3])
print(lista [-4])"""

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(lista[0:3])
print(lista[4:6])
print(lista[2:6:2])

for elemento in lista:
    print(elemento)

print("Comprimento da lista:", len(lista))

for i in range(len(lista)):
    print(i)

    lista = [1, 3, 12, 8, 2]
print("Pré append:", lista)
lista.append(3)
print("Depois do append:", lista)
lista.insert(2, 10)
print("Depois Insert", lista)

lista2 = [1, 2, 3, 4, 5]

lista.extend(lista2)
print("dps extend", lista)

lista.pop()
print("dps pop", lista)

lista.remove(3)
print("dps remove", lista)

print("Quantidade de '1' na lista:", lista.count(2))

print("indice de '12': ", lista.index(12))

lista.sort
print(lista)

print(len(lista))
print(sum(lista))
print(max(lista))
print(min(lista))