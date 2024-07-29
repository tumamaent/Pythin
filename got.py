# # solicitar o nome e o endereço do usuário
# nome = "Steve"
# apelido = "Rosh"
# rua = "Rua da Agua"
# cidade_codigo_postal = "Cidade 55574309"

# #Imprimir a Informação
# print(f"{nome} {apelido} {rua} {cidade_codigo_postal}")

# #Solicitar o nome do usuário
# nome = input("Por favor digite um nome: ")

# #Solicitar o ano ao usuário 
# ano = int(input("Por favor digite um ano: "))

# #Imprime a hostória com os dados fornecidos pelo usuário
# print(f"Em {ano}, {nome} descobriu um tesouro escondido em uma ilha misteriosa. Ele foi o primeiro a encontrar o tesouro em {ano}.")


# #Mudar o nome da cidade

# cidade = "São Paulo"
# print("cidade")

# cidade = "Rio Janiero"
# print("cidade")

# #Variavel striking
# nome = "João"
# print(f"Olá, {nome}, tipo; {type(nome)}")

# #Variavel inteiro
# idade = 30
# print(f"Olá, {nome}, você tem {idade} anos, tipo; {type(idade)}")

# #Variavel float
# altura = 1.80
# print(f"Olá, {nome}, você tem {idade} anos e {altura} metros de altura, tipo; {type(altura)}")

# nome = input("Digite seu nome: ")
# ano = input("Digite um ano: ")

# frase = "Ante cavaleiro, na"
# frase_completa = nome + "," + ano + " " + frase
# print(frase_completa)


# ano = int(input("Coloque aqui o ano de nascimento"))
# print(f("Ao final de 2024 voce terá: (2024 - ano)"))

# altura = float(input("Qual é sua altura"))
# peso = float(input("Qual é seu peso"))

# imc = peso / (altura / 100) ** 2
# print(f"Seu IMC é: {imc:}")


# numero = int(input("Digite um número: "))
# inc = numero * 5
# print(f"(numero) vezes 5 é (numero * 5) ")

# nome = input("Qual é seu nome: ")
# ano = int(input("Em que ano voce nasceu: "))

# ano = int(input("Coloque aqui o ano de nascimento"))
# print(f"Ao final de 2024 voce terá: (2024 - ano)")



# preco_produto = float(input("Digite o seu preço:R$ "))
# desconto = float(input("Digite o desconto (%): "))
# valor_desconto = (preco_produto * desconto)
# novo_preco = preco_produto - desconto
# print(f"O preço do produto é R$ {preco_produto:.2f}")
# print(f"O desconto é de R$ {valor_desconto:.2f}")

# valor_em_reais = float(input("Digite o valor em reais: "))
# taxa_de_cambio = 0.18
# valor_em_dolares = valor_em_reais * taxa_de_cambio
# print(f"R${valor_em_reais:.2f} equivalem a ${valor_em_dolares:.2f} dólares americanos.")

# idade = int(input("Digite a idade da pessoa:"))

# if idade >= 16:
#     print("Pode votar")

# else:
#    print("Não pode votar")

# num1 = float(input("Diite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# media = (num1 + num2) / 2
# print("A média é: ", media)

# gol_casa = int(input("Pontuação de casa: "))
# gol_visitante = int(input("Pontuação do visitante: "))
# if gol_casa > gol_visitante:
#     print("Casa venceu")
# elif gol_casa < gol_visitante:
#   print("Visitante venceu")


# num3 = int(input("Digite o primeiro número: "))
# num4 = int(input("Digite o segundo número: "))

# if num3 == num4:
#    print("Os números são iguais")
# else:
#    if num3 > num4:
#       print("O primeiro número é maior")
# else:
# print("O segundo número é maior")

# nome1 = input("Digite o primero nome")
# idade1 = input("Digite a primeira idade")

# nome2 = input("Digite o segundo nome")
# idade2 = input("Digite a segunda idade")
# if idade1 > idade2:
#    print(f"{nome1} é mais velho(a)")
# elif idade2 > idade1:
#    print(f"{nome2} é mais velho(a)")
# else:
#    print("São da mesma idade")


#    numero = int(input("Entre com um numero"))
#    if numero >= 5 and numero <= 8:
#       print("O numero está entre 5 e 8")

# idade = int(input("Digite sua idade: "))      
# if idade < 5:
#    print("Essa idade não é plausivel.")
# elif idade > 120:
#   print("Essa idade não é plausivel.")
# else:
#    print("Essa idade é plausivel.")
   
# nome = input("Digite seu nome: ")
# if nome == "Huginho" or nome == "Zezinho" or nome == "Luisinho":
#   print(f"{nome} é um dos sobrinhos do Pato Donald")
# elif nome == "Chiquinho" or nome == "Francisquinho":
#    print(f"{nome} é um dos sobrinhos do Myker Mouse")
# else:
#    print("Essa pessoa não é um dos sobrinhos do Pato Donald ou do Mykey Mouse.")

