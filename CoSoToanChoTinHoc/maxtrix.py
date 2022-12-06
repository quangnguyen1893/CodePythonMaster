import cvxopt
import numpy as np
P = cvxopt.matrix(np.array([[4.0, 0],
                            [0, 2]]))

q = cvxopt.maxtrix(np.array([0.0, 0]))
A = cvxopt.maxtrix(np.array([[1.0], [1]]))
b = cvxopt.maxtrix([1.0])

result = cvxopt.solvers.qp(P, q, A=A, b=b)

