import random
import math
import os 
def clearConsole():
    command = 'clear'
    if os.name in ['nt','dos']: command = 'cls'
    os.system(command)
def __init__():
    clearConsole()
    def user_input():
        user_input0=int(input("Enter-Player1: "))
        user_input1=int(input("Enter-Player2: "))
        return user_input0, user_input1

    a,b =  user_input() 

    def random0(): 
        rand=random.randint(1,100)
        return rand

    x = random0()

    def play0():
        if math.dist((a,), (x,)) < math.dist((b,), (x,)):
            print("Player One wins!")
        elif math.dist((a,), (x,)) > math.dist((b,), (x,)):
            print("Player Two wins!")
        else:
            print("DRAW!")
        print('Computer = ', x)
        # print(a)
        # print(b)
    play0()
    go_next = (input("Enter-'True'or'False'")) 

    if go_next == 'True' or 'true':
        play0()
        __init__()
        clearConsole()
    elif go_next == 'False' or 'false':
        print("Goodbye!")
        __init__()
__init__()