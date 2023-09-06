# Meny program

run_program = True
while run_program:
    print('Menu')

    c = input('Choice')
    if c == 'j':
        pass
    elif c == 'n':
        pass 
    else:
        print('Wrong choice')
        continue
    while True:
        x = input('You want to continue?(y/n)')
        if x == 'y':
            break
        elif x == 'n':
            run_program = False
            break
        else:
            print('Try better!!')

    

