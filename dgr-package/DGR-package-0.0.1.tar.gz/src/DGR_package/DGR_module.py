import os
import sys
import getopt

import pkg_resources

def getFile():
	file = None

	argv = sys.argv[1:]
	try:
		opts, args = getopt.getopt(argv, "f:", 
					["file = "])
	except getopt.GetoptError:
		print("your_script.py -f file_name.ext")
		sys.exit(2)

	for opt, arg in opts:
		if opt in ["-f", "--file"]:
			file = arg
	if (not(os.path.exists(str(file)))):
		print("File does not exist in current directory")
		sys.exit(2)
	return(file)

def getDir():
	dir = None

	argv = sys.argv[1:]
	try:
		opts, args = getopt.getopt(argv, "d:", 
					["directory = "])
	except getopt.GetoptError:
		print("your_script.py -d directory_name/")
		sys.exit(2)

	for opt, arg in opts:
		if opt in ["-d", "--directory"]:
			dir = arg
	if (not(os.path.exists(str(dir)))):
		print("Directory does not exist")
		sys.exit(2)
	return(dir)

def getFileDir(file):
	fileDir = os.path.splitext(os.path.basename(file))[0] + "_file_directory"
	return(fileDir)

def getOutputFileDir(fileDirStr, fileNameStr): 
	return(fileDirStr + "/" + fileNameStr + "_genome_output")

def getFileName(file):
	fileName = os.path.splitext(os.path.basename(file))[0]
	return(fileName)

def checkDir(fileDir):
	if (not (os.path.isdir(fileDir))):
		os.system("mkdir "+ fileDir)

def truncateFile(file, str):
	if os.path.exists(getFileDir(file)):
		open(getFileDir(file) + "/" + getFileName(file) + str, "w").close()
		print("deleted " + getFileDir(file) + "/" + getFileName(file) + str)

def truncateOutputFile(file, str): 
	if os.path.exists(getOutputFileDir(getFileDir(file), getFileName(file))): 
		open(getOutputFileDir(getFileDir(file), getFileName(file)) + "/" + getFileName(file) + str, "w").close()
		print("deleted " + getOutputFileDir(getFileDir(file), getFileName(file)) + "/" + getFileName(file) + str)

def findRTs(file):
	data_path = pkg_resources.resource_filename("DGR_package", "data/")
	data_file = pkg_resources.resource_filename("DGR_package", "data/Custom_DGR_RT.hmm")
	os.system("prodigal -a "+ getFileDir(file) + "/" + getFileName(file) + "_prot_trans.fasta -f gbk -g 11 -i " + file + " -o " + getFileDir(file) + "/" + getFileName(file) + "_output.txt -p single -s " + getFileDir(file) + "/" + getFileName(file) + "_genomic_coord.txt")
#	os.system("hmmsearch --tblout " + getFileDir(file) + "/" + getFileName(file) + "_hmmer_table.txt Custom_DGR_RT.hmm " + getFileDir(file) + "/" + getFileName(file) + "_prot_trans.fasta")
	os.system("hmmsearch --tblout " + getFileDir(file) + "/" + getFileName(file) + "_hmmer_table.txt " + data_file + " " + getFileDir(file) + "/" + getFileName(file) + "_prot_trans.fasta")

def findAlignments(file):
	os.system("makeblastdb -in " + getFileDir(file) + "/" + getFileName(file) + "_window_output.fasta -dbtype nucl -out " + getFileDir(file) + "/" + getFileName(file) + "_blast_DB")
	os.system("blastn -db " + getFileDir(file) + "/" + getFileName(file) + "_blast_DB -query " + getFileDir(file) + "/" + getFileName(file) + "_window_output.fasta -outfmt 5 -out " + getFileDir(file) + "/" + getFileName(file) + "_alignments.xml -word_size 8 -reward 1 -penalty -1 -evalue 1e-5 -gapopen 6 -gapextend 6 -perc_identity 50")

def clusterTRVRs(file):
	os.system("cd-hit-est -i " +  getFileDir(file) + "/" + getFileName(file) + "_path_to_TR_sequences_file_for_output.fasta -o " + getOutputFileDir(getFileDir(file), getFileName(file)) + "/" + getFileName(file) + "_clustered_TR_sequences.fasta -c 0.95 -n 8")
	os.system("cd-hit-est -i " + getFileDir(file) + "/" + getFileName(file) + "_path_to_VR_sequences_file_for_output.fasta -o " + getOutputFileDir(getFileDir(file), getFileName(file)) + "/" + getFileName(file) + "_clustered_VR_sequences.fasta -c 0.95 -n 8")
