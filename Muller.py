import cmath


def muller(x):
    # Ecuación original: 3x^5 - 7x^4 + 8x^3 - 30
    return 3 * pow(x, 5) - 7 * pow(x, 4) + 8 * pow(x, 3) - 30


def metodo(p0, p1, p2, numeroMaxIt, tolerancia=1e-6):
    # Validación inicial de iteraciones
    if numeroMaxIt <= 0:
        print("El número de iteraciones no puede ser menor o igual a cero.")
        return False

    print(f"{'Iteración':<10}{'Aproximación p3':<35}{'Error Absoluto':<20}")
    print("-" * 65)

    i = 1
    while i <= numeroMaxIt:
        # Evaluamos la función en los tres puntos actuales
        f0 = muller(p0)
        f1 = muller(p1)
        f2 = muller(p2)

        # Diferencias fundamentales del método de Müller
        h1 = p1 - p0
        h2 = p2 - p1
        delta1 = (f1 - f0) / h1
        delta2 = (f2 - f1) / h2

        # Cálculo de los coeficientes a, b y c de la parábola aproximada
        a = (delta2 - delta1) / (h2 + h1)
        b = a * h2 + delta2
        c = f2

        # Cálculo del discriminante usando cmath para soportar números complejos
        discriminante = cmath.sqrt(b**2 - 4 * a * c)

        # Creamos los dos denominadores posibles
        denom1 = b + discriminante
        denom2 = b - discriminante

        # Elegimos el denominador con mayor valor absoluto (magnitud)
        aprox = denom1 if abs(denom1) > abs(denom2) else denom2

        # Si el denominador es cero, el método no puede continuar
        if aprox == 0:
            print("Error: Denominador cero. No se puede continuar.")
            return False

        # Calculamos la nueva aproximación p3
        p3 = p2 - (2 * c / aprox)

        # Calculamos el error estimado (distancia entre la nueva aproximación y la anterior)
        errorActual = abs(p3 - p2)

        # Mostramos los resultados de la iteración actual limpios
        # Si la parte imaginaria es extremadamente pequeña, la mostramos simplificada
        p3_print = p3 if abs(p3.imag) > 1e-9 else p3.real
        print(f"{i:<10}{str(p3_print):<35}{errorActual:<20.2e}")

        # Criterio de parada: Si el error es menor que la tolerancia, terminamos con éxito
        if errorActual < tolerancia:
            print("-" * 65)
            print(f"¡Raíz encontrada con éxito en la iteración {i}!")
            print(f"Resultado final: {p3_print}")
            return True

        # Actualización de puntos para la siguiente iteración
        p0 = p1
        p1 = p2
        p2 = p3
        i += 1

    print("-" * 65)
    print("Se alcanzó el número máximo de iteraciones sin converger completamente.")
    return False


# Ejecución del método con tus puntos iniciales: p0=1, p1=2, p2=3
metodo(1, 2, 3, 100)
