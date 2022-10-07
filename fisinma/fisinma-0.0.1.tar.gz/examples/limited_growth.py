#!/usr/bin/env python3

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


# Import custom functions for optimization
from FisInMa.solving import fischer_determinant
from FisInMa.data_structures import FischerModel
from FisInMa.optimization import find_optimal


# System of equation for pool-model and sensitivities
###############################
### USER DEFINES ODE SYSTEM ###
###############################
def exp_growth(y, t, Q, P, Const):
    (a,) = P
    (Temp,) = Q
    (n_max,) = Const
    (n, sa) = y
    return [
        Temp * a * (n_max - n),
        Temp *     (n_max - n) - Temp * a * sa
    ]


if __name__ == "__main__":
    ###############################
    ### USER DEFINES PARAMETERS ###
    ###############################

    # Define constants for the simulation duration
    n_max = 2e4
    constants = (n_max,)

    # Define initial parameter guesses
    a = 0.065
    parameters = (a,)

    # Define bounds for sampling
    temp_low = 3.0
    temp_high = 8.0

    # Define bounds for times
    times_low = 0.0
    times_high = 16.0

    # Initial values for complete ODE (with S-Terms)
    n0 = 0.25
    y0_t0 = (np.array([n0, 0]), times_low)

    # Construct parameter hyperspace
    n_times = 4
    n_temps = 3
    
    # Values for temperatures (Q-Values)
    q_values = [
        np.linspace(temp_low, temp_high, n_temps)
    ]
    
    # Choose initial guess of time values
    times = np.full((n_temps, n_times,), np.linspace(times_low, times_high, n_times))

    # Create a complete Fischer Model
    fsm = FischerModel(
        times=times,
        parameters=parameters,
        q_values=q_values,
        constants=constants,
        y0_t0=y0_t0,
        ode_func=exp_growth,
        observable_func=fischer_determinant
    )

    ####################
    ### OPTIMIZATION ###
    ####################
    fsr = find_optimal(times, times_high, fsm, "scipy_differential_evolution", discrete=0.5)
    print(fsr.times)
    print(fsr.observable)
    d = fsr.observable
    solutions = fsr.ode_solutions

    ####################
    ##### PLOTTING #####
    ####################
    fig, axs = plt.subplots(len(solutions), figsize=(12, 4*len(solutions)))
    for i, (t, q, r) in enumerate(solutions):
        # Plot solution to ode
        t_values = np.linspace(times_low, times_high)
        res = sp.integrate.odeint(exp_growth, y0_t0[0], t_values, args=(q, fsm.parameters, fsm.constants)).T[0]
        axs[i].plot(t_values, res, color="#21918c", label="Ode Solution")

        # Determine where multiple time points overlap by rounding
        t_round = t.round(1)
        unique, indices, counts = np.unique(t_round, return_index=True, return_counts=True)

        # Plot same time points with different sizes to distinguish
        axs[i].scatter(unique, r[0][indices], s=counts*80, alpha=0.5, color="#440154", label="Q_values: " + str(q))
        axs[i].legend()
    fig.savefig("out/Result.svg")
