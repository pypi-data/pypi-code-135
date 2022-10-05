import pandas    as pd

# =============================================================================
# LAMMPS Frame (Multiple Frames)
# =============================================================================
class TrajMultiFrames:   
	"""Create an Object for a multi-FRAMEs of trajectories from MD simulation.

		- read frome XYZ file 
	""" 
	def __init__(self, **kwargs):
		"""initilize the TrajFrame object
		Note:
			Use mutator, so do not use self.* when define value
		"""
		##==== optional Inputs 
		## read DumpFile
		if 'readXYZ' in kwargs:
			filename = kwargs['readXYZ']
			self.readXYZ(filename)
		elif 'readPDB' in kwargs:
			filename = kwargs['readPDB']
			self.readPDB(filename)	
		else: raise Exception('file format is unsupported')
		## some initial setting
		self.fmtSTR = "%.6f"    # dont use %g, because it will lost precision

		return
	#####=======
	

	def readXYZ(self, filename):
		"""The **method** create Multi-FRAME object by reading XYZ file.
		
		Args:
			filename (str): name of input file

		Returns:
			Obj (TrajFrame): update FRAME

		Examples:
			```py
			da = io.TrajFrame(pdb_file='mydata.pdb')
			```
		"""
		## Read whole text and break lines
		with open(filename,'r') as fileID:
			C = fileID.read().splitlines()              # a list of strings

		## Extract positions of block
		P = [line.split(" ") for line in C]          # list-of-lists
		blockIndex=[i for i,line in enumerate(P) if len(line)==1 ]
		## Extract each block as frame
		ldf = [None]*(len(blockIndex))
		for i,item in enumerate(blockIndex):
			if i < (len(blockIndex)-1):
				data = P[blockIndex[i]+2 : blockIndex[i+1]]    # list-of-lists
			else: 
				data = P[blockIndex[i]+2 :] 

			## extract columns
			if i==0:
				myColumn = ['element','x','y','z']
				if len(data[0])>4:
					for k in range(4,len(data[0])):
						myColumn = myColumn + ['c'+str(k-3)]
			## Conert type on some columns of DataFrame
			df0 = pd.DataFrame(data, columns=myColumn)  # create DataFrame
			df1 = df0.drop('element',axis=1).astype(float)
			df = pd.concat([df0['element'],df1], axis=1)
			ldf[i] = df

		## Save out put to CLASS's attributes
		self.name      = filename
		self.frame     = ldf           # List of DataFrame
		return
	#####=======

