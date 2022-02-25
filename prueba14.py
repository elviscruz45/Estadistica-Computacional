import random

class Borracho:
    def __init__(self,nombre):
        self.nombre=nombre
        
        
class BorrachoTradicional(Borracho):
    def __init__(self,nombre):
        super().__init__(nombre)
        
    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])
    
    


class Campo:
    def __init__(self):
        self.coordenadas_de_borrachos={}
        
    def anadir_borracho(self,borracho,coordenada):
        self.coordenadas_de_borrachos[borracho]=coordenada
        
    def mover_borracho(self,borracho):
        delta_x,delta_y=borracho.camina()
        coordenada_actual=self.coordenadas_de_borrachos[borracho]
        nueva_coordenada=coordenada_actual.mover(delta_x,delta_y)
        
        self.coordenadas_de_borrachos[borracho]=nueva_coordenada
        
    def obtener_coordenada(self,borracho):
        return self.coordenadas_de_borrachos[borracho]
    

class Coordenada:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def mover(self,delta_x,delta_y):
        return Coordenada(self.x+delta_x,self.y+delta_y)
    
    def distancia(self,otra_coordenada):
        delta_x=self.x - otra_coordenada.x
        delta_y=self.y - otra_coordenada.y
        return (delta_x**2+delta_y**2)**0.5

campo=Campo()



campo.anadir_borracho(BorrachoTradicional("David"),Coordenada(0,0))


print(campo.coordenadas_de_borrachos)



