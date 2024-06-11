# -*- coding: utf-8 -*-
"""Atividade-PauloCabral.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aDXBE01RCSFr8RI4T1L6i8xyJPN-nE8m

1. Faça um Programa que peça dois números e imprima o maior deles.
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2 :
    print(f"o numero maior é {n1}")
elif n2 > n1:
    print(f"o numero maior é {n2}")
else :
    print("Os números são iguais")

"""2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

valor = int(input("Digite um valor:"))

if valor > 0:
    print("o valor é positivo")
else :
    print("o valor é negativo")

"""3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

sexo = input("Digite o sexo: ")

if sexo == "F" or sexo == "f":
    print("Feminino")
elif sexo == "M" or sexo == "m":
    print("Masculino")
else :
    print("Sexo Inválido")

"""4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = input("Digite uma letra: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("Vogal")
else :
    print("Cosoante")

"""5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")
else :
    print("Reprovado")

"""# Estrutura De Repeticao

1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

nota = float(input("digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    nota = float (input("digite uma nota entre 0 e 10 "))

"""2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

usuario = input("digite o seu nome ")
senha = input("digite a sua senha ")

while usuario == senha:
    usuario = input("digite o seu nome ")
    senha = input("digite a sua senha ")

"""3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento."""

paisa = 80000
paisb = 200000
ano = 0

while paisa <= paisb:
    paisa = paisa + (paisa * 0.03)
    paisb = paisb + (paisb * 0.015)
    ano = ano + 1

print (f"o numero de anos necessario é {ano} anos")