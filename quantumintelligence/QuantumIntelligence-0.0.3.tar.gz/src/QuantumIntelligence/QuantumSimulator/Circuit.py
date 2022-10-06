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

import numpy as np
import torch as tc
import copy
from QuantumIntelligence.QuantumSimulator import Gate
from QuantumIntelligence.BasicFunSZZ import tensor_trick as tt


# [1, 0] is |0>, [0, 1] is |1>
# do not use fake functions, it will be removed soon
# please apply gate on position as list(range(?)) as much as possible, this will make it faster
# please control gate on position as list(range(?, n_qubit)) as much as possible, this will make it faster

class Circuit:

    def __init__(self, n_qubit, device='cpu', dtype=tc.complex64, size=None):
        self.n_qubit = n_qubit
        self.device = device
        self.dtype = dtype
        self.size = size
        self.gate_list = list()
        self.position_list = list()
        self.control_list = list()
        self.barrier_index = list()
        self.noised = False
        self.ready4experiment = False

    @property
    def requires_grad(self):
        flag = list()
        for gg in self.gate_list:
            flag.append(gg.requires_grad)
        return flag

    @requires_grad.setter
    def requires_grad(self, requires_grad):
        if isinstance(requires_grad, bool):
            for gg in self:
                gg.requires_grad = requires_grad
        else:
            for nn in range(len(self)):
                self.gate_list[nn].requires_grad = requires_grad[nn]

    # core functions start

    def compose(self, circuit, position=None, control=None, inverse=False):
        if isinstance(circuit, Circuit):
            tmp_circuit = copy.deepcopy(circuit)
            if inverse:
                tmp_circuit.inv()
            self.__extend(tmp_circuit, position=position, control=control)
        elif isinstance(circuit, Gate.Gate):
            if position is None:
                raise ValueError('position is needed when compose gate')
            self.add_single_gate(gate=circuit, position=position, control=control, inverse=inverse)
        else:
            raise ValueError('input is not Gate or Circuit')

    def __extend(self, circuit, position=None, control=None):
        if not isinstance(circuit, Circuit):
            raise TypeError('this function is used to extend circuit. Use append or compose to add single gate')
        if control is None:
            control = []
        if position is None:
            if self.n_qubit == circuit.n_qubit:
                for ii in range(len(circuit)):
                    cc = circuit[ii]
                    self.append(gate=cc[0], position=cc[1], control=cc[2])
            else:
                raise ValueError('error in extend, position is needed')
        elif len(position) == circuit.n_qubit:
            for ii in range(len(circuit)):
                cc = circuit[ii]
                new_p = list()
                new_c = list()
                for oo in cc[1]:
                    new_p.append(position[oo])
                for oo in cc[2]:
                    new_c.append(position[oo])
                for oo in control:
                    new_c.append(oo)
                self.append(gate=cc[0], position=new_p.copy(), control=new_c.copy())
        else:
            raise ValueError('error in extend, check position')

    def add_single_gate(self, gate, position, control=None, inverse=False):
        # gate can be sparse, but there seems to be no speedup
        # one should be careful when add inverse gates
        # the gate will be cloned and detached by default

        # do not change the following code, or some bugs would occur in circuit.ch
        gate = Gate.Gate(gate, independent=True)
        # gate = Gate.Gate(gate, independent=True).to(self.device).to(self.dtype)

        if tt.have_same_iterable(position, control):
            raise ValueError('position and control have same qubits')
        self.position_list.append(position)
        if control is None:
            control = []
        self.control_list.append(control)
        if inverse:
            gate.inv()
        self.gate_list.append(gate)

    def append(self, gate, position, control=None, inverse=False):
        # this is just another name of add single gate
        self.add_single_gate(gate, position=position, control=control, inverse=inverse)

    def repeat_append(self, gate, position_list, inverse=False):
        for position in position_list:
            self.add_single_gate(gate, position=position, inverse=inverse)

    def inv(self):
        self.gate_list.reverse()
        self.position_list.reverse()
        self.control_list.reverse()
        for gate in self.gate_list:
            gate.inv()

    def return_inv(self):
        tmp_circuit = copy.deepcopy(self)
        tmp_circuit.gate_list.reverse()
        tmp_circuit.position_list.reverse()
        tmp_circuit.control_list.reverse()
        for gate in tmp_circuit.gate_list:
            gate.inv()
        return tmp_circuit

    def to(self, device_or_dtype):
        for cc in self.gate_list:
            cc.to(device_or_dtype)
        return self

    def square(self):
        for gate in self.gate_list:
            gate.square()

    def regularize_position(self, index):

        self.position_list[index] = list(map(lambda x: x % self.n_qubit, self.position_list[index]))
        self.control_list[index] = list(map(lambda x: x % self.n_qubit, self.control_list[index]))

    def regularize_all_position(self):
        for ii in range(len(self)):
            self.regularize_position(ii)

    def __getitem__(self, index):
        return self.gate_list[index], self.position_list[index], self.control_list[index]

    def __len__(self):
        return len(self.gate_list)

    def __add__(self, circuit):

        if circuit.n_qubit != self.n_qubit:
            raise ValueError('error in +, n_qubit not equal')

        tmp_circuit = Circuit(self.n_qubit, device=self.device, dtype=self.dtype)
        tmp_circuit.gate_list = self.gate_list + circuit.gate_list
        tmp_circuit.position_list = self.position_list + circuit.position_list
        tmp_circuit.control_list = self.control_list + circuit.control_list
        return tmp_circuit

    def __copy__(self):
        raise NameError('I do not permit copy for now. Please use deepcopy().')

    def pop(self, index):
        self.gate_list.pop(index)
        self.position_list.pop(index)
        self.control_list.pop(index)

    def add_noise_gate(self, strength=0.01):
        for ii in range(len(self)):
            if self.control_list[ii] is not None:
                tmp_noise = Gate.noise_gate_single_gaussian(strength=strength, device=self.device, dtype=self.dtype)
                self.gate_list[ii].tensor = self.gate_list[ii].tensor.mm(tmp_noise.tensor)
        self.noised = True

    def cal_barrier(self):
        self.regularize_all_position()
        position_list = list(range(self.n_qubit))
        flag = False
        for ii in range(len(self)):
            for nn in self.position_list[ii]:
                if nn not in position_list:
                    flag = True
            for nn in self.control_list[ii]:
                if nn not in position_list:
                    flag = True

            if flag:
                self.barrier_index.append(ii)
                position_list = list(range(self.n_qubit))
                flag = False
            for nn in self.position_list[ii]:
                position_list.remove(nn)
            for nn in self.control_list[ii]:
                position_list.remove(nn)

    def regularize_gates(self):
        new_gate_list = []
        new_position_list = []
        new_control_list = []
        while len(self) > 0:
            index_list_strict = list(range(self.n_qubit))
            index_list_loose = list(range(self.n_qubit))
            ii = 0
            while ii < len(self):

                flag = True
                for nn in self.position_list[ii]:
                    if nn not in index_list_strict:
                        flag = False
                for nn in self.control_list[ii]:
                    if nn not in index_list_loose:
                        flag = False

                if flag:
                    for nn in self.position_list[ii]:
                        if nn in index_list_strict:
                            index_list_strict.remove(nn)
                        if nn in index_list_loose:
                            index_list_loose.remove(nn)
                    for nn in self.control_list[ii]:
                        if nn in index_list_strict:
                            index_list_strict.remove(nn)
                        if nn in index_list_loose:
                            index_list_loose.remove(nn)
                    new_gate_list.append(self.gate_list[ii])
                    new_position_list.append(self.position_list[ii])
                    new_control_list.append(self.control_list[ii])
                    self.pop(ii)
                else:
                    for nn in self.position_list[ii]:
                        if nn in index_list_strict:
                            index_list_strict.remove(nn)
                        if nn in index_list_loose:
                            index_list_loose.remove(nn)
                    for nn in self.control_list[ii]:
                        if nn in index_list_strict:
                            index_list_strict.remove(nn)
                    ii = ii + 1
        self.gate_list = new_gate_list
        self.position_list = new_position_list
        self.control_list = new_control_list

    # core functions end
    # practical functions start

    # universal gate set from experiment

    def rx_gate(self, position, theta=np.pi, control=None):
        tmp_gate = Gate.rx_gate(theta=theta, device=self.device, dtype=self.dtype)
        for pp in position:
            self.add_single_gate(tmp_gate, position=[pp], control=control)

    def ry_gate(self, position, theta=np.pi, control=None):
        tmp_gate = Gate.ry_gate(theta=theta, device=self.device, dtype=self.dtype)
        for pp in position:
            self.add_single_gate(tmp_gate, position=[pp], control=control)

    def rz_gate(self, position, theta=np.pi, control=None):
        tmp_gate = Gate.rz_gate(theta=theta, device=self.device, dtype=self.dtype)
        for pp in position:
            self.add_single_gate(tmp_gate, position=[pp], control=control)

    def cz_gate(self, position):
        tmp_gate = Gate.cz_gate(device=self.device, dtype=self.dtype)
        for pp in position:
            self.add_single_gate(tmp_gate, position=pp)

    # decompose circuit to experimental gates

    def decompose2experimental_gate(self):
        # global phases are ignored

        old_gate_list = self.gate_list
        old_position_list = self.position_list
        old_control_list = self.control_list

        self.gate_list = list()
        self.position_list = list()
        self.control_list = list()

        experimental_gate_set = ('RX', 'RY', 'RZ', 'CZ')
        supported_label = ('X', 'Y', 'Z')
        for ii in range(len(old_gate_list)):
            tmp_label = old_gate_list[ii].label
            if isinstance(tmp_label, tuple):
                tmp_label = tmp_label[0]
            tmp_position = old_position_list[ii]
            tmp_control = old_control_list[ii]

            if tmp_label is None:
                ValueError('The ', str(ii), '-th gate has no label')
            if len(tmp_control) > 1:
                ValueError('Do not support multi controlled ', tmp_label)

            elif tmp_label in experimental_gate_set:
                if len(tmp_control) == 0:
                    self.append(old_gate_list[ii], position=tmp_position)
                elif len(tmp_control) == 1:
                    ValueError('Waiting to support controlled ', tmp_label)
            elif tmp_label in supported_label:
                if tmp_label == 'Z':
                    if len(tmp_control) == 0:
                        self.rz_gate(position=tmp_position, theta=np.pi)
                    elif len(tmp_control) == 1:
                        self.cz_gate(position=[tmp_position+tmp_control])
                    else:
                        ValueError('tired')
                elif tmp_label == 'X':

                    if len(tmp_control) == 0:
                        self.rx_gate(position=tmp_position, theta=np.pi)
                    elif len(tmp_control) == 1:
                        self.rz_gate(position=tmp_position, theta=np.pi)
                        self.ry_gate(position=tmp_position, theta=np.pi/2)
                        self.cz_gate(position=[tmp_position+tmp_control])
                        self.ry_gate(position=tmp_position, theta=-np.pi / 2)
                        self.rz_gate(position=tmp_position, theta=-np.pi)

                    else:
                        ValueError('tired')
                elif tmp_label == 'Y':
                    if len(tmp_control) == 0:
                        self.ry_gate(position=tmp_position, theta=np.pi)
                    elif len(tmp_control) == 1:
                        self.rz_gate(position=tmp_position, theta=3*np.pi/2)
                        self.ry_gate(position=tmp_position, theta=-np.pi/2)
                        self.cz_gate(position=[tmp_position+tmp_control])
                        self.ry_gate(position=tmp_position, theta=np.pi/2)
                        self.rz_gate(position=tmp_position, theta=-3*np.pi/2)
                    else:
                        ValueError('tired')

    # useful gates and circuits

    def x_gate(self, position, control=None):
        tmp_gate = Gate.x_gate(device=self.device, dtype=self.dtype)
        for pp in position:
            self.add_single_gate(tmp_gate, position=[pp], control=control)

    def y_gate(self, position, control=None):
        tmp_gate = Gate.y_gate(device=self.device, dtype=self.dtype)
        for pp in position:
            self.add_single_gate(tmp_gate, position=[pp], control=control)

    def z_gate(self, position, control=None):
        tmp_gate = Gate.z_gate(device=self.device, dtype=self.dtype)
        for pp in position:
            self.add_single_gate(tmp_gate, position=[pp], control=control)

    def hadamard(self, position, control=None):
        tmp_gate = Gate.hadamard(device=self.device, dtype=self.dtype)
        for pp in position:
            self.add_single_gate(tmp_gate, position=[pp], control=control)

    def phase_shift(self, position, theta=tc.pi, control=None):
        for pp in position:
            tmp_gate = Gate.phase_shift(theta, device=self.device, dtype=self.dtype)
            self.add_single_gate(tmp_gate, position=[pp], control=control)

    def not_gate(self, position, control=None):
        for pp in position:
            tmp_gate = Gate.not_gate(device=self.device, dtype=self.dtype)
            self.add_single_gate(tmp_gate, position=[pp], control=control)

    def rand_gate(self, dim, position, control=None, requires_grad=False):
        tmp_gate = Gate.rand_gate(dim, device=self.device, dtype=self.dtype, requires_grad=requires_grad)
        self.add_single_gate(tmp_gate, position=position, control=control)

    def swap_gate(self, position, control=None):
        if len(position) != 2:
            print('wrong use')
        else:
            tmp_gate = Gate.swap_gate(device=self.device, dtype=self.dtype)
            self.add_single_gate(tmp_gate, position=position, control=control)

    def time_evolution(self, hamiltonian, time, position, control=None):
        tmp_gate = Gate.time_evolution(hamiltonian, time, device=self.device, dtype=self.dtype)
        self.add_single_gate(tmp_gate, position=position, control=control)

    def qft(self, position, control=None, inverse=False):
        if control is None:
            control = []
        tmp_circuit = qft(self.n_qubit, position=position, control=control, inverse=inverse, device=self.device, dtype=self.dtype)
        self.__extend(tmp_circuit)

    def ch(self, unitary, position_phi, position_c, control=None, inverse=False):
        tmp_circuit = ch(self.n_qubit, unitary, position_phi, position_c, control, inverse, device=self.device, dtype=self.dtype)
        self.__extend(tmp_circuit)

    def qpe(self, unitary, position_phi, position_qpe, control=None, inverse=False):
        tmp_circuit = qpe(self.n_qubit, unitary, position_phi, position_qpe, control, inverse, device=self.device, dtype=self.dtype)
        self.__extend(tmp_circuit)

    def add_one(self, position=None, control=None, inverse=False):
        tmp_circuit = add_one(self.n_qubit, position, control, inverse, device=self.device, dtype=self.dtype)
        self.__extend(tmp_circuit)

    def qhc(self, unitary, position_phi, position_qpe, position_f, n_f=None,
            control=None, inverse=False):
        tmp_circuit = qhc(self.n_qubit, unitary, position_phi, position_qpe, position_f,
                          n_f, control, inverse, device=self.device, dtype=self.dtype)
        self.__extend(tmp_circuit)

    def quantum_coin(self, unitary, position_phi, position_coin, control=None, inverse=False):
        tmp_circuit = quantum_coin(self.n_qubit, unitary, position_phi, position_coin,
                                   control, inverse, device=self.device, dtype=self.dtype)
        self.__extend(tmp_circuit)

    def qdc(self, unitary, position_phi, position_coin, position_f,
            n_f=None, control=None, inverse=False):
        tmp_circuit = qdc(self.n_qubit, unitary, position_phi, position_coin, position_f,
                          n_f, control, inverse, device=self.device, dtype=self.dtype)
        self.__extend(tmp_circuit)


