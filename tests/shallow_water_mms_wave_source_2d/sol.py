# This file was *autogenerated* from the file sol.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_0p0 = RealNumber('0.0'); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
t = var('t')
x = var('x')
y = var('y')
c = var('c')
k = var('k')
g = var('g') # gravity
H = var('H') # depth
a = _sage_const_0 
b = _sage_const_1 

eta = -c * sin(k*x+t)
u_x = c * sin(k*x+t)
u_y = _sage_const_0p0 

print "u_x: ", u_x
print "u_y: ", u_y
print "eta: ", eta
print "mom source x: ", g*diff(eta, x) + diff(u_x, t)
print "mom source y: ", g*diff(eta, y) + diff(u_y, t)
print "cont source: ", diff(eta, t) + diff(H*u_x, x) + diff(H*u_y, y)
