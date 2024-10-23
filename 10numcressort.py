lista = []
n = 1
while len(lista) < 10:
    num = int(input(f"Digite 10 números. Número {n}:"))
    if num >= 10:
        print("Digite apenas números de 1 dígito.")
    else:
        lista.append(num)
        n += 1
        print(lista)
if len(lista) == 10:
    lista.sort()
    print("Lista em ordem crescente:")
    print(sorted(lista))
    
