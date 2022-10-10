import numpy as np
from scipy.signal import fftconvolve

from auxiliaries import choose_kernel
from simulator import Simulator


class PCNNModel(object):
    """
    Simple PCNN format
    - S = input
    - M = feeding synaptic weight
    - W = linking synaptic weight
    - alpha
    - beta

    f = e ^ -alpha_f
    g = e ^ -alpha_theta


    each neuron denoted with (i, j) and one of its neighbours (k, l)
    WHERE:
    S = the input image
    U = membrane potential
    Y = the neuron outputs
    Theta = the state of the dynamic thresholds
    0 < g < f < 1, scalars values
    v_theta =  large scalar used to increase the dynamic threshold after firing
    M = weights for each Y
    """

    def __init__(self, shape):
        #scalar variables are n, i, j - iterations, position in image
        # matrix variables
        # F: Feeding input
        self.F = np.zeros(shape)
        # L: Linking input
        self.L = np.zeros(shape)
        # U: Membrane potential / internal activity
        self.U = np.zeros(shape)
        # Y: output / action potential
        self.Y = np.zeros(shape)
        # Theta: threshold
        self.Theta = np.ones(shape)

        # matrix parameters
        # feeding synaptic weight
        self.M = [0.707, 1, 0.707]
        # linking synaptic weight
        self.W = [0.707, 1, 0.707]

        # scalar parameters
        alpha_theta = 0.2
        alpha_f = 0.2 # exponential decay factor
        alpha_l = 0.5
        self.f = np.exp(-alpha_f) # exponential decay factor
        self.g = np.exp(-alpha_theta)
        self.h = np.exp(-alpha_l)

        self.v_f = 0.1
        self.v_l = 0.2
        self.v_theta = 6
        # the action potential v_theta increases the threshold by
        # an amount Vh so that a secondary action potential has no
        # capability to be generated during a certain period, and the
        # increased threshold decays with the constant e^-alpha_theta .

        # beta: constant amplifying the linking input impact
        self.beta = 0.5
        self.gamma = 0.5


    def iterate(self, S):
        # S is the input
        pass


    def segment_image(self, image, gamma, beta, v_theta, kernel_type):
        self.Theta = np.full(image.shape, 255)
        self.gamma = gamma
        self.beta = beta
        self.v_theta = v_theta

        self.W = choose_kernel(kernel_type)
        self.M = choose_kernel(kernel_type)

        firednum = 0
        n = 0
        N = image.size

        T = np.full((image.shape), 0)
        while firednum < N:
            n += 1
            self.L = self.convolve(self.Y, self.W)
            self.Theta = self.Theta - self.gamma + self.v_theta * self.Y
            flag = 1
            while flag == 1:
                Q = self.Y
                self.U = image * (1 + self.beta * self.L)
                # step / activation function
                self.Y = np.where(self.U > self.Theta, 1, 0)
                if np.array_equal(Q, self.Y):
                    flag = 0
                else:
                    self.L = self.convolve(self.Y, self.W)
            firednum = firednum + np.sum(self.Y)
            T = T + n * self.Y

        # print(T)
        return np.full((image.shape), 256) - T


    def histogram(self, image):
        H = np.zeros((256, ))
        self.Theta = np.full(image.shape, 255)
        self.gamma = 1
        self.v_theta = 256

        for n in range(0, 255):
            self.U = image
            self.Theta = self.Theta - self.gamma + self.v_theta * self.Y
            self.Y = np.where(self.U > self.Theta, 1, 0)
            H[256-n] = np.sum(self.Y)

        return H


    def convolve(self, Y, W):
        return fftconvolve(Y, W, mode='same')


    def simulate(self, image):
        simulator = Simulator()
        simulator.iterate(image, self, steps=20)
        simulator.plot_results()