def convertir_entre_bases(numero, base_origen, base_destino):
    decimal = int(numero, base_origen)

    if base_destino == 2:
        convertido = bin(decimal)[2:]
    elif base_destino == 8:
        convertido = oct(decimal)[2:]
    elif base_destino == 16:
        convertido = hex(decimal)[2:].upper()
    elif base_destino == 10:
        convertido = str(decimal)
    else:
        convertido = ""
        while decimal > 0:
            resto = decimal % base_destino
            if resto < 10:
                convertido = str(resto) + convertido
            else:
                convertido = chr(ord('A') + resto - 10) + convertido
            decimal //= base_destino

    print(f"{numero} en base {base_origen} = {convertido} en base {base_destino}")


# Conversión directa: del 32 en base 8 (octal) a base 2 (binario)
convertir_entre_bases("32", 8, 2)
