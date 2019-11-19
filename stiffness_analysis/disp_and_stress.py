## Displacements and stresses within the beam structure
from sympy import solve_linear_system, Matrix, count_ops,Mul,factor_nc
import sympy as sp
x, l = sp.symbols('x l')
wx = Matrix(([[(1 - ((3*x**2)/l**2)+((2*x**3)/l**3)),(x-((2*x**2)/l)+(x**3)/l**2),
               (((3*x**2)/l**2)-(2*x**3)/l**3), (((-x**2)/l)+(x**3)/l**2)] ]))

# at 0m
# wx = 0
w = 0
def displacement(xx,ll):
    global w
    w = w+1
    solution = wx.subs({x: xx, l: ll})
    if ll==8:
        disp = Matrix(([0], [-0.00131], [-0.00686], [-0.000321]))
    elif ll == 3.2:
        disp = Matrix(([-0.00686],[-0.000321],[-0.00708],[0.000192]))
    elif ll == 8.8:
        disp = Matrix(([-0.00708],[0.000192],[0],[0.00131]))
    else:
        pass
    solution1 = solution * disp
    print(' '*100)
    print('displacement @ {}m within element of length {}m'.format(xx, ll), solution1)
# at 2m, 4m and 8m(within element 1 L=8m)
dist = [2,4,6,8]
for i in dist:
    displacement(i,8)
## at 10m(within element 2 L = 3.2m) '
displacement(2,3.2)
## at 0.8m(within element 3 l = 8.3m)
dsipp = [0.8,2.8,4.8,6.8]
for i in dsipp:
    displacement(i,8.8)
## stress at nodal point

E = 33.2*10**6#KN/m2
I = 0.2916#m4
disp3 = Matrix(([-0.00708],[0.000192],[0],[0.00131]))
disp = Matrix(([0],[-0.00131],[-0.00686],[-0.000321]))
disp1 = Matrix(([-0.00686], [-0.000321], [-0.00708], [0.000192]))
# at 0m in the 1st beam element
lz = 8
stress = E*I/lz**2
matri_0 = Matrix(([6,4*lz,-6,2*lz]))
matri_011 = matri_0
matri_01 = matri_0.reshape(1,4)
print(" "*100)
# print('Nodal stress of the beam WRT nodal displacement at {}m '.format(lz), matri_01,matri_01.shape)
# at 8m
stress0 = stress*matri_01
# print(stress0,'\n',disp,disp.shape,'\n', matri_01,matri_01.shape)
ans1 =stress0*disp
print(" "*100)
print('nodal stress @ point 0',ans1 )
matri_1 = Matrix(([-6,-2*lz,6,-4*lz]))
stress1 = (stress*matri_1).reshape(1,4)

ans2=stress1* disp
print(" "*100)
print('corect at this point nodal stress @ point L', ans2)

#@ 14m
lz = 8.8#m
disp2 = Matrix(([-0.00708],[0.0001925],[0],[0.00131]))
matri_1 = Matrix(([-6,-2*lz,6,-4*lz]))
stressz = E*I/lz**2
stress0 = (stressz*matri_1).reshape(1,4)

ans2=stress0* disp2
print(" "*100)
print('nodal stress @ point 20m', ans2)

## internal stress with respect to the beam
flexuaral_rigidity  = E * I
length = [8,3.2, 8.8 ]

lz = 8#m
xx = [2, 4, 6]#metres
for lz in length:
    if lz == 8:
        print(" " * 100)
        print("internal stress for {}".format(lz))
        print("-" * 100)
        for x in xx:
            stress_eqn = Matrix(([(6/(lz**2))-(12*x)/(lz**3), 4/lz-6*x/(lz**2),(-(6/lz**2)+((12*x)/(lz**3))), (2/lz)-((6*x)/(lz**2))]))
            qwdd = (flexuaral_rigidity*stress_eqn).reshape(1,4)
            qwd = qwdd*disp
            print("stress analysis at {}m within element{}m".format(x, lz), qwd)
    if lz == 3.2:
        print(" " * 100)
        print("internal stress for {}".format(lz))
        print("-" * 100)
        xx = [2]
        for x in xx:
            stress_eqn = Matrix(([(6/(lz**2))-(12*x)/(lz**3), 4/lz-6*x/(lz**2),(-(6/lz**2)+((12*x)/(lz**3))), (2/lz)-((6*x)/(lz**2))]))
            qwdd = (flexuaral_rigidity*stress_eqn).reshape(1,4)
            qwd = qwdd*disp1
            print("stress analysis at {}m within element{}m".format(x, lz), qwd)

    if lz == 8.8:

        print(" "*100)
        print("internal stress for {}".format(lz))
        print("-"*100)
        xx = [0.8]#meteres
        for x in xx:
            stress_eqn = Matrix(([(6/(lz**2))-(12*x)/(lz**3), 4/lz-6*x/(lz**2),(-(6/lz**2)+((12*x)/(lz**3))), (2/lz)-((6*x)/(lz**2))]))
            qwdd = (flexuaral_rigidity*stress_eqn).reshape(1,4)
            qwd = qwdd*disp2
            print("stress analysis at {}m within element {}m".format(x, lz), qwd)

