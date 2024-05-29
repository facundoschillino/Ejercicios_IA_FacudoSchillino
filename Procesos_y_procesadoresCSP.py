import itertools
from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)

variables = [
"Limpiador de datos",
"Convertidor de entradas",
"Entrenador de modelos",
"Almacenador de estadísticas",
"Graficador de resultados",
"Servidor de API"
]
Requisitos = { #Cantidad de procesadores, ram y grafica
"Limpiador de datos": [2, 10, False],
"Convertidor de entradas":[5, 20, False],
"Entrenador de modelos":[2,14, True],
"Almacenador de estadísticas":[1,1,False],
"Graficador de resultados":[2,2,False],
"Servidor de API":[2,8,False]
}

caracteristicas= {
    "Tesla": [8, 32, True], 
    "Goedel": [4, 16, False],
    "Bohr": [4, 16, False]
}
posibilidades = {
    "Tesla", 
    "Goedel", 
    "Bohr"
}
dominio = {
"Limpiador de datos": posibilidades,
"Convertidor de entradas": posibilidades,
"Entrenador de modelos": "Tesla" ,
"Almacenador de estadísticas": posibilidades,
"Graficador de resultados": posibilidades,
"Servidor de API": posibilidades
}


restricciones = []

def quenoseterminelaramn(variables, valores): #Aca voy a pasar cada una de las variables(Procesos), la cual va a tener asignada una serie de valores(Osea, los procesadores)
    ram_tesla = caracteristicas["Tesla"][1]
    ram_Goeandel = caracteristicas["Goedel"][1]
    ram_Bohr = caracteristicas["Bohr"][1]
    for proceso, procesador in zip(variables, valores):
        nucleos,ram,_ = Requisitos[procesos]
        if (procesador == "Tesla"):
            ram_tesla-= ram
        elif(procesador == "Goedel"):
            ram_Goeandel -= ram
        else: ram_Bohr -= ram
    return ((ram_Bohr>=0)and(ram_Goeandel>=0)and(ram_tesla>=0))

def quenoseterminenlosprocesadores(variables, valores): #Aca voy a pasar cada una de las variables(Procesos), la cual va a tener asignada una serie de valores(Osea, los procesadores)
    proc_tesla = caracteristicas["Tesla"][0]
    proc_Goeandel = caracteristicas["Goedel"][0]
    proc_Bohr = caracteristicas["Bohr"][0]
    for proceso, procesador in zip(variables, valores):
        nucleos,ram,_ = Requisitos[procesos]
        if (procesador == "Tesla"):
            proc_tesla-= nucleos
        elif(procesador == "Goedel"):
            proc_Goeandel -= nucleos
        else: proc_Bohr -= nucleos
    return ((proc_Bohr>=0)and(proc_Goeandel>=0)and(proc_tesla>=0)) 

restricciones.append((posibilidades, quenoseterminelaramn))
restricciones.append((posibilidades, quenoseterminenlosprocesadores))
problema = CspProblem(variables, dominio, restricciones)
solucion = min_conflicts(problema)

print("Solución encontrada:", solucion)