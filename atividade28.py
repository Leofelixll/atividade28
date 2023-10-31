# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
today = date.today()
AnoAtual = today.year 

idadeMaior = []
idadeMenor = []

for n in range(1,8):
    AnoNacimento = int(input("digite o seu ano de nacimento: "))
    IdadePessoa = AnoAtual - AnoNacimento 
    
    if IdadePessoa >= 18:
      idadeMaior.append(AnoNacimento)
    else: 
      idadeMenor.append(AnoNacimento)

print("Maiores de idade {} ". format(idadeMaior)) 
print("Menor de idade {} ". format(idadeMenor)) 
