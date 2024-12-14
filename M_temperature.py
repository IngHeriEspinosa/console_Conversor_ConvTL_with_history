# PAQUETES Y MODULOS
from p_temperature_converter.M_celsius import celsiusConverter
from p_temperature_converter.M_fahrenheit import fahrenheitConverter 
from p_temperature_converter.M_kelvin import kelvinConverter
from p_history.M_history import addHistory

nameTemp = ["Celsius", "Fahrenheit", "Kelvin"]

def temperatureConv(nameTemp):
    typeCurrent = ""
    wantTemp = ""
    value = ""

    print("Saludos, soy ConvTL y te ayudare a convertir una Temperatura en especifico al tipo que gustes")
    while True:
        typeCurrent = input('Que tipo de temperatura deseas convertir: 1.Celsius, 2.Fahrenheit, 3.Kelvin ?\n');
        # Validar opciones de la temperatura actual
        if typeCurrent not in("1","2","3"):
            while True:
                print(f'\n{typeCurrent} no es una opcion valida.');
                typeCurrent = input('Que tipo de temperatura deseas convertir: 1.Celsius, 2.Fahrenheit, 3.Kelvin ?\n');
                if typeCurrent in("1","2","3"):
                    break;

        value = input(f'Ingresa el valor en {nameTemp[(int(typeCurrent) - 1)]}:\n')
        # Validar si el valor es un un valor numerico
        if not value.replace('.', '', 1).isdigit():
            while True:
                print("\nSolo puedes ingresar numeros.")
                value = input(f'Ingresa el valor en {nameTemp[(int(typeCurrent) - 1)]}:\n')
                if value.isdigit():
                    break
            
        value = float(value)

        wantTemp = input('A que tipo de temperatura deseas convertir: 1.Celsius, 2. Fahrenheit, 3.Kelvin ?\n');
        # Validar opciones de la temperatura a la que quiere convertir                    
        if wantTemp not in("1","2","3") or typeCurrent == wantTemp:
            while True:
                if wantTemp not in("1","2","3"):
                    print(f'\n{wantTemp} no es una opcion valida.');
                    wantTemp = input('A que tipo de temperatura deseas convertir: 1.Celsius, 2. Fahrenheit, 3.Kelvin ?\n');
                    
                    if wantTemp not in("1","2","3"):
                        continue
                
                if(typeCurrent == wantTemp):
                    while True:
                        if typeCurrent == wantTemp:
                            print('No se puede hacer una conversion al mismo tipo de temperatura.\nPor favor ingresar un tipo de temperatura diferente:\n');
                        
                        if wantTemp not in("1","2","3"):
                            print(f'\n{wantTemp} no es una opcion valida.');
                        
                        wantTemp = input('A que tipo de temperatura deseas convertir: 1.Celsius, 2. Fahrenheit, 3.Kelvin ?\n');
                        if wantTemp in("1","2","3") and typeCurrent != wantTemp:
                            break
                
                if wantTemp == "1":
                    result = celsiusConverter(typeCurrent, value);
                    view = f'La conversion fue realizada con exito, la temperatura es {result} °C'
                    print(view + "\n");
                    # Agregar al historial de conversion
                    addHistory(value, nameTemp[(int(typeCurrent) - 1)], nameTemp[(int(wantTemp) - 1)], view, 'T');
                    break

                if wantTemp == "2":
                    result = fahrenheitConverter(typeCurrent, value);
                    view = f'La conversion fue realizada con exito, la temperatura es {result} °F'
                    print(view + "\n");
                    # Agregar al historial de conversion
                    addHistory(value, nameTemp[(int(typeCurrent) - 1)], nameTemp[(int(wantTemp) - 1)], view, 'T');
                    break

                if wantTemp == "3":
                    result = kelvinConverter(typeCurrent, value);
                    view=f'La conversion fue realizada con exito, la temperatura es {result} K'
                    print(view + "\n");
                    # Agregar al historial de conversion
                    addHistory(value, nameTemp[(int(typeCurrent) - 1)], nameTemp[(int(wantTemp) - 1)], view, 'T');
                    break

        else:
            if wantTemp == "1":
                result = celsiusConverter(typeCurrent, value);
                view = f'La conversion fue realizada con exito, la temperatura es {result} °C'
                print(view + "\n");
                # Agregar al historial de conversion
                addHistory(value, nameTemp[(int(typeCurrent) - 1)], nameTemp[(int(wantTemp) - 1)], view, 'T');
                

            if wantTemp == "2":
                result = fahrenheitConverter(typeCurrent, value);
                view = f'La conversion fue realizada con exito, la temperatura es {result} °F'
                print(view + "\n");
                # Agregar al historial de conversion
                addHistory(value, nameTemp[(int(typeCurrent) - 1)], nameTemp[(int(wantTemp) - 1)], view, 'T');

            if wantTemp == "3":
                result = kelvinConverter(typeCurrent, value);
                view=f'La conversion fue realizada con exito, la temperatura es {result} K'
                print(view + "\n");
                # Agregar al historial de conversion
                addHistory(value, nameTemp[(int(typeCurrent) - 1)], nameTemp[(int(wantTemp) - 1)], view, 'T');
        break;
   