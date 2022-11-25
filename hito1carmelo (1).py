compra = []
print("|===================|")
print(" - TIENDA DE ADRIEL -")
print("|===================|")
print()

while True:
    print("1. Escoja el producto que quiera comprar.")
    print("2. Eliminar producto.")
    print("3. Mostrar la lista de la compra.")
    print("4. Pagar la lista de la compra.")
    print("5. Salir del programa.")
    print()
    opcion = input("--> ")
    print()
    if opcion == "1":
        producto = input("Introduce el producto: ").capitalize()
        if producto in compra:
            print("Ese producto ya esta en la lista")
        else:
            compra.append(producto)
    elif opcion == "2":
        producto = input("Introduce el producto: ").capitalize()
        if producto not in compra:
            print("Ese producto no esta en la lista.")
        else:
            compra.remove(producto)
    elif opcion == "3":
        print("Lista de la compra:")
        for e in compra:
            print(" -", e)
    elif opcion == "4":
        cliente = input("Introduce tus datos personales: ").capitalize()

        def mostrar_menu(opciones):
            print('Seleccione una opción:')
            for clave in sorted(opciones):
                print(f' {clave}) {opciones[clave][0]}')


        def leer_opcion(opciones):
            while (a := input('Opción: ')) not in opciones:
                print('Opción incorrecta, vuelva a intentarlo.')
            return a


        def ejecutar_opcion(opcion, opciones):
            opciones[opcion][1]()


        def generar_menu(opciones, opcion_salida):
            opcion = None
            while opcion != opcion_salida:
                mostrar_menu(opciones)
                opcion = leer_opcion(opciones)
                ejecutar_opcion(opcion, opciones)
                print()


        def menu_principal():
            opciones = {
                '1': ('Dime tu DNI', accion1),
                '2': ('Dime tu ciudad', accion2),
                '3': ('Dime tu telefono', accion3),
                '4': ('Dime tu email', accion4),
                '5': ('Realizar compra', accion5),
                '6': ('Salir', salir)
            }

            generar_menu(opciones, '6')

        def accion1():
            print('Has elegido la opción 1')
            nombre=input('Escribe tu DNI')


        def accion2():
            print('Has elegido la opción 2')
            ciudad=input('Dime tu ciudad')


        def accion3():
            print('Has elegido la opción 3')
            tlf=int(input('Dime tu telefono'))
            print(tlf)

        def accion4():
            print('Has elegido la opción 4')
            email=input('Dime tu correo electronico')
            print(email)

        def accion5():
            print('Pedido completado')
            print(f"Factura enviada al email {email} enviada correctamente")
            print(f"Numero de seguimiento enviado al {tlf} enviado correctamente")


        def salir():
            print('Saliendo')


        if __name__ == '__main__':
            menu_principal()

    elif opcion == "5":
        break
    else:
        print("Introduce una opcion correcta.")
    print()