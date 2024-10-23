print("CAUCULE A IDADE PELAS DATAS")

dia1 = int(input("Digite a dia inicial:"))
mes1 = int(input("Digite a mes inicial:"))
ano1 = int(input("Digite a ano inical:"))

dia2 = int(input("Digite o dia final:"))
mes2 = int(input("Digite o mes final:"))
ano2 = int(input("Digite o ano final:"))

dia = 1
mes = dia * 30
ano = mes * 12

subano = ano2 - ano1
submes = mes2 - mes1
subdia = dia2 - dia1

interano = subano * ano
intermes = submes * mes
interdia = subdia * dia

dias = interano + intermes + interdia
idade = dias/360

print("Se passaram ", dias, "dias entre ", dia1, "/", mes1, "/", ano1, " e ", dia2, "/", mes2, "/", ano2)
print("Você tem ", format(idade, ".0f"), " anos")