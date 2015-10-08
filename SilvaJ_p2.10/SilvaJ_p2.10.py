import pandas 
import numpy 
import scipy 
import math
import pylab
import matplotlib.pyplot as plt

def multiplicity(q,n): #multiplicity, where n is number of oscillators
    return (math.factorial(q+n-1))/(math.factorial(q)*math.factorial(n-1))

#A represents solid with 200 oscillators
#B represents solid with 100 oscillators

qA= [i+1 for i in xrange(100)] 
qB = [100-i for i in xrange(100)]
omegaA=[float(multiplicity(i,200)) for i in xrange(100)] 
omegaB=[float(multiplicity(100-i,100)) for i in xrange(100)]
omegaTotal=[a*b for a,b in zip(omegaA,omegaB)]

data = {'$q_A$':qA, 
        '$\Omega (N,q_A)$':omegaA,
        '$q_B$':qB,
        '$\Omega (N,q_B)$':omegaB,
        '$\Omega_{total}$':omegaTotal}

table = pandas.DataFrame(data,columns=['$q_A$','$\Omega (N,q_A)$','$q_B$','$\Omega (N,q_B)$', '$\Omega_{total}$'])

print table

#Now, plot results from qA to omegaTotal
plt.plot(qA,omegaTotal)
pylab.savefig('SilvaJ_p2.10_plt.png')

#Most probable macrostate:
maxvalue = max(omegaTotal)
qAprob=omegaTotal.index(maxvalue)
qBprob=100-qAprob

print("The most probable macrostate, qA= %d" % qAprob)
print("The most probable macrostate, qB= %d" % qBprob)

#Probability of this macrostate:
# P = omega(n)/omega(all)

prob= omegaTotal[qAprob]/sum(omegaTotal)
perc_prob = prob*100

print("Probability of most probable macrostate P= %f" % prob )
print("Probability (in percent) of most probable macrostate P= %f" % perc_prob )

#Least probable macrostate:
minvalue = min(omegaTotal)
qAprob_l=omegaTotal.index(minvalue)
qBprob_l=100-qAprob_l

print("The least probable macrostate, qA= %d" % qAprob_l)
print("The least probable macrostate, qB= %d" % qBprob_l)

#Probability of this macrostate:
# P = omega(n)/omega(all)

prob= omegaTotal[qAprob_l]/sum(omegaTotal)

print prob







