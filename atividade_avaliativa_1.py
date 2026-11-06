#Questão 1
valor = float(input())
print(f"Valor do Produto  = R$ {valor:.2f}")
print(f"Valor do Desconto = R$ {valor * 0.1:.2f}")
print(f"Valor Final       = R$ {valor - (valor * 0.1):.2f}")

#Questão 2
item = int(input())

listas = []
listas.append([0,10])
listas.append([1,2])
listas.append([2,7])
listas.append([3,8])
listas.append([4,5])
listas.append([5,3])
listas.append([6,22])
listas.append([7,17])
listas.append([8,18])

print("{",end="")
print(f"0:10, 1:2, 2:7, 3:8, 4:5, 5:3, 6:22, 7:17, 8:18",end="")
print("}",end="\n\n")

contador = 0
while contador < len(listas):
 if item in listas[contador]:
  print(f"Item: {item}, foi encontrado na posicao {contador}.")
  break
 contador += 1

if contador == len(listas):
 print(f'Item: {item}, "nao" foi encontrado.')

#Questão 3
valor = float(input())

if valor < 5000:
 print(f"Valor do Produto        = R$ {valor:.2f}")
 print(f"Valor do Desconto (10%) = R$ {valor * 0.1:.2f}")
 print(f"Valor Final             = R$ {valor - (valor * 0.1):.2f}")
else:
 print(f"Valor do Produto        = R$ {valor:.2f}")
 print(f"Valor do Desconto (15%) = R$ {valor * 0.15:.2f}")
 print(f"Valor Final             = R$ {valor - (valor * 0.15):.2f}")

#Questão 4
numero = int(input())

for i in range(numero):
 for j in range(numero):
  if (i not in [0,numero-1]) and (j not in [0,numero-1]):
   print("@ ", end="")
  else:
    print("* ", end="")
 print()

#Questão 5
texto = input()
for j in range(3):
 for i in range(len(texto)):
  print(texto[i], end=" ")
 print()

#Questão 6
texto = input().translate(str.maketrans("", "", ".")).split()
print(f"Existem {len(texto)} palavras, são elas:",end="\n\n")
for i in range(len(texto)):
 print(f"{i+1}a. palavra = "+texto[i])

#Questão 7
valor = int(input())
print("{",end="")
for i in range(valor-1):
  print(i % 2, end=", ")
print(f"{(i+1) % 2}",end="")
print("}",end="")

#Questão 8
lista = []
for i in range(7):
 lista.append(int(input()))

for i in range(len(lista)):
 print(f"x[{i}] = {lista[i]}")

menor = min(lista)
posMenor = lista.index(menor)
maior = max(lista)
posMaior = lista.index(maior)
print()
print(f"Menor elemento, x[%d] = %d" % (posMenor, menor),end="\n")
print(f"Maior elemento, x[%d] = %d" % (posMaior, maior))

#Questão 9
valor = int(input())
for i in range(10):
 print(f"x[{i}] = {valor} + {i} = {valor + i}",end="\n")

#Questão 10
tamanho = int(input())
lista1 = []
for i in range(tamanho):
 lista1.append(int(input()))

lista2 = []
for i in range(tamanho):
 if (lista1[i] < 0):
    lista2.append(-1)
 elif (lista1[i] == 0):
    lista2.append(0)
 else:
    lista2.append(1)

print(lista1,end="\n")
print(lista2)
