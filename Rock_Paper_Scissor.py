import random
while 1:
    a=input('''Press Enter to play <--- Rock! Paper! and Sciccor! -->
            To 'QUIT' press any key and press enter !''')
    if a=='':
        l=["Rock","Paper","Scissor"]
        a=random.randint(0,2)
        print(l[a])
    else:
        break