##VERTICAL DISPLACEMENT COMPUTATION
# print(vertical_displacement_matr.shape, vertical_displacement_matr)
nodal = Matrix(([0], [0.00021], [0.00243], [0.000167]))
nodal1 = Matrix(([0.00243], [0.000167],[0.00254], [-0.0000988]))
nodal2 = Matrix(([0.00254], [-0.00000988], [0], [-0.000216]))
# wx = Matrix(([[(1 - ((3 * x ** 2) / l ** 2) + ((2 * x ** 3) / l ** 3)), (x - ((2 * x ** 2) / l) + (x ** 3) / l ** 2),
#        (((3 * x ** 2) / l ** 2) - (2 * x ** 3) / l ** 3), (((-x ** 2) / l) + (x ** 3) / l ** 2)]])).reshape(1, 4)

element_length = [8,3.2,8.8]#m
for l in element_length:
    print("-" * 100)
    if l == 8:

        xx =  [0, 2, 4, 6,8]#metres
        for x in xx:
            wx = Matrix((  [[(1 - ((3 * x ** 2) / l ** 2) + ((2 * x ** 3) / l ** 3)), (x - ((2 * x ** 2) / l) + (x ** 3) / l ** 2),
                  (((3 * x ** 2) / l ** 2) - (2 * x ** 3) / l ** 3), (((-x ** 2) / l) + (x ** 3) / l ** 2)]])).reshape( 1, 4)
            bert_dis= wx*nodal
            print(" "*100)
            print("vertical displacement at {}m within the element of {}m length".format(x, l), bert_dis )
    elif l ==3.2:
        x = 2#meters within element 2
        wx = Matrix(([[(1 - ((3 * x ** 2) / l ** 2) + ((2 * x ** 3) / l ** 3)), (x - ((2 * x ** 2) / l) + (x ** 3) / l ** 2),
               (((3 * x ** 2) / l ** 2) - (2 * x ** 3) / l ** 3), (((-x ** 2) / l) + (x ** 3) / l ** 2)]])).reshape(1,4)
        bert_dis = wx * nodal1
        print(" " * 100)
        print("vertical displacement at {}m within the element of {}m length".format(x, l), bert_dis)
    elif l == 8.8:
        xx = [0.8, 2.8,4.8, 6.8,8.8]
        for x in xx:
            wx = Matrix((  [[(1 - ((3 * x ** 2) / l ** 2) + ((2 * x ** 3) / l ** 3)), (x - ((2 * x ** 2) / l) + (x ** 3) / l ** 2),
                  (((3 * x ** 2) / l ** 2) - (2 * x ** 3) / l ** 3), (((-x ** 2) / l) + (x ** 3) / l ** 2)]])).reshape( 1, 4)
            bert_dis= wx*nodal2
            print(" "*100)
            print("vertical displacement at {}m within the element of {}m length".format(x, l), bert_dis )

## Nodal stresses of beam element in relation to the nodal dispacements
nod_dis = Matrix(([0], [0.00021], [0.00243], [0.000167]))
nod_dis1 = Matrix(([0.00254], [-0.0000988], [0], [-0.000216]))
print("-" * 100)
asx = stress*matri_01
asxx = asx*nod_dis
print(" "*100)
print("Nodal stress at 0m node 1", asxx)
lz = 8#m
matri_1 = Matrix(([-6,-2*lz,6,-4*lz]))
asx = stress*matri_1.reshape(1,4)
asxx = asx*nod_dis
print(" "*100)
print("Nodal stress at 8m node 1", asxx)


