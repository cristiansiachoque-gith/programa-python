# =====================================================================
# CURSO: Fundamentos de Programación Código: 213022
# FASE 5: Evaluación Final POA
# PROBLEMA 3: Auditoría de Inventario
# =====================================================================

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Módulo (función) que determina la cantidad exacta a pedir para un artículo.
    Lógica de negocio:
    - Si Stock Actual < Stock Mínimo: Pide la diferencia.
    - Si Stock Actual >= Stock Mínimo: Pide 0.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


def generar_informe_pedidos(inventario):
    """
    Módulo que recorre la matriz de inventario generada por el usuario
    e imprime la lista de pedidos con el nombre y la cantidad a solicitar.
    """
    print("\n==================================================")
    print("        INFORME DE PEDIDOS DE REABASTECIMIENTO    ")
    print("==================================================")
    print(f"{'ARTÍCULO':<20} | {'CANTIDAD A PEDIR':<15}")
    print("--------------------------------------------------")
    
    for fila in inventario:
        nombre = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]
        
        cantidad_solicitar = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        print(f"{nombre:<20} | {cantidad_solicitar:<15}")
        
    print("==================================================\n")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    print("=== SISTEMA DE AUDITORÍA DE INVENTARIO ===")
    
    # La guía pide que la matriz tenga AL MENOS 5 artículos.
    # Validamos que el usuario ingrese un número válido mayor o igual a 5.
    while True:
        try:
            num_articulos = int(input("¿Cuántos artículos deseas registrar? (Mínimo 5): "))
            if num_articulos >= 5:
                break
            else:
                print("Por favor, ingresa 5 o más artículos para cumplir con la guía.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    # Matriz vacía que iremos llenando
    matriz_inventario = []
    
    # Ciclo para capturar los datos por teclado
    for i in range(num_articulos):
        print(f"\n--- Registro del Artículo #{i + 1} ---")
        codigo = input("Código del artículo: ")
        nombre = input("Nombre del artículo: ")
        
        # Validamos que los stocks sean números válidos
        while True:
            try:
                stock_actual = int(input(f"Stock Actual de '{nombre}': "))
                stock_minimo = int(input(f"Stock Mínimo Requerido de '{nombre}': "))
                if stock_actual >= 0 and stock_minimo >= 0:
                    break
                else:
                    print("Los valores de stock no pueden ser negativos.")
            except ValueError:
                print("Por favor, ingresa números enteros válidos para el stock.")
        
        # Guardamos la fila en nuestra matriz
        fila_articulo = [codigo, nombre, stock_actual, stock_minimo]
        matriz_inventario.append(fila_articulo)
    
    # Una vez llena la matriz, procesamos y mostramos el informe
    generar_informe_pedidos(matriz_inventario)