# leer achivo y escribir cada línea
# abrir archivo en modo lectura
with open ('informacion.txt','r', encoding ='utf-8') as archivo:
    
    lineas = archivo.readlines()
    

for numero_linea, linea in enumerate (lineas, start = 1):
    print (f"linea {numero_linea}: {linea.strip()} ")
    