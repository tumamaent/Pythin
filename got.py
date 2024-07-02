# solicitar o nome e o endereço do usuário
nome = "Steve"
apelido = "Rosh"
rua = "Rua da Agua"
cidade_codigo_postal = "Cidade 55574309"

#Imprimir a Informação
print(f"{nome} {apelido} {rua} {cidade_codigo_postal}")

#Solicitar o nome do usuário
nome = input("Por favor digite um nome: ")

#Solicitar o ano ao usuário 
ano = int(input("Por favor digite um ano: "))

#Imprime a hostória com os dados fornecidos pelo usuário
print(f"Em {ano}, {nome} descobriu um tesouro escondido em uma ilha misteriosa. Ele foi o primeiro a encontrar o tesouro em {ano}.")


#Mudar o nome da cidade

cidade = "São Paulo"
print("cidade")

cidade = "Rio Janiero"
print("cidade")

#Variavel striking
nome = "João"
print(f"Olá, {nome}, tipo; {type(nome)}")

#Variavel inteiro
idade = 30
print(f"Olá, {nome}, você tem {idade} anos, tipo; {type(idade)}")

#Variavel float
altura = 1.80
print(f"Olá, {nome}, você tem {idade} anos e {altura} metros de altura, tipo; {type(altura)}")

nome = input("Digite seu nome: ")
ano = input("Digite um ano: ")

frase = "Ante cavaleiro, na"
frase_completa = nome + "," + ano + " " + frase
print(frase_completa)


ano = int(input("Coloque aqui o ano de nascimento"))
print(f("Ao final de 2024 voce terá: (2024 - ano)"))

altura = float(input("Qual é sua altura"))
peso = float(input("Qual é seu peso"))

imc = peso / (altura / 100) ** 2
print(f"Seu IMC é: {imc:}")


numero = int(input("Digite um número: "))
inc = numero * 5
print(f"(numero) vezes 5 é (numero * 5) ")

nome = input("Qual é seu nome: ")
ano = int(input("Em que ano voce nasceu: "))

ano = int(input("Coloque aqui o ano de nascimento"))
print(f"Ao final de 2024 voce terá: (2024 - ano)")



preco_produto = float(input("Digite o seu preço:R$ "))
desconto = float(input("Digite o desconto (%): "))
valor_desconto = (preco_produto * desconto)
novo_preco = preco_produto - desconto
print(f"O preço do produto é R$ {preco_produto:.2f}")
print(f"O desconto é de R$ {valor_desconto:.2f}")

valor_em_reais = float(input("Digite o valor em reais: "))
taxa_de_cambio = 0.18
valor_em_dolares = valor_em_reais * taxa_de_cambio
print(f"R${valor_em_reais:.2f} equivalem a ${valor_em_dolares:.2f} dólares americanos.")

idade = int(input("Digite a idade da pessoa:"))

if idade >= 16:
    print("Pode votar")

else:
   print("Não pode votar")

num1 = float(input("Diite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
media = (num1 + num2) / 2
print("A média é: ", media)

gol_casa = int(input("Pontuação de casa: "))
gol_visitante = int(input("Pontuação do visitante: "))
if gol_casa > gol_visitante:
    print("Casa venceu")
elif gol_casa < gol_visitante:
  print("Visitante venceu")


num3 = int(input("Digite o primeiro número: "))
num4 = int(input("Digite o segundo número: "))

if num3 == num4:
   print("Os números são iguais")
else:
   if num3 > num4:
      print("O primeiro número é maior")
else:
print("O segundo número é maior")

nome1 = input("Digite o primero nome")
idade1 = input("Digite a primeira idade")

nome2 = input("Digite o segundo nome")
idade2 = input("Digite a segunda idade")
if idade1 > idade2:
   print(f"{nome1} é mais velho(a)")
elif idade2 > idade1:
   print(f"{nome2} é mais velho(a)")
else:
   print("São da mesma idade")


   numero = int(input("Entre com um numero"))
   if numero >= 5 and numero <= 8:
      print("O numero está entre 5 e 8")

idade = int(input("Digite sua idade: "))      
if idade < 5:
   print("Essa idade não é plausivel.")
elif idade > 120:
  print("Essa idade não é plausivel.")
else:
   print("Essa idade é plausivel.")
   
nome = input("Digite seu nome: ")
if nome == "Huginho" or nome == "Zezinho" or nome == "Luisinho":
  print(f"{nome} é um dos sobrinhos do Pato Donald")
elif nome == "Chiquinho" or nome == "Francisquinho":
   print(f"{nome} é um dos sobrinhos do Myker Mouse")
else:
   print("Essa pessoa não é um dos sobrinhos do Pato Donald ou do Mykey Mouse.")

nomezinho = input("Digite o nome do aluno: ")
pontos = int(input("Digite a primeira nota: "))

if pontos < 0:
 print("impossivel")
elif pontos > 49:
 print("Reprovado")
elif pontos > 59:
 print("1")
elif pontos > 69:
 print("2")
elif pontos > 79:
   print("3")
elif pontos > 89:
   print("4")
elif pontos > 99:
   print("5")
else:
   print("impossivel")

numero = int(input("Digite um número inteiro: "))
if numero % 3 == 0 and numero % 5 == 0:
   print("FizzBuzz")
elif numero % 3 == 0:
   print("Fizz")
elif numero % 5 == 0:
   print("Buzz")
else:
   print(numero)

while True:
   numero = int(input("Digite um número inteiro: ou digite  -1 para pagar: "))
   if numero == -1:
      break

      print("numero ** 2")
      print("Programa enrrado,Obrigado!")

while True:
   codigo = input("Por favor,insira o PIN:")
   if codigo == "1234":
      break
   print("Errado!.. tente de novo")

   print("PIN correto! Obrigado")


print("Ola")
while True:
   resposta = input("Voce quer continuar?: ")
   if resposta.lower() == "Não":
      print("Okay! Até a proxima")
      break

from math import sqrt
while True:
   numero = int(input("Digite um número inteiro: "))
   if numero < 0:
      print("Número Invalido")
   elif numero > 0:
      print("Á raiz quadrada de {numero} e {sqrt{numero}}")
      break

numero = 5
print("Contagem Regresiva!")
while numero > 0:
   print(numero)
   numero -= 1
print("Agora!")

   


