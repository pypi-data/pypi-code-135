"""
This module contains functions to define some specific scripts.
"""


import numpy as np
from ..model            import box_orientation, CoordTransform, shells_fcc


## Define scipt to copmute FCCUBIC:
def FCCUBIC_script(a_fcc,zDirect, label='mcv',
				   alpha=27, partialCompute=False, atoms='@mdatoms', atomsA=None, atomsB=None, options=''):
	"""PLUMED script to compute FCCUBIC

	Args:
		a_fcc (float): Lattice constant of FCC crystal
		zDirect (str): specify the z-direction of crystal
		label (str): label of PLUMED command
		alpha (int): ALPHA parameter to compute FCCUBIC colvar.
		atoms (str): specify atom-ids in computed group.
		partialCompute (bool): compute for some atoms.
		atomsA (str): specify atom-ids in group A.
		atomsB (str): specify atom-ids in group B.
		options (str): add options.

	Returns:
		list (list): list of strings.
	"""
	## select atoms
	if partialCompute:
		if not atomsA or not atomsB:
			raise Exception('Must set keywords: "atomsA" and "atomsB"')
	else:
		if not atoms:
			raise Exception('Must set keywords: "atoms"')

    ##$ Switching: CUBIC --> compute d0 from lattice constant
    ## FCC_shells
	shell = shells_fcc(a_fcc)
	shell_1, shell_2 = shell[0], shell[1]
	## Cutoff
	d0   = shell_1 + (shell_2 - shell_1)/20
	dmax = shell_1 + (shell_2 - shell_1)/2  # distance between shell 1 and shell 2

    ### =============================================================================
    ### print FCCUBIC setting
    ### =============================================================================
	## compute Euler Angles
	newAxis,_ = box_orientation(zDirect=zDirect)
	oldAxis = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
	BT = CoordTransform(old_orient=newAxis, new_orient=oldAxis)        # use reverse rotation since FCCUBIC roteate positions to principal axes then calculated it
	Phi,Theta,Psi = BT.euler_angle(unit='rad')

	##
	C = []
	C.append('%s: FCCUBIC ...'                             %(label) )
	C.append('\tSWITCH={CUBIC D_0=%.8f D_MAX=%.8f}'        % (d0, dmax) )
	C.append('\tALPHA=%i PHI=%.10f THETA=%.10f PSI=%.10f'  % (alpha, Phi, Theta, Psi) )
	if partialCompute:
		C.append('\tSPECIESA=%s SPECIESB=%s %s'            %(atomsA, atomsB, options) )
	else:
		C.append('\tSPECIES=%s %s'                         %(atoms, options) )
	C.append('...')
	return C
##====


## Define scipt to copmute FCCUBIC:
def LOCAL_CRYSTALINITY_script(a_fcc,zDirect, label='mcv',
							  vectors=[[1,0,0], [0,1,0], [0,0,1]], atoms='@mdatoms', options=''):
	"""PLUMED script to compute LOCAL_CRYSTALINITY

	Args:
		a_fcc (float): Lattice constant of FCC crystal
		zDirect (str): specify the z-direction of crystal
		label (str): label of PLUMED command
		vectors (list): 2xN list of lists, to specify directions of reciprocal vectors.
		atoms (str): specify atom-ids in computed group.
		options (str): add options.

	Returns:
		list (list): list of strings.	
	"""
    ##$ Switching: CUBIC --> compute d0 from lattice constant
    ## FCC_shells
	shell = shells_fcc(a_fcc)
	shell_1, shell_2 = shell[0], shell[1]
	## Cutoff
	d0 = shell_1 + (shell_2 - shell_1)/8
	dmax = shell_1 + (shell_2 - shell_1)*2/5  # distance between shell 1 and shell 2

    ### =============================================================================
    ### print LOCAL_CRYSTALINIY setting
    ### =============================================================================
	## compute reciprocal vectors
	g = (4*np.pi/a_fcc)*np.asarray(vectors)
	## Rotate vectors
	newAxis,_ = box_orientation(zDirect=zDirect)
	BT = CoordTransform(new_orient=newAxis)          # old_orient=newAxis,
	g = BT.rotate_3d(g)
	##
	C = ['{:s}: LOCAL_CRYSTALINITY ...'.format(label)]
	C.append('\tSPECIES={:s}'.format(atoms) )
	C.append('\tSWITCH={CUBIC D_0=%.8f D_MAX=%.8f}' % (d0,dmax) )
	## G-vetors
	for i in range(g.shape[0]):
		C.append("\tGVECTOR%i=%.9f,%.9f,%.9f" 		% (i+1, g[i,0], g[i,1], g[i,2]) )

	C.append('\t{:s}'.format(options) )
	C.append('...')
	return C
