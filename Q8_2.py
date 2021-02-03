
import utilities as li
#providing eq of ellipse
def f(x,y,z):
    pts=(x**2)/1 + (y**2)/(1.5**2) + (z**2)/(2**2)
    return(pts)
function=f
list=[1,1.5,2]
# call function from utilities
volume,N,Frac=li.M_C_volume(100,list,function)
li.plotting(N,Frac,"step number","fractional error","Fractional error vs step number")
