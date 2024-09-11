def calcular_salario(horas_trabajadas: float, antiguedad: int) -> float:
   
    salario_base = horas_trabajadas * 10
    incremento = 0.03 * antiguedad
    salario_total = salario_base * (1 + incremento)
    return salario_total

def calcular_productividad(artefactos_producidos: int, horas_trabajadas: float) -> float:
    
    while horas_trabajadas <= 0:
       print("La cantidad de horas trabajadas debe ser mayor a cero.")
       horas_trabajadas = float(input("Ingrese un valor correcto:"))
    
    return artefactos_producidos / horas_trabajadas

def reportar_informacion(nombre: str, edad: int, horas_trabajadas: float, antiguedad: int, artefactos_producidos: int):
    
    salario = calcular_salario(horas_trabajadas, antiguedad)
    productividad = calcular_productividad(artefactos_producidos, horas_trabajadas)
    
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Salario: ${salario:.2f}")
    print(f"Productividad: {productividad:.2f} artefactos por hora")