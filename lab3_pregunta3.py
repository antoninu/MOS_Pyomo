"""
Antonio Aspite Fermin 201629586
Jose Restom 201514617
"""
# pyomo solve lab3_pregunta3.py --solver='glpk'

from __future__ import division
from pyomo.environ import *

from pyomo.opt import SolverFactory

# MODELO
M = ConcreteModel()

# CONJUNTO
M.i = RangeSet(0, 7)

# PARAMETROS

# ROCK AND ROLL
M.rock = Param(M.i, mutable=True)
M.rock[0] = 0
M.rock[1] = 1
M.rock[2] = 0
M.rock[3] = 1
M.rock[4] = 0
M.rock[5] = 1
M.rock[6] = 0
M.rock[7] = 1

# BLUES ROCK
M.blues = Param(M.i, mutable=True)
M.blues[0] = 1
M.blues[1] = 0
M.blues[2] = 1
M.blues[3] = 0
M.blues[4] = 1
M.blues[5] = 0
M.blues[6] = 0
M.blues[7] = 1

# DURACION
M.duration = Param(M.i, mutable=True)
M.duration[0] = 4
M.duration[1] = 5
M.duration[2] = 3
M.duration[3] = 2
M.duration[4] = 4
M.duration[5] = 3
M.duration[6] = 5
M.duration[7] = 4

# SIN GENERO
M.sg = Param(M.i, mutable=True)
M.sg[0] = 0
M.sg[1] = 0
M.sg[2] = 0
M.sg[3] = 0
M.sg[4] = 0
M.sg[5] = 0
M.sg[6] = 1
M.sg[7] = 0

# VARIABLES
M.lado_a = Var(M.i, domain=Binary)
M.lado_b = Var(M.i, domain=Binary)

# FUNCION OBJETIVO
M.obj = Objective(expr=sum(M.lado_a[i] + M.lado_b[i] for i in M.i), sense=minimize)

# RESTRICCIONES

# Cada canción no puede asignarse a ambos lados
M.ambos_lados_cons1 = Constraint(expr=M.lado_a[0] + M.lado_b[0] <= 1)
M.ambos_lados_cons2 = Constraint(expr=M.lado_a[1] + M.lado_b[1] <= 1)
M.ambos_lados_cons3 = Constraint(expr=M.lado_a[2] + M.lado_b[2] <= 1)
M.ambos_lados_cons4 = Constraint(expr=M.lado_a[3] + M.lado_b[3] <= 1)
M.ambos_lados_cons5 = Constraint(expr=M.lado_a[4] + M.lado_b[4] <= 1)
M.ambos_lados_cons6 = Constraint(expr=M.lado_a[5] + M.lado_b[5] <= 1)
M.ambos_lados_cons7 = Constraint(expr=M.lado_a[6] + M.lado_b[6] <= 1)
M.ambos_lados_cons8 = Constraint(expr=M.lado_a[7] + M.lado_b[7] <= 1)

# Si la canción 2 y 4 están en el lado A, entonces la canción 1 debe estar en el lado B:
M.constraint1 = Constraint(expr=M.lado_a[1] + M.lado_a[3] <= 2 * M.lado_b[0])

# Si la canción 1 está en el lado A, la canción 5 no debe estar en el lado A.
M.constraint2 = Constraint(expr=M.lado_a[0] + M.lado_a[4] <= 1)

# Cada lado debe tener exactamente 2 canciones de Blues:
M.constraint3 = Constraint(expr=sum(M.lado_a[i] * M.blues[i] for i in M.i) == 2)
M.constraint4 = Constraint(expr=sum(M.lado_b[i] * M.blues[i] for i in M.i) == 2)

# El lado A debe tener al menos 3 canciones tipo Rock and Roll:
M.constraint5 = Constraint(expr=sum(M.lado_a[i] * M.rock[i] for i in M.i) >= 3)

# Las canciones de cada lado del cassette deben durar en total entre 14 y 16 minutos:
M.constraint6 = Constraint(expr=sum(M.lado_a[i] * M.duration[i] for i in M.i) >= 14)
M.constraint7 = Constraint(expr=sum(M.lado_a[i] * M.duration[i] for i in M.i) <= 16)
M.constraint8 = Constraint(expr=sum(M.lado_b[i] * M.duration[i] for i in M.i) >= 14)
M.constraint9 = Constraint(expr=sum(M.lado_b[i] * M.duration[i] for i in M.i) <= 16)

# RESOLVER
SolverFactory('glpk').solve(M)
# MOSTRAR RESULTADO FINAL
M.display()
