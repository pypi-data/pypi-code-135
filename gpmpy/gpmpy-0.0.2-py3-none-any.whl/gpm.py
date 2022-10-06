import numpy as np
from scipy import special
class PSM:
    """
    Legendre and Birkhoff Pseudospectral method for optimal control problems 
    """
    def __init__(self,N,scale=1) -> None:
        """
        xn or taon is equal to the Matching point which is between -1 and 1.
        pn or Ln is the N-order Legendre Polynomial value in xn whose size is N
        L is the Legendre Polynomial Value Maxtrix from 0-order to N-order  
        """
        self.N=N
        self.xn,self.pn,self.L=self.LGLPoint(N)
        self.D=self.LGLDMatrix(self.xn,self.pn)
        self.W=self.LGLWeight(N,self.pn)
        self.B=self.BirkhoffMatrix(self.W*scale,self.N,self.L)


    @classmethod
    def LGLPoint(self,N):
        """
        计算配点及最后的N阶Legendre多项式
        """
        k = np.arange(0, N + 1)
        xn = np.cos(np.pi * k / N)         
        xn = np.sort(xn)
        #这是在调用Legendre计算一个多项式，用于迭代计算配点
        Pn, Pn_,L = self.LegendrFunction(N, xn)   
        dx = (xn * Pn - Pn_) / ((N + 1) * Pn)
        keson = max(abs(dx))
        #这是设置配点的计算精度，当差距在1e-16的时候，代表比较精确了
        while keson > 1e-16:
            xn = xn - dx                  #将经过处理的高精度的cheb点作为基础点传入勒让德函数做处理得出的点为更高精度的点
            [Pn, Pn_,L] = self.LegendrFunction(N, xn)
            dx = (xn * Pn - Pn_) / ((N + 1) * Pn)
            keson = max(abs(dx))
        return xn, Pn,L
    #这是计算Legendre多项式，这个多项式既用于计算LGL配点又用于计算LGL在配点的微分
    @classmethod
    def LegendrFunction(self,N,x):
        """
        迭代计算Legendre多项式在各阶各配点上的取值
        """
        m = np.size(x)
        L = np.zeros((N + 1, m))     #生成一个0矩阵
        L[0, :] = np.ones(m)        #矩阵的第一行所有元素赋值为1
        L[1, :] = x
        # L[2, :] = (3 * x ** 2 - 1) / 2
        for n in range(1, N):
            L[n + 1, :] = ((2 * n + 1) * x * L[n, :] - n * L[n - 1, :]) / (n + 1)
        Ln = L[N, :]
        Ln_ = L[N - 1, :]
        return Ln,Ln_,L
    @classmethod
    def LGLDMatrix(self,tao_n,pn):                       
        """
        计算LGL在配点的微分
        """                                          
        N = len(pn)  
        N = N - 1
        D = np.zeros((N + 1, N + 1))
        for k in range(0, N + 1):
            for i in range(0, N + 1):
                if i != k:
                    D[k, i] = pn[k] / (pn[i] * (tao_n[k] - tao_n[i]))
        D[0, 0] = -N * (N + 1) / 4
        D[N, N] = N * (N + 1) / 4
        return D
    def LGLWeight(self,N,Ln):
        """
        计算权重矩阵, 但还需要实际问题中的tf和t0做最后的映射计算
        w=w_tem*(tf-t0)/2
        """
        W_tem=2/(N*(N+1)*Ln**2) 
        return W_tem
  
    def BirkhoffMatrix(self,W,N,L):
        """
        计算Birkhoff矩阵
        """
        B=np.zeros((N+1,N+1))
        Beta=np.zeros((N+1,N+1))
        Fai=np.zeros((N+1,N+1))
        B[:,0]=1
        B[0,1:]=0
        # B[N,:]=0
        direct_computing=True
        if direct_computing:
            for k in range (0,N):
                for j in range(1,N+1):
                    Beta[k,j]=W[j]*(L[k,j]-((-1)**(N+k))*L[N,j])
            # sy.Matrix(Beta)   
            for k in range (0,N):
                for i in range(0,N+1):
                    if k>=1:
                        Fai[k,i]=(1/(2*k+1))*(L[k+1,i]-L[k-1,i])/(2/(2*k+1))
                    else:
                        Fai[k,i]=(L[k+1,i]+1)/(2/(2*k+1))
            # sy.Matrix(Fai)
            for i in range(0,N+1):
                for j in range(1,N+1):
                    temp=0
                    for k in range(0,N):
                        temp=temp+Beta[k,j]*Fai[k,i]
                    B[i,j]=temp
            # B_m=sy.Matrix(B)
        return B

