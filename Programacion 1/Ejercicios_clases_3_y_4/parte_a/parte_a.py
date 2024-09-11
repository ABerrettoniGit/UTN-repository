# #Ejercicio 1
# def mostrar_numero(numero : int) -> None:
#     print(numero)

# #Ejercicio 2
# def comprobar_par(numero : int) -> bool:
#     if numero % 2 == 0:
#         return True 
#     else:
#         return False
    
# #Ejercicio 3
# def validar_numero(numero : int, menor : int, mayor : int) -> bool:
#     if numero > menor and numero < mayor:
#         print("Esta entre los parametros")
#         return True
#     else:
#         print("No esta entre los parametros")
#         return False

# #Ejercicio 4
# def restar1(a: int, b: int) -> int:
#     return a - b

# def restar2() -> int:
#     a = 10  
#     b = 5   
#     return a - b

# def restar3(a: int, b: int):
#     print(a - b)

# def restar4():        
#     a = 20  
#     b = 8   
#     print(a - b)

# #Ejercicio 5
# def realizar_descuento(numero : int) -> int:
#     descuento = numero *(5 / 100)
#     numero_descuento = numero - descuento
#     return numero_descuento

# def aplicar_descuento(numero : int) -> None:
#     if validar_numero(numero, 10, 100) == True:
#         numero_descuento = realizar_descuento(numero)
#         print("Numero con descuento: ", numero_descuento)
#     else:
#         print("El numero ingresado no es correcto")

# #Ejercicio 6
# def sumar(numero1 : int, numero2 : int) -> int:
#     return numero1 + numero2

# def operacion(numero1 : int, numero2 : int) -> None:
#     if validar_numero(numero1, 10, 100) == True and validar_numero(numero2, 10, 100) == True:
#         resultado_suma = sumar(numero1, numero2)
#         resultado_resta = restar1(numero1, numero2)
#         print(f"""Resultado Suma: {resultado_suma}
# Resultado resta: {resultado_resta}""")
#     else:
#         print("Numero no valido")