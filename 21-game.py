#Trying out my first proper github program
def MyFirstGame(num):
    if num >= 4:
        close = num + (4 - (num % 4))
    else:
        close = 4
    return close

def lose1():
    print ("\n\nYou lost the game!")
    print("Maybe next time!")
    exit(0)

def check(abc):
    i = 1
    while i < len(abc):
        if (abc[i] - abc[i - 1]) != 1:
            return False
        i = i + 1
    return True

def start1():
    abc = []
    last = 0
    while True:
        print ("Enter 'f' to take the first chance.")
        print("Enter 's' to take the second chance.")
        chance = input('> ')

        if chance == "f":
            while True:
                if last == 20:
                    lose1()
                else:
                    print ("\nYour Turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    inp = int(input('> '))

                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print ("Wrong input. You are disqualified from the game.")
                        lose1()

                    i, j = 1, 1

                    print ("Now enter the values")
                    while i <= inp:
                        a = input('> ')
                        a = int(a)
                        abc.append(a)
                        i = i + 1

                    # store the last element of xyz.
                    last = abc[-1]

                    # checks whether the input
                    # numbers are consecutive
                    if check(abc) == True:
                        if last == 21:
                            lose1()

                        else:
                            # "Computer's turn."
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print ("Order of inputs after computer's turn is: ")
                            print (abc)
                            last = abc[-1]
                    else:
                        print ("\nYou did not input consecutive integers.")
                        lose1()

        elif chance == "s":
            comp = 1
            last = 0
            while last < 20:

                j = 1
                while j <= comp:
                    abc.append(last + j)
                    j = j + 1
                print ("Order of inputs after computer's turn is:")
                print (abc)
                if abc[-1] == 20:
                    lose1()

                else:
                    print ("\nYour turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    inp = input('> ')
                    inp = int(inp)
                    i = 1
                    print ("Enter your values")
                    while i <= inp:
                        abc.append(int(input('> ')))
                        i = i + 1
                    last = abc[-1]
                    if check(abc) == True:

                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:

                        print ("\nYou did not input consecutive integers.")
                        lose1()
            print ("\n\nCONGRATULATIONS !!!")
            print ("YOU WON !")
            exit(0)

        else:
            print ("wrong choice")


game = True
while game == True:
    print ("Player 2 is a computer.")
    print("Do you want to play the 21 number game? (yes / no)")
    ans = input('> ')
    if ans == 'yes':
        start1()
    else:
        print ("Do you want quit the game?(yes / no)")
        aaa = input('> ')
        if aaa == "yes":
            print ("You are quitting the game...")
            exit(0)
        elif aaa == "no":
            print ("The game is going to continue")
        else:
            print ("Bad choice")
