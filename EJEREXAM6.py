def ejercicio6():
    print ()
    print ('JUGADORES (GAMERS)')
    print ('____________')

    for x in range (8):

        jugador = input ('ingrese el nombre del jugador: ')
        edad = int (input ('ingrese la edad del jugador: '))

        Novato = 'Novato'
        Experto = 'Experto'
        Super_Experto = 'Super_Experto'

        if edad < 14:
            print ('INGRESO UNA EDAD NO VALIDA')
            return ()

        elif edad >= 14 and edad <= 16:
            print ([jugador], [edad], [Novato])


        elif edad > 16 and edad <= 20:
            print ([jugador], [edad], [Experto])

        elif edad > 20:
            print ([jugador], [edad], [Super_Experto])


ejercicio6 ()