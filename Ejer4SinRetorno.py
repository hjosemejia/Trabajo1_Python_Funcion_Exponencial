import math #importamos la libreria math para la funcion pow

def funcion_serie(num1):
    sum = 1 + num1
    y = 2
    
    for i in range(1, 50): 
        fct = 1
        for j in range(1,y+1): 
            fct = fct * j          
        m = math.pow(num1, y) / fct 
        sum = sum + m 
        y += 1
    
    print(f"EL VALOR DE LA FUNCION ESPONECIAL CON X = {num1} Y CON N = 50 ")
    print(f"e^X = {sum}")
 

def main():
    num1 = int(input("DIGITE UN NUMERO: "))
    funcion_serie(num1)

if __name__ == "__main__":
    main()
