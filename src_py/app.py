import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento
#from benchmarking import Benchmarking


if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodosOrdenamiento()
    
    ##tam = 10000
    tamanios = [5000,10000,20000]
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
        resultados =[]
    
        for nombre, fun_metodo in metodos_dic.items():
            tiempo_reusltado = bench.medir_tiempo(fun_metodo,arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_reusltado)
            resultados.append(tupla_resultado)
            
        for tam, nombre, tiempo in resultados:
            print(f"Tamaño: {tam}, nombre metodo: {nombre}, tiempo: {tiempo:.6f} segundos")
        