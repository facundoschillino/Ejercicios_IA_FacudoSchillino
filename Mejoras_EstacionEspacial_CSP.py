import itertools
from simpleai.search import (CspProblem, backtrack, min_conflicts,
                             MOST_CONSTRAINED_VARIABLE,
                             LEAST_CONSTRAINING_VALUE,
                             HIGHEST_DEGREE_VARIABLE)

variables = [
    "sl1", "sl2", "sl3"
]

mejoras = {
    "Baterias":[12.5, 300],
    "Brazo Robotico":[60,50],
    "Ventana": [100, 550],
    "Antena": [20,30],
    "Laboratorio plantas": [80,250],
    "Laboratorio fisica" : [75,300], #Solo puede haber uno
    "Computadora de control": [50,20],
    "Reciclador" : [30, 100]
}