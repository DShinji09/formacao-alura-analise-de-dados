#Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

#Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Olá, {nome}, você tem {idade} anos.")

#Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
nome = input("digite seu nome:")
idade = int(input("digite sua idade:"))
altura = float(input("digite sua altura em metros:"))
print(f"Olá, {nome}, você tem {idade} anos e mede {altura} metros!")

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))
resultado1 = numero1 + numero2
print(f"A soma dos valores é: {resultado1}")

#Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
numero3 = float(input("Digite o terceiro valor: "))
resultado2 = numero1 + numero2 + numero3
print(f"A soma dos três valores é: {resultado2}")

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
numero4 = float(input("Digite o primeiro valor: "))
numero5 = float(input("Digite o segundo valor: "))
resultado3 = numero4 * numero5
print(f"A multiplicação dos valores é: {resultado3}")

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0
numero6 = float(input("Digite o numerador: "))
numero7 = float(input("Digite o denominador (não pode ser 0): "))
if numero7 == 0:
    print("O denominador não pode ser 0. Por favor, digite um valor diferente de 0.")
else:
    resultado4 = numero6 / numero7
    print(f"A divisão dos valores é: {resultado4}")

#Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
numero8 = float(input("Digite um numero: "))
numero9 = float(input("Digite outro numero: "))
resultado5 = numero8 ** numero9
print(f"A exponenciação dos valores é: {resultado5}")

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0
numero10 = float(input("Digite o numerador: "))
numero11 = float(input("Digite o denominador (não pode ser 0): "))
if numero11 == 0:
    print("O denominador não pode ser 0. Por favor, digite um valor diferente de 0.")
else:
    resultado6 = numero10 // numero11
    print(f"A divisão inteira dos valores é: {resultado6}")

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0
numero12 = float(input("Digite o numerador: "))
numero13 = float(input("Digite o denominador (não pode ser 0): "))
if numero13 == 0:
    print("O denominador não pode ser 0. Por favor, digite um valor diferente de 0.")
else:
    resultado7 = numero12 % numero13
    print(f"O resto da divisão dos valores é: {resultado7}")

#Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media}")

#Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
numero1 = 5
numero2 = 12
numero3 = 20
numero4 = 15
peso1 = 1
peso2 = 2
peso3 = 3
peso4 = 4
media_ponderada = (numero1 * peso1 + numero2 * peso2 + numero3 * peso3 + numero4 * peso4) / (peso1 + peso2 + peso3 + peso4)
print(f"A média ponderada é: {media_ponderada}")

#Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
frase = "Olá, mundo!"
print(frase)

#Crie um código que solicite uma frase e depois imprima a frase na tela.
frase = input("Digite uma frase: ")
print(frase)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
frase = input("Digite uma frase: ")
print(frase.upper())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
frase = input("Digite uma frase: ")
print(frase.lower())

#Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
frase = "   Olá, mundo!   "
print(frase.strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim
frase = input("Digite uma frase: ")
print(frase.strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = input("Digite uma frase: ")
print(frase.strip().lower())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra "f"
frase = input("Digite uma frase: ")
frase_modificada = frase.replace("e", "f").replace("E", "F")
print(frase_modificada)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”
frase = input("Digite uma frase: ")
frase_modificada = frase.replace("a", "@").replace("A", "@")
print(frase_modificada)

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”
frase = input("Digite uma frase: ")
frase_modificada = frase.replace("s", "$").replace("S", "$")
print(frase_modificada)