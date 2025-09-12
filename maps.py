import requests

# Funciones de búsqueda
def busqueda_lineal(lista, nombre):
    for pais in lista:
        if pais["name"]["common"].lower() == nombre.lower():
            return pais
    return None

def busqueda_binaria(lista, nombre):
    inicio = 0
    fin = len(lista) - 1
    nombre = nombre.lower()
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        pais_medio = lista[medio]["name"]["common"].lower()
        
        if pais_medio == nombre:
            return lista[medio]
        elif pais_medio < nombre:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

def main():
    url = "https://restcountries.com/v3.1/region/europe"
    response = requests.get(url)
    
    paises = response.json()
    
    # Ordena la lista para búsqueda binaria por nombre del país
    paises_ordenados = sorted(paises, key=lambda x: x["name"]["common"].lower())
    
    print("Búsqueda de Países en Europa")
    nombre = input("Ingrese el nombre del país a buscar: ").strip()
    print("Seleccione el tipo de búsqueda:")
    print("1. Búsqueda lineal")
    print("2. Búsqueda binaria")
    
    opcion = input("Opción: ").strip()
    
    if opcion == "1":
        resultado = busqueda_lineal(paises, nombre)
    elif opcion == "2":
        resultado = busqueda_binaria(paises_ordenados, nombre)
    else:
        print("Opción inválida, porfavor ingrese una opción valida")
        return
    
    if resultado:
        print("País encontrado:")
        print("Nombre:", resultado["name"]["common"])
        print("URL Google Maps:", resultado["maps"]["googleMaps"])
    else:
        print("País no encontrado en la lista de Europa.")

main()