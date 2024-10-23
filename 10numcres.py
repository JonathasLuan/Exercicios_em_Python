# Inicializa uma lista vazia para armazenar os números
listNum = []

# Lê 10 números do usuário
print("Digite 10 números:")
for _ in range(10):
    num = int(input())
    listNum.append(num)

# Função para ordenar a lista usando o algoritmo de ordenação por bolha (bubble sort)
def bubble_sort(nums):
    n = len(nums)
    # Faz várias passagens pela lista
    for i in range(n):
        # Em cada passagem, compara pares de elementos adjacentes
        for j in range(0, n-i-1):
            # Se os elementos estiverem fora de ordem, troque-os
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# Ordena a lista
bubble_sort(listNum)

# Exibe os números em ordem crescente
print("Números em ordem crescente:")
for num in listNum:
    print(num)
