def function(x): 

#Functional form with 0 -a*exp(b(x-c)) terms and 4 -a*tanh(b(x-c)) terms.
#10 total terms with combinations of tanh() and exp() were attempted. 
#Fit had the lowest number of terms within 0.5 percent of the best mean-squared-error. 

 import numpy as np 
 p=[3.97249189e-07,3.97641208e+00,4.57610244e-02,1.82886144e+00,2.83455677e-01,3.40262087e+00,5.54957428e-02,4.72586553e-01,1.00000000e+02,9.97670357e-01,3.33321278e+00,6.63935380e+00,1.29979808e+00] 
 y = p[0]  - p[1] * np.tanh(p[2] * (x - p[3])) - p[4] * np.tanh(p[5] * (x - p[6])) - p[7] * np.tanh(p[8] * (x - p[9])) - p[10] * np.tanh(p[11] * (x - p[12]))
 return y