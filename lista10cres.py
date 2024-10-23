# Escreva um programa em pyhton3 que leia uma lista com 10 elementos
# numéricos, coloque essa lista em ordem crescente e
# mostre-a no monitor.

L1 = [0] * 10
x = y = i = aux = 0
while i < 10 :
    L1[i] = int (input('digite o num.{}: '.format(i+1)))
    i = i + 1

while x < 9 :
    y = x + 1
    while y < 10 :
        if L1[x] > L1[y]:
            aux = L1[x]
            L1[x] = L1[y]
            L1[y] = aux
        y = y + 1
    x = x + 1

print(L1)
print ("fim da execucao")