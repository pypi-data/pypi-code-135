import importlib
import DGR_package.DGR_module as DGR_module
importlib.reload(DGR_module)
import DGR_package.parse_hmmer_module as parse_hmmer_module
importlib.reload(parse_hmmer_module)
import DGR_package.sliding_window_master_module as sliding_window_master_module
importlib.reload(sliding_window_master_module)
import DGR_package.BlastXML_to_alignment_module as BlastXML_to_alignment_module
importlib.reload(BlastXML_to_alignment_module)
import DGR_package.generate_VR_TR_RT_summary_table_module as generate_VR_TR_RT_summary_table_module
importlib.reload(generate_VR_TR_RT_summary_table_module)
import os
import csv
from csv import reader

def find_DGRs(file):
	fileDir = DGR_module.getFileDir(file)
	fileName = DGR_module.getFileName(file)
	fileOutputDir = DGR_module.getOutputFileDir(DGR_module.getFileDir(file), DGR_module.getFileName(file))

	DGR_module.truncateFile(file, "_prot_trans.fasta") #added
	DGR_module.truncateFile(file, "_prot_trans.gbk")
	DGR_module.truncateFile(file, "_genomic_coord.txt")
	DGR_module.truncateFile(file, "_output.txt")
	DGR_module.truncateFile(file, "_20kbs.fasta")
	DGR_module.truncateFile(file, "_hmmer_table.txt")
	DGR_module.truncateFile(file, "_summary_table.txt")
	DGR_module.truncateFile(file, "_window_output.fasta")
	DGR_module.truncateFile(file, "_blast_DB")
	DGR_module.truncateFile(file, "_blast_DB.nhr")
	DGR_module.truncateFile(file, "_blast_DB.nin")
	DGR_module.truncateFile(file, "_blast_DB.nsq")
	DGR_module.truncateFile(file, "_alignments.xml")
	DGR_module.truncateFile(file, "_DGR_csv.csv")
	DGR_module.truncateFile(file, "_prot_trans.gbk")
	DGR_module.truncateFile(file, "_path_to_TR_sequences_file_for_output.fasta")
	DGR_module.truncateFile(file, "_path_to_VR_sequences_file_for_output.fasta")
	DGR_module.truncateOutputFile(file, "_clustered_TR_sequences.fasta")
#	DGR_module.truncateOutputFile(file, "_clustered_TR_sequences.clstr")
	DGR_module.truncateOutputFile(file, "_clustered_VR_sequences.fasta")
#	DGR_module.truncateOutputFile(file, "_clustered_VR_sequences.clstr")
	DGR_module.truncateOutputFile(file,  "_RT_sequences.fasta")
	DGR_module.truncateOutputFile(file, "_RT_coordinates_table.csv")

	DGR_module.checkDir(fileDir)
	DGR_module.checkDir(fileOutputDir)

	DGR_module.findRTs(file)

	parse_hmmer_module.parseTable(file)
	file_20kbs = fileDir + "/" + fileName + "_20kbs.fasta"

	if (os.stat(fileDir + "/" + fileName + "_20kbs.fasta").st_size != 0):
		file_window_output = fileDir + "/" + fileName + "_window_output.fasta"
		sliding_window_master_module.get_windows(file_20kbs, 200, 50, file_window_output)

		DGR_module.findAlignments(file)

		BlastXML_to_alignment_module.findVRTRs(file)

		DGR_module.clusterTRVRs(file)
	print()
	print("Done!")

def clear_global_files(globalOutputFolder, dirName):
	if os.path.exists(globalOutputFolder + "/All_VRs_" + dirName + ".fasta"):
		open(globalOutputFolder + "/All_VRs_" + dirName + ".fasta", "w").close()
	if os.path.exists(globalOutputFolder + "/All_TRs_" + dirName + ".fasta"):
		open(globalOutputFolder + "/All_TRs_" + dirName + ".fasta", "w").close()
	if os.path.exists(globalOutputFolder + "/TR_VR_RT_" + dirName + "_summary_table.csv"):
		open(globalOutputFolder + "/TR_VR_RT_" + dirName + "_summary_table.csv", "w").close()
	if os.path.exists(globalOutputFolder + "/All_RTs_" + dirName + ".fasta"): 
		open(globalOutputFolder + "/All_RTs_" + dirName + ".fasta", "w").close()
	if os.path.exists(globalOutputFolder + "/RT_" + dirName + "_summary_table.csv"):
		open(globalOutputFolder + "/RT_" + dirName + "_summary_table.csv", "w").close()

#	with open(globalOutputFolder + "/TR_VR_RT_" + dirName + "_summary_table.csv", "w") as summary_file: 
#		summary_writer = csv.writer(summary_file)
#		summary_writer.writerow(["Genome", "Contig", "Feature", "Start", "Stop"])


