from random import randint, choice


def tiro():
    pit = 0
    deztiro = 0

    p5 = ['Diluc', 'Mona', 'Keqing', 'Jean']
    p4 = ['Barbara', 'Fishl', 'Noele', 'Razor']
    p3 = ['Flop']

    if pit == 90:
        print("Você recebeu o personagem {}." .format(choice(p5)))
        pit = 0
        if deztiro >= 9:
            deztiro = 0
        else:
            deztiro += 1
    elif deztiro >= 9:
        chance = randint(1, 10000)
        if chance <= 160:
            print("Você recebeu o personagem \033[1;31m{}\033[0;0m." .format(choice(p5)))
        else:
            print("Você recebeu o personagem \033[1;34m{}\033[0;0m." .format(choice(p4)))
    else:
        chance = randint(1, 10000)
        if chance <= 63:
            print("Você recebeu o personagem \033[1;31m{}\033[0;0m." .format(choice(p5)))
            deztiro += 1
            pit = 0
        elif chance >= 8800:
            print("Você recebeu o personagem \033[1;34m{}\033[0;0m." .format(choice(p4)))
            deztiro = 0
            pit += 1
        else:
            print("Você recebeu o personagem {}." .format(choice(p3)))
            pit += 1
            deztiro += 1