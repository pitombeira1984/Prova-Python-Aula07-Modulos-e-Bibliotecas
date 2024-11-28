from random import choice

def SomarDadosLancados():
    print("Bem vindo ao jogo de dados!")
    dado1 = choice(range(1, 7))
    dado2 = choice(range(1, 7))
    soma = dado1 + dado2
    print(f"Você jogou {dado1} e {dado2} e a soma foi {soma}")
SomarDadosLancados()
