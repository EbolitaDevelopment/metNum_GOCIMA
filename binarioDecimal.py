def bin_a_notacion_cientifica(binario_str):
    pos_punto = binario_str.index('.')
    pos_primer_uno = binario_str.index('1')
    exponente = pos_punto - pos_primer_uno - 1
    digitos = binario_str.replace('.', '').lstrip('0')
    
    if len(digitos) > 1:
        resultado = f"{digitos[0]}.{digitos[1:]} * 2^{exponente}"
    else:
        resultado = f"{digitos[0]} * 2^{exponente}"
        
    return exponente, digitos[1:] if len(digitos) > 1 else digitos[0] 

def binario_decimal(binario):
    matriza = 0
    exponente = 0
    decimal = 0
    j = 0
    sign = 0
    for i,bit in enumerate(reversed(binario)):
        if bit == '1' and i < quantMatriza:
            matriza += 2 ** -(quantMatriza - i)
            
        elif bit == '1' and quantMatriza <= i < quantBits:
            exponente += 2 ** (i - quantMatriza)
            
        elif bit == '1' and i <= quantBits:
            sign = 1
    decimal = (-1) ** sign * 2 ** (exponente - expNeg)*(1 + matriza)
    return decimal

def decimal_binario(decimal):
    sign = '1' if decimal < 0 else '0'
    decimal = abs(decimal)

    parInt = int(decimal)
    parFrac = decimal-parInt
    bin_entera = bin(parInt)[2:] if parInt > 0 else '0'
    
    bin_frac = ""
    for _ in range(quantBits * 2):
        parFrac *= 2
        if parFrac >= 1:
            bin_frac += '1'
            parFrac -= 1
        else:
            bin_frac += '0'
    
    binario_completo = f"{bin_entera}.{bin_frac}"

    exponente_real, mantisa = bin_a_notacion_cientifica(binario_completo)

    mantisa_truncada = mantisa[:quantMatriza] 

    exponente_con_sesgo = exponente_real + expNeg

    if exponente_con_sesgo >= (2 ** quantExp) or exponente_con_sesgo < 0:
        raise ValueError("El número es demasiado grande o chico para este formato de bits.")

    bin_exponente = bin(exponente_con_sesgo)[2:].zfill(quantExp)
    return f"{sign}{bin_exponente}{mantisa_truncada}"


def main():
    print("*****************************************************")
    print("PROGRAMA DE CONVERSIÓN BINARIO-DECIMAL REGLA IEEE 754")
    global quantMatriza, quantExp, expNeg, quantBits
    quantBits = int(input("\nElige con cuantos bits deseas trabajar: 16, 32 o 64:    "))
    if quantBits == 16:
        quantMatriza = 10
        quantExp = 5
    elif quantBits == 32:
        quantMatriza = 23
        quantExp = 8
    elif quantBits == 64:
        quantMatriza = 52
        quantExp = 11
    else:
        print("Opción no válida. Se usará 16 bits por defecto.")
        quantMatriza = 23
        quantExp = 8
    expNeg = (2 ** (quantExp - 1)) - 1


    while True:
        print("\nSeleccione una opción:")
        print("1. Convertir binario a decimal")
        print("2. Convertir decimal a binario")
        print("3. Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            binario = input("Ingrese un número binario (ejemplo: 110101): ")
            try:
                decimal = binario_decimal(binario)
                print(f"El número decimal es: {decimal}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == '2':
            decimal = float(input("Ingrese un número decimal: "))
            try:
                binario = decimal_binario(decimal)
                print(f"El número binario es: {binario}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
main()