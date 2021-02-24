import personagens
from time import sleep

parar = 0

while parar != 1:

    escolha = input("""BANNER DE PERSONAGENS
-----------------OPÇÕES---------------------
[1] - 1 Tiro:
0.63% de chance de personagens 5 estrelas;
11% de chance de personagens 4 estrelas.
[2] - 10 Tiros:
0.63% de chance de personagens 5 estrelas;
11% de chance de personagens 4 estrelas.
QUAL A SUA OPÇÃO? """)
    if escolha == "1":
        sleep(1)
        personagens.tiro()
        sleep(1)
    elif escolha == "2":
        for i in range(10):
            sleep(1)
            personagens.tiro()
            sleep(1)
    parar = input("""DESEJA PARAR DE ATIRAR?
     [1]SIM
     [2]NÃO
     QUAL SUA OPÇÃO? """)
