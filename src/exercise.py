def main():
    # delete the 'pass' statement, then begin coding below:
    # p ass
    
    # Entradas
    numero = int(input("Introduzca un número: "))
    
    # Proceso
    if numero % 10 == 0:
        resultado = "sí"
    else:
        resultado = "no"
        
    # Salidas
    print("El número", numero, resultado, "es múltiplo de 10")
    

if __name__ == '__main__': 
    main()