##====





## Define scipt to copmute LogMFD:
def LOGMFD_script(ARG, FICT, FICT_MIN, FICT_MAX, TEMP, DELTA_T,
                  INTERVAL, KAPPA, deltaF, deltaX, kB, label='mfd', FLOG=5000, MFDstat='VS'):
	"""PLUMED script to compute LOGFMD

	Args:
		ARG (str): the scalar input for this action
		FICT (float): The initial values of the fictitious dynamical variables
		FICT_MIN (float): Boundaries of CV_space 
		FICT_MAX (float): Boundaries of CV_space
		TEMP (float): Temperature of the fictitious dynamical variables
		DELTA_T (float): Time step for the fictitious dynamical variables (MFD step)
		INTERVAL (int): Period of MD steps ( Nm) to update fictitious dynamical variables
		KAPPA (int): Spring constant of the harmonic restraining potential for the fictitious dynamical variables
		deltaF (float): Energy Barrier to estimate ALPHA (Alpha parameter for LogMFD)
		deltaX (float): CV distance at each MFDstep, to estimate MFICT, VFICT (mass & velocity of fictitious dynamical variable)
		kB (float): Boltzmann constant
	    label (str): label of PLUMED command
		FLOG (float): The initial free energy value in the LogMFD, initial F(X)
		MFDstat (str): Type of thermostat for the fictitious dynamical variables. NVE, NVT, VS are available.
		
	Returns:
		list (list): list of strings.			
	"""
	### =============================================================================
	### estimated ALPHA
	### =============================================================================
	ALPHA = (1.5/(kB*TEMP)) *np.log(deltaF/(kB*TEMP))         # deltaF in unit eV
	### estimated MFICT + VFICT (initial velocity)
	MFICT = kB*TEMP * (DELTA_T/deltaX)**2
	VFICT = np.sqrt( (kB*TEMP)/MFICT )

	### =============================================================================
	## Define scipt to copmute LogMFD:
	### =============================================================================
	D = []
	D.append('%s: LOGMFD ...'                         % (label))
	D.append('\tARG=%s'                               % (ARG))
	D.append('\tFICT=%.7f FICT_MIN=%.7f FICT_MAX=%.7f'% (FICT, FICT_MIN, FICT_MAX) )
	D.append('\tTEMP=%.2f DELTA_T=%.2f INTERVAL=%i'   % (TEMP,DELTA_T,INTERVAL) )
	D.append('\tFLOG=%.1f ALPHA=%f KAPPA=%g '         % (FLOG,ALPHA,KAPPA) )
	D.append('\tMFICT=%f VFICT=%f '                   % (MFICT,VFICT) )
	D.append('\tTHERMOSTAT=%s'                        % (MFDstat) )
	## for NVT thermostat
	if MFDstat=='NVT':
		META = MFICT/1                          # or take: kB*temp *10000
		VETA = np.sqrt( (kB*TEMP)/META )
		D.append('\tMETA=%f VETA=%f'  % (META, VETA))
	D.append('...')
	return D



