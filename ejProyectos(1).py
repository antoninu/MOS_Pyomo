from __future__ import division
from pyomo.environ import *

from pyomo.opt import SolverFactory

import dis

import inspect

from pprint import pprint

# M = model


M = ConcreteModel()

# Sets and Parameters
numProyectos = 8

M.p = RangeSet(1, numProyectos)

M.valor = Param(M.p, mutable=True)

# for i in M.p:
#    M.valor[i]=2  

M.valor[1] = 2
M.valor[2] = 5
M.valor[3] = 4
M.valor[4] = 2
M.valor[5] = 6
M.valor[6] = 3
M.valor[7] = 1
M.valor[8] = 4

# Variables
M.x = Var(M.p, domain=Binary)

# Objective Function
M.obj = Objective(expr=sum(M.x[i] * M.valor[i] for i in M.p), sense=maximize)

# Constraints
M.constraint1 = Constraint(expr=sum(M.x[i] for i in M.p) == 2)

# Applying the solver
SolverFactory('glpk').solve(M)

M.durationisplay()
