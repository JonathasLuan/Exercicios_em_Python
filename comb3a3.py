l1 = [0] * 10
for num in range(0,10):
    l1[num] = int(input("Digite um numero: "))
    
for a in range(0,2):
    for b in range(a+1,3):
        for c in range(b+1,4):
            for d in range(c+1,5):
                for e in range(d+1,6):
                    for f in range(e+1,7):
                        for g in range(f+1,8):
                            for h in range(g+1,9):
                                for i in range(h+1,10):
                                    print(l1[a], l1[b], l1[c], l1[d], l1[e], l1[f], l1[g], l1[h], l1[i])