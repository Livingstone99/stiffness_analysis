## to simplifiy computation and matrix analysis,
## instead of computing the matrix directly, sub-matrices
## were expressed as algebra, so that an expression is obtained
## the package that is responsible for is known as sympy
from sympy import solve_linear_system, Matrix,count_ops,Mul,factor_nc
import sympy as sp

## this are the algebraic expression used as an unknown
## representing the displacements at different time nodes
a, b, c, d = sp.symbols('a b c d')

## the 5x5 matrix was derfined here
# ad = Matrix(([43.40545,28.48027,116.9097,-38.5054,54.4152,2.920781],
#   [5.784294,62.87667,128.8607,-65.5794,111.8554,6.79818],
#   [43.25159,76.95156,213.4786,-86.8678, 133.1502, 7.577213],
#   [-8.60325,-66.378,-117.747,64.62665,-129.661,-6.49153],
#   [8.497068,76.28095,122.9437,-70.798,178.8714,31.72376],
#   [3.195358,32.69512,48.7202,-26.7079,92.99589,29.85679]))
# ad = Matrix(([43.4054521,,89.37228383,-29.43107859,41.58742804,2.232279193],
#              [4.42187235,47.61884673,98.49939683,-50.12837303,85.49130185,5.197293782],
#              [33.06784508,58.82903771,162.7185426,-66.39683246, 101.7619999,5.791834911],
#              [-6.577545234,-50.73497055,-89.99118795,48.95343628,-99.10102548,-4.960590993],
#              [6.495107269,58.30039078,93.95679337,-54.12242812, 136.251602, 24.25306435],
#              [2.441912142,24.98622333,37.22926487,-20.4094036,71.08252381,22.35919964]))


ad = Matrix(([43.40545201,28.48026862,116.9097156,-38.50538787,54.41520412,2.920780601],
             [5.784293927,62.87667231,128.8606613,-65.57941952,111.8553703,6.798179781],
             [43.25159376,76.95155896,213.4785728,-86.86780425, 133.1502364,7.5772127],
             [-8.603250523,-66.37802039,-117.7467845,64.626648,-129.6610589,-6.491532874],
             [8.49706758,76.2809468,122.9437048,-70.79797734, 178.8713702, 31.72376085],
             [3.195357913,32.69512365,48.72020154,-26.70788302,92.99589366,29.85679111]))
## fb holds the identity matrix
fb= Matrix(([1,0,0,0,0,0],
            [0,1,0,0,0,0],
            [0,0,1,0,0,0],
            [0,0,0,1,0,0],
            [0,0,0,0,1,0],
            [0,0,0,0,0,1]))
## ab holds the soution matrix
ab = Matrix(([-0.005561183],
            [0.000201554],
            [-0.00359965],
            [-0.00021756],
            [0.003039968],
            [0.004253913]))

#for the symbol definitions, az, bz and fz
## are the algebraic representation of the
## sub-matrices
az = sp.symbols('az',commutative = False)
bz = sp.symbols('bz',commutative = False)
fz = sp.symbols('fz',commutative = False)

## the gauss jordan elimination method was adopted to
## to find the displacements, the last entry at each row of the matrix
## represents the solution matrix
gen = Matrix(([az, fz, 0, 0,bz],
                [fz,az,fz,0,bz],
                [0,fz,az,fz,bz],
                    [0,0,fz,az,bz]
                   ))

first_solution = []
## sove_linear_system is a method that
## that solves the the variable 'gen'
## using gauss elimination
answer = solve_linear_system(gen,a,b,c,d)
for values in answer.values():
    first_solution.append(values)
# print('yeap',first_solution)
disolved = []
dft = []
done = []
## at this point the algebraic expression of each solution matrices has beeen obtained
## to simplify the algebraic expressions because they were to complicated...
## solute.simplify().as_numer_denom() simplifies the expression in a simpler
## couldn't be processed
for solute in first_solution:
    disolved.append(zip(solute.simplify().as_numer_denom(),(1,-1)))
for dissolved in disolved:
    dft.append(Mul(*[factor_nc(b)**e for b,e in dissolved]))

## 'dff.subs({az:ad,fz:fb,bz:ab},simultaneous = True).doit())' with
##  this code, the algebraic expresssions were substituted for
## matrice
for dff in dft:
    done.append(dff.subs({az:ad,fz:fb,bz:ab},simultaneous = True).doit())
count = 0
## the result were printed out
## with this for loop
##
for true in done:
    count +=1
    print('solution', count,'#'*100)
    print(true)

## end
