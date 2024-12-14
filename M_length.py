# PAQUETES Y MODULOS
from p_length_converter.M_feet import feetConverter
from p_length_converter.M_meters import meterConverter
from p_length_converter.M_kilometers import kilometerConverter 
from p_length_converter.M_miles import milesConverter
from p_history.M_history import addHistory

nameLeng = ["Pies", "Metros", "Kilometros", "Millas"]

def lengthConv(nameLeng):
    lengthCurrent = ""
    wantLeng = ""
    value = ""

    print("Saludos, soy ConvTL y te ayudare a convertir una Longitud en especifico al tipo que gustes")
    while True:
        lengthCurrent = input('Que tipo de longitud deseas convertir: 1.Pies, 2.Metros, 3.Kilometros 4.Millas ?\n');
        # Validar opciones de la logitud actual
        if lengthCurrent not in("1","2","3","4"):
            while True:
                print(f'\n{lengthCurrent} no es una opcion valida.');
                lengthCurrent = input('Que tipo de longitud deseas convertir: 1.Pies, 2.Metros, 3.Kilometros 4.Millas ?\n');
                if lengthCurrent in("1","2","3"):
                    break;

        value = input(f'Ingresa el valor en {nameLeng[(int(lengthCurrent) - 1)]}:\n')
        # Validar si el valor es un un valor numerico
        if not value.replace('.', '', 1).isdigit():
            while True:
                print("\nSolo puedes ingresar numeros.")
                value = input(f'Ingresa el valor en {nameLeng[(int(lengthCurrent) - 1)]}:\n')
                if value.isdigit():
                    break
            
        value = float(value)

        wantLeng = input('A que tipo de Longitud deseas convertir: 1.Pies, 2.Metros, 3.Kilometros 4.Millas ?');
        # Validar opciones de la longitud a la que quiere convertir                    
        if wantLeng not in("1","2","3","4") or lengthCurrent == wantLeng:
            while True:
                if wantLeng not in("1","2","3","4"):
                    print(f'\n{wantLeng} no es una opcion valida.');
                    wantLeng = input('A que tipo de longitud deseas convertir: 1.Pies, 2.Metros, 3.Kilometros 4.Millas ?\n');
                    
                    if wantLeng not in("1","2","3","4"):
                        continue
                
                if(lengthCurrent == wantLeng):
                    while True:
                        if lengthCurrent == wantLeng:
                            print('No se puede hacer una conversion al mismo tipo de longitud.\nPor favor ingresar un tipo de longitud diferente:\n');
                        
                        if wantLeng not in("1","2","3","4"):
                            print(f'\n{wantLeng} no es una opcion valida.');
                        
                        wantLeng = input('A que tipo de longitud deseas convertir: 1.Pies, 2.Metros, 3.Kilometros 4.Millas ?\n');
                        if wantLeng in("1","2","3","4") and lengthCurrent != wantLeng:
                            break
                
                if wantLeng == "1":
                    result = feetConverter(lengthCurrent, value);
                    view = f'La conversion fue realizada con exito, la longitud es {result} ft';
                    print(view + "\n");
                    # Agregar al historial de conversion
                    addHistory(value, nameLeng[(int(lengthCurrent) - 1)], nameLeng[(int(wantLeng) - 1)], view, 'L');
                    break

                if wantLeng == "2":
                    result = meterConverter(lengthCurrent, value);
                    view = f'La conversion fue realizada con exito, la longitud es {result} m';
                    print(view + "\n");
                    # Agregar al historial de conversion
                    addHistory(value, nameLeng[(int(lengthCurrent) - 1)], nameLeng[(int(wantLeng) - 1)], view, 'L');
                    break

                if wantLeng == "3":
                    result = kilometerConverter(lengthCurrent, value);
                    view = f'La conversion fue realizada con exito, la longitud es {result} km';
                    print(view + "\n");
                    # Agregar al historial de conversion
                    addHistory(value, nameLeng[(int(lengthCurrent) - 1)], nameLeng[(int(wantLeng) - 1)], view, 'L');
                    break

                if wantLeng == "4":
                    result = milesConverter(lengthCurrent, value);
                    view = f'La conversion fue realizada con exito, la longitud es {result} mi';
                    print(view + "\n");
                    # Agregar al historial de conversion
                    addHistory(value, nameLeng[(int(lengthCurrent) - 1)], nameLeng[(int(wantLeng) - 1)], view, 'L');
                    break

        else:
            if wantLeng == "1":
                result = feetConverter(lengthCurrent, value);
                view = f'La conversion fue realizada con exito, la longitud es {result} ft';
                print(view + "\n");
                # Agregar al historial de conversion
                addHistory(value, nameLeng[(int(lengthCurrent) - 1)], nameLeng[(int(wantLeng) - 1)], view, 'L');

            if wantLeng == "2":
                result = meterConverter(lengthCurrent, value);
                view = f'La conversion fue realizada con exito, la longitud es {result} m';
                print(view + "\n");
                # Agregar al historial de conversion
                addHistory(value, nameLeng[(int(lengthCurrent) - 1)], nameLeng[(int(wantLeng) - 1)], view, 'L');

            if wantLeng == "3":
                result = kilometerConverter(lengthCurrent, value);
                view = f'La conversion fue realizada con exito, la longitud es {result} km';
                print(view + "\n");
                # Agregar al historial de conversion
                addHistory(value, nameLeng[(int(lengthCurrent) - 1)], nameLeng[(int(wantLeng) - 1)], view, 'L');

            if wantLeng == "4":
                result = milesConverter(lengthCurrent, value);
                view = f'La conversion fue realizada con exito, la longitud es {result} mi';
                print(view + "\n");
                # Agregar al historial de conversion
                addHistory(value, nameLeng[(int(lengthCurrent) - 1)], nameLeng[(int(wantLeng) - 1)], view, 'L');
        break;