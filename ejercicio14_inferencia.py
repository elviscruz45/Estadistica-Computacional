import random
import math
from bokeh.plotting import figure, show

def media(X):
    return sum(X)/len(X)

def varianza(X):
    mu=media(X)
    acumulador=0
    for x in X:
        acumulador +=(x-mu)**2
    return acumulador / len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))

def graficar(x, y):
    figura = figure()
    
    figura.dot(x, y, size=50)

    show(figura)

if __name__=="__main__":
    X=[random.randint(1,21) for i in range(100)]
    count={i:X.count(i) for i in set(X)}
    print(count)
    mu=media(X)
    Var=varianza(X)
    sigma=desviacion_estandar(X)
    x=list(count.keys())
    y=list(count.values())
    
    print(f"Arreglo X: {X}")
    print(f"Media X: {mu}")
    print(f"Varianza X: {Var}")
    print(f"Desviacion Estandar X: {sigma}")
    graficar(x, y)
    print(x)
    print(y)