lz = 8.8#m
stress = E*I/lz**2
matri_1 = Matrix(([-6,-2*lz,6,-4*lz]))
asx = stress*matri_1.reshape(1,4)
asxx = asx*nod_dis1
print("-" * 100)
print(" "*100)
print("Nodal stress at 8m node 1", asxx)


## internal stress within the beam element in relation to the nodal displacement

inter_disp = Matrix(([0], [0.00021], [0.00243], [0.000167]))
inter_disp1 = Matrix(([0.00243], [0.000167], [0.00254], [-0.0000988]))
inter_disp2 = Matrix(([0.00254], [-0.0000988], [0], [-0.000216]))
# element_length = [8, 3.2, 8.8]

for lz in element_length:
    print("-" * 100)
    if  lz==8:
        xz =  [2, 4, 6]#metres

        for x in xz:
            stress_eqnn = Matrix(([(6 / (lz ** 2)) - (12 * x) / (lz ** 3), 4 / lz - 6 * x / (lz ** 2),
                                   (-(6 / lz ** 2) + ((12 * x) / (lz ** 3))), (2 / lz) - ((6 * x) / (lz ** 2))]))
            ans = ((flexuaral_rigidity * stress_eqnn).reshape(1, 4))*inter_disp
            print(" " * 100)
            print("Internal stress, {}m within element {} of length {}m".format(x, element_length.index(lz)+1, lz), ans)

    elif lz == 3.2:
        x = 2#m
        stress_eqnn = Matrix(([(6 / (lz ** 2)) - (12 * x) / (lz ** 3), 4 / lz - 6 * x / (lz ** 2),
                               (-(6 / lz ** 2) + ((12 * x) / (lz ** 3))), (2 / lz) - ((6 * x) / (lz ** 2))]))
        ans = ((flexuaral_rigidity * stress_eqnn).reshape(1, 4)) * inter_disp1
        print(" " * 100)
        print("Internal stress, {}m within element {} of length {}m".format(x, element_length.index(lz)+1, lz), ans)
    elif lz == 8.8:
        xz = [0.8,2.8,4.8,6.8]#m
        for x in xz:
            stress_eqnn = Matrix(([(6 / (lz ** 2)) - (12 * x) / (lz ** 3), 4 / lz - 6 * x / (lz ** 2),
                                   (-(6 / lz ** 2) + ((12 * x) / (lz ** 3))), (2 / lz) - ((6 * x) / (lz ** 2))]))
            ans = ((flexuaral_rigidity * stress_eqnn).reshape(1, 4)) * inter_disp2
            print(" "*100)
            print("Internal stress, {}m within element {} of length {}m".format(x, element_length.index(lz)+1, lz), ans)

## VERTICAL DISPLACEMENT WITHIN THE BEAM ELEMENT IN RELATION TO ITS NODAL DISPLACEMENT
nodal_disp = Matrix(([0], [0.000476], [0.00391], [0.000228]))
nodal_disp1 = Matrix(([0.00391], [0.000228], [0.00405], [-0.000141]))
nodal_disp2 = Matrix(([0.00405], [-0.000141], [0], [-0.000474]))
for l in element_length:
    print("-" * 100)
    if l == 8:

        xx =  [0, 2, 4, 6,8]#metres
        for x in xx:
            wx = Matrix((  [[(1 - ((3 * x ** 2) / l ** 2) + ((2 * x ** 3) / l ** 3)), (x - ((2 * x ** 2) / l) + (x ** 3) / l ** 2),
                  (((3 * x ** 2) / l ** 2) - (2 * x ** 3) / l ** 3), (((-x ** 2) / l) + (x ** 3) / l ** 2)]])).reshape( 1, 4)
            bert_dis= wx*nodal_disp
            print(" "*100)
            print("vertical displacement at {}m within element {} of {}m length".format(x, element_length.index(l), l),
                  bert_dis)
    elif l ==3.2:
        x = 2#meters within element 2
        wx = Matrix(([[(1 - ((3 * x ** 2) / l ** 2) + ((2 * x ** 3) / l ** 3)), (x - ((2 * x ** 2) / l) + (x ** 3) / l ** 2),
               (((3 * x ** 2) / l ** 2) - (2 * x ** 3) / l ** 3), (((-x ** 2) / l) + (x ** 3) / l ** 2)]])).reshape(1,4)
        bert_dis = wx * nodal_disp1
        print(" " * 100)
        print("vertical displacement at {}m within element {} of {}m length".format(x, element_length.index(l), l), bert_dis )
    elif l == 8.8:
        xx = [0.8, 2.8,4.8, 6.8,8.8]
        for x in xx:
            wx = Matrix((  [[(1 - ((3 * x ** 2) / l ** 2) + ((2 * x ** 3) / l ** 3)), (x - ((2 * x ** 2) / l) + (x ** 3) / l ** 2),
                  (((3 * x ** 2) / l ** 2) - (2 * x ** 3) / l ** 3), (((-x ** 2) / l) + (x ** 3) / l ** 2)]])).reshape( 1, 4)
            bert_dis= wx*nodal_disp2
            print(" "*100)
            print("vertical displacement at {}m within element {} of {}m length".format(x, element_length.index(l), l), bert_dis )

