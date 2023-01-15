string = input("enter your name:")
height = 7
width = (2 * height) - 1


def A():
    n = width // 2
    for i in range(0, height):
        for j in range(0, width + 1):
            if j == n or j == (width - n) or (i == (height // 2) and n < j < (width - n)):
                print("*", end="")
            else:
                print(end=" ")
        print()
        n = n - 1


# Function to print the pattern of 'B'
def B():
    half = height // 2

    for j in range(0, height):
        print("*", end="")
        for j in range(0, width):
            if (j == 0 or j == height - 1 or j == half) and j < (width - 2):
                print("*", end="")
            elif j == (width - 2) and not (j == 0 or j == height - 1 or j == half):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'C'
def C():
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height - 1):
            if (i == 0 or i == height - 1):
                print("*", end="")
            else:
                continue
        print()


# Function to print the pattern of 'D'
def D():
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0 or i == height - 1) and j < height - 1):
                print("*", end="")
            elif (j == height - 1 and i != 0 and i != height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'E'
def E():
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0 or i == height - 1) or (i == height // 2 and j <= height // 2)):
                print("*", end="")
            else:
                continue
        print()


# Function to print the pattern of 'F'
def F():
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0) or (i == height // 2 and j <= height // 2)):
                print("*", end="")
            else:
                continue
        print()


# Function to print the pattern of 'G'
def G():
    for i in range(0, height):
        for j in range(0, width - 1):
            if ((i == 0 or i == height - 1) and (j == 0 or j == width - 2)):
                print(end=" ")
            elif (j == 0):
                print("*", end="")
            elif (i == 0 and j <= height):
                print("*", end="")
            elif (i == height // 2 and j > height // 2):
                print("*", end="")
            elif (i > height // 2 and j == width - 2):
                print("*", end="")
            elif (i == height - 1 and j < width - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'H'
def H():
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((j == height - 1) or (i == height // 2)):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'I'
def I():
    for i in range(0, height):
        for j in range(0, height):
            if (i == 0 or i == height - 1):
                print("*", end="")
            elif (j == height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'J'
def J():
    for i in range(0, height):
        for j in range(0, height):
            if (i == height - 1 and (j > 0 and j < height - 1)):
                print("*", end="")
            elif ((j == height - 1 and i != height - 1) or (i > (height // 2) - 1 and j == 0 and i != height - 1)):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'K'
def K():
    half = height // 2
    dummy = half
    for i in range(0, height):
        print("*", end="")
        for j in range(0, half + 1):
            if (j == abs(dummy)):
                print("*", end="")
            else:
                print(end=" ")
        print()
        dummy = dummy - 1


# Function to print the pattern of 'L'
def L():
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height + 1):
            if (i == height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'M'
def M():
    counter = 0
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height + 1):
            if (j == height):
                print("*", end="")
            elif (j == counter or j == height - counter - 1):
                print("*", end="")
            else:
                print(end=" ")
        if (counter == height // 2):
            counter = -99999
        else:
            counter = counter + 1

        print()


# Function to print the pattern of 'N'
def N():
    counter = 0
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height + 1):
            if (j == height):
                print("*", end="")
            elif (j == counter):
                print("*", end="")
            else:
                print(end=" ")
        counter = counter + 1
        print()


# Function to print the pattern of 'O'
def O():
    space = height // 3
    width = height // 2 + height // 5 + space + space
    for i in range(0, height):
        for j in range(0, width + 1):
            if (j == width - abs(space) or j == abs(space)):
                print("*", end="")
            elif ((i == 0 or i == height - 1) and j > abs(space) and j < width - abs(space)):
                print("*", end="")
            else:
                print(end=" ")

        if (space != 0 and i < height // 2):
            space = space - 1
        elif (i >= (height // 2 + height // 5)):
            space -= 1

        print()


# Function to print the pattern of 'P'
def P():
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height):
            if ((i == 0 or i == height // 2) and j < height - 1):
                print("*", end="")
            elif (i < height // 2 and j == height - 1 and i != 0):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'Q'
def Q():
    O()
    d = height
    for i in range(0, height // 2):
        for j in range(0, d + 1):
            if (j == d):
                print("*", end="")
            else:
                print(end=" ")
        print()
        d = d + 1


# Function to print the pattern of 'R'
def R():
    half = (height // 2)
    for i in range(0, height):
        print("*", end="")
        for j in range(0, width):
            if ((i == 0 or i == half) and j < (width - 2)):
                print("*", end="")
            elif (j == (width - 2) and not (i == 0 or i == half)):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'S'
def S():
    for i in range(0, height):
        for j in range(0, height):
            if ((i == 0 or i == height // 2 or i == height - 1)):
                print("*", end="")
            elif (i < height // 2 and j == 0):
                print("*", end="")
            elif (i > height // 2 and j == height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'T'
def T():
    for i in range(0, height):
        for j in range(0, height):
            if (i == 0):
                print("*", end="")
            elif (j == height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'U'
def U():
    for i in range(0, height):
        if (i != 0 and i != height - 1):
            print("*", end="")
        else:
            print(end=" ")
        for j in range(0, height):
            if (((i == height - 1) and j >= 0 and j < height - 1)):
                print("*", end="")
            elif (j == height - 1 and i != 0 and i != height - 1):
                print("*", end="")
            else:
                print(end=" ")
        print()


# Function to print the pattern of 'V'
def V():
    counter = 0
    for i in range(0, height):
        for j in range(0, width + 1):
            if (j == counter or j == width - counter - 1):
                print("*", end="")
            else:
                print(end=" ")

        counter = counter + 1
        print()


# Function to print the pattern of 'W'
def W():
    counter = height // 2
    for i in range(0, height):
        print("*", end="")
        for j in range(0, height + 1):
            if (j == height):
                print("*", end="")
            elif ((i >= height // 2) and (j == counter or j == height - counter - 1)):
                print("*", end="")
            else:
                print(end=" ")
        if (i >= height // 2):
            counter = counter + 1
        print()


# Function to print the pattern of 'X'
def X():
    counter = 0
    for i in range(0, height + 1):
        for j in range(0, height + 1):
            if (j == counter or j == height - counter):
                print("*", end="")
            else:
                print(end=" ")
        counter = counter + 1
        print()


# Function to print the pattern of 'Y'
def Y():
    counter = 0
    for i in range(0, height):
        for j in range(0, height + 1):
            if (j == counter or j == height - counter and i <= height // 2):
                print("*", end="")
            else:
                print(end=" ")
        print()
        if (i < height // 2):
            counter = counter + 1


# Function to print the pattern of 'Z'
def Z():
    counter = height - 1
    for i in range(0, height):
        for j in range(0, height):
            if (i == 0 or i == height - 1 or j == counter):
                print("*", end="")
            else:
                print(end=" ")
        counter = counter - 1
        print()


l = len(string)
for i in range(0, l):
    if (string[i] == "A" or string[i] == "a"):
        A()
    elif (string[i] == "B" or string[i] == "b"):
        B()
    elif (string[i] == "C" or string[i] == "c"):
        C()
    elif (string[i] == "D" or string[i] == "d"):
        D()
    elif (string[i] == "E" or string[i] == "e"):
        E()
    elif (string[i] == "F" or string[i] == "f"):
        F()
    elif (string[i] == "G" or string[i] == "g"):
        G()
    elif (string[i] == "H" or string[i] == "h"):
        H()
    elif (string[i] == "I" or string[i] == "i"):
        I()
    elif (string[i] == "J" or string[i] == "j"):
        J()
    elif (string[i] == "K" or string[i] == "k"):
        K()
    elif (string[i] == "L" or string[i] == "l"):
        L()
    elif (string[i] == "M" or string[i] == "m"):
        M()
    elif (string[i] == "N" or string[i] == "n"):
        N()
    elif (string[i] == "O" or string[i] == "o"):
        O()
    elif (string[i] == "P" or string[i] == "p"):
        P()
    elif (string[i] == "Q" or string[i] == "q"):
        Q()
    elif (string[i] == "R" or string[i] == "r"):
        R()
    elif (string[i] == "S" or string[i] == "s"):
        S()
    elif (string[i] == "T" or string[i] == "t"):
        T()
    elif (string[i] == "U" or string[i] == "u"):
        U()
    elif (string[i] == "V" or string[i] == "v"):
        V()
    elif (string[i] == "W" or string[i] == "w"):
        W()
    elif (string[i] == "X" or string[i] == "x"):
        X()
    elif (string[i] == "Y" or string[i] == "y"):
        Y()
    elif (string[i] == "Z" or string[i] == "z"):
        Z()
    elif string[i] == " ":
        print()
    print()
