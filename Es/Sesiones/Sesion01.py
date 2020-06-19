# Introducción a python en QGIs 3.x 
name = input('Digit your name:')
print('Hi',name)

# Intrucción de asignación
name = 'Antony'
edad = 25 
peso = 65.7

# Variables (generalmente son mínusculas, excepto si es una constate VAR = 32) 

# Nunca se empieza con un número:
10v = 200

# No se usa carácteres especiales:
precio$ = 124.56

# No se usa palabras reservadas:
class = 'Programación'

## Obs: Exiten más de 10 palabras reservadas en python (if, and, class, import, True, ...)

# Tipos de variables básicas en python (númerico, carácteres, lógico)

# Integer
print(1231213123123123121231234  + 1 )
print(10)

# Número binario :v 
print(0b10)
print(0B10)

# Número octal :'v
print(0o10)
print(0O10)

# Número Hexadecimal :''v 
print(0x10)
print(0X10)

# Identificando los tipos de objectos en python
type(0o10)
type(0b10)
type(0x10)

type(0.2)
type(True)
type('name')
type(24)

# Números complejos aj + b 
 
complejo = 2j + 3 
print(complejo, type(complejo))

# Strings

print('Hola mundo')
print('-----'*12)
print('2 + 3 es = ', 2+3)

 # Concatenación de strings "+"

a = 'SQL'
a + ' is cool <3'

# Tres funciones básicas para trabajar con strings

a = 'antony'
b = 'BARJA'
print(a)

# Mayusculas 
a.upper()

# Minusculas
b.lower()

# Remplazar un string

c = 'hello world'
print(c)
c.replace('h', 'H')

#  Para contat cuantas veces se repite un string "count()"

lista = ['Hi', 'Hello', 'Hola', 'Hi', 'Hi']
len(lista)
lista.count('Hi')

# Usanfo la función "format" para crear strings 
'{0} es el mejor lenguage de programación {1}'.format('Python','<3!')

# Especiales secuencias

print("a \tb")
xprint("a\nb")
print("a\\b")
print("a\fb")
print("a\bb")
print("a\vb")
print('a \N{rightwards arrow}')
print('\u2192')

# Uso de comillas

print('Hola "Antony" :v ')
print("Hi my names is 'Antony' and I'm 'data analyst' ")

# Boleanos o lógicos
type(True)
print('Do you always lies?\n', True)

10 == 10 
10 == 11

'antony' == 'antony'
'antony' == 'Antony'

10 != 10 
11 != 10
'Hi' != 'Hello'

# Usando algunos  operadores <, >, <= or >=

10 > 10 
10 < 11
10 <= 10
2 >= 8  
10 < 8 <= 11
True < False 
True <= True > False
'antony' > 'boruto'
'ab' < 'bc' 
'z' > 'a'
'aa' < 'bb'

# Operadores matemáticos simples 

3 + 3  # Suma
3 - 3  # Resta
3 / 3  # División
3 % 2  # Resto
5 // 3 # Cociente 
3 * 3  # Multipicación
3 ** 2 # Potencia 

num = 3 
num = num - 1 
print(num)
print(num,'\t',type(num))

num = num + 10
print(num)  

num += 10 
print(num)

num -= 10
print(num)

num *= -1
print(num)

# Orden de operaciones "PEDMAS"

3 + 2 * 5 
(3 + 2) * 5
10 + 4 / 2
(10 + 4 ) / 2

# Referencias: https://realpython.com/python-data-types/