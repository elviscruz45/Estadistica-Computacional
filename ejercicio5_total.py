#--------------------------BORRACHO--------------------------------------------------------------------
import random
from bokeh.plotting import figure,show

class Borracho:
    def __init__(self,nombre):
        self.nombre=nombre

class BorrachoTradicional(Borracho):
    def __init__(self,nombre):
        super().__init__(nombre)
        
    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])
    
borracho=BorrachoTradicional("David")
    
#-------------------------------CAMPO-------------------------------------------------------------------

class Campo:
    def __init__(self):
        self.coordenada_de_borracho={}
    
    def anadir_borracho(self,borracho,coordenada):
        self.coordenada_de_borracho[borracho]=coordenada
    
    def mover_borracho(self,borracho):
        delta_x,delta_y=borracho.camina()
        coordenada_actual=self.coordenada_de_borracho[borracho]
        nueva_coordenada=coordenada_actual.mover(delta_x,delta_y)
        self.coordenada_de_borracho[borracho]=nueva_coordenada
        
    def obtener_coordenada(self,borracho):
        return self.coordenada_de_borracho[borracho]
            
        
#-------------------------------COORDENADA--------------------------------------------------------------

class Coordenada:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def mover(self,delta_x,delta_y):
        return Coordenada(self.x+delta_x,self.y+delta_y)
    
    def distancia(self,otra_coordenada):
        delta_x=self.x-otra_coordenada.x
        delta_y=self.y-otra_coordenada.y
        return (delta_x**2+delta_y**2)**0.5



#-------------------------------ALEATORIO----------------------------------------------------------------

def caminata(campo,borracho,pasos):
    inicio=campo.obtener_coordenada(borracho)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos,numero_de_intentos,tipo_de_borracho):
    borracho=tipo_de_borracho("David")
    origen=Coordenada(0,0)
    campo=Campo()
    distancias=[]
    
    for _ in range(numero_de_intentos):
        campo.anadir_borracho(borracho,origen)
        simular_caminata=caminata(campo,borracho,pasos)
        distancias.append(round(simular_caminata,1))
    return distancias
        
#-------------------------------GRAFICA------------------------------------------------------------------

def graficar(x,y):
    grafica=figure(title="caminon aleatorio",x_axis_label="pasos",y_axis_label="distancia recorrida")
    grafica.line(x,y,legend="distancia media")
    show(grafica)
    
#-------------------------------ALEATORIO----------------------------------------------------------------
    
def main(distancia_de_caminata,numero_de_intentos,tipo_de_borracho):
    distancias_media_por_caminata=[]
    for pasos in distancia_de_caminata:
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
        
    



if __name__== "__main__":
    distancias_de_caminata=[10,100,1000,10000]
    numero_de_intentos=100
    main(distancias_de_caminata,numero_de_intentos,BorrachoTradicional)