def qft(n_qubit, position, control=None, inverse=False, device='cpu', dtype=tc.complex64):
    if control is None:
        control = []
    tmp_circuit = Circuit(n_qubit, device, dtype)
    m_qft = len(position)
    perm = list(range(m_qft))
    perm.reverse()
    theta_list = []
    theta = 2 * np.pi
    if inverse:
        theta = -theta
    for mm in range(m_qft + 1):
        theta_list.append(theta)
        theta = theta / 2
    for mm in range(m_qft):
        tmp_circuit.hadamard([position[mm]])
        for nn in range(mm + 1, m_qft):
            tmp_circuit.phase_shift(theta_list[nn - mm + 1], [position[mm]], control=[position[nn]] + control)
    for mm in range(m_qft // 2):
        tmp_circuit.swap_gate([position[mm], position[- mm - 1]], control=control)
    if inverse:
        tmp_circuit.inv()
    return tmp_circuit


def ch(n_qubit, unitary, position_phi, position_c, control=None, inverse=False, device='cpu', dtype=tc.complex64):
    if control is None:
        control = []
    tmp_circuit = Circuit(n_qubit, device, dtype)
    if isinstance(unitary, Gate.Gate):
        tmp_gate = Gate.Gate(unitary)
    elif isinstance(unitary, Circuit):
        tmp_gate = copy.deepcopy(unitary)
    else:
        raise TypeError('the unitary should be a gate')
    m_fch = len(position_c)
    for mm in range(m_fch):
        tmp_circuit.compose(tmp_gate, position_phi, [position_c[- mm - 1]] + control, inverse)
        tmp_gate.square()
    if inverse:
        tmp_circuit.inv()
    return tmp_circuit


def qpe(n_qubit, unitary, position_phi, position_qpe, control=None, inverse=False, device='cpu', dtype=tc.complex64):
    if control is None:
        control = []
    tmp_circuit = Circuit(n_qubit, device, dtype)
    tmp_circuit.hadamard(position_qpe, control=control)
    tmp_circuit.ch(unitary, position_phi, position_qpe, control, False)
    tmp_circuit.qft(position_qpe, control=control, inverse=True)
    if inverse:
        tmp_circuit.inv()
    return tmp_circuit


def qhc(n_qubit, unitary, position_phi, position_qpe, position_f, n_f=None,
        control=None, inverse=False, device='cpu', dtype=tc.complex64):
    tmp_circuit = Circuit(n_qubit, device, dtype)
    if control is None:
        control = []
    if n_f is None:
        n_f = 2 ** (len(position_f) - 1) - 1
    if n_f > (2 ** len(position_f) - 1) / 2:
        print('warning, n_f is too large')
    for nn in range(n_f):
        tmp_circuit.not_gate(position_f, control)
        tmp_circuit.qpe(unitary, position_phi, position_qpe,
                        control=position_f + control, inverse=False)
        # sample(1000, position_qpe)
        tmp_circuit.not_gate(position_f, control)
        tmp_circuit.add_one(position_f, [position_qpe[0]] + control, inverse=False)
        tmp_circuit.not_gate(position_f, control)
        tmp_circuit.qpe(unitary, position_phi, position_qpe,
                        control=position_f + control, inverse=True)
        tmp_circuit.not_gate(position_f, control)
        tmp_circuit.add_one(position_f, control=control, inverse=False)
        tmp_circuit.not_gate(position_qpe, control)
        tmp_circuit.add_one(position_f, control=position_qpe + control, inverse=True)
        tmp_circuit.not_gate(position_qpe, control)
    if inverse:
        tmp_circuit.inv()
    return tmp_circuit


def add_one(n_qubit, position=None, control=None, inverse=False, device='cpu', dtype=tc.complex64):
    tmp_circuit = Circuit(n_qubit, device, dtype)
    if control is None:
        control = []
    if position is None:
        position = list(range(n_qubit))
    m_a = len(position)
    for mm in range(m_a):
        tmp_circuit.not_gate([position[mm]], control=position[mm + 1:] + control)
    if inverse:
        tmp_circuit.inv()
    return tmp_circuit


def quantum_coin(n_qubit, unitary, position_phi, position_coin, control=None, inverse=False,
                 device='cpu', dtype=tc.complex64):
    tmp_circuit = Circuit(n_qubit, device, dtype)
    if control is None:
        control = []
    tmp_circuit.hadamard(position_coin, control)
    tmp_circuit.compose(unitary, position_phi, position_coin)
    tmp_circuit.not_gate(position_coin, control)
    tmp_circuit.compose(unitary, position_phi, position_coin, True)
    # self.phase_shift(-eig_value, position_coin, control)
    tmp_circuit.not_gate(position_coin, control)
    tmp_circuit.hadamard(position_coin, control)
    if inverse:
        tmp_circuit.inv()
    return tmp_circuit


def qdc(n_qubit, unitary, position_phi, position_coin, position_f, n_f=None,
        control=None, inverse=False, device='cpu', dtype=tc.complex64):
    tmp_circuit = Circuit(n_qubit, device, dtype)
    if control is None:
        control = []
    if n_f is None:
        n_f = 2 ** (len(position_f) - 1) - 1
    if n_f > (2 ** len(position_f) - 1):
        print('warning, n_f is too large')
    for nn in range(n_f):
        tmp_circuit.not_gate(position_f, control)
        tmp_circuit.quantum_coin(unitary, position_phi, position_coin, control=position_f + control, inverse=False)
        tmp_circuit.not_gate(position_f, control)
        tmp_circuit.add_one(position_f, position_coin + control, inverse=False)
    if inverse:
        tmp_circuit.inv()
    return tmp_circuit
