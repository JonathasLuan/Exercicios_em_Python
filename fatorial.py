
sub = 0
print("CÁLCULO DE FATORIAL")
num = int(input("Digite um número:"))
fat = [num]
sub = num - 1
while sub > 0:
    #print(sub)
    fat.append(sub)
    sub -= 1
print(fat)

produto = fat[0]

# Itera sobre os números restantes da lista fat
for i in range(1, len(fat)):
    produto *= fat[i]

# Imprime o produto final
print("O produto dos números na lista é:", produto)