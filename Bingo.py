import random

print("|_|_|_|_|_|")
print("|_|_|_|_|_|")
print("|_|_|_|_|_|")
print("|_|_|_|_|_|")
print("|_|_|_|_|_|")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
lx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


def grid():
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    lt = [l1, l2, l3, l4, l5]
    for i in range(25):
        b = random.choice(l)
        new = l.index(b)
        l.pop(new)
        r_lst = random.choice(lt)
        while True:
            if len(r_lst) < 5:
                r_lst.append(b)
                break
            elif len(l1) == len(l2) == len(l3) == len(l4) == len(l5) == 5:
                break
            else:
                r_lst = random.choice(lt)
    return l1, l2, l3, l4, l5


def bingo_play():
    v = 0
    a = list(grid())
    while True:
        # print(a)
        if v % 2 == 0:

            ui = int(input("enter your number"))
            v += 1
            ch = input("if u win then type BINGO STOP")
            if ch.upper() == "BINGO STOP":
                print("You win")
                break
            for i in a:
                if ui in i:
                    k = i.index(ui)
                    j = a.index(i)
                    a[j][k] = "*"
                    # print(a)
                    break
            bingo = ["B", "I", "N", "G", "O"]
            if a[0] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[1] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[2] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[3] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[4] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[0][0] == a[1][1] == a[2][2] == a[3][3] == a[4][4] == "*":
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[0][4] == a[1][3] == a[2][2] == a[3][1] == a[4][0] == "*":
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break

            for i in range(5):
                if a[0][i] == a[1][i] == a[2][i] == a[3][i] == a[4][i] == "*":
                    bingo.pop()
                    if bingo == []:
                        print("computer wins")
                        break
                break

        else:
            ci = random.choice(lx)
            print("computer chose ==> ", ci)

            new2 = lx.index(ci)
            lx.pop(new2)
            # print(lx)
            # print(l1)
            v += 1

            for i in a:
                if ci in i:
                    k = i.index(ci)
                    j = a.index(i)
                    a[j][k] = "*"
                    # print(a)
                    break

            bingo = ["B", "I", "N", "G", "O"]
            if a[0] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[1] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[2] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[3] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[4] == ['*', '*', '*', '*', '*']:
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[0][0] == a[1][1] == a[2][2] == a[3][3] == a[4][4] == "*":
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break
            elif a[0][4] == a[1][3] == a[2][2] == a[3][1] == a[4][0] == "*":
                bingo.pop()
                if bingo == []:
                    print("computer wins")
                    break

            for i in range(5):
                if a[0][i] == a[1][i] == a[2][i] == a[3][i] == a[4][i] == "*":
                    bingo.pop()
                    if bingo == []:
                        print("computer wins")
                        break
                break


bingo_play()
