from quspin_vqa.algo.qaoa import QAOA
import scipy.linalg as la
import numpy as np
import scipy.optimize as opt
from quspin_vqa.utils import hamiltonian_s
from itertools import product
from quspin_vqa.utils import normalize
import random
import wandb


class VQITE(QAOA):
    """Variational QITE ansatz

    Use the QITE ansatz to solve the optimization problem. Here, the ansatz is the complete;
    As opposed to the compact ansatz, which is a low rank approximation the complete ansatz.
    """

    def __init__(self, physics_system, q, pauli_site):
        """Initialize the CVQITE ansatz.

        Args:
            physics_system (PhysicsSystem): the physics system.
            q (int): the number of qubits.
            ham_pool_length (int): the length of the hamiltonian pool.
            pauli_site (int): the numbers of the sites the pauli operator acts on.
        """
        self._name = 'v-QITE'
        self.physics_system = physics_system
        self._extract_physics_system()
        self.q = q
        self.params = None

        # generate the pauli hamiltonian pool
        self._pauli_pool = ['I', 'x', 'y', 'z']
        self.pauli_site = pauli_site
        self._generate_ham_pool()

    def _generate_ham_pool(self):
        """Generate the pool of hamiltonians.
        """
        # hamiltonian pool
          
        # shallowly thinking about this
        # the hamiltonian pool grows exponentially
        # TODO: check that 
        basis = self.physics_system.basis
        L = self.physics_system.L
        sites = list(range(L))

        pauli_str_list = list(map(lambda x: ''.join(x), product(self._pauli_pool, repeat=self.pauli_site)))

        # pauli_str_list = random.sample(pauli_str_list, k=100)
        pauli_str_list = random.sample(pauli_str_list, k=10)

        print('the pauli string pattern: ', ' '.join(pauli_str_list))
        ham_pool = []
        for pauli_str in pauli_str_list:
            static = [[pauli_str, [[1, *sites]]]]
            ham_pool.append(hamiltonian_s(static, [], basis=basis, check_herm=False).tocsc())
        
        # ham_pool = random.sample(ham_pool, k=10)
        self.ham_pool = ham_pool
        self.ham_pool_length = len(ham_pool)

    def _initial_x0(self):
        """Generate the initial guess of the parameters.
        """
        x0 = np.random.uniform(0, 2 * np.pi, self.q * self.ham_pool_length)
        return normalize(x0, normal_val=self.q * self.ham_pool_length)

    @property
    def initial_guess(self):
        """Generate the initial guess for the sovler
        """
        return self._initial_x0()
        

    def evolve(self, params):
        """Evolve the system with the given parameters.

        Args:
            variational_ansatz (tuple): the ordering of the hamiltonians
            params (np.ndarray): the parameters of the variational ansatz.
        """
        u = np.copy(self.psi_initial)

        assert len(params) % self.ham_pool_length == 0, "The number of parameters should be the multiple of hamiltonian pool length."
        N_q = len(params) // self.ham_pool_length
        
        for i in range(N_q):
            mat = sum([ c * h for c, h in zip(params[i * self.ham_pool_length: (i + 1) * self.ham_pool_length], self.ham_pool)])
            expmat = la.expm(-1j * mat).toarray()
            u = np.dot(expmat, u)
        return u

    def fidelity(self, params):
        """Compute the fidelity between the target state and the evolved state.
        """
        u = self.evolve(params)
        wandb.log({'fidelity': self._compute_fidelity(u)})
        return self._compute_fidelity(u)

    def expected_energy(self, params):
        """Compute the expected energy of the evolved state.
        """
        u = self.evolve(params)
        return self._compute_expected_energy(u)

    def get_reward(self, params, reward_type='fidelity'):
        """Compute the reward of the evolved state.
        """
        if reward_type == 'fidelity':
            return self.fidelity(params)
        elif reward_type == 'energy':
            return - self.expected_energy(params)
        else:
            raise NotImplementedError("The reward type is not supported.")

    # TODO: add the noise reward (maybe to the noise module, which is supposed to add more method to the class)

    @property
    def name(self):
        return self._name