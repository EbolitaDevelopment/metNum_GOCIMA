def func(x):
    r = -3*x**2-8*x+6
    return r
def derivada(x):
    r = -6*x -8
    return r

def metodoNewtonRaphson(x0,maxIt):
    i = 0
    errActual = 0.0
    print(f"{'Iteraciones' :<14}  {'Aproximación a Raiz':^20}  {'Error':^20}")
    while (i<maxIt):
        aproxRaiz = x0 - (func(x0)/derivada(x0))
        errActual = abs(x0 - aproxRaiz)
        print(f"{i:<14}  {aproxRaiz:^20}  {errActual:^20}")
        x0 = aproxRaiz
        if errActual < 1e-20 : break
        i+=1
    return x0
metodoNewtonRaphson(1,25)