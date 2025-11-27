import random
import json

lista_barquitos = list()

def elegir_barquito():
    elegir_barco = random.choice(lista_barquitos)
    print(f"Elegiste un barquito peruano lleno de: {elegir_barco}.")

def agregar_barquito():
    agregar_nuevo_barco = input("Un barquito peruano lleno de: ")
    lista_barquitos.append(agregar_nuevo_barco)
    print("Agregaste un nuevo tema a la lista de barquitos.")
    
def guardar_barquitos():
    with open ("barquitos.json", "w+") as archivo_json:
        json.dump(lista_barquitos, archivo_json, indent=4)
    print("Agenda guardada correctamente.")
    
def cargar_barquitos():
    global lista_barquitos
    try:
        with open("agenda.json", "r") as archivo_json:
            lista_barquitos = json.load(archivo_json)
        print("Lista cargada correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo con la lista. Asegúrese de haber guardado todo previamente.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Asegúrese de que el formato sea correcto.")
    
def barquito_peruano():
    
    while True :
        print("1. Lista de barquitos")
        print("2. Elegir un barquito")
        print("3. Agregar nuevo tema") 
        print("4. Guardar barquitos") 
        print("5. Cargar barquitos") 
        print("6. Salir del sistema") 
        
        option = input("Seleccioná una opción: ")
        
        match option:
            case "1":
                print(lista_barquitos)
                pass
            
            case "2":
                elegir_barquito()
                pass
            
            case "3":
                agregar_barquito()
                print("Nuevo barquito ingresado.")
                pass
            
            case "4":
                guardar_barquitos()
                pass
            
            case "5":
                cargar_barquitos()
                pass
            
            case "6":
                print("Saliendo del avanzado sistema de barquitos. Hasta luego.")
                break
            case _:
                print("Opción no válida. Escribí otra opción del 1 al 5 o 6 para salir del sistema")
                
barquito_peruano()