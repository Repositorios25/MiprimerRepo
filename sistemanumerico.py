def convertir_entre_bases(numero, base_origen, base_destino):
    decimal = int(numero, base_origen) 
    if base_destino == 2:
        convertido = bin(decimal)[2:]  
    elif base_destino == 8: 
        convertido = oct(decimal)[2:]
    elif base_destino == 10:
        convertido = str(decimal)
    elif base_destino == 16:
        convertido = hex(decimal)[2:].upper()
    else:
        raise ValueError("Base de destino no soportada. Usa 2, 8, 10 o 16.")
    return convertido
def menu_completo():
    print("Conversor de Bases Numéricas")
    print("1. Binario a Decimal")
    print("2. Decimal a Binario")
    print("3. Octal a Decimal")
    print("4. Octal a Binario")
    print("5. Decimal a Octal")
    print("6. Hexadecimal a Decimal")
    print("7. Decimal a Hexadecimal")
    print("8. Salir")
    
    while True:
        opcion = input("Selecciona una opción (1-8): ")
        if opcion == '1':
            numero = input("Introduce un número binario: ")
            resultado = convertir_entre_bases(numero, 2, 10)
            print(f"Decimal: {resultado}")
        elif opcion == '2':
            numero = input("Introduce un número decimal: ")
            resultado = convertir_entre_bases(numero, 10, 2)
            print(f"Binario: {resultado}")
        elif opcion == '3':
            numero = input("Introduce un número octal: ")
            resultado = convertir_entre_bases(numero, 8, 10)
            print(f"Decimal: {resultado}")
        elif opcion == '4':
            numero = input("Introduce un número decima octal: ")
            resultado = convertir_entre_bases(numero, 8, 2)
            print(f"Binario: {resultado}")
        elif opcion == '5':
            numero = input("Introduce un número decimal: ")
            resultado = convertir_entre_bases(numero, 10, 8)
            print(f"Octal: {resultado}")
        elif opcion == '6':
            numero = input("Introduce un número hexadecimal: ")
            resultado = convertir_entre_bases(numero, 16, 10)
            print(f"Decimal: {resultado}")
        elif opcion == '7':
            numero = input("Introduce un número decimal: ")
            resultado = convertir_entre_bases(numero, 10, 16)
            print(f"Hexadecimal: {resultado}")
        elif opcion == '8':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
if __name__ == "__main__":
    menu_completo()
