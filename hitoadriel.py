totalapagar=0
class Cliente():
    @staticmethod #es un decorador para no tener que dar argumentos en las estancias
    def registrar():
        while True:
            inicio=input('Bienvenido, registrese o haz login: ')                
            if inicio=='registrarse':
                correo=input('Introduzca su correo: ')
                nombre=input('Introduzca su nombre: ')
                contrasena=input('Introduzca una contraseña: ')
                numero=input('Introduzca número de telefono: ')
                print('Te has registrado correctamente')
                break
            elif inicio=='login':
                nombre=input('Introduzca su nombre ')
                contraseña=input('Escribe su contraseña')
                print('Inicio sesion')
                break
            else:
                print('Error de sintaxis')
                
class Pedidos(Cliente):
    @staticmethod
    def tienda():
        print('Tenemos 3 productos a la venta' )
        print('calzoncillos=10€(sin contar el iva)')
        print('calcetines=5€(sin contar el iva)')
        print('camiseta=15€(sin contar el iva)')
        print('Compra lo que mas te guste y para tener el recibo escribe: pedido')
        pedido=0
        while True:
            pedidos=input('Elija los productos que desea comprar:')
            if pedidos=='calzoncillos':
                precio=3
                pedido=pedido+1
                totalapagar=totalapagar+precio    
                print('ha comprado calzoncillos')
            elif pedidos=='calcetines':
                precio=2
                totalapagar=totalapagar+precio
                pedido=pedido+1
                print('ha comprado calcetines')
            elif pedidos=='camiseta':
                precio=8
                totalapagar=totalapagar+precio
                pedido=pedido+1
                print('ha comprado camiseta')
            elif pedidos=='pedido':
                break
            else:
                print('No ha seleccionado objeto')
        print(f'Has realizado un total de {pedido} pedidos')
    def imprimirfactura():
        pais=(input('¿Eres de España?: '))
        if pais== 'si':
            factura=totalapagar+8
            print(f'Su factura total es de {factura}')
        else:
            factura=totalapagar+15
            print(f'Su factura total es de {factura}')
        print('Su factura le llegará a su número de teléfono y correo.')

cliente1=Cliente()
cliente1.registrar()
pedidos1=Pedidos()
pedidos1.tienda()
pedidos1.imprimirfactura()