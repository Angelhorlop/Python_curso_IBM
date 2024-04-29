#Dados dos números, escriba un código Python para encontrar el mínimo de estos dos números
a = int(input("Escribe un numero entero :"))
b = int(input("Escribe el segundo numero entero:"))
def minimo (a,b):
    if a < b :
        return (a)
    else :
        return (b)
print(minimo(a,b))