def generate_file_summary(file, dirName):
	fileDir = DGR_module.getFileDir(file)
	fileName = DGR_module.getFileName(file)
	fileOutputDir = DGR_module.getOutputFileDir(fileDir, fileName) #in ""_file_directory, inner output file
	globalOutputFolder = dirName + "_output" #in same directory, global output file
	DGR_module.checkDir(globalOutputFolder)

	#string file names for global output
	globalAllTRs = globalOutputFolder + "/All_TRs_" + dirName + ".fasta"
	globalAllVRs = globalOutputFolder + "/All_VRs_" + dirName + ".fasta"
	globalTRVRRT = globalOutputFolder + "/TR_VR_RT_" + dirName + "_summary_table.csv"
	globalAllRTs = globalOutputFolder + "/All_RTs_" + dirName + ".fasta"
	globalRTSummary = globalOutputFolder + "/RT_" + dirName + "_summary_table.csv"

	#string file names for genome output
	VR_path = fileOutputDir + "/" + fileName + "_clustered_VR_sequences.fasta"
	TR_path = fileOutputDir + "/" + fileName + "_clustered_TR_sequences.fasta"
	RT_sequence_path = fileOutputDir + "/" + fileName + "_RT_sequences.fasta"
	RT_coord_path = fileOutputDir + "/" + fileName + "_RT_coordinates_table.csv" 

	#global TR, VR, RT summary file generation
	if (os.path.exists(VR_path) and os.path.exists(TR_path)):
		print("\n" + "TR and VR path exist: " + str(os.path.exists(VR_path) and os.path.exists(TR_path)) + "\n")
		os.system("cat " + VR_path + " >> " + globalAllVRs) #global file
		os.system("cat " + TR_path + " >> " + globalAllTRs) #global file
		with open(globalTRVRRT, "a") as summary_file: 
			if (os.stat(globalTRVRRT).st_size == 0):
				summary_writer = csv.writer(summary_file)
				summary_writer.writerow(["Genome", "Contig", "Feature", "Start", "Stop"])
		TR_dict = generate_VR_TR_RT_summary_table_module.getDict(str(file), "TR")
		TR_dict = generate_VR_TR_RT_summary_table_module.checkForSplit(TR_dict)
		VR_dict = generate_VR_TR_RT_summary_table_module.getDict(str(file), "VR")
		VR_dict = generate_VR_TR_RT_summary_table_module.checkForSplit(VR_dict)
		full_dict = generate_VR_TR_RT_summary_table_module.combineDicts(TR_dict, VR_dict)
		print("full dict" + "\n")
		print(full_dict)
		generate_VR_TR_RT_summary_table_module.writeTableToFile(str(file), full_dict, globalTRVRRT) #global file
		test_file = open(globalTRVRRT)
		file_contents = test_file.read()
		print(file_contents)
		generate_VR_TR_RT_summary_table_module.checkDGRInRT(RT_coord_path, globalTRVRRT)

	#global RT file generation
	print(os.path.exists(RT_sequence_path) and os.path.exists(RT_coord_path))
	with open(globalRTSummary, "a", newline = "") as csvfile:
		print("opened csvfile")
		RT_writer = csv.writer(csvfile)
		if (os.path.exists(RT_sequence_path) and os.path.exists(RT_coord_path)): 
			print("\n" + "RT path exists: " + str((os.path.exists(RT_sequence_path) and os.path.exists(RT_coord_path))))
			os.system("cat " + RT_sequence_path + " >> " + globalAllRTs)
			if (os.stat(globalRTSummary).st_size == 0):
				RT_writer.writerow(["ID", "Start_Pos", "Stop_Pos", "Direction", "Clade", "Contains DGR"])
			with open (RT_coord_path, 'r') as read_obj:
				csv_reader = reader(read_obj)
				next(csv_reader)
				for row in csv_reader:
					RT_writer.writerow(row)

def extract_amino_acid_seq(file):
	fileDir = DGR_module.getFileDir(file)
	fileName = DGR_module.getFileName(file)
	prot_trans_path = fileDir + "/" + fileName + "_prot_trans.fasta"
	if (os.path.exists(prot_trans_path)):
		with open(prot_trans_path, 'r') as read_obj:
# fix this for prot_trans file			for q_result in SearchIO.parse(fileDir + "/" + fileName + "_hmmer_table.txt", "hmmer3-tab"):
				for hit in q_result:
					title = hit.description()

def run_file_cmd():
	file = DGR_module.getFile()
	find_DGRs(file)
	dirName = DGR_module.getFileName(file)
	globalOutputFolder = dirName + "_output"
	clear_global_files(globalOutputFolder, dirName)
	generate_file_summary(file, dirName)

def run_file_path(file):
	find_DGRs(file)
	dirName = DGR_module.getFileName(file)
	globalOutputFolder = dirName + "_output"
	clear_global_files(globalOutputFolder, dirName)
	generate_file_summary(file, dirName)

def run_folder(dir):
	dirName = dir
	if (dir[-1] == "/"):
		dirName = dir[0:-1]
	else: #check success of else block
		dir = dir + "/"
	dirName = os.path.basename(dirName)
	print(dirName)
	globalOutputFolder = dirName + "_output"
#	DGR_module.checkDir(fileOutputFolder)

	clear_global_files(globalOutputFolder, dirName)

	entries = os.listdir(dir)
#	RT_writer = csv.writer(RT_coordinates_file)
	with os.scandir(dir) as entries: 
		if entries:
			for entry in entries:
				if (entry.name.endswith(".fasta") or entry.name.endswith(".fa")):
					print(entry.name)
					#make sure to enter folder with slash after
					file_path = dir + entry.name
					find_DGRs(file_path)
					generate_file_summary(file_path, dirName)

def run_folder_cmd():
	print("beginning of method")
	dir = DGR_module.getDir()
	print("in method")
	print(dir)
	run_folder(dir)

def run_folder_path(dir):
	run_folder(dir)
