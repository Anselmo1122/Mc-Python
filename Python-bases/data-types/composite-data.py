
# ==== Listas

list = ["Anselmo Del Hoyo", "ADH", True, 1.85]

# Acceder a valores de la lista
print(list)
print(list[0])
print(list[list.__len__() - 1])

# Podemos modificar sus valores
list[3] = 1.81
print(list)

# ==== Tuplas

tuple = ("Anselmo Del Hoyo", "ADH", True, 1.85)

# Acceder a valores de la tupla
print(tuple[2])

# No podemos modificar sus valores

#! TypeError: 'tuple' object does not support item assignment
# tuple[3] = 1.81
# print(tuple)

# ==== Conjunto

# Creando un conjunto (set) (no se accede a elementos por índice, no almacena datos duplicados, y devuelve datos desordenados)

conjunto = {"Anselmo Del Hoyo", "ADH", True, 1.85, "Anselmo Del Hoyo"}

print(conjunto)

# ==== Dict

diccionario = {
#   Key    :    Value
  "nombre" : "Luis Del Hoyo",
  "canal"  : "ADH",
  "es_desarrollador" : True,
  "altura" : 1.86
}

print(diccionario["es_desarrollador"])