# a) 
def Promedio_top_20(lista_ingresos) -> None:

    n = 0
    for _ in lista_ingresos:
        n += 1

    cantidad_mayor = n // 5  
    suma_mayor = 0
    contador_mayor = 0

    for _ in range(cantidad_mayor):
        maximo = lista_ingresos[0]
        for ingreso in lista_ingresos:
            if ingreso > maximo:
                maximo = ingreso
        
        suma_mayor += maximo
        contador_mayor += 1
        
        nueva_lista = []
        encontrado = False
        for ingreso in lista_ingresos:
            if ingreso == maximo and not encontrado:
                encontrado = True
                continue
            nueva_lista = nueva_lista + [ingreso] 
        lista_ingresos = nueva_lista

    if contador_mayor == 0:
        return 0
    return suma_mayor / contador_mayor

# b) 
def Promedio_todos(lista_ingresos):
    suma = 0
    contador = 0
    for ingreso in lista_ingresos:
        suma += ingreso
        contador += 1
    return suma / contador if contador > 0 else 0

# c)
def Valor_mas_repetido(lista_ingresos):
    conteos = {}
    for ingreso in lista_ingresos:
       
        if ingreso in conteos:
            conteos[ingreso] += 1
        else:
            conteos[ingreso] = 1
    
    max_repeticiones = 0
    for clave in conteos:
        if conteos[clave] > max_repeticiones:
            max_repeticiones = conteos[clave]

    valores_mas_repetidos = []
    for clave in conteos:
        if conteos[clave] == max_repeticiones:
            valores_mas_repetidos = valores_mas_repetidos + [clave]  
    
    return valores_mas_repetidos

# d)
def Media_geometrica(lista_ingresos):
    producto_total = 1
    contador = 0
    for ingreso in lista_ingresos:
        producto_total *= ingreso
        contador += 1

    if contador == 0:
        return 0

    
    raiz = producto_total ** (1 / contador)  

    return raiz

# e)
def Recorrer_lista_ambos_sentidos(lista_ingresos):
    recorrido = []
    for ingreso in lista_ingresos:
        recorrido = recorrido + [ingreso]  
    
    n = 0
    for _ in lista_ingresos:
        n += 1

    for i in range(n - 1, -1, -1):
        recorrido = recorrido + [lista_ingresos[i]]
    
    return recorrido

#2


#a

def Definir_mayor_menor(lista_edad: list, lista_nombres: list):
    edad_mayor = 0
    nombre_mayor = ""

    edad_menor = 0
    nombre_menor = ""

    contador = 0

    for i in range(len(lista_edad)):

        if contador == 0:
            edad_mayor = lista_edad[i]
            nombre_mayor = lista_nombres[i]

            edad_menor = lista_edad[i]
            nombre_menor = lista_nombres[i]
            contador += 1
    
        if edad_mayor < lista_edad[i]:
            edad_mayor = lista_edad[i]
            nombre_mayor = lista_nombres[i]

        if edad_menor > lista_edad[i]:
            edad_menor = lista_edad[i]
            nombre_menor = lista_nombres[i]

    print("Menor", edad_menor, nombre_menor, "Mayor", edad_mayor, nombre_mayor)
        
    
#b
def Encontrar_mayor_65(lista_edad: list, lista_nombres: list):

    nombre_mayor_65 = ""
    edad = 0

    for i in range(len(lista_edad)):
        if lista_edad[i] > 65:
            nombre_mayor_65 = lista_nombres[i]
            print ("Es mayor de 65 es: ", nombre_mayor_65)
            break

#c
def Calcular_media_etaria(lista_edad: list):
    suma_mayor_40 = 0
    contador_media_etaria = 0
    promedio_media_etaria = 0
    for edad in lista_edad:
        if edad < 40:
            continue

        suma_mayor_40 += edad
        contador_media_etaria += 1

    if contador_media_etaria != 0:
        promedio_media_etaria = suma_mayor_40 / contador_media_etaria

        print(f"la media etaria es: {promedio_media_etaria}")

#3 

nombres = []
sexos = []
horas_trabajadas = []
ingresos_semanales = []

def Agregar_respondente():
    
    while True:
        nombre = input("Ingrese el nombre del respondente (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        sexo = input("Ingrese el sexo del respondente (M/F): ")
        horas = int(input("Ingrese la cantidad de horas trabajadas: "))
        ingreso = float(input("Ingrese el ingreso semanal: "))

        
        nombres.append(nombre)
        sexos.append(sexo)
        horas_trabajadas.append(horas)
        ingresos_semanales.append(ingreso)


#4

#5
def Corregir_listas(lista: list):
    None

#6
def Pedir_numeros(lista_numeros: list) -> list:
    i = 0
    
    while i < 10:
        numero = int(input("Ingrese un numero: "))
        while numero <= 10 or numero >= 30:
            numero = int(input("Ingrese un numero correcto 10 - 30: "))

        lista_numeros.append(numero)
        
        i += 1 
    
    return lista_numeros

#7 
def Encontrar_menor_edad(lista_edad: list, lista_nombres: list) -> list:

    lista_menores = []
    lista_nombres_menores = []
    menor_edad = 0
    menor_edad_nombre = ""
    contador = 0
    for i in range(len(lista_edad)):
       
        if contador == 0:
           menor_edad = lista_edad[i]
           menor_edad_nombre = lista_nombres[i]
           contador += 1
           
        
        if menor_edad >= lista_edad[i]:
           menor_edad = lista_edad[i]
           menor_edad_nombre = lista_nombres[i]
        else:
            continue
    
        lista_menores.append(menor_edad)
        lista_menores.append(menor_edad_nombre)
        

        
    return lista_menores

#8
def verificar_tipos(lista):
    
    tipos = {type(elemento) for elemento in lista}  

    if len(tipos) == 1:
        print(tipos)  
    else:
        print(tipos) 


#9
def cargar_lista(nueva_lista: list) -> list:

    seguir = "s"
   
    if type(nueva_lista) != list:
        print("La funcion debe recibir una lista")
        return None

    tipo = type(nueva_lista)
    print(f"La lista contiene elementos del tipo: {tipo}")

    while seguir == "s":
        match tipo:
            case tipo if str:
                nuevo_elemento = input("Ingrese el nuevo elemento: ")
            case tipo if int:
                nuevo_elemento = int(input("Ingrese el nuevo elemento: "))
            case tipo if float:
                nuevo_elemento = float(input("Ingrese el nuevo elemento: "))

        nueva_lista += [nuevo_elemento]

        seguir = input("desea continuar? s/n ").lower()
    
    return nueva_lista


#11

def Buscar_binario_recursivo(lista: list, buscado: any, inicio: int, final: int):    
    if inicio > final: 
        return None
    medio = (inicio + final) // 2
    
    if lista[medio] == buscado:
        return medio
    elif lista[medio] < buscado:
        return Buscar_binario_recursivo(lista, buscado, medio + 1, final) 
    else:
        return Buscar_binario_recursivo(lista, buscado, inicio, medio - 1) 

lista_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor_buscado = 8

inicio = 0
final = len(lista_ejemplo) - 1

resultado = Buscar_binario_recursivo(lista_ejemplo, valor_buscado, inicio, final)

if resultado == None:
    print(f"Valor {valor_buscado} no encontrado")
else:
    print(f"Valor {valor_buscado} encontrado en el índice: {resultado}")



