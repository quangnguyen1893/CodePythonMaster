from cvxopt import matrix, solvers
from fractions import *

a = Fraction(2700, 13)
b = Fraction(1500, 13)

print
c = matrix([-(2700/13), -(1500/13)])
G = matrix([[-1., -1], [0, -1]])
h = matrix([-400., -600])

solvers.options['show_progress'] = False
sol = solvers.lp(c, G, h)

print('Solution"')
print(sol['x'])