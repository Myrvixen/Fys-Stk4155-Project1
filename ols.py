import numpy as np
from cls_reg import LinReg
from Franke import FrankeFunction
import matplotlib.pylab as plt
import plotparams

N = 1000
degrees = range(9)
#degrees = [5]

x = np.random.uniform(0, 1, (N, 1))
y = np.random.uniform(0, 1, (N, 1))
noise = 0.5*np.random.randn(N, 1)
z = FrankeFunction(x, y) + noise

print("OLS REGRESSION")
print("| Degree | MSE Train | MSE Test |  R2 Train | R2 Test |")
print("="*55)
for i in range(len(degrees)):

    a = LinReg(x, y, z, degrees[i])

    beta = a.ols(a.XY_Train, a.z_Train)
    zpred_train = a.XY_Train @ beta
    zpred_test = a.XY_Test @ beta

    mse_train = a.MSE(a.z_Train, zpred_train)
    mse_test = a.MSE(a.z_Test, zpred_test)
    r2_train  = a.R2(a.z_Train, zpred_train)
    r2_test  = a.R2(a.z_Test, zpred_test)

    print("|%8i|%11f|%10f|%10f|%10f|" % \
        (degrees[i], mse_train, mse_test, r2_train, r2_test))
    #print("-"*75)