## Nodal stresses of the beam element in relation to the nodal displacements
## 0.4 and 1.0s is represented as
disp_nodal = Matrix(([0], [0.000476], [0.00391], [0.000228]))
disp_nodal1 = Matrix(([0.00405],[-0.000141],[0], [-0.000474]))
lz = 8
matri_0 = Matrix(([6,4*lz,-6,2*lz]))
matri_1 = Matrix(([-6,-2*lz,6,-4*lz]))
stressw = E*I/lz**2
anss = (stressw*matri_0).reshape(1,4)
ansz = anss*disp_nodal
print("At 0m nodal 1(where L = 8m)",ans2)
anss2 = (stressw*matri_1).reshape(1,4)
ansz2  = anss2 *disp_nodal
print("At 8m nodal 2(where L = 8m)",ansz2)

lz = 8.8
matri_1 = Matrix(([-6,-2*lz,6,-4*lz]))
stressw = E*I/lz**2
anss3 = (stressw*matri_1).reshape(1,4)
ansz3 = anss3*disp_nodal1
print("At 20m nodal 4(where L = 8.8m)",ansz3)

# internal stressses within the beam element in relation to the nodal displacements
disp_fin = Matrix(([0], [0.000561], [0.00443], [0.000253]))
disp_fin1 = Matrix(([0.00443], [0.000253], [0.00458],[-0.000161]))
disp_fin2 = Matrix(([0.00458], [-0.000161], [0], [-0.000552]))


for lz in element_length:
    print("-" * 100)
    if  lz==8:
        xz =  [2, 4, 6]#metres

        for x in xz:
            stress_eqnn = Matrix(([(6 / (lz ** 2)) - (12 * x) / (lz ** 3), 4 / lz - 6 * x / (lz ** 2),
                                   (-(6 / lz ** 2) + ((12 * x) / (lz ** 3))), (2 / lz) - ((6 * x) / (lz ** 2))]))
            ans = ((flexuaral_rigidity * stress_eqnn).reshape(1, 4))*disp_fin
            print(" " * 100)
            print("Internal stress, {}m within element {} of length {}m".format(x, element_length.index(lz)+1, lz), ans)

    elif lz == 3.2:
        x = 2#m
        stress_eqnn = Matrix(([(6 / (lz ** 2)) - (12 * x) / (lz ** 3), 4 / lz - 6 * x / (lz ** 2),
                               (-(6 / lz ** 2) + ((12 * x) / (lz ** 3))), (2 / lz) - ((6 * x) / (lz ** 2))]))
        ans = ((flexuaral_rigidity * stress_eqnn).reshape(1, 4)) * disp_fin1
        print(" " * 100)
        print("Internal stress, {}m within element {} of length {}m".format(x, element_length.index(lz)+1, lz), ans)
    elif lz == 8.8:
        xz = [0.8,2.8,4.8,6.8]#m
        for x in xz:
            stress_eqnn = Matrix(([(6 / (lz ** 2)) - (12 * x) / (lz ** 3), 4 / lz - 6 * x / (lz ** 2),
                                   (-(6 / lz ** 2) + ((12 * x) / (lz ** 3))), (2 / lz) - ((6 * x) / (lz ** 2))]))
            ans = ((flexuaral_rigidity * stress_eqnn).reshape(1, 4)) * disp_fin2
            print(" "*100)
            print("Internal stress, {}m within element {} of length {}m".format(x, element_length.index(lz)+1, lz), ans)
