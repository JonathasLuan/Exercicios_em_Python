pal1 = []
pal2 = []

pal1 = input("Digite a primeira palavra:")
pal2 = input("Digite a segunda palavra:")

tam1 = len(pal1)
tam2 = len(pal2)

if tam1 > tam2:
    maior = pal1
    menor = pal2
else:
    maior = pal2
    menor = pal1
print(maior)
print(menor)