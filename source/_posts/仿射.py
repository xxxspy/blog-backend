import sympy
x1, x2, x3, y1, y2, y3, z1, z2, z3 = sympy.symbols(
    'x1,x2,x3,y1,y2,y3,z1,z2,z3')
theta = sympy.Symbol('theta')

x = sympy.Matrix([x1, x2, x3])
y = sympy.Matrix([y1, y2, y3])
z = theta * x + (1-theta)*y

xz = z-x
yz = z-y
print(xz)
print(yz)

