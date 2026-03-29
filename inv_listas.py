def submenu_opciones():
    salir_submenu = False
    while not salir_submenu:
        print('''
              --- SUBMENU ---
              1.
              2.
              3.
              4.
              ''')
        opcion_sub = input('Ingrese opción: ')

        if opcion_sub == '1':
            print()
        elif opcion_sub == '2':
            print()
        elif opcion_sub == '4':
            salir_submenu = True
        else:
            print('\nOpción inválida, intente nuevamente.')

def main_menu():
    salir_main = False
    while not salir_main:
        print('''
              --- MAIN MENU ---
              1.
              2.
              3.
              4.
              ''')
        opcion_main = input('Ingrese una opcion: ')
        
        if opcion_main == '1':
            submenu_opciones()
        elif opcion_main == '2':
            print()
        elif opcion_main == '4':
            salir_main = True
        else:
            print('\nOpción inválida, intente nuevamente.')

# Hace de punto de partida, señalando que inicie desde la funcion deseada
if __name__ == '__main__':
    main_menu()
