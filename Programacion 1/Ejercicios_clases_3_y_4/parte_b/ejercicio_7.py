# def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones
# = 15):
# resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
# resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
# resultado_final = resultado_nacional + resultado_exportaciones
# return resultado_final

def calcular_iva(iva: int = 21) -> float:
    '''
    Calcula el valor del iva 
    
    Parametros:
    ------------
    iva (int)

    Retorna:
    ------------
    retorna el valor del iva calculado
    '''
    resultado = (1 / (1 + (iva / 100)))
    return resultado
    
def calcular_retenciones(retenciones: int = 15) -> float:
    '''
    Calcula el valor de las retenciones 
    
    Parametros:
    ------------
    retenciones (int)

    Retorna:
    ------------
    retorna el valor de las retenciones calculadas
    '''
    resultado = (1 - (retenciones / 100))
    return resultado


def resultado_nacional(valor_venta_nacionales: int) -> int:
    '''
    Calcula el valor de las ventas nacionales con el iva
    
    Parametros:
    ------------
    valor_venta_nacionales (int)

    Retorna:
    ------------
    retorna el valor de las ventas nacionales con el iva agregado
    '''

    res_nacional = valor_venta_nacionales * (calcular_iva)

    return res_nacional

def resultado_exportaciones(valor_exportaciones: int) -> int:
    '''
    Calcula el valor de las exportanciones con las retenciones
    
    Parametros:
    ------------
    valor_exportaciones (int)

    Retorna:
    ------------
    retorna el valor de las exportanciones con las retenciones agregadas
    '''

    res_exportaciones = valor_exportaciones * (calcular_retenciones)

    return res_exportaciones

def resultado_final() -> float:
    '''
    Calcula el valor final de resultado nacional y resultado exportaciones
    
    Parametros:
    ------------
    

    Retorna:
    ------------
    retorna el valor final 
    '''
    res_final = resultado_nacional + resultado_exportaciones

    return res_final