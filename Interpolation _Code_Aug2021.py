# Python libraries 
from numpy import arange
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz
import numpy
import math
import pandas as pd

# importing data from file
data = pd.read_csv("/home/cebo/Desktop/Cross Sections/208Pb.dat",names=["Col1","Col2","Col3"],sep="\t")    
x = data["Col1"]   # Gamma Energy [MeV]
y = data["Col2"]   # Cross section data [mb]
dy = data["Col3"]  # Uncertainty of cross section data [mb]


###################################### INTERPOLATION & INTEGRATION ###########################################

f = interp1d(x,y,kind = 'cubic')            ## Cubic spline interpolation
g = interp1d(x,dy,kind = 'cubic')

xint = np.arange(min(x),max(x),0.01)     ## Integration range
yint = f(xint)                           ## Interpolationg function
yint2 = f(xint)/(xint**2)			     ## sigma(-2) integrand [mb/MeV]

gyint = g(xint)
gyint2 = g(xint)/(xint**2)                  


with open("output_data.dat", "w") as out_file:  ## Saving interpolation data
    for i in range(len(xint)):
       output_string = ""
       output_string += str(xint[i])
       output_string += " " + str(yint[i])
       output_string += "\n"
       out_file.write(output_string)


## COMPOSITE TRAPEZOIDAL RULE INTEGRATION

a = numpy.trapz(yint,xint,axis = 0)           ## Total crossection integral
b = numpy.trapz(yint2,xint,axis = 0)          ## sigma(-2) value calculation [mb/MeV]
c = (numpy.trapz(gyint2,xint,axis =0))        ## Error E1_sigma(-2)


print("REPORTING INTEGRALS")
print("Raw_Total_sig: ",     a ,"mb-MeV")     ### The total Integral
print("(-2)sig           : ", b ,"mb/MeV")    ### (-2)sigma value
print("(-2)sig_Error     : ", c ,"mb/MeV")


###################################### PLOTS FOR VISUALISATION ####################################################

plt.plot(x,y,'s',c='b',label = r'$\sigma(\gamma,n)$') 
plt.plot(xint,yint,'-',c='r',label='interpolant')
#plt.plot(x,dy,'*',c='y')

plt.xlabel('Energy [MeV]')
plt.ylabel('Photo-nuclear Cros-section [mb]')
#plt.title()

plt.legend(loc='upper right', bbox_to_anchor=(0.95, 1))

plt.show()

#//////////////////////////////////////////// END ///////////////////////////////////////////////////////////////////#

