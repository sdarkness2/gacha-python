from random import randint, choice
import sqlite3
from datetime import date

data_atual = date.today()

conn = sqlite3.connect('desejo.db')
cursor = conn.cursor()

#Função de inserir personagem no sqlite
def inserirSql(aleatorio):
    cursor.execute("""
    INSERT INTO desejos (personagem, data)
    VALUES (?, ?)
    """, (aleatorio, data_atual))

#função para selecionar personagem de forma aleatoria
def tiro():
    pit = 0
    deztiro = 0

    p5 = ['Diluc', 'Mona', 'Keqing', 'Jean']
    p4 = ['Barbara', 'Fishl', 'Noele', 'Razor']
    p3 = ['Flop']

    if pit == 90:
        randomize = choice(p5)
        inserirSql()
        print("Você recebeu o personagem {}." .format(randomize))
        pit = 0
        if deztiro >= 9:
            deztiro = 0
        else:
            deztiro += 1
    elif deztiro >= 9:
        chance = randint(1, 10000)
        if chance <= 160:
            randomize = choice(p5)
            print("Você recebeu o personagem \033[1;31m{}\033[0;0m." .format(randomize))
            inserirSql(randomize)
        else:
            randomize = choice(p4)
            print("Você recebeu o personagem \033[1;34m{}\033[0;0m." .format(randomize))
            inserirSql(randomize)
    else:
        chance = randint(1, 10000)
        if chance <= 63:
            randomize = choice(p5)
            print("Você recebeu o personagem \033[1;31m{}\033[0;0m." .format(choice(randomize)))
            inserirSql(randomize)
            deztiro += 1
            pit = 0
        elif chance >= 8800:
            randomize = choice(p4)
            print("Você recebeu o personagem \033[1;34m{}\033[0;0m." .format(randomize))
            inserirSql(randomize)
            deztiro = 0
            pit += 1
        else:
            randomize = choice(p3)
            print("Você recebeu o personagem {}." .format(randomize))
            inserirSql(randomize)
            pit += 1
            deztiro += 1
    conn.commit()

def lervalores():
    cursor.execute("""
    SELECT * FROM desejos;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()