def feladat1(a):
    i: int= 1
    while (i <= a):
        if i % 3 == 0:
            print(i, end=", ")
        i += 1


def feladat2(a):
    i: int= a
    while (1 <= i):
        if i== 1:
            print(i)
        else:
            print(i, end="; ")
        i -= 1


def feladat3(a):
    while a % 5 != 0:
        print("Ajon meg egy 5-el osztható számot: ")
        return
    else:
        print(f"{a} öttel osztható!")


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