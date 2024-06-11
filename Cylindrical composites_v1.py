import numpy as np


L = float(input("length of composite structure:  "))
Ni = int(input("Number of Layers: "))
N = int (Ni + 1)
Tc = float(input("temperature at core: "))
Ta = float(input("Ambience temperature: "))
ho = float(input("thermal conductivity of fluid in ambience: "))

Rx = []
k =  []
for g in range(0,N,1):
    if g == 0:
        Radius = float(input(f"radius of  fluid-cylinder: "))
        ki = float(input(f"Thermal conductivity or h of fluid: "))
    else: 
        Radius = float(input(f"Insulation radius of cylinder {g}: "))
        ki = float(input(f"Thermal conductivity of insulation {g} : "))   
    Rx.append(Radius)
    k.append(ki)

#calculation 
w1 = float((Tc-Ta)*2*3.14*L)
w4 = float((1/(k[0]*Rx[0])) + (1/(ho*Rx[N-1])))
w3 = [w4]
for gx in range(0,N-1,1):
    w2 = (np.log(Rx[gx+1]/Rx[gx]))/k[gx+1]
    w3.append(w2)
    print(w2)
value = sum(w3)
#print(w4,value)
#print(Rx,k)


Q = float(w1/value)
print(w1,Q)
