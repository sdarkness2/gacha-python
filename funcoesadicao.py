import sqlite3
conn2 = sqlite3.connect('ordem.db')

cursor2 = conn2.cursor()

def aumentarQuatro():
    cursor2.execute("""
    UPDATE ordem SET quatro = quatro +1;
    """)
    conn2.commit()

def aumentarCinco():
    cursor2.execute("""
    UPDATE ordem SET cinco = cinco +1;
    """)
    conn2.commit()

def zerarQuatro():
    cursor2.execute("""
    UPDATE ordem SET quatro = 0;
    """)
    conn2.commit()

def zerarCinco():
    cursor2.execute("""
    UPDATE ordem SET cinco = 0;
    """)
    conn2.commit()

def pitQuatro():
    cursor2.execute("""
    SELECT quatro FROM ordem""")
    pitQuatroPrint = cursor2.fetchall()
    return pitQuatroPrint

def pitCinco():
    cursor2.execute("""
    SELECT cinco FROM ordem""")
    pitCincoPrint = cursor2.fetchall()
    return pitCincoPrint

def pit2Quatro():
    cursor2.execute("""
    SELECT pitquatro FROM ordem""")
    pit2QuatroPrint = cursor2.fetchall()
    return pit2QuatroPrint

def pit2Cinco():
    cursor2.execute("""
    SELECT pitcinco FROM ordem""")
    pit2CincoPrint = cursor2.fetchall()
    return pit2CincoPrint