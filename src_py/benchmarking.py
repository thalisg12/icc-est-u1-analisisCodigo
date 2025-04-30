import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    
    def __init__(self):
        print("Benchmarking instanciado")
        self.mO = MetodosOrdenamiento()
        arreglo = self.build_arreglo(10000)
        tarea = lambda: self.mO.sort_bubble(arreglo)
        tiempoM = self.contar_con_current_time_milles_(tarea)
        tiempoN = self.contar_con_nano_time(tarea)
        
        tarea2 = lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo)
        tiempoNBM = self.contar_con_nano_time(tarea2)
        
        tarea3 = lambda: self.mO.sort_seleccion(arreglo)
        tiempoNMS = self.contar_con_nano_time(tarea3)
        
        
        
        print(f"Tiempo en nanosegundos de MB: {tiempoN}")
        print(f"Tiempo en nanosegundos de MBM: {tiempoNBM}")
        print(f"Tiempo en nanosegundos de MS: {tiempoNMS}")
    
    def build_arreglo(self, tamano):
        arreglo = []
        for i in range(tamano):
            numero = random.randint(0,99999)
            arreglo.append(numero)
        return arreglo
    
    def contar_con_current_time_milles_(self,tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return fin - inicio
    
    def contar_con_nano_time(self,tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio)/1_000_000_000.0