class LegendreGaussLobatto:
    """
    Legendre and Birkhoff Pseudospectral method for optimal control problems 
    """
    def __init__(self,N,scale=1) -> None:
        """
        xn or taon is equal to the Matching point which is between -1 and 1.
        pn or Ln is the N-order Legendre Polynomial value in xn whose size is N
        L is the Legendre Polynomial Value Maxtrix from 0-order to N-order  
        """
        self.N=N
        self.xn,self.pn,self.L=self.LGLPoint(N)
        self.D=self.LGLDMatrix(self.xn,self.pn)
        self.W=self.LGLWeight(N,self.pn)
        self.B=self.BirkhoffMatrix(self.W*scale,self.N,self.L)


    @classmethod
    def LGLPoint(self,N):
        """
        计算配点及最后的N阶Legendre多项式
        """
        k = np.arange(0, N + 1)
        xn = np.cos(np.pi * k / N)         
        xn = np.sort(xn)
        #这是在调用Legendre计算一个多项式，用于迭代计算配点
        Pn, Pn_,L = self.LegendrFunction(N, xn)   
        dx = (xn * Pn - Pn_) / ((N + 1) * Pn)
        keson = max(abs(dx))
        #这是设置配点的计算精度，当差距在1e-16的时候，代表比较精确了
        while keson > 1e-16:
            xn = xn - dx                  #将经过处理的高精度的cheb点作为基础点传入勒让德函数做处理得出的点为更高精度的点
            [Pn, Pn_,L] = self.LegendrFunction(N, xn)
            dx = (xn * Pn - Pn_) / ((N + 1) * Pn)
            keson = max(abs(dx))
        return xn, Pn,L
    #这是计算Legendre多项式，这个多项式既用于计算LGL配点又用于计算LGL在配点的微分
    @classmethod
    def LegendrFunction(self,N,x):
        """
        迭代计算Legendre多项式在各阶各配点上的取值
        """
        m = np.size(x)
        L = np.zeros((N + 1, m))     #生成一个0矩阵
        L[0, :] = np.ones(m)        #矩阵的第一行所有元素赋值为1
        L[1, :] = x
        # L[2, :] = (3 * x ** 2 - 1) / 2
        for n in range(1, N):
            L[n + 1, :] = ((2 * n + 1) * x * L[n, :] - n * L[n - 1, :]) / (n + 1)
        Ln = L[N, :]
        Ln_ = L[N - 1, :]
        return Ln,Ln_,L
    @classmethod
    def LGLDMatrix(self,tao_n,pn):                       
        """
        计算LGL在配点的微分
        """                                          
        N = len(pn)  
        N = N - 1
        D = np.zeros((N + 1, N + 1))
        for k in range(0, N + 1):
            for i in range(0, N + 1):
                if i != k:
                    D[k, i] = pn[k] / (pn[i] * (tao_n[k] - tao_n[i]))
        D[0, 0] = -N * (N + 1) / 4
        D[N, N] = N * (N + 1) / 4
        return D
    def LGLWeight(self,N,Ln):
        """
        计算权重矩阵, 但还需要实际问题中的tf和t0做最后的映射计算
        w=w_tem*(tf-t0)/2
        """
        W_tem=2/(N*(N+1)*Ln**2) 
        return W_tem
  
    def BirkhoffMatrix(self,W,N,L):
        """
        计算Birkhoff矩阵
        """
        B=np.zeros((N+1,N+1))
        Beta=np.zeros((N+1,N+1))
        Fai=np.zeros((N+1,N+1))
        B[:,0]=1
        B[0,1:]=0
        # B[N,:]=0
        direct_computing=True
        if direct_computing:
            for k in range (0,N):
                for j in range(1,N+1):
                    Beta[k,j]=W[j]*(L[k,j]-((-1)**(N+k))*L[N,j])
            # sy.Matrix(Beta)   
            for k in range (0,N):
                for i in range(0,N+1):
                    if k>=1:
                        Fai[k,i]=(1/(2*k+1))*(L[k+1,i]-L[k-1,i])/(2/(2*k+1))
                    else:
                        Fai[k,i]=(L[k+1,i]+1)/(2/(2*k+1))
            # sy.Matrix(Fai)
            for i in range(0,N+1):
                for j in range(1,N+1):
                    temp=0
                    for k in range(0,N):
                        temp=temp+Beta[k,j]*Fai[k,i]
                    B[i,j]=temp
            # B_m=sy.Matrix(B)
        return B

