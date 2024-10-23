senha = input("Crie uma senha: ")
tent = 0

while tent < 5:
    senha_1 = input("Digite a senha: ")
    
    if senha_1 == senha:
        print("Senha correta.")
        break
    else:
        tent += 1
        print("A senha está incorreta.")
        print("Você tem " + str(5 - tent) + " tentativas restantes.")
        
if tent == 5:
    print("Acabaram suas tentativas.")

exit = input("Pressione enter para sair.")