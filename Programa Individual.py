#Código del ejercicio 3.2

#Datos del alumno:
#Nombre y matricula: Fernando Javier Noh Requena (19070052)
#Materia: Lenguaje y Autómatas
#Semestre y grupo: 5°B
#Fecha de entrega: 09 de noviembre del 2021

#Librerias que usaré en el programa:
import re
import string

#A continuación se hace el código que nos permitira leer y usar un archivo de tipo txt:
filename='prueba'
archivo=open(filename, "r") #Este txt. es que usaremos para ejecutar todas las opciones

# Hacemos el menú de opciones para nuestro programa
print('Menu de opciones a realizar: ')
print('\n 1. Variables \n 2. Enteros y decimales \n 3. Expresiones aritmeticas \n 4. Operadores condicionales \n 5. Cadena de caracteres')
print("")
eleccion=int(input("Escriba el número de la opción que ha elegido:"))
print("")

# A continuación, hice un menú que realizará una determinada acción dependiendo de la elección del usuario:
# Hacemos un if para poder hacer un acción dependiendo de lo que elija el usuario:

#Búsqueda de variables
if eleccion==1:
    regex1 = "[^\'\"\d][a-zA-Z_][a-zA-Z_0-9]*[^\'\"]"
    re1 = re.compile(regex1)
    for line in archivo:
        lista1 = re1.findall(line)
        print(lista1)
    archivo.close()

# Hacemos la búsqueda de enteros y decimales
if eleccion==2:
    regex2= "[\d.]+"
    re2=re.compile(regex2)
    for line in archivo:
        lista2=re2.findall(line)
        print(lista2)
    archivo.close()

# Aquí se realiza la búsqueda de expresiones aritmeticas
if eleccion==3:
    regex3 = "([A-za-z]\w*|\d\.?\d*)\s?(\+|\-|\*|\/)\s?([A-za-z]\w*|\d\.?\d*)"
    re3 = re.compile(regex3)
    for line in archivo:
        lista3 = re3.findall(line)
        print(lista3)
    archivo.close()

# Aqui buscamos los operadores condicionantes
if eleccion==4:
    regex4="([A-za-z]\w*|\d\.?\d*)\s?(\>|\<|\>=|\<=|=|!=|\=\=)\s?([A-za-z]\w*|\d\.?\d*)"
    re4=re.compile(regex4)
    for line in archivo:
        lista4 = re4.findall(line)
        print(lista4)
    archivo.close()

# Búsqueda de cadenas de palabras
if eleccion==5:
    signos = string.punctuation  #Python nos deja usar una opción en la que podemos seleccionar todos los signod de puntuación
    regex5="\"[\w"+signos+"\s]+"   #Aquí juntamos la variable anterior y completamos con el resto de expresiones faltantes
    re5=re.compile(regex5)
    for line in archivo:
        lista5 = re5.findall(line)
        print(lista5)
    archivo.close()

