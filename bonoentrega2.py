"""
Antonio Aspite Fermin 201629586
Jose Restom 201514617
"""
# pyomo solve lab3_pregunta2.py --solver='glpk'

from __future__ import division
from pyomo.environ import *

from pyomo.opt import SolverFactory

# MODELO
M = ConcreteModel()

# SET MUNICIPIOS DE LA GUAJIRA
M.i = RangeSet(1, 15)

# FALLECIDOS POR MUNICIPIO EN 2019
M.f = Param(M.i, within=Any, mutable=True)
M.f[1] = 8
M.f[2] = 4
M.f[3] = 13
M.f[4] = 5
M.f[5] = 1
M.f[6] = 2
M.f[7] = 2
M.f[8] = 4
M.f[9] = 26
M.f[10] = 1
M.f[11] = 16
M.f[12] = 12
M.f[13] = 5
M.f[14] = 2
M.f[15] = 1
"""Fuente fallecidos por municipios: Medicina Legal (
https://www.medicinalegal.gov.co/documents/20143/49511/Accidentes+De+Transito.pdf) """

# COORDENADAS DE CADA MUNICIPIO (PARA PODER CALCULAR LAS DISTANCIAS ENTRE ELLOS)
M.c = Param(M.i, within=Any, mutable=True)
M.c[1] = (11.160833, -72.591111)
M.c[2] = (10.9575, -72.788611)
M.c[3] = (11.272778, -73.309167)
M.c[4] = (10.896111, -72.885833)
M.c[5] = (10.651944, -72.924167)
M.c[6] = (10.885833, -72.846944)
M.c[7] = (11.064722, -72.761944)
M.c[8] = (10.509722, -73.071944)
M.c[9] = (11.377222, -72.241944)
M.c[10] = (11.7775, -72.445556)
M.c[11] = (11.548056, -72.910278)
M.c[12] = (10.768889, -73.0025)
M.c[13] = (11.714722, -72.265556)
M.c[14] = (10.563056, -73.013333)
M.c[15] = (10.604722, -72.978889)
"""Fuente coordenadas de los municipios: GeoHack (
https://geohack.toolforge.org/geohack.php?language=es&pagename=La_Guajira&params=11_09_39_N_72_35_28_W_ """

# SALARIO DE UN ESPECIALISTA EN URGENCIAS
M.salary = Param(initialize=2500000, within=Any)

# PRESUPUESTO EN PESOS PARA CONTRATAR ESPECIALISTAS EN URGENCIAS
M.budget = Param(initialize=100000000, within=Any)

# FUNCION PARA CALCULAR DISTANCIAS ENTRE MUNICIPIOS
# math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

# NUMEROS DE MEDICOS ASIGNADOS EN MUNIMUPIO i
M.n = Var(M.i, domain=NonNegativeIntegers)

# PROBABILIDAD DE SER ATENTIDO POR ACCIDENTE EN MUNICIPIO Ni, DEPENDE DEL VALOR DE Mi
M.p = Var(M.i, domain=NonNegativeReals)

# FUNCION OBJETIVO
"""La función objetivo busca maximizar el promedio de la probabilidad de ser atendido  a  lo  largo  de  cualquier 
 departamento,  con  el  fin  de  mejorar  la  salud  del departamento.  La  F.O  indica  que  tenemos  que  tener  en 
  cuenta  el  número  de especialistas en urgencias asignado a cada municipio, pues de este valor dependela 
  probabilidad de ser atendido P(Ni) en cada municipio. """
M.obj = Objective(expr=(sum(M.p[i] for i in M.i)), sense=maximize)

# RESTRICCIONES
# ASEGURAR QUE CADA DIA CUMPLE EL MINIMO DE TRABAJADORES REQUERIDOS
"""La restricción 2 tiene el propósito de garantizar que las contrataciones al personal de salud especializado 
nu supere el presupuesto de la gobernación. Esta restricción es importante para solucionar el problema de debido a 
que la gobernaci ón cuenta con un monto limitado con el que debe maximizar su uso para maximizar las probabilidades 
de atención en los accidentes. """
M.expenditure_less_than_budget = Constraint(expr=sum(M.n[i]*M.salary for i in M.i) <= M.budget)

# RESOLVER
SolverFactory('glpk').solve(M)
# MOSTRAR RESULTADO FINAL
M.display()
