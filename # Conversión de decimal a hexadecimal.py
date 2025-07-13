# Conversión de decimal a hexadecimal

# Solicitar un número decimal al usuario
decimal = int(input("Introduce un número decimal: "))

# Convertir a hexadecimal usando la función hex()
hexadecimal = hex(decimal)

print("El número hexadecimal es:", hexadecimal[2:].upper())