class LegendreGauss:
    def __init__(self, nc):
        self.ncp = nc
        self.nx = nc + 2
        self.cps = self.generate_collocation_points()
        self.xtao = np.concatenate([[-1], self.cps, [1]])
        self.utao = self.cps

        self.jacobiWeights = self.generate_jacobi_weights()
        self.integralWeights = np.concatenate([[0], self.jacobiWeights, [0]])
        self.PDM, self.PIM = self.generate_PIM_PDM()

    def generate_collocation_points(self):
        roots, _ = special.roots_jacobi(self.ncp, 0, 0)
        return roots

    def generate_jacobi_weights(self):
        """ Return Gauss-Legendre weights. """
        w = np.zeros((self.ncp,))
        for i in range(self.ncp):
            _, derivative = special.lpn(self.ncp, self.cps[i])
            w[i] = 2 / ((1 - self.cps[i] ** 2) * derivative[-1] ** 2)
        return w

    def barycentricWeights(self):
        ksi = (-1) ** np.arange(self.ncp) * np.sqrt((1 - self.cps ** 2) * self.jacobiWeights)
        return ksi

    def generate_PIM_PDM(self):
        ksi = self.barycentricWeights()

        D = np.zeros((self.ncp, self.ncp))
        for k in range(self.ncp):
            for i in range(self.ncp):
                if k != i:
                    D[k, i] = ksi[i] / ksi[k] / (self.cps[k] - self.cps[i])
        for k in range(self.ncp):
            D[k, k] = -np.sum(D[k, :])

        PDM = np.zeros((self.ncp, self.nx))
        for k in range(self.ncp):
            for i in range(self.ncp):
                if k == i:
                    PDM[k, i + 1] = (1 + (self.cps[k] + 1) * D[k, i]) / (self.cps[i] + 1)
                else:
                    PDM[k, i + 1] = ((self.cps[k] + 1) * D[k, i]) / (self.cps[i] + 1)
        PDM[:, 0] = -np.sum(PDM[:, 1:], axis=1)  # 其余元素的和的相反数
        PIM = np.zeros((self.ncp + 1, self.ncp))
        PIM[:-1] = np.linalg.inv(PDM[:, 1:-1])
        PIM[-1] = self.integralWeights[1:-1]
        return PDM, PIM


