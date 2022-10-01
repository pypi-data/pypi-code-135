import pysam
class ComparaBAM(object):
	"""docstring for ComparaBAM"""
	def __init__(self, path):
		super(ComparaBAM, self).__init__()
		self.path = path
		self.samfile = pysam.AlignmentFile(path, "rb")

	def msa(self, chromosome = "6A", 
		start = 550635582, 
		end   = 550644763 ):
		iter = samfile.fetch("seq1", 10, 20)
		for x in iter:
    		print (str(x))
    		break
		pass
		