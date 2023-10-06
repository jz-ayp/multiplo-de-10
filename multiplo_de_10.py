"""
Determinar si un número es múltiplo de 10
"""

# Entradas
numero = eval(input("Introduzca un número: "))
	
# Proceso
if numero % 10 == 0:
    resultado = "sí"
else:
	resultado = "no"
# Salidas
print("El número", numero, resultado, "es múltiplo de 10.")
