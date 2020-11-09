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

# DIAS DE LA SEMANA
M.i = RangeSet(1, 7)

# DEMANDA POR DIA
M.d = Param(M.i, mutable=True)
M.d[1] = 17
M.d[2] = 13
M.d[3] = 15
M.d[4] = 19
M.d[5] = 14
M.d[6] = 16
M.d[7] = 11

# EL NUMERO DE TRABAJADORES QUE EMPIEZA A TRABAR EN EL DIA X Y TERMINA 5 DIAS DESPUES
M.x = Var(M.i, domain=NonNegativeReals)
M.x[1] = 0
M.x[2] = 0
M.x[3] = 0
M.x[4] = 0
M.x[5] = 0
M.x[6] = 0
M.x[7] = 0

# FUNCION OBJETIVO
M.obj = Objective(expr=sum(M.x[i] for i in M.i), sense=minimize)

# RESTRICCIONES
# ASEGURAR QUE CADA DIA CUMPLE EL MINIMO DE TRABAJADORES REQUERIDOS
M.lunes = Constraint(expr=M.x[1] + M.x[4] + M.x[5] + M.x[6] + M.x[7] >= M.d[1])
M.martes = Constraint(expr=M.x[1] + M.x[2] + M.x[5] + M.x[6] + M.x[7] >= M.d[2])
M.miercoles = Constraint(expr=M.x[1] + M.x[2] + M.x[3] + M.x[6] + M.x[7] >= M.d[3])
M.jueves = Constraint(expr=M.x[1] + M.x[2] + M.x[3] + M.x[4] + M.x[7] >= M.d[4])
M.viernes = Constraint(expr=M.x[1] + M.x[2] + M.x[3] + M.x[4] + M.x[5] >= M.d[5])
M.sabado = Constraint(expr=M.x[2] + M.x[3] + M.x[4] + M.x[5] + M.x[6] >= M.d[6])
M.domingo = Constraint(expr=M.x[3] + M.x[4] + M.x[5] + M.x[6] + M.x[7] >= M.d[7])

# RESOLVER
SolverFactory('glpk').solve(M)
# MOSTRAR RESULTADO FINAL
M.display()
