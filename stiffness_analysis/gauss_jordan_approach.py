from sympy import solve_linear_system, Matrix,count_ops,Mul,factor_nc
import sympy as sp

a, b, c, d, e,f = sp.symbols('a b c d e f')

ad = Matrix(([43.40545,28.48027,116.9097,-38.5054,54.4152,2.920781],
  [5.784294,62.87667,128.8607,-65.5794,111.8554,6.79818],
  [43.25159,76.95156,213.4786,-86.8678, 133.1502, 7.577213],
  [-8.60325,-66.378,-117.747,64.62665,-129.661,-6.49153],
  [8.497068,76.28095,122.9437,-70.798,178.8714,31.72376],
  [3.195358,32.69512,48.7202,-26.7079,92.99589,29.85679]))

fb= Matrix(([1,0,0,0,0,0],
            [0,1,0,0,0,0],
            [0,0,1,0,0,0],
            [0,0,0,1,0,0],
            [0,0,0,0,1,0],
            [0,0,0,0,0,1]))
# fb = 1
ab = Matrix(([-0.0055612],
            [0.00020155],
            [-0.00366],
            [-0.0002176],
            [0.00303997],
            [0.00425391]))

#for the symbol definitions
az = sp.symbols('az',commutative = False)
bz = sp.symbols('bz',commutative = False)
fz = sp.symbols('fz',commutative = False)

gen = Matrix(([az, fz, 0, 0, 0, 0,bz],
                [fz,az,fz,0,0,0,bz],
                [0,fz,az,fz,0,0,bz],
                    [0,0,fz,az,fz,0,bz],
                    [0,0,0,fz,az,fz,bz],
                    [0,0,0,0,fz,az,bz]))
first_solution = []
answer = solve_linear_system(gen,a,b,c,d,e,f)
for values in answer.values():
    first_solution.append(values)
# print('yeap',first_solution)
disolved = []
dft = []
done = []

## to simplify the algebraic expressions because they were to complicated... hence,
## couldn't be processed
for solute in first_solution:
    disolved.append(zip(solute.simplify().as_numer_denom(),(1,-1)))
for dissolved in disolved:
    dft.append(Mul(*[factor_nc(b)**e for b,e in dissolved]))


for dff in dft:
    done.append(dff.subs({az:ad,fz:fb,bz:ab},simultaneous = True).doit())
count = 0
for true in done:
    count +=1
    print('solution', count,'#'*100)
    print(true)

#
