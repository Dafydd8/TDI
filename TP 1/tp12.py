import binario_balanceado


continuar: bool = True
print("Funciones disponibles \n------------------------------")
print("A. Desarrollo binario [n] \nB. Es binario balanceado \nC. Cantidad binarios balanceados entre [n,m]\nD. Siguiente binario balanceado [n]\nE. Anterior binario balanceado [n]\nF. Binario balanceado mas cercano [n]\nG. Finalizar")
    
accion: str = input("Por favor elija una funcion: ")
if(accion.upper() == "G"):
    continuar = False
    
while(continuar):
    if accion.upper() == "A":
        num: int = int(input("Por favor introduzca un numero: "))
        res: str = binario_balanceado.decimal_a_binario(num)
        print("El numero " + str(num) + " en binario es: " + res)
        print("Presione enter para continuar")
        input()
        accion = input("Por favor elija una funcion: ")

    elif(accion.upper() == "B"):
        num: int = int(input("Por favor introduzca un numero: "))
        res : bool = binario_balanceado.es_binario_balanceado(num)
        if res:
            print("El numero " + str(num) + " es binario balanceado")
        else:
            print("El numero " + str(num) + " no es binario balanceado") 
        print("Presione enter para continuar")
        input()
        accion = input("Por favor elija una funcion: ")

    elif(accion.upper() == "C"):
        num1: int = int(input("Por favor introduzca el primer numero: "))
        num2: int = int(input("Por favor introduzca el segundo numero: "))
        res: int = binario_balanceado.cantidad_binarios_balanceados_entre(num1, num2)
        print("Hay " + str(res) + " binarios balanceados entre " + str(num1) + " y " + str(num2))
        print("Presione enter para continuar")
        input()
        accion = input("Por favor elija una funcion: ")

    elif(accion.upper() == "D"):
        num: int = int(input("Por favor introduzca un numero: "))
        res: int = binario_balanceado.siguiente_binario_balanceado(num)
        print("El siguiente binario balanceado de " + str(num) + " es " + str(res))
        print("Presione enter para continuar")
        input()
        accion = input("Por favor elija una funcion: ")

    elif(accion.upper() == "E"):
        num: int = int(input("Por favor introduzca un numero: "))
        res: int = binario_balanceado.anterior_binario_balanceado(num)
        print("El anterior binario balanceado de " + str(num) + " es " + str(res))
        print("Presione enter para continuar")
        input()
        accion = input("Por favor elija una funcion: ")

    elif(accion.upper() == "F"):
        num: int = int(input("Por favor introduzca un numero: "))
        res: int = binario_balanceado.binario_balanceado_mas_cercano(num)
        print("El binario balanceado mas cercano a " + str(num) + " es " + str(res))
        print("Presione enter para continuar")
        input()
        accion = input("Por favor elija una funcion: ")

    elif(accion.upper() == "G"):
        continuar = False
    
    else:
        print("Entrada inválida")
        print("Presione enter para continuar")
        input()
        accion = input("Por favor elija una funcion: ")