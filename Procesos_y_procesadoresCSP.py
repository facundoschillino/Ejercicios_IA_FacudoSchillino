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
caracteristicas= {
    "Tesla": [8, 32, True], 
    "Goedel": [4, 16, False],
    "Bohr": [4, 16, False]
}
dominio = {}
posibilidades = {
    "Tesla", 
    "Goedel", 
    "Bohr"
}
Requisitos = { #Cantidad de procesadores, ram y grafica
"Limpiador de datos": [2, 10, False],
"Convertidor de entradas":[5, 20, False],
"Entrenador de modelos":[2,14, True],
"Almacenador de estadísticas":[1,1,False],
"Graficador de resultados":[2,2,False],
"Servidor de API":[2,8,False]
}

tesla = caracteristicas["Tesla"]

def quenoseterminelaramnilosprocesadores(variables, valores): #Aca voy a pasar cada una de las variables(Procesos), la cual va a tener asignada una serie de valores(Osea, los procesadores)
    procesos = variables #Lo hago solamente para identificarlo mejor
    procesador= valores
    ram_tesla = caracteristicas["Tesla"][1]
    ram_Goeandel = caracteristicas["Goedel"][1]
    ram_Bohr = caracteristicas["Bohr"][1]
    

    

