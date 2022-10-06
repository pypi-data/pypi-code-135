import numpy as np

# Generates orthogonal sets of search directions from one provided direction
def householder(q):
    H = np.identity(len(q)) - 2 / np.dot(q.T,q) * np.outer(q,q)
    
    return H


# Generates a set of non-dimensional poll points
def poll_points(ndim, ratio):
    # Generate a random a set of orthogonal poll direction vectors
    q = np.random.rand(ndim,1)
    H = householder(q)

    # Find intersection of search directions with bounding hyperplanes
    built = False
    for i in range(0, H.shape[0]):
        for j in range(0, H.shape[0]):
            intersect = H[i,:] / H[i,j]
            if np.max(np.abs(intersect))==1.0:
                if built==False:
                    points = intersect
                    built = True
                else:
                    points = np.vstack((points,intersect))
                points = np.vstack((points,-intersect))

    # Round the points to the nearest mesh point on the hyperplane
    points = np.round((points + 1) / 2 / ratio) * ratio * 2 - 1
    
    return points


# The OrthoMADS optimizer
def orthomads(design_variables, bounds_upper, bounds_lower, objective_function, dp_tol, nitermax, displog):
    # Set the print options
    np.set_printoptions(formatter={'float': '{: 0.10f}'.format})

    # Get the dimensions of the design space
    ndim = np.shape(design_variables)[0]
    
    # Define starting non-dimensional poll and mesh sizes
    dp = 1
    dm = 1

    # Evaluate the initial objective function
    optimal_objective = objective_function(design_variables)
    optimal_variables = np.copy(design_variables)

    # Store a history of all objective functions and design variables evaluated
    objective_history = np.array([optimal_objective])
    variables_history = np.copy(design_variables)
    
    # Store the number of iterations and function evaluations
    niter = 1
    neval = 0

    # Iterate until the poll size or iteration tolerances are met
    while dp>dp_tol and niter <= nitermax:
        # Get poll points on a non-dimensional hypersurface
        trial_points = poll_points(ndim, dm/dp)

        # Dimensionalize the poll points using the bounds and poll size
        for i in range(0, ndim):
            trial_points[:,i] = trial_points[:,i] * (bounds_upper[i] - bounds_lower[i]) * dp / 2 + optimal_variables[i]

        # Evaluate the objective function at the poll points
        for i in range(0, trial_points.shape[0]):
            # Assume the poll point should be evaluated
            skip = False
            
            # Verify the poll point is within the lower/upper bounds
            for j in range(0, ndim):
                if trial_points[i,j] < bounds_lower[j] or trial_points[i,j] > bounds_upper[j]:
                    skip = True
                    
            # Verify the poll point has not been evaluated already
            if neval > 0:
                for j in range(0, variables_history.shape[0]):
                    if np.amax(np.absolute(trial_points[i,:] - variables_history[j,:])) == 0:
                        skip = True
            
            # Evaluate if it is inside bounds and not previously evaluated
            if skip==False:
                trial_objective = objective_function(np.copy(trial_points[i,:]))
                variables_history = np.vstack((variables_history,trial_points[i,:]))
                objective_history = np.vstack((objective_history,np.array([trial_objective])))
                neval = neval + 1
                if displog: 
                    if trial_objective > 0:
                        print('Objective: ', '%.10f' % trial_objective, 'Parameters:', trial_points[i,:], 'Iter/Eval:', niter, neval)
                    else:
                        print('Objective:', '%.10f' % trial_objective, 'Parameters:', trial_points[i,:], 'Iter/Eval:', niter, neval)
        
        # If the minimum is less than the incumbent then replace and shrink the mesh/poll sizes
        if(np.min(objective_history) < optimal_objective):
            optimal_objective = np.min(objective_history)
            optimal_variables = variables_history[np.argmin(objective_history), :]
            dp = dp * 2
            dm = dm * 4
        else:
            dp = dp / 2
            dm = dm / 4

        # Increment in the iteration count
        niter = niter + 1

    # Print progress to the console
    if displog: 
        print('\nOptimization Results...')
        print('Objective:', '%.10f' % optimal_objective, 'Parameters:', optimal_variables)

    return optimal_objective, optimal_variables