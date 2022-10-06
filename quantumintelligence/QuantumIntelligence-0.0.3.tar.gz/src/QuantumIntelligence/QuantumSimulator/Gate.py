# Copyright (C) <2022>  <Zheng-Zhi Sun>
# This file is part of QuantumIntelligence. QuantumIntelligence 
# is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the 
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. 
# QuantumIntelligence is distributed in the hope that it will be 
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details. You should have received a 
# copy of the GNU General Public License along with QuantumIntelligence. 
# If not, see <https://www.gnu.org/licenses/>.

import torch as tc
import numpy as np


pauli_x = tc.tensor([[0, 1], [1, 0]])
pauli_y = tc.tensor([[0, -1j], [1j, 0]])
pauli_z = tc.tensor([[1, 0], [0, -1]])


class Gate:
    def __init__(self, unitary, label=None, inverse=False, independent=True, check_unitary=False, unitary_acc=1e-6,
                 is_fast=False):
        if isinstance(unitary, Gate):
            if independent:
                self.tensor = unitary.tensor.clone().detach()
            else:
                self.tensor = unitary.tensor
            self.inverse = unitary.inverse
            self.label = unitary.label
            if inverse:
                self.inverse = not self.inverse
        elif isinstance(unitary, tc.Tensor):
            if independent:
                self.tensor = unitary.clone().detach()
            else:
                self.tensor = unitary
            self.inverse = inverse
            self.label = label
        if check_unitary:
            self.check_unitary(unitary_acc)
        self.is_fast = is_fast

    @property
    def requires_grad(self):
        return self.tensor.requires_grad

    @requires_grad.setter
    def requires_grad(self, requires_grad):
        self.tensor.requires_grad = requires_grad

    @property
    def grad(self):
        return self.tensor.grad

    @grad.setter
    def grad(self, value):
        self.tensor.grad = value

    # core functions start

    def check_unitary(self, acc=1e-6):
        identity_matrix = tc.eye(self.tensor.shape[0], device=self.tensor.device, dtype=self.tensor.dtype)
        diff = tc.dist(self.tensor.mm(self.tensor.conj().t()), identity_matrix)
        flag = (diff > acc)
        if flag:
            raise ValueError('the gate is not unitary. distance is ', diff)

    def inv(self):
        self.inverse = not self.inverse

    def square(self):
        if self.tensor.is_sparse:
            self.tensor = tc.sparse.mm(self.tensor, self.tensor)
        else:
            self.tensor = self.tensor.mm(self.tensor)

    def controlled_gate(self, n_control=1, output=False):
        # this function has not been tested
        c_gate = self.tensor.clone().detach()
        a_m = tc.tensor([[1, 0], [0, 0]], device=self.tensor.device, dtype=self.tensor.dtype)
        b_m = tc.tensor([[0, 0], [0, 1]], device=self.tensor.device, dtype=self.tensor.dtype)
        new_shape = c_gate.shape
        for nn in range(n_control):
            n_dim = round(c_gate.numel() ** 0.5)
            eye_m = tc.eye(n_dim, dtype=self.tensor.dtype, device=self.tensor.device)
            new_shape = new_shape + (2, 2)
            c_gate = tc.kron(a_m, eye_m) + tc.kron(b_m, c_gate.view(n_dim, n_dim))
        if output:
            return c_gate.view(new_shape)
        else:
            self.tensor = c_gate

    def to(self, device_or_dtype):
        self.tensor = self.tensor.to(device_or_dtype)
        return self

    def __copy__(self):
        return Gate(self)

    # core function end

# Experimental univerisal gate set


def rx_gate(theta=np.pi, device='cpu', dtype=tc.complex64):
    # exp(-i*theta * x/2)
    gate = tc.eye(2)*np.cos(theta/2) - 1j * np.sin(theta/2)*pauli_x
    return Gate(gate.to(device).to(dtype), label=('RX', theta))


def ry_gate(theta=np.pi, device='cpu', dtype=tc.complex64):
    # exp(-i*theta * y/2)
    gate = tc.eye(2)*np.cos(theta/2) - 1j * np.sin(theta/2)*pauli_y
    return Gate(gate.to(device).to(dtype), label=('RY', theta))


def rz_gate(theta=np.pi, device='cpu', dtype=tc.complex64):
    # exp(-i*theta * z/2)
    gate = tc.eye(2)*np.cos(theta/2) - 1j * np.sin(theta/2)*pauli_z
    return Gate(gate.to(device).to(dtype), label=('RZ', theta))


def cz_gate(device='cpu', dtype=tc.complex64):
    gate = tc.eye(4)
    gate[-1, -1] = -1
    return Gate(gate.to(device).to(dtype), label='CZ')


# practical gates with label

def hadamard(device='cpu', dtype=tc.complex64):
    gate = tc.tensor([[1, 1], [1, -1]], device=device, dtype=dtype) / np.sqrt(2)
    return Gate(gate, label='H')


def phase_shift(theta, device='cpu', dtype=tc.complex64):
    gate = tc.eye(2, device=device, dtype=dtype)
    gate[1, 1] = tc.exp(tc.tensor(theta * 1j))
    return Gate(gate)


def not_gate(device='cpu', dtype=tc.complex64):
    # this gate will be discarded
    gate = tc.tensor([[0, 1], [1, 0]], device=device, dtype=dtype)
    return Gate(gate, label='NOT')


def x_gate(device='cpu', dtype=tc.complex64):
    return Gate(pauli_x.to(device).to(dtype), label='X')


def y_gate(device='cpu', dtype=tc.complex64):
    return Gate(pauli_y.to(device).to(dtype), label='Y')


def z_gate(device='cpu', dtype=tc.complex64):
    return Gate(pauli_z.to(device).to(dtype), label='Z')


def swap_gate(device='cpu', dtype=tc.complex64):
    gate = tc.zeros(4, 4, device=device, dtype=dtype)
    gate[0, 0] = 1
    gate[1, 2] = 1
    gate[2, 1] = 1
    gate[3, 3] = 1
    return Gate(gate, label='SWAP')

# gate without label


def rand_gate(dim=2, device='cpu', dtype=tc.complex64, requires_grad=False):
    # Haar random gate
    tmp_tensor = tc.randn(dim, dim, device=device, dtype=dtype)
    q, r = tc.linalg.qr(tmp_tensor)
    sign_matrix = tc.sign(tc.real(tc.diag(r)))
    gate = tc.einsum('ij,j->ij', q, sign_matrix)
    gate = Gate(gate)
    gate.requires_grad = requires_grad
    return gate


def noise_gate_single_gaussian(strength=0.01, device='cpu', dtype=tc.complex64):
    theta = tc.randn(1, device=device) * (strength ** 0.5)
    direction = tc.randn(3, device=device)
    direction = direction / direction.norm()
    sigma = direction[0] * pauli_x + direction[1] * pauli_y + direction[2] * pauli_z
    gate_matrix = tc.cos(theta)*tc.eye(2) + tc.sin(theta) * 1j * sigma
    gate_matrix = gate_matrix.to(device).to(dtype)
    return Gate(gate_matrix)



def time_evolution(hamiltonian, time, device='cpu', dtype=tc.complex64):
    hamiltonian = hamiltonian.to(device).to(dtype)
    if hamiltonian.is_sparse:
        gate = tc.matrix_exp(-1j * hamiltonian.to_dense() * time)
        gate = gate.to_sparse()
    else:
        gate = tc.matrix_exp(-1j * hamiltonian * time)
    return Gate(gate)