# nomezinho = input("Digite o nome do aluno: ")
# pontos = int(input("Digite a primeira nota: "))

# if pontos < 0:
#  print("impossivel")
# elif pontos > 49:
#  print("Reprovado")
# elif pontos > 59:
#  print("1")
# elif pontos > 69:
#  print("2")
# elif pontos > 79:
#    print("3")
# elif pontos > 89:
#    print("4")
# elif pontos > 99:
#    print("5")
# else:
#    print("impossivel")

# numero = int(input("Digite um número inteiro: "))
# if numero % 3 == 0 and numero % 5 == 0:
#    print("FizzBuzz")
# elif numero % 3 == 0:
#    print("Fizz")
# elif numero % 5 == 0:
#    print("Buzz")
# else:
#    print(numero)

# while True:
#    numero = int(input("Digite um número inteiro: ou digite  -1 para pagar: "))
#    if numero == -1:
#       break

#       print("numero ** 2")
#       print("Programa enrrado,Obrigado!")

# while True:
#    codigo = input("Por favor,insira o PIN:")
#    if codigo == "1234":
#       break
#    print("Errado!.. tente de novo")

#    print("PIN correto! Obrigado")


# print("Ola")
# while True:
#    resposta = input("Voce quer continuar?: ")
#    if resposta.lower() == "Não":
#       print("Okay! Até a proxima")
#       break

# from math import sqrt
# while True:
#    numero = int(input("Digite um número inteiro: "))
#    if numero < 0:
#       print("Número Invalido")
#    elif numero > 0:
#       print("Á raiz quadrada de {numero} e {sqrt{numero}}")
#       break

# numero = 5
# print("Contagem Regresiva!")
# while numero > 0:
#    print(numero)
#    numero -= 1
# print("Agora!")




# senha = input("Digite sua senha: ")
# while senha != "1234":
#    print("Senha incorreta! Tente novamente")
#    senha = input("Digite sua senha: ")
#    print("Senha correta! Obrigado")
#    break

# tentativas = 0
# while True:
#    pin = input("Digite o codigo PIN: ")
#    tentativas +=1
#    if pin == "4231":
#       print("PIN correto! Obrigado")
#       break


# numero = int(input("Por favor, diigte um numero: "))
# while numero < 10:
#    print("Numero")
#    numero += 1
#    print("Execução Finalizada")


# numero = 2
# while numero < 30:
#    print(numero)
#    numero +=2




# print("Voce esta pronto?")
# numero = int(input("Por favor, digite um numero"))
# while numero != 42:
#    print(numero)
#    print("Agora")
#    numero += 1

# numero = int(input("Digite um número: "))
# i = 1
# while i < numero:
#    print(i)
#    i += 1
#    break

# def dobrar_ate_limite(limite)
#    numero = 1
#    while numero < limite:
#       print(numero * 2)
#       numero += 1
#       limite = int(input("Digite o seu limite: "))
#       dobrar_ate_limite(limite)

# base = int(input("Digite a base: "))
# expoente = int(input("Digite o expoente: "))

# resultado = 1
# while expoente > 0:
#    resultado *= base
#    expoente -= 1
#    print("O resultado é: ", resultado)

# soma = 0
# numero = 0
# while numero <= 100:
#    numero = int(input("Digite um número: "))
#    soma += numero
#    print("A soma total é: ", soma)

# import re
# def valida_senha(senha):
#    if len (senha) < 8:
#       return False
#    if not re.search("[a-z]", senha):
#       return False
#    if not re.search("[A-Z]", senha):
#       return False
#    if not re.search("[0-9]", senha):
#       return False
#    if not re.search("[@#$%&]", senha):
#       return False
#       return True
#    while True:
#       senha = input("Digite sua senha: ")
#       if valida_senha(senha):
#          print("Senha válida")
#          break
#       else:
#          print("Senha inválida")

# import random
# numero_secreto = random.randint(1,100)
# tentativas = 0
# while tentativas < 5:
#    tentativas = int(input("Adivinhe o número entre 1 a 100: "))
#    tentativas += 1
#    if tentativas == numero_secreto:
#       print("Parabéns, voce acertou")
#       break
#    elif tentativas < numero_secreto:
#       print("Tente um número maior")
#    else:
#       print("Tente um número menor")
#       if tentativas == 5:
#          print("Você perdeu")

# saldo_disponivel: 1000
# while True:
#    valor_saque = int(input("Insira o valor do saque: "))
#    if valor_saque %10 == 0:
#       print("Valor Invalido")
#       print("Saque Efetuado")
#       break

