# =====================================================================
# CURSO: Fundamentos de Programación (Código: 213022)
# FASE 5: Evaluación Final POA
# PROBLEMA 3: Auditoría de Inventario y Reabastecimiento
# =====================================================================

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Módulo (función) que determina la cantidad exacta a pedir para un artículo.
    Lógica de negocio:
    - Si Stock Actual < Stock Mínimo: Pide la diferencia.
    - Si Stock Actual >= Stock Mínimo: Pide 0.
    """
    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0
        
    return cantidad_pedir


def generar_informe_pedidos(inventario):
    """
    Módulo que recorre la matriz de inventario, procesa los datos
    e imprime la lista de pedidos con el nombre y la cantidad a solicitar.
    """
    print("\n==================================================")
    print("        INFORME DE PEDIDOS DE REABASTECIMIENTO    ")
    print("==================================================")
    print(f"{'ARTÍCULO':<20} | {'CANTIDAD A PEDIR':<15}")
    print("--------------------------------------------------")
    
    # Recorremos cada fila de la matriz
    for fila in inventario:
        # Extraemos los datos según el formato de la matriz
        codigo = fila[0]
        nombre = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]
        
        # Llamamos a la función lógica para calcular la cantidad
        cantidad_solicitar = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # Imprimimos el resultado formateado
        print(f"{nombre:<20} | {cantidad_solicitar:<15}")
        
    print("==================================================\n")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    # Matriz inicial con 5 artículos (Formato: [Código, Nombre, Stock Actual, Stock Mínimo])
    # Se incluyen casos donde el stock es bajo y otros donde es suficiente.
    matriz_inventario = [
        ["A001", "Teclado Mecánico", 12, 15],  # Requiere (15 - 12 = 3)
        ["A002", "Mouse Óptico",      25, 20],  # No requiere (0)
        ["A003", "Monitor 24'",        4,  8],  # Requiere (8 - 4 = 4)
        ["A004", "Auriculares Gamer", 30, 30],  # No requiere (0)
        ["A005", "Cable HDMI 2m",      8, 20]   # Requiere (20 - 8 = 12)
    ]
    
    # Ejecutamos el módulo que genera las salidas en pantalla
    generar_informe_pedidos(matriz_inventario)
