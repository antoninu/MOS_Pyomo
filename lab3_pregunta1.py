"""
Antonio Aspite Fermin 201629586
Jose Restom 201514617
"""
# pyomo solve lab3_pregunta1.py --solver='glpk'

from __future__ import division
from pyomo.environ import *

from pyomo.opt import SolverFactory

# MODELO
Model = ConcreteModel()

# SETS & PARAMETERS********************************************************************
numCiudades = 6

N = RangeSet(1, numCiudades)

cost = {(1, 1): 0, (1, 2): 10, (1, 3): 20, (1, 4): 30, (1, 5): 30, (1, 6): 20,
        (2, 1): 10, (2, 2): 0, (2, 3): 25, (2, 4): 35, (2, 5): 20, (2, 6): 10,
        (3, 1): 20, (3, 2): 25, (3, 3): 0, (3, 4): 15, (3, 5): 30, (3, 6): 20,
        (4, 1): 30, (4, 2): 35, (4, 3): 15, (4, 4): 0, (4, 5): 15, (4, 6): 25,
        (5, 1): 30, (5, 2): 20, (5, 3): 30, (5, 4): 15, (5, 5): 0, (5, 6): 14,
        (6, 1): 20, (6, 2): 10, (6, 3): 20, (6, 4): 25, (6, 5): 14, (6, 6): 0}

# VARIABLES****************************************************************************
Model.x = Var(N, N, domain=Binary)

# OBJECTIVE FUNCTION*******************************************************************
Model.obj = Objective(expr=sum(Model.x[i, j] for i in N for j in N))

# CONSTRAINTS**************************************************************************
Model.rest1 = Constraint(expr=sum(Model.x[i, j] for i in N for j in N if cost[i, j] <= 15) >= 1)

# RESOLVER
SolverFactory('glpk').solve(Model)

# MOSTRAR RESULTADO FINAL
Model.display()
