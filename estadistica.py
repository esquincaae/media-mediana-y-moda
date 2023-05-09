import statistics

# Pedimos la serie de números al usuario
numeros = input("Introduce la serie de números separados por comas: ")
numeros = [int(x) for x in numeros.split(",")]

# Calculamos la media, moda, mediana, frecuencia absoluta y frecuencia relativa
media = statistics.mean(numeros)
moda = statistics.mode(numeros)
mediana = statistics.median(numeros)
frec_abs = {x: numeros.count(x) for x in numeros}
frec_rel = {x: numeros.count(x) / len(numeros) for x in numeros}
absoluto = int(0)
relativo = int(0)
# Guardamos los resultados en un archivo de texto
with open("resultados.txt", "a") as f:
    f.write(f"Serie de numeros: {numeros}\n")
    f.write(f"Media: {media}\n")
    f.write(f"Moda: {moda}\n")
    f.write(f"Mediana: {mediana}\n")
    f.write("Frecuencia absoluta:\n")
    for k, v in frec_abs.items():
        f.write(f"{k}: {v}\n")
        absoluto = v + absoluto
    f.write(f"Total de frecuencia absoluta: {absoluto}\n")    
    f.write("Frecuencia relativa:\n")
    for k, v in frec_rel.items():
        f.write(f"{k}: {v}\n")
        relativo = v + relativo
    f.write(f"Total de frecuencia relativa: {relativo}")
    f.write("\n\n\n\n\n")
# Imprimimos los resultados por consola
print(f"Media: {media}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print("Frecuencia absoluta:")
for k, v in frec_abs.items():
    print(f"{k}: {v}")
print(f"Total frecuencia absoluta: {absoluto}")
print("Frecuencia relativa:")
for k, v in frec_rel.items():
    print(f"{k}: {v}")
print(f"Total de frecuencia relativa: {relativo}")    