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
        opcion_main = input('Ingrese opción: ')

        if opcion_main == '1':
            print()
        elif opcion_main == '2':
            print()
        elif opcion_main == '4':
            salir_submenu = True
        else:
            print('Opción inválida.')

def main_menu():
    salir_main = False
    while not salir_main:
        print('''
              --- SUBMENU ---
              1.
              2.
              3.
              4.
              ''')
        opcion_main = input('Ingrese una opcion: ')
        
        if opcion_main == '1':
            print()
        elif opcion_main == '2':
            print()
        elif opcion_main == '4':
            salir_main = True
        else:
            print('Opción inválida.')

# Hace de punto de partida, señalando que inicie desde la funcion indentada
if __name__ == '__main__':
    main_menu()