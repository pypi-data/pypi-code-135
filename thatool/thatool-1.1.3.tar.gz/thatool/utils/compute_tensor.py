import numpy as np


def ke_tensor(vx, vy, vz, mass, kb):
	"""Compute Kinetic Energy tensors, and Temp
	NOTE: - vx, vy, vz : 1D vector of components of per-atom velocity
		  - m : 1D vector of atomic mass
		  - inUNIT=['angstrom','ps','amu','eV'], outUNIT=['eV','K']
	Return: Kinetic energy tensor, Kinetic scalar, Temperature scalar"""
	import scipy.constants as sc
	# refine input & convert inUNIT to SI unit
	veloFact=sc.angstrom/sc.pico      # velocity unit A/ps --> m/s
	vx=np.asarray(vx)*veloFact; vy=np.asarray(vy)*veloFact; vz=np.asarray(vz)*veloFact
	m = np.asarray(mass)*sc.atomic_mass  # mass unit amu --> kg
	kb = kb*sc.eV                     # Boltzmann constant in eV/K --> J/K    
	# compute kinetic energy tensor  
	Kxx = (1/2)*np.einsum('i,i,i',m,vx,vx)  # Element-wise multiply, then summing
	Kyy = (1/2)*np.einsum('i,i,i',m,vy,vy)
	Kzz = (1/2)*np.einsum('i,i,i',m,vz,vz)
	Kxy = (1/2)*np.einsum('i,i,i',m,vx,vy)
	Kxz = (1/2)*np.einsum('i,i,i',m,vx,vz)
	Kyz = (1/2)*np.einsum('i,i,i',m,vy,vz)
	KEtensor = np.array([Kxx, Kyy, Kzz, Kxy, Kxz, Kyz])
	# Kinetic energy & Temperature
	KE = Kxx + Kyy + Kzz
	Temp = (2*KE)/ (3*vx.shape[0]*kb)
	# Convert SI unit to outUNIT 
	KEtensor = KEtensor/sc.eV   # energy J --> eV
	KE = KE/sc.eV
	return KEtensor, KE, Temp 
## --------



def stress_tensor(per_atom_stress_tensor, atomic_volume,unitFac=1):
	"""Compute local pressure/stress
	NOTE: - per_atom_stress_tensor : Nx6 array of the per-atom stress tensor
		  - atomVol    : Nx1 vector of atomVol
		  - inUNIT=['bar','angstrom'], outUNIT=['bar'] --> unitFac=1e-4 for ['GPa'] 
	Return: pressure scalar, Stress tensor """                                                                     
	# refine input
	S = np.array(per_atom_stress_tensor)                                                                       
	# compute stress/pressureure tensor
	Sxx = unitFac*sum(S[:,0])/sum(atomic_volume)
	Syy = unitFac*sum(S[:,1])/sum(atomic_volume)
	Szz = unitFac*sum(S[:,2])/sum(atomic_volume)
	Sxy = unitFac*sum(S[:,3])/sum(atomic_volume)
	Sxz = unitFac*sum(S[:,4])/sum(atomic_volume)
	Syz = unitFac*sum(S[:,5])/sum(atomic_volume)  
	stress_tensor = np.array([Sxx, Syy, Szz, Sxy, Sxz, Syz])
	# static pressureure   
	pressure = -(Sxx + Syy + Szz)/3
	return pressure, stress_tensor  