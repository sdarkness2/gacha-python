from random import randint, choice
import sqlite3
from datetime import date
import funcoesadicao

data_atual = date.today()

conn = sqlite3.connect('desejo.db')
cursor = conn.cursor()

conn2 = sqlite3.connect('ordem.db')
cursor2 = conn2.cursor()

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

    if funcoesadicao.pitCinco() == funcoesadicao.pit2Cinco():
        randomize = choice(p5)
        inserirSql(randomize)
        print("Você recebeu o personagem {}." .format(randomize))
        funcoesadicao.zerarCinco()
        if funcoesadicao.pitQuatro() == funcoesadicao.pit2Quatro():
            funcoesadicao.zerarQuatro()
        else:
            funcoesadicao.aumentarQuatro()
    elif funcoesadicao.pitQuatro() == funcoesadicao.pit2Quatro():
        chance = randint(1, 10000)
        if chance <= 160:
            randomize = choice(p5)
            print("Você recebeu o personagem \033[1;31m{}\033[0;0m." .format(randomize))
            inserirSql(randomize)
            funcoesadicao.zerarCinco()
            funcoesadicao.zerarQuatro()
        else:
            randomize = choice(p4)
            print("Você recebeu o personagem \033[1;34m{}\033[0;0m." .format(randomize))
            inserirSql(randomize)
            funcoesadicao.zerarQuatro()
    else:
        chance = randint(1, 10000)
        if chance <= 63:
            randomize = choice(p5)
            print("Você recebeu o personagem \033[1;31m{}\033[0;0m." .format(choice(randomize)))
            inserirSql(randomize)
            #deztiro += 1
            funcoesadicao.aumentarQuatro()
            #pit = 0
            funcoesadicao.zerarCinco()
        elif chance >= 8800:
            randomize = choice(p4)
            print("Você recebeu o personagem \033[1;34m{}\033[0;0m." .format(randomize))
            inserirSql(randomize)
            #deztiro = 0
            funcoesadicao.zerarQuatro()
            #pit += 1
            funcoesadicao.aumentarCinco()
        else:
            randomize = choice(p3)
            print("Você recebeu o personagem {}." .format(randomize))
            inserirSql(randomize)
            #pit += 1
            funcoesadicao.aumentarCinco()
            #deztiro += 1
            funcoesadicao.aumentarQuatro()
    conn.commit()

def lervalores():
    cursor.execute("""
    SELECT * FROM desejos;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()