import math

import numpy as np
import matplotlib.pyplot as plt


class AnisotropicMHD():
    def __init__(self):
        self.set_param()
        
    def set_param(
        self, gam=5/3,
        eps1=1.0, eps2=1.0,
        th1=np.deg2rad(87.5),
        beta1=1.0,
        Mn2=None):
        self.gam = gam
        self.eps1 = eps1
        self.th1 = th1
        self.beta1 = beta1
        self.eps2 = eps2
        self.Mn2 = Mn2
        
        if Mn2 == None:
            self.Mn2 = np.linspace(1e-4,1.2,10000)
    
    def solve(self):
        Gamp = (self.gam + 1.)/self.gam
        Gamm = (self.gam - 1.)/self.gam

        xi1 = Gamm*(self.Mn2 - 2. + 1./self.eps2) \
            - (2. + 1./self.eps2)/(3.*self.gam)
        xi2 = (self.Mn2 - 1.)**2

        csq = math.cos(self.th1)**2
        tsq = math.tan(self.th1)**2
        
        Lama = Gamm*xi2/csq - xi1*self.Mn2*tsq

        Lamb = xi2*(
            Gamm*2.*(1.0-self.eps1)/(3.0*csq) \
            + 0.5*self.eps1*self.beta1/csq - self.eps2*self.Mn2
        ) + self.eps1*xi1*self.Mn2*tsq

        Lamc = self.Mn2*(
            self.eps2**2*xi2*(
                Gamp*self.Mn2 \
                - self.eps1*self.beta1/self.eps2/csq \
                + self.eps1/self.eps2 - 1.0 \
                + (4.*Gamm*(self.eps2-1.0) - (2.0*self.eps1+1.0)*tsq
                )/(3.0*self.eps2)
            ) - self.eps1**2*xi1*tsq
        )

        x=Lamb**2-Lama*Lamc
        self.Mn1m = (-Lamb-np.sqrt(x))/(Lama*self.eps1)
        self.Mn1p = (-Lamb+np.sqrt(x))/(Lama*self.eps1)

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.plot(self.Mn2, self.Mn1m, 'k-')
        plt.plot(self.Mn2, self.Mn1p, 'k-')
        ax.set_aspect('equal')
        plt.ylabel(r'$M_{A1}^2$')
        plt.xlabel(r'$M_{A2}^2$')
        xmax = np.max(self.Mn2)
        plt.xlim([0,xmax])
        plt.ylim([0,xmax])
        plt.grid()
        plt.show()
                        