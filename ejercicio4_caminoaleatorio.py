from ejercicio1_borracho import BorrachoTradicional
from ejercicio2_coordenada import Coordenada
from ejercicio3_campo import Campo

from bokeh.plotting import figure, show



def caminata(campo,borracho,pasos):
    inicio=campo.obtener_coordenada(borracho)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))



def simular_caminata(pasos,numero_de_intentos,tipo_de_borracho):
    
    borracho=tipo_de_borracho(nombre="David")
    
    origen=Coordenada(0,0)
    campo=Campo()

    distancias=[]


    for _ in range(numero_de_intentos):

        campo.anadir_borracho(borracho,origen)
        simular_caminata=caminata(campo,borracho,pasos)
        distancias.append(round(simular_caminata,1))
        
    return distancias

def graficar(x,y):
    grafica=figure(title="camino aleatorio", x_axis_label="pasos",y_axis_label="distancia recorrida")
    grafica.line(x,y, legend="distancia media")
    
    show(grafica)


def main(distancias_de_caminata,numero_de_intentos,tipo_de_borracho): #(2)
    distancias_media_por_caminata=[]
    for pasos in distancias_de_caminata:
        
        distancias=simular_caminata(pasos,numero_de_intentos,tipo_de_borracho)


        distancia_media=round(sum(distancias)/len(distancias),3)
        distancia_maxima=max(distancias)
        distancia_minima=min(distancias)
        
        distancias_media_por_caminata.append(distancia_media)
        print(f"{tipo_de_borracho.__name__} caminata aleatoria de  {pasos} pasos")
        print(f"Media={distancia_media}")
        print(f"Max= {distancia_maxima}")
        print(f"Min= {distancia_minima}")
        
    graficar(distancias_de_caminata,distancias_media_por_caminata)

if __name__=="__main__":
    distancias_de_caminata=[10,100,1000,10000]
    numero_de_intentos=100
    main(distancias_de_caminata,numero_de_intentos,BorrachoTradicional) #(1)