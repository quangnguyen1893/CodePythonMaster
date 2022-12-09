# Optimization with equality constraints
# Suppose we have a refinery that must ship fnished goods to some storage tanks.
# Suppose further that there are two pipelines, A and B, to do the shipping.
# The cost of shipping x units on A is ax2; the cost of shipping y units on B is by2, where a = 5 and b = 7.
# How can we ship 100 units while minimizing cost.
# a.	Mô hình hoá về bài toán tối ưu
# b.	Giải bài toán trên bằng phương pháp Larange
# c.	Giải bằng thư viện CVXOPT
import cvxopt
import numpy as np
P = cvxopt.matrix(np.array([[10.0, 0.0],[0.0, 14]]))
q = cvxopt.matrix(np.array([0.0, 0]))
A = cvxopt.matrix(np.array([[1.0, 1]]))
b = cvxopt.matrix(100.0)
result = cvxopt.solvers.qp(P, q, A=A, b=b)
y= result['x']
print(y)