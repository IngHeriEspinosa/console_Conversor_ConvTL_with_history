# Conversor de temperatura y longitud.

# PAQUETES Y MODULOS
from M_temperature import temperatureConv
from M_length import lengthConv
from p_history.M_history import showHistory

# Menu principal
print('Bienvenido al conversor de Temperatura y Longitud "ConvTL"');
while True:
    # Nombres de conversiones
    nameTemp = ["Celsius", "Fahrenheit", "Kelvin"]
    nameLeng = ["Pies", "Metros", "Kilometros", "Millas"]

    op = input('Opciones de conversion: 1.Temperatura 2.Longitud 3.Historial de conversion 4.Salir:\n');

    if(op not in("1", "2", "3", "4")):
        print(f"{op} no es una opcion valida");
        break

    elif(op == "1"):
        temperatureConv(nameTemp)
        
    elif(op == "2"):
        lengthConv(nameLeng)

    elif(op == "3"):
        showHistory()
        break;

    elif(op == "4"):
        print("Bye, hasta luego.")
        break;

