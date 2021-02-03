
import matplotlib.pyplot as plt
import math as m
import utilities as li
R=[]
N=[]
r=[250,750,1050,1550,2050]
# plotting R vs square root of N
for i in r:
    X,Y,R_,Dx,Dy,R_avg=li.random_walk(i)
    R.append(R_)
    N.append(m.sqrt(i))
    print(i,"steps")
    print("avg displacement in x direction",Dx)
    print("avg displacement in y direction",Dy)
    print("R=",R_avg)

    print("Rrms",R_)
li.plotting(R,N,r'$\sqrt{N}$',r'$R_{rms}$',"Rrms vs square root(N)")

# output:
# 250 steps
# avg displacement in x direction 0.5334461187660261
# avg displacement in y direction -0.5335574045505337
# R= 13.93680407100246
# Rrms 15.431652885674309
# 750 steps
# avg displacement in x direction -0.25327832598728195
# avg displacement in y direction 1.7363015686295775
# R= 22.97140409388281
# Rrms 26.026832726273607
# 1050 steps
# avg displacement in x direction -0.1882566701390237
# avg displacement in y direction -0.477666164861248
# R= 26.997680580475663
# Rrms 30.251922997580653
# 1550 steps
# avg displacement in x direction 3.2387862015005315
# avg displacement in y direction 0.29476762740118584
# R= 32.98919628411535
# Rrms 37.21796401706004
# 2050 steps
# avg displacement in x direction 0.2639066256053304
# avg displacement in y direction -2.7308426596828177
# R= 37.96637948775465
# Rrms 42.687311915187536
