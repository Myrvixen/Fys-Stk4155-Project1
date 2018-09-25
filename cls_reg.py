import numpy as np
import scipy.linalg as scl
from sklearn.preprocessing import PolynomialFeatures
from Franke import FrankeFunction
from sklearn.linear_model import LinearRegression, RidgeCV, Lasso

class LinReg:
    def __init__(self, x, y, z, deg):

        self.x = x
        self.y = y
        self.z = z
        self.deg = deg
        self.N = x.shape[0]

        xy = np.append(x, y, axis=1)
        poly = PolynomialFeatures(degree = deg)
        self.XY = poly.fit_transform(xy)

    def ols(self, XY = None, z = None):

        if XY is None: XY = self.XY
        if z is None: z = self.z

        #beta = scl.inv(XY.T @ XY) @ XY.T @ z
        beta = np.linalg.pinv(XY) @ z

        self.varz = np.var(z)
        self.var_ols = np.linalg.pinv(XY.T @ XY)*self.varz

        return beta

    def ridge(self, lamb, XY = None, z = None):

        if XY is None: XY = self.XY
        if z is None: z = self.z

        I = np.identity(XY.shape[1])
        beta = scl.inv(XY.T @ XY + lamb*I) @ XY.T @ z

        return beta


    def lasso(self, lamb, XY = None, z = None):

        if XY is None: XY = self.XY
        if z is None: z = self.z

        lass = Lasso([float(lamb)])
        lass.fit(XY, z)
        print(lass.intercept_)

        beta = lass.coef_

        return beta


    def MSE(self, z, zpred):

        return 1.0/z.shape[0]*np.sum((z - zpred)**2)


    def R2(self, z, zpred):

        zmean = np.average(z)

        return 1 - np.sum((z - zpred)**2)/np.sum((z - zmean)**2)


    def bootstrap(self, nBoots):

        boot_mse = np.zeros(nBoots)

        for i in range(nBoots):
            idx = np.random.choice(self.N, self.N)
            XY = self.XY[idx]
            z = self.z[idx]

            beta = self.ols()
            zpredict = XY @ beta
            mse = self.MSE(z, zpredict)
            boot_mse[i] = mse

        self.boot_mse = np.average(boot_mse)
        self.boot_ave = np.var(boot_mse)
        print("Average MSE after %i resamples: " %(nBoots), self.boot_mse)
        print("Variance of MSE after %i resamples: " %(nBoots), self.boot_ave)


    def kfold(self, nfolds):

        XY_folds = np.array_split(self.XY, nfolds, axis = 0)
        z_folds = np.array_split(self.z, nfolds, axis = 0)
        mse_ave = 0

        for i in range(nfolds):

            XY_Train = XY_folds.copy()
            XY_Test = XY_Train.pop(i)
            XY_Train = np.concatenate(XY_Train)

            Z_Train = z_folds.copy()
            Z_Test = Z_Train.pop(i)
            Z_Train = np.concatenate(Z_Train)

            beta = self.ols(XY_Train, Z_Train)
            zpredict = XY_Test @ beta
            mse = self.MSE(Z_Test, zpredict)
            mse_ave += mse

        mse_ave /= nfolds
        print("k-fold average MSE: ", mse_ave)