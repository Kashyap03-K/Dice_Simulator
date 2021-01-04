import random
while 1:
    a=input('''Press 1 to roll the dice.
                   Press any key to exit the simulator''')
    if a=='':
        print(random.randint(1,6))
    else:
        break

