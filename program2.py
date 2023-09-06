
# har_fått_maträtt = False
# while not har_fått_maträtt:
#     pass
while True:
    print('Sebbes kök'.center(24,'-'))
    print('A. Hamburgare')
    print('B. Pasta')
    print('C. Husman')
    print('Q. Avsluta')
    val = input('Gör ett val: ').lower()
    if val == 'a':
        fel_val = True
        while fel_val == True:
            sötpotatis_eller_ej = input(
                'Vill du ha sötpotatis?(j/n) eller välj "ångra" för att gå tillbaka till menyn'
                ).lower()
            if sötpotatis_eller_ej == 'j':
                print('Varsågod! Här en en hamburgare med sötpotatis till!')
                fel_val = False
            elif sötpotatis_eller_ej == 'n':
                print('Varsågod! Här en en hamburgare med pommes till!')
                fel_val = False
            elif sötpotatis_eller_ej == 'ångra':
                break
            else:
                print('Välj rätt din jäkel!')

    elif val == 'b':
        while True:
            print('1. Carbonara\n2. Bolognese')
            pasta_rätt = input('Välj pastarätt: ')
            if pasta_rätt == '1':
                print('Varsågod! Här har du en Carbonara!')
                break
            elif pasta_rätt == '2':
                print('Varsågod! Här har du en Bolognese!')
                break
            else:
                print('Men välj rätt för tusan!')
    elif val == 'c':
        print('Husman finns inte din jäkel!')
        print('Köket stänger!! Hej då!')
        break
    elif val == 'q':
        break
    else:
        print('Fel inmatning på menyval! Testa igen!!!')
    

# menyval1 = 2

# if menyval1 == 1:
#     pass
# elif menyval1 == 2:
#     pass
