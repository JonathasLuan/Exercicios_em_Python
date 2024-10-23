l1 = [0] * 10
x = 0
y = 0
i = 0
aux = 0

while i < 10:
    l1[i] = int(input('Digite um num.{}: '.format(i+1)))
    i = i + 1
    
while x < 9:
    y = x + 1
    while y < 10:
            if l1[x] > l1[y]:
                aux = l1[x]
                l1[x] = l1[y]
                l1[y] = aux
            y = y + 1
    x = x + 1

print(l1)

print("fim da execucao")