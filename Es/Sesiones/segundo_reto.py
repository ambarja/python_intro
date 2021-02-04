# Consideraciones iniciales 
usuario_1 = input('Nombre del primero usuario: ')
edad_1    = input('Hola ' + usuario_1 + ' ' + 'ingrese su edad: ')
usuario_2 = input('Nombre del segundo usuario: ')
edad_2    = input('Hola ' + usuario_2 + ' ' + 'ingrese su edad: ')

# Creación de condificiones simples 
if usuario_1 > usuario_2 :
    print(usuario_1 + 'es mayor que ' + usuario_2) 
elif usuario_1 < usuario_2 :
    print(usuario_1 + 'es menor que ' + usuario_2)
else : 
    print(usuario_1 + 'tiene la misma edad que el ' + usuario_2) 
