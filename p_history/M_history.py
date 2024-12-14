import csv
import os

# Crear el historial de conversion
def addHistory (value, mensure1, mensure2, result, typeConvertion, nombre='p_history/historyConverter.csv'):
    
    # Buscar el nombre del archivo como ruta
    file_exist = os.path.exists('p_history/historyConverter.csv')

    with open(nombre, mode='a', newline='', encoding='utf-8') as archivo_csv:
        escribir = csv.writer(archivo_csv)

        # Escribe el encabezado y las lineas si no existe el archivo
        if not file_exist:
            escribir.writerow(['Valor de conversion', 'De', 'A', 'Resultado', 'tipo de conversion'])
            escribir.writerow([value, mensure1, mensure2, result, typeConvertion])
        else:    
            # Escribe los datos en una nueva línea
            escribir.writerow([value, mensure1, mensure2, result, typeConvertion])
    
    if(typeConvertion == "T"):
        # Buscar el nombre del archivo como ruta
        file_exist = os.path.exists('p_history/historyConverterTemperature.csv')
        nombre = 'p_history/historyConverterTemperature.csv'

        with open(nombre, mode='a', newline='', encoding='utf-8') as archivo_csv:
            escribir = csv.writer(archivo_csv)

            # Escribe el encabezado y las lineas si no existe el archivo
            if not file_exist:
                escribir.writerow(['Valor de conversion', 'De', 'A', 'Resultado', 'tipo de conversion'])
                escribir.writerow([value, mensure1, mensure2, result, typeConvertion])
            else:    
                # Escribe los datos en una nueva línea
                escribir.writerow([value, mensure1, mensure2, result, typeConvertion])

    if(typeConvertion == "L"):
        # Buscar el nombre del archivo como ruta
        file_exist = os.path.exists('p_history/historyConverterLength.csv')
        nombre = 'p_history/historyConverterLength.csv'

        with open(nombre, mode='a', newline='', encoding='utf-8') as archivo_csv:
            escribir = csv.writer(archivo_csv)

            # Escribe el encabezado y las lineas si no existe el archivo
            if not file_exist:
                escribir.writerow(['Valor de conversion', 'De', 'A', 'Resultado', 'tipo de conversion'])
                escribir.writerow([value, mensure1, mensure2, result, typeConvertion])
            else:
                # Escribe los datos en una nueva línea
                escribir.writerow([value, mensure1, mensure2, result, typeConvertion])


# Mostrar el historial de conversion
def showHistory ():
    print('Historial de conversion\n')

    while True:
        typeHistory = input('Cual historial que deseas consultar: 1.Todo 2.Temperatura 3.Lonitud 4.Salir \n')

        if typeHistory not in("1", "2", "3", "4"):
            print(f"{typeHistory} no es una opcion valida");
            break

        elif typeHistory == "1":
            nombre='p_history/historyConverter.csv'

            # Verifica si el archivo existe
            if not os.path.exists(nombre):
                message = "El archivo no existe."
                print(message)
                return message

            # Leer los datos del archivo
            with open(nombre, mode='r', newline='', encoding='utf-8') as archivo_csv:
                lector = csv.DictReader(archivo_csv)
                datos = list(lector)  # Convierte los datos a una lista de diccionarios

            # Mostrar los datos ordenados
            for fila in datos:
                print(fila)

            break;

        elif typeHistory == "2":
            nombre='p_history/historyConverterTemperature.csv'
            
            # Verifica si el archivo existe
            if not os.path.exists(nombre):
                message = "El archivo no existe."
                print(message)
                return message

            # Leer los datos del archivo
            with open(nombre, mode='r', newline='', encoding='utf-8') as archivo_csv:
                lector = csv.DictReader(archivo_csv)
                datos = list(lector)  # Convierte los datos a una lista de diccionarios

            # Mostrar los datos ordenados
            for fila in datos:
                print(fila)

            break;

        elif typeHistory == "3":
            nombre='p_history/historyConverterLength.csv'
            
            # Verifica si el archivo existe
            if not os.path.exists(nombre):
                message = "El archivo no existe."
                print(message)
                return message

            # Leer los datos del archivo
            with open(nombre, mode='r', newline='', encoding='utf-8') as archivo_csv:
                lector = csv.DictReader(archivo_csv)
                datos = list(lector)  # Convierte los datos a una lista de diccionarios

            # Mostrar los datos ordenados
            for fila in datos:
                print(fila)

            break;

        elif typeHistory == "4":
            break;