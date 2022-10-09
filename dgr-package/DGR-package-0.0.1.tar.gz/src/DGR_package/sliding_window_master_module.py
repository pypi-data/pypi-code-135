from itertools import product
from Bio import SeqIO
import csv
import os
import sys
import getopt
import DGR_package.DGR_module as DGR_module

def slidingWindow(dna,winSize,step,fileout,name):
	
	try: it = iter(dna)
	except TypeError:
		raise Exception("**ERROR** sequence must be iterable.")
	if not ((type(winSize) == type(0)) and (type(step) == type(0))):
		raise Exception("**ERROR** type(winSize) and type(step) must be int.")
	if step > winSize:
		raise Exception("**ERROR** step must not be larger than winSize.")
	if winSize > len(dna):
		return
	# Pre-compute number of chunks to emit
	numOfChunks = (int) (((len(dna)-winSize)/step)+1)
	
	# Do the work
	x=1
	for i in range(0,numOfChunks*step,step):
		
		y=x+winSize
		xs=str(x)
		ys=str(y)
		dna_window = dna[i:i+winSize]
		dna_window=str(dna_window)
		output = open(fileout, "a")
		output.write('>' + name + '_' + xs + '_' + 'to' + '_' + ys + '\n' + dna_window + '\n')
		x=x+50
	
#def getFile():
#	file = None
#	inputFile = None

#	argv = sys.argv[1:]
#	try:
#		opts, args = getopt.getopt(argv, "f:i:", ["file = ", "input = "])
#	except getopt.GetoptError: 
#		print("your_script.py -f file_name.ext -i input_file_name.ext")
#		sys.exit(2)

#	for opt, arg in opts: 
#		if opt in ["-f", "--file"]:
#			file = arg
#		elif opt in ["-i", "--input"]: 
#			inputFile = arg
#	if (not(os.path.exists(str(file)))):
#		print("File does not exist in current directory")
#		sys.exit(2)
#	files = {"file" : file, "input" : inputFile}
#	print(files)
#	return(files)


def get_windows(sequence,win,by,fileout):
	for record in SeqIO.parse(sequence, 'fasta'):
		newseq=record.seq
		name=record.id
		print("created sliding window for " + record)
		slidingWindow(newseq,win,by,fileout,name)
		
#creates a directory for all intermediate files, stores files in directory	
#fileDir = DGR_module.getFileDir()
#fileName = DGR_module.getFileName()
#if (not (os.path.isdir(fileDir))):
#        os.system("mkdir "+ fileDir)

#figure out how to pass the file
#get_windows((getFile()["input"]), 200,50, fileDir + "/" + fileName + "_window_output.fasta")
