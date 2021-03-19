from random import randint, choice
import sqlite3
from datetime import date

data_atual = date.today()

conn = sqlite3.connect('desejo.db')
cursor = conn.cursor()

#função principal de desejos
def desejos():
    p5 = ['Diluc', 'Mona', 'Keqing', 'Jean']
    p4 = ['Barbara', 'Fishl', 'Noele', 'Razor']
    p3 = ['Flop']

    if pitCinco() == pit2Cinco():
        randomize = choice(p5)
        inserirSql(randomize)
        print("Você recebeu o personagem \033[1;31m{}\033[0;0m." .format(randomize))
        zerarCinco()
        if pitQuatro() == pit2Quatro():
            zerarQuatro()
        else:
            aumentarQuatro()
    elif pitQuatro() == pit2Quatro():
        chance = randint(1, 10000)
        if chance <= 160:
            randomize = choice(p5)
            print("Você recebeu o personagem \033[1;31m{}\033[0;0m." .format(randomize))
            inserirSql(randomize)
            zerarCinco()
            zerarQuatro()
        else:
            randomize = choice(p4)
            print("Você recebeu o personagem \033[1;34m{}\033[0;0m." .format(randomize))
            inserirSql(randomize)
            zerarQuatro()
    else:
        chance = randint(1, 10000)
        if chance <= 63:
            randomize = choice(p5)
            print("Você recebeu o personagem \033[1;31m{}\033[0;0m." .format(choice(randomize)))
            inserirSql(randomize)
            aumentarQuatro()
            zerarCinco()
        elif chance >= 8800:
            randomize = choice(p4)
            print("Você recebeu o personagem \033[1;34m{}\033[0;0m." .format(randomize))
            inserirSql(randomize)
            zerarQuatro()
            aumentarCinco()
        else:
            randomize = choice(p3)
            print("Você recebeu o personagem {}." .format(randomize))
            inserirSql(randomize)
            aumentarCinco()
            aumentarQuatro()
    conn.commit()

#le os valores e mostra na tela
def lervalores():
    cursor.execute("""
    SELECT * FROM desejos;
    """)
    for linha in cursor.fetchall():
        print(linha)

#Aumenta o numero do pit de 4 estrelas, no caso para chegar ao pit
def aumentarQuatro():
    cursor.execute("""
    UPDATE ordem SET quatro = quatro +1;
    """)
    conn.commit()

#Aumenta o numero do pit de 5 estrelas, no caso para chegar ao pit
def aumentarCinco():
    cursor.execute("""
    UPDATE ordem SET cinco = cinco +1;
    """)
    conn.commit()

#zera o pit de 4 estrelas
def zerarQuatro():
    cursor.execute("""
    UPDATE ordem SET quatro = 0;
    """)
    conn.commit()

#zera o pit de 5 estrelas
def zerarCinco():
    cursor.execute("""
    UPDATE ordem SET cinco = 0;
    """)
    conn.commit()

#mostra como está o pit de 4 estrelas(ex, fez 3 desejos, vai estar 3)
def pitQuatro():
    cursor.execute("""
    SELECT quatro FROM ordem""")
    pitQuatroPrint = cursor.fetchall()
    return pitQuatroPrint

#mostra como está o pit de 5 estrelas(ex, fez 3 desejos, vai estar 3)
def pitCinco():
    cursor.execute("""
    SELECT cinco FROM ordem""")
    pitCincoPrint = cursor.fetchall()
    return pitCincoPrint

#mostra o pit de 4 estrelas, no caso 9
def pit2Quatro():
    cursor.execute("""
    SELECT pitquatro FROM ordem""")
    pit2QuatroPrint = cursor.fetchall()
    return pit2QuatroPrint

#mostra o pit de 5 estrelas, no caso 89
def pit2Cinco():
    cursor.execute("""
    SELECT pitcinco FROM ordem""")
    pit2CincoPrint = cursor.fetchall()
    return pit2CincoPrint

#Função de inserir personagem no sqlite
def inserirSql(aleatorio):
    cursor.execute("""
    INSERT INTO desejos (personagem, data)
    VALUES (?, ?)
    """, (aleatorio, data_atual))