from sympy import*
import pprint
import numpy as np
# import theano as th

az = Matrix([[43.4,26.5,115,-40.5,52.4,0.921],
  [3.78,62.9,127,-67.6,110,4.80],
  [41.25,75.0,213,-88.9, 131, 5.88],
  [-10.6,-68.4,-120,64.6,-132,-8.49],
  [6.5,74.3,121,-72.8,179,29.7],
  [1.2,30.7,49.7,-28.7,91,29.9]])

aa = Symbol('aa')
gen = Matrix([[aa, 1, 0, 0, 0, 0],
                [1,aa,1,0,0,0],
                [0,1,aa,1,0,0],
                    [0,0,1,aa,1,0],
                    [0,0,0,1,aa,1],
                    [0,0,0,0,1,aa]])

inverse_genn = gen**-1
print(inverse_genn)
inverse_gen = simplify(inverse_genn)

# ad = Matrix(([43.40545201,28.48026862,116.9097156,-38.50538787,54.41520412,2.920780601],
#              [5.784293927,62.87667231,128.8606613,-65.57941952,111.8553703,6.798179781],
#              [43.25159376,76.95155896,213.4785728,-86.86780425, 133.1502364,7.5772127],
#              [-8.603250523,-66.37802039,-117.7467845,64.626648,-129.6610589,-6.491532874],
#              [8.49706758,76.2809468,122.9437048,-70.79797734, 178.8713702, 31.72376085],
#              [3.195357913,32.69512365,48.72020154,-26.70788302,92.99589366,29.85679111]))
print('inverse',inverse_gen)
bz = Matrix([[2],
            [3],
            [3],
            [4],
            [5],
            [5]])
bzz = Matrix([[bz],[bz],[bz],[bz],[bz],[bz]])
solution = inverse_genn*bzz
print('shape',solution.shape )
print('a*b',solution)
_1st_displacement = simplify(solution[0][0])
# s = _1st_displacement.simplify()
# print(count_simplify(s))

_1st_solution = _1st_displacement.subs({aa:az},simultaneous = True).doit()
# print('type',solution[0].shape)
# print('solution',_1st_displacement)
# print('solved', _1st_solution)
# print('##'*100)
# print('displacement matrix', solution, len(solution[0]))
soluty = []
solved = []

for i in solution[0]:
    soluty.append(Matrix([simplify(i)]))
for i in soluty:
    solved.append(i.subs({aa:az},simultaneous = True,).doit())
print('soloi',solved[0])
simmp = simplify(solved[0])
print('at the end',simmp)