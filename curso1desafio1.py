#Imprima a frase Escola de Dados da Alura!
print('Escola de Dados da Alura!')
#Imprima seu nome e seu sobrenome seguindo a estrutura abaixo:
#Nome: [seu nome]
#Sobrenome: [seu sobrenome]
#M
#I
#R
#L
#A

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

for letra in nome:
    print(letra)


for letra in sobrenome:
    print(*letra, sep="\n")

#Imprima o dia do seu nascimento em formato dia mês ano. Lembrando que os valores de dia e ano não podem estar entre aspas. Supondo uma data de aniversário dia 28 de fevereiro de 2003, o formato deve estar como no exemplo abaixo:
#28 fevereiro 2003
dia_nascimento = int(input('Digite o dia denascimento: '))
mes_nascimento = input('Digite o mês de nascimento: ')
ano_nascimento = int(input('Digite o ano de nascimento: '))
print(f'{dia_nascimento} {mes_nascimento} {ano_nascimento}')

#Imprima, em um único print, o atual ano que você está fazendo esse curso. O valor do ano deve ser um dado numérico e a saída do print deve ser a seguinte:
ano_curso = int(input('Digite o ano que esta fazendo esse curso: '))
print(ano_curso)