from matplotlib import pyplot as plt
import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento
#from benchmarking import Benchmarking


if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodosOrdenamiento()
    
    ##tam = 10000
    tamanios = [500, 1000, 2000]
    resultados =[]
    
    for tam in tamanios:
        
        arreglo_base = bench.build_arreglo(tam)
        key = "burbuja"
        value = metodosO.sort_bubble
        
        metodos_dic = {
        "burbuja": metodosO.sort_bubble,
        "burbuja_mejorado": metodosO.sort_burbuja_mejorado_optimizado,
        "seleccion": metodosO.sort_seleccion,
        "shell":metodosO.sort_shell,
    }
    
    
    
        for nombre, fun_metodo in metodos_dic.items():
            tiempo_reusltado = bench.medir_tiempo(fun_metodo,arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_reusltado)
            resultados.append(tupla_resultado)
            
        for tam, nombre, tiempo in resultados:
            print(f"Tamaño: {tam}, nombre metodo: {nombre}, tiempo: {tiempo:.6f} segundos")
            
    # preparar datos para ser graficados 
    # 1. crear un diccionario o map para almacenar resultados por metodos
    tiempos_by_metodo = {
        "burbuja": [],
        "burbuja_mejorado": [],
        "seleccion": [],
        "shell":[],
    } 
    
    
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)
        
    plt.figure(figsize=(10,6))      
    
    # graficar los tiempos de ejecucion para cada metodo
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label = nombre, marker ="o")  
        
    plt.title("Comparacion de tiempo para cada metodo de ordenamiento")
    plt.xlabel("Tamaño de los arreglos")
    plt.ylabel("Tiempo de Ejecucion(s)")
    
    plt.legend()
    plt.show()
            
        