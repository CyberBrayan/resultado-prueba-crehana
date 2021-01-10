import time

from concurrent.futures import ThreadPoolExecutor

class Concurrence:
    def __init__(self):
        self.semaphore = False

    def get_result(self,x,y):
        i = 1

        while ((i<len(x)) and (not self.semaphore)):
            if((x[0] + x[i]) == y):
                self.semaphore = True
                print("\n================Éxito================\n")
                
                print("Primer número: %s, Segundo número: %s" % (x[0],x[i]))
            else:
                i = i + 1
    
    def valid_number(self,a):
        try:
            return int(a)
        except:
            return "s"

if __name__ == "__main__":
    value = Concurrence()
    print("==============================Array de solo números==============================\n")
    x = []
    y = 0

    encontrado = False
    print("Ingrese los números que formarán parte de nuestro Array - Para finalizar ingrese un carácter diferente a un número\n")
    while not encontrado:
        a = input()
        
        if (type(value.valid_number(a)).__name__) != 'int':
            encontrado = True
        else:
            x.append(int(a))

    if len(x) != 0:
        encontrado = False
        print("Ingrese la suma a calcular - La operación no se detendra hasta que ingrese un valor numérico:\n")
        while not encontrado:
            y = input()
            
            if (type(value.valid_number(y)).__name__) == 'int':
                encontrado = True
        
        if len(x) <= 61:
            executor = ThreadPoolExecutor(max_workers=len(x) - 1)
        else:
            executor = ThreadPoolExecutor(max_workers=61)
            
        for i in range(len(x) - 1):
            executor.submit(value.get_result,x[i:len(x)],int(y))
    else:
        print("No se ha definido ningún elemento para el array")

input("\nPress the <ENTER> key to continue...")