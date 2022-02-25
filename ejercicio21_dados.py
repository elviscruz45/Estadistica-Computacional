import random
import collections
from bokeh.plotting import figure,show
from bokeh.layouts import row

def population(number_of_throw):
    throws =[]
    throws_sample=[]
    sample_mean =[] #media de todas las muestas 
    for _ in range(number_of_throw):
        dice = random.choice([1,2,3,4,5,6])
        throws.append(dice)
        throws_sample.append(dice)
        if( _ %100==0): #promediamos la muestra de los 10 lanzamientos
            sample = sum(throws_sample)/len(throws_sample)
            sample_mean.append(sample)
            throws_sample=[] 

    throws=sorted(throws)
    sample_mean=sorted(sample_mean)
    sample_mean=dict(collections.Counter(sample_mean))
    throws=dict(collections.Counter(throws))
    return (throws, sample_mean)

def graph(values,title):
    
    number_of_dice=list(values.keys())
    values_of_throws=list(values.values())
    p = figure(title=title, x_axis_label='Number of Dice', y_axis_label='Quantity')
    p.vbar(x=number_of_dice,top=values_of_throws,width=0.5, color="#CAB2D6")
    return p

def main():
    quantity=int(input("Cantidad de lanzamientos: "))
    values_throws,values_sample = population(quantity) #tengo x lanzamientos de dados que me da una un gráfico uniforme
    # gráfico uniforme por que cada número del dado tiene la misma posibilidad de salir (1/6)
    show(row(graph(values_throws,"Dice Throws"),graph(values_sample,"Media Sample")))


if __name__ == "__main__":
    main()
