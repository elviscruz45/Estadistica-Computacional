import sys

def fibonacci(n):
    save={}
    if n==0 or n==1:
        save[n]=1
        
    try:
        return save[n]
    except KeyError:
        resultado=fibonacci(n-1)+fibonacci(n-2)
        save[n]=resultado
        return resultado
    



if __name__=="__main__":
    sys.setrecursionlimit(10002)
    resultado=fibonacci(10)
    print(resultado)