class LegendreGaussRadau:
    """ Legendre-Gauss-Radau Pseudospectral method
    Gauss-Radau xtao are roots of :math:`P_n(x) + P_{n-1}(x)`. """

    def __init__(self, nc):
        self.ncp = nc
        self.nx = nc + 1
        self.cps = self.generate_collocation_points()
        self.xtao = np.concatenate([self.cps, [1]])

        self.jacobiWeights = self.generate_jacobi_weights()
        self.integralWeights = np.concatenate([self.jacobiWeights, [0]])
        self.PDM, self.PIM = self.generate_PIM_PDM()

    def generate_collocation_points(self):
        """ Return Gauss-Radau-Radau collocation points. """
        roots, _ = special.roots_jacobi(self.ncp - 1, 0, 1)
        cps = np.hstack((-1, roots))
        return cps

    def generate_jacobi_weights(self):
        """ Return Gauss-Legendre-Radau weights. """
        tao = self.cps
        w = np.zeros((self.ncp,))
        for i in range(self.ncp):
            pnz, _ = special.lpn(self.ncp - 1, self.cps[i])
            w[i] = (1 - tao[i]) / (self.ncp ** 2 * pnz[-1] ** 2)
        return w

    def generate_PIM_PDM(self):
        Y = np.tile(self.xtao.reshape((-1, 1)), (1, self.nx))
        Ydiff = Y - Y.transpose() + np.eye(self.nx)
        WW = np.tile((1. / np.prod(Ydiff, axis=0)).reshape((-1, 1)), (1, self.nx))
        D = WW / (WW.transpose() * Ydiff)
        np.fill_diagonal(D, 1 - sum(D))  # 替换对角元素

        # full differentiation matrix
        D = -D.transpose()
        PDM = D[:-1, :]

        # find integration matrix E
        PIM = np.linalg.inv(PDM[:, 1: self.nx])
        return PDM, PIM

    def barycentricWeights(self):
        ksi = (-1) ** np.arange(self.ncp) * np.sqrt((1 - self.cps) * self.integralWeights)
        ksi[0] = 2 * np.sqrt(self.jacobiWeights[0])
        return ksi


class flippedLegendreGaussRadau:
    """ flipped Legendre-Gauss-Radau Pseudospectral method
    Gauss-Radau xtao are roots of :math:`P_n(x) - P_{n-1}(x)`.
    Note that fLGR does not have weights"""

    def __init__(self, nc):
        self.ncp = nc
        self.nx = nc + 1
        self.cps = self.generate_collocation_points()
        self.xtao = np.concatenate([[-1], self.cps])

        self.jacobiWeights = self.generate_jacobi_weights()
        self.integralWeights = np.concatenate([[0], self.jacobiWeights])
        self.PDM, self.PIM = self.generate_PIM_PDM()

    def generate_collocation_points(self):
        """ Return flipped-Gauss-Legendre-Radau collocations points. """
        roots, _ = special.roots_jacobi(self.ncp - 1, 0, 1)
        cps = np.hstack((-1, roots))
        cps = -cps[::-1]
        return cps

    def generate_jacobi_weights(self):
        """Return flipped-Gauss-Legendre-Radau weight."""
        tao = self.cps
        w = np.zeros((self.ncp,))
        for i in range(self.ncp):
            pnz, _ = special.lpn(self.ncp, -self.cps[i])
            w[i] = (1 + tao[i]) / (self.ncp ** 2 * pnz[-1] ** 2)
        return w

    def generate_PIM_PDM(self):
        tao = self.cps
        ksi = np.zeros((self.ncp,))
        for i in range(self.ncp):
            ksi[i] = (-1) ** i * np.sqrt((1 + tao[i]) * self.jacobiWeights[i])

        D = np.zeros((self.ncp, self.ncp))
        for k in range(self.ncp):
            for i in range(self.ncp):
                if k != i:
                    D[k, i] = ksi[i] / ksi[k] / (tao[k] - tao[i])
        for k in range(self.ncp):
            D[k, k] = -np.sum(D[k, :])

        PDMif = np.zeros((self.ncp, self.nx))
        for k in range(self.ncp):
            for i in range(self.ncp):
                if k == i:
                    PDMif[k, i + 1] = (1 + (tao[k] + 1) * D[k, i]) / (tao[i] + 1)
                else:
                    PDMif[k, i + 1] = ((tao[k] + 1) * D[k, i]) / (tao[i] + 1)
        PDMif[:, 0] = -np.sum(PDMif[:, 1:], axis=1)  # 其余元素的和的相反数

        PIMnt = np.linalg.inv(PDMif[:, 1: self.nx])
        return PDMif, PIMnt


if __name__=="__main__":   
    N=10
    LGLD=LegendreGaussLobatto(N).D
    LGRD=LegendreGaussRadau(N).PDM
    LGD=LegendreGauss(N).PDM
    

