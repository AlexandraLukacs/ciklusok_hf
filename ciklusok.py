def feladat1():
    a: int= 9
    i: int= 1
    while (i <= a):
        if i % 3 == 0:
            print(i, end=", ")
        i += 1

def feladat2():
    a: int= 8
    i: int= 1
    while (i <= a):
        print(a, end="; ")
        i -= 1


def feladat3():
    a: int= int(input("Adjon meg egy 5-el osztható számot: "))
    while (a % 5 == 0):
        if a % 5 == 0:
            print(f"A(z) {a} osztható 5-el!")
        else:
            print("A szám, nem osztható 5-el, adjon meg egy 5-el osztható számot!")


def feladat4(a):
    i: int= 1
    while (i <= a):
        if i % 3 == 0 and i % 2 == 0:
            print("BUMMBAM", end=" ")
        elif i % 2 == 0:
            print("BAM", end=", ")
        elif i % 3 == 0:
            print("BUMM", end=", ")
        else:
            print(i, end=", ")
        i += 1