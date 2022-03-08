# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля).
import random
def randomizing():
    global komp_number
    komp_number = random.randint(0, 9)
    return komp_number

komp_number_all = []

for _ in range(4):
    while randomizing() in komp_number_all:
        randomizing()
    komp_number_all.append(komp_number)