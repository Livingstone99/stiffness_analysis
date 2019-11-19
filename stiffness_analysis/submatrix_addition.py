# Consistent Mass and stiffness matrices for the beam elements
from sympy import solve_linear_system, Matrix, count_ops,Mul,factor_nc, init_session,init_printing,pprint
element = []
stiffness = []
E = 33.2*10**6#KN/m2
I = 0.2916#m4
## mass matrix for a beam element
m = 2592#kg/
length = [8,3.2,8.8]
for l in length:
    coeff = (m*l)/420
    stiffness_coef = (E*I)/l**3
    mat =coeff * Matrix(([[156, 22*l, 54, -13*l],
                         [22*l, 4*l**2, 13*l,-3*l**2],
                         [54, 13*l, 156, -22*l],
                         [-13*l, -3*l**2, -22*l, 4*l**2]]))
    element.append(mat)
    stiff = stiffness_coef*Matrix(([[12, 6*l, -12, 6*l],
                                    [6*l, 4*l**2, -6*l, 2*l**2],
                                    [-12, -6*l, 12, -6*l],
                                    [6*l, 2*l**2, -6*l, 4*l**2]]))
    stiffness.append(stiff)
print("CONSISTENT MASS MATRIX FOR THE BEAM STRUCTURE")
for matrix, lent in zip(element, length):

    print("-"*100)
    print("Element {} with length {}m".format(element.index(matrix)+1, lent))
    pprint(matrix)
print('*'*500)
print("STIFFNESS MATRIX FOR THE BEAM STRUCTURES")
for matrix, lent in zip(stiffness, length):
    print("-"*100)
    print("Element {} with length {}m".format(stiffness.index(matrix)+1, lent))
    pprint(matrix)

## stiffness matrix

