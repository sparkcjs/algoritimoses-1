# num =  int (input ("Digite um valor: "))
# if (num >0):
#     print("O numero e positivo")
# else:
#     print ("O numero e negativo")

# num1 = int(input("Digite um numero: "))
# num2 = int(input("Digite outro numero: "))
#
# if (num1 > num2):
#     print("O numero maior é",  num1)
# else:
#     print("O numero menor é", num2)
#Faça um programa que peça um valor e informe na tela se o número é par ou ímpar.

# num = int(input("Digite um numero: "))
# if (num %2):
#     print("O numero digitado e Impar")
# else:
#     print("Onumero digitado e Par")

#Faça um Programa que peça um número e informe se este número é múltiplo de 3.
# num = int(input("Digite um numero:" ))
# if not (num %3):
#     print("É multiplo de 3")
# else:
#     print("Não é multiplo de 3")

#Faça um programa que peça dois números e informe se o primeiro é múltiplo do segundo.
# num = int(input("Digite um numero: "))
# num2 =int(input("Digite outro numero: "))
# if not (num%3):
#     print("O numero e multiplo do primeiro")
# else:
#     print("O numero não é multiplo")

#Faça um Programa que verifique o sexo de uma pessoa. O usuário deve informar ‘F’ ou ‘M’
# sexo = input("Digite um sexo (M ou F)?: "))
# sexo = sexo.upper();
# if (sexo == 'M' or sexo == "MASCULINO"):
#     print("O sexo e Masculino")
# else:
#     print("O sexo e Feminino")

#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é maior que C.
#
# num = input("Digite um numero:" )
# num2 = input("Digite outro valor" )
# num3 = input("Digite Mais um valor" )
# num = int(num)
# num2 = int(num2)
# soma = num + num2
# soma = int(soma)
# num3 = int(num3)
# if (soma > num3):
#     print("A soma de num + num2 e menor que num3")
# else:
#     print("A soma de num+num2 maior que num3")
#
# Faça um algoritmo que peça um número e se ele for par some 5, se não, some 8.
#
# num1 = int(input("Digite um numero: "))
# if (num1 %2):
#     print("O numero é impar", num1+8)
# else:
#     print("O numero é par" , num1+5)
#
# Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
#
# trab = input ("Qual foi a nota do trabalho? 0 a 100? ")
# trab = int(trab)
# prov = input("Qual foi a nota da prova? 0 a 100?")
# prov = int(prov)
# ano = trab + prov
# ano = int(ano)
# result = ano /2
# result = int(result)
# if (result>= 60):
#     print("aprovado")
# else:
#     print("reprovado")

# idade = input("Digite sua idade: ")
# idade = int(idade)
#
# if(idade < 0 ):
#     print("Idade inválida!")
# elif (idade < 3):
#     print("Bebê detectado!")
# elif(idade <= 12 ):
#     print("Criança detectado")
# elif(idade < 18):
#     print("Adolescente!")
# elif(idade < 60 ):
#     print("Adulto!")
# else:
#     print("Melhor idade :D")


# print("1- Cadastrar")
# print("2- Alterar")
# print("3- Excluir")
# print("4- Consultar")
# print("5- Imprimir relatorio")
#
# op = input(" Qual opção você deseja? ")
# op = int(op)
#
# if(op == 1):
#     print("você escolheu cadastrar")
# elif(op == 2):
#     print("você escolheu alterar dados")
# elif(op == 3):
#     print("você escolheu excluir dados")
# elif(op == 4):
#     print("você escolheu imprimir relatorio")
# else:
#     print("opção não encontrada")

# a=  input("Digite um valor: ")
# b= input("Digite outro valor: ")
# c= input("Digite outro Valor: ")
#
# a= int(a)
# b= int(b)
# c= int(c)
#
# if (a> b and a>c ):
#     print("Valor A e maior que numero")
# elif (b > a and b>c ):
#     print("Valor b é o maior numero")
# elif(c> a and c>b):
#     print("Valor c é o maior numero")

#Construa um programa que recebe três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente

a= input("Digite um valor: ")
b= input("Digite outro valor: ")
c= input("Digite outro Valor: ")

a= int(a)
b= int(b)
c= int(c)

if (a > b and a > c and b > c ):
    print("Os numeros são: ",a,b,c)
elif(a>b and a>c and c>b):
    print("Os numeros são: ",a,c,b)

elif(c > b and c > a and b > a ):
    print("Os numeros são:",c,b,a)

elif(b > a and b > c and a > c ):
    print("Os numeros são:",b,a,c)

elif(c > a and b > c and b > a ):
    print("Os numeros são:",c,a,b)

elif(b > c and b > c and a < c ):
    print("Os numeros são:",c,b,a)




# if(a>b and a>c):
#     if(b>c):
#         print(a,b,c)
#     else:
#         print(a,c,b)
# elif()    metodo simples
