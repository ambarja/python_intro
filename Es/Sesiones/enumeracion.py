# Determinar si un número aletorio tiene una raíz cuadrada 

objetivo   =  int(input('Escoge un número: '))  
respuesta =  0

while respuesta**2 < objetivo : 
    respuesta += 1

if respuesta**2 == objetivo : 
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else :
    print(f'El {objetivo} no tiene una raiz cuadrada exacta')     