
from bayes import *
from genotype import *

from rose import *
from tulip import *
from pansy import *
from cosmos import *
from lily import *
from hyacinth import *
from windflower import *
from mum import *

w0 = RoseSeedWhite
y0 = RoseSeedYellow
r0 = RoseSeedRed

w1 = (w0 *w0)
p0 = w1.Pick(   PickColor( Color.PURPLE))
#print( w1)
#print( p0)

print(" yellow x red ")
y1 = (y0 *y0).Pick( PickColor( Color.YELLOW))
r0y1 = (r0 *y1)
print( r0y1)
o0 = r0y1.Pick( PickColor( Color.ORANGE))
print( o0)

print(" black x orange ")
k0 = (r0 *r0).Pick( PickColor( Color.BLACK))
print( k0)
ok1 = (o0 *k0).Pick( PickColor( Color.ORANGE))
print( ok1)
ok2 = (ok1 *k0).Pick( PickColor( Color.ORANGE))
print( ok2)

print(" orange x orange ")
oo1 = (o0 *o0).Pick( PickColor( Color.ORANGE))
print( oo1)

print(" purple x black ")
kp1 = (p0 *k0)
print( kp1)
kp2 = (p0 *kp1).Pick( PickColor( Color.RED))
print( kp2)

print(" purple x yellow ")
py1 = (p0 *y1)
print( py1)
py2 = (p0 *py1).Pick( PickColor( Color.PURPLE))
print( py2)

#child_colors = [Color.PURPLE]
#child_colors = [Color.PURPLE,Color.PURPLE]
child_colors = [Color.PURPLE,Color.PURPLE,Color.PURPLE]
#child_colors = [Color.PURPLE,Color.WHITE]
parent0,parent1 = py2,py2

parents = parent0.Concatenate( parent1)
parentx = BreedOutcome( parent0, parent1, child_colors)
print( parents)
print( parentx)

