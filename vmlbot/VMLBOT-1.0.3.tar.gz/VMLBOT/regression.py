import numpy as np
import matplotlib.pyplot as plt



class LWR:
    def __init__(self, data):
        np.random.seed(8)
        self.X = np.random.randn(data, 1)
        print("Displaying first 10 datasets:", self.X[0:10])
        self.y = 2 * (self.X ** 3) + 10 + 4.6 * np.random.randn(data, 1)
        print("Displaying first 10 datasets of fitting curve:", self.y[0:10])
        self.plot_predictions(self.X, self.y, 0.08, 100)


    def wm(self, point, X, tau):
        m = X.shape[0]
        w = np.mat(np.eye(m))
        for i in range(m):
            xi = X[i]
            d = (-2 * tau * tau)
            w[i, i] = np.exp(np.dot((xi-point), (xi-point).T)/d)
        return w

    def predict(self, X, y, point, tau):
        m = X.shape[0]
        X = np.append(X, np.ones(m).reshape(m,1), axis=1)
        point_ = np.array([point, 1])
        w = self.wm(point, X, tau)
        theta = np.linalg.pinv(X.T*(w * X))*(X.T*(w * y))
        pred = np.dot(point_, theta)
        return theta, pred

    def plot_predictions(self, X, y, tau, nval):
        X_test = np.linspace(-3, 3, nval)
        preds = []
        for point in X_test:
            theta, pred = self.predict(X, y, point, tau)
            preds.append(pred)
        X_test = np.array(X_test).reshape(nval,1)
        preds = np.array(preds).reshape(nval,1)
        plt.plot(X, y, 'b.')
        plt.plot(X_test, preds, 'r.')
        plt.show()