# while True:
#    palavra1 = input("Digite a primeira palavra:  ")
#    palavra2 = input("Digite a segunda palavra:  ")
#    if palavra1 == palavra2:
#       print("Palavras iguais")
#       break
#    else:
#       print("Palavras diferentes")

# palavra = "banana"
# print("palavra",3)

# string_entrada = input("Por favor, digite uma strikng")
# print("string_entrada ")
# print("" * len(string_entrada))

# def encontrar_maior_string(string1,string2)
#    if len(string1) > len(string2):
#       return string1
#    else:
#       return string2
# string1 = input("Digite a primeira string: ")
#    string2 = input("Digite a segunda string: ")
#    print(encontrar_maior_string(string1,string2))
#    if len (string1) == len(string2)
#    print("As strings são igualmente longas")
#   else:
#   print(f"A string mais longa")


# import re
 
# while True:
#     entrada = input("Ingrese la longitud de la línea de hashes: ")
   
#     if re.fullmatch("[0-9]+", entrada):
#         longitud = int(entrada)
#         break
#     else:
#         print("Entrada no válida. Por favor, ingrese un número entero.")
 
# print('#' * longitud)

# def pritn_string(string)
#    if len(string) >= 20:
#       print(string[:20] + "...")
#    else:
#      print('*'* (20 - len(string)) + string)
#      string = input("Digite uma string: ")
#      print_string(string)


# def imprime_quadrao(palavra):
#    largura =30
#    tamanho_palavra = len(palavra)
#    espacos_laterais = (largura - tamanho_palavra) // 2
#    print("*" * largura)
#    print("*" + " " * espacos_laterais + palavra + " " * espacos_laterais)
#    print("*" * largura)
#    palavra = input("Digite uma palavra: ")
#    imprime_quadrao(palavra)


# while True: #Inicia um Loop Infinito
#    numero = int(input("Por favor digite um numero: ")) #Solicita ao usuario para digitar um numero
#    if numero == -1: #Verifica se o numero digitado # -1
#       break #Se o numero digitado for -1, o loop é encerrado
#    while numero > 0: #Continua o Loop enquanto o numero for maior que 0
#       print(numero) #Imprime o numero digitado
#       numero = 1 #Decrementa o numero 1


# def messeage():
#   print("Hello World")
# messeage()

# def sete_irmãos():
#    irmãos = ["João","Maria","Pedro","Ana","José","Beatriz","Carlos"]
#    irmãos.sort()
#    print(irmãos)
#    sete_irmãos()

# def média (num1,num2,num3):
#    media = (num1 + num2 + num3) / 3
#    print(media)
#   media(10,20,30)

# def printa_varias_vezes(texto, vezes):
#    for _ in range(vezes):
#       print(texto)
#       printa_varias_vezes("Ola,mundo!",3)


# def quadrado_hastag(tamnho):
#    print("#" * tamnho)
#    quadrado_hastag(5)


# def tablero_ajedrez(tamano):
#     fila = 0
#     while fila < tamano:
#         columna = 0
#         linea = ""
#         while columna < tamano:
#             if (fila + columna) % 2 == 0:
#                 linea += "1"
#             else:
#                 linea += "0"
#             columna += 1
#         print(linea)
#         fila += 1
 
def caixa (nome):
    print("##### " , nome)
   
def cumprimentar_varias_vezes(nome, vezes):
    while vezes > 0:
        caixa(nome)
        vezes -= 1
cumprimentar_varias_vezes("####", 3)

#Recebe uma lista como parametro
show_tamanhos = [45, 44, 39, 40]
def mediana(minha_lista: list):
    ordenada = sorted(minha_lista)
    centro_lista = len(ordenada) // 2
    return ordenada[centro_lista]
print( "A mediana é",mediana(show_tamanhos))

idades = [1, 56, 34, 22, 5, 77, 5]
print("A mediana das idades é",mediana(idades))

#retorna uma lista
def entrada_numeros():
    numeros = []
    while True:
        entrada_usuario = input ("Por favor, digite um numero inteiro, deixe em branco para sair: ")
        if entrada_usuario == 0:
            break
        numeros. append(int(entrada_usuario))
        return numeros
    
def tamanh(lista):
    return len(lista)

def rango(numeros):
    if not numeros:
        return 0
    menor = numeors[0]
    maior = numeros[0]
    for i in range(1, len(numeros)):
        if numeros[i] < menor:
            menor = numeros[i]
            if numeros > maior:
                maior = numeros[i]
                return maior - menor
            lista_de_numeros = [1, 5, 3, 8, 2]
            diferenca = rango(lista_de_numeros)
            print("A diferença entre o maior numero e o menor é: {diferenca}")

minha_lista = [1, 2, ,3, 4, 5]

for item in minha_lista:
    print(item)

minha_lista = "python"
for item in minha_lista:
    print(f"(item) * ", end="")
          
