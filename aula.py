# a = float(input ("Digite um numero:" ))
# b = float(input ("Digite outro um numero: "))
# c = float(input ("Digite mais um numero: "))
#
# if (a > b and a > c):
#     print("O numero e",a )
# elif (b > a and b > c):
#     print("O numero e", b)
# elif (c > b and c > a):
#     print("O numero e", c)
# else:
#     print("O numero informado esta incorreto.")


tempo = int(input("Informe o tempo: "))
valor = float(input("Digite o valor da parcela:R$ "))

if (tempo == 1):
    taxa = 2
else:
    taxa = tempo * 2

prestacao = valor + (valor * (taxa / 100) * tempo)
print (prestacao)
