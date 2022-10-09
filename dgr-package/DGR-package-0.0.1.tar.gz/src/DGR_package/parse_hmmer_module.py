from Bio import SeqIO
from Bio import SearchIO
import re
import sys
import getopt
import os
import csv
import DGR_package.DGR_module as DGR_module

def parseTable(file):
	print("$$$_entered_HMM_parse_$$$")
	fileDir = DGR_module.getFileDir(file)
	fileName = DGR_module.getFileName(file)
	fileOutputDir = DGR_module.getOutputFileDir(fileDir, fileName)

	print(sys.path)

	with open (fileDir + "/" + fileName + "_20kbs.fasta", "w") as f, open (fileOutputDir + "/" + fileName + "_RT_coordinates_table.csv", "w") as f2, open (fileOutputDir + "/" + fileName + "_RT_sequences.fasta", "w") as rt_file, open (fileOutputDir + "/" + fileName + "_AA.fasta", "w") as aa_file: #changed line
		#f is 20 kbs file
		#f2 is RT Coordinates Table
		#rt_file is RT Sequences File 
		writer = csv.writer(f2)
		genome_id=str(fileName)
		gene_ids = []
		writer.writerow(["ID", "Start_Pos", "Stop_Pos", "Direction", "Clade"]) #changed line
		all_q_results = []
		all_q_results = SearchIO.parse(fileDir + "/" + fileName + "_hmmer_table.txt", "hmmer3-tab")
		print("before try catch block")
		try: 
			print("in try catch block")
			for q_result in all_q_results:
				print(q_result)
		except ValueError: 
			print("caught error!")
			return
#		for seq_record in SeqIO.parse(file, "fasta"):
#			print(seq_record.id)
		for q_result in SearchIO.parse(fileDir + "/" + fileName + "_hmmer_table.txt", "hmmer3-tab"):
			for hit in q_result:
				id = "" #reset at correct point
				hash_count = 0
				descr = hit.description
#				print(descr)
				hash_count = 0
				num1 = ""
				num2 = ""
				index = 0
				dir = ""
				for char in descr:
					if char != "#" and hash_count < 2: 
						num1 += char
					elif char != "#" and hash_count < 3:
						num2 += char
					elif char != "#" and hash_count < 4:
						dir += char
					if char == "#":
						if hash_count < 2: 
							num1 = num1.strip()
						elif hash_count < 3:
							num2 = num2.strip()
						elif hash_count < 4:
							dir = dir.strip()
						hash_count = hash_count + 1
				#accessing the prodigal amino acid sequences
				for amino_acid_seq in SeqIO.parse(fileDir + "/" + fileName + "_prot_trans.fasta", "fasta"):
					if (hit.id == amino_acid_seq.id):
						aa_file.write(">" + hit.id + "\n")
						aa_file.write(str(amino_acid_seq.seq) + "\n")
				#end of prodigal amino acid seq code

#				print("AG_TEST_id:$" + hit.id + "$")
#				print("AG_TEST_coords:" + num1 + " " + num2 + " " + dir)
				for seq_record in SeqIO.parse(file, "fasta"):
#					print("seq. record id: " + seq_record.id)
#					print("hit.id: " + hit.id)
#					idNum = re.search(r"^" + seq_record.id, str(hit.id))
#					idNum = re.fullmatch(seq_record.id, hit.id) #testing this line
#					idNum = re.search(r"\b" + str(seq_record.id), str(hit.id))

					isSubsetted = False
					index = len(hit.id)
					shortened_id = ""
					while not(isSubsetted):
						if (hit.id[index-1:index] == "_"): 
							shortened_id = hit.id[:index-1]
							isSubsetted = True
						else:
							index = index - 1
						print(shortened_id)

					#accessing the prodigal amino acid sequences
#					for amino_acid_seq in SeqIO.parse(fileDir + "/" + fileName + "_prot_trans.fasta", "fasta"):
#						if (hit.id == amino_acid_seq.id):
#							aa_file.write(">" + hit.id + "\n")
#							aa_file.write(str(amino_acid_seq.seq) + "\n")
					#end of prodigal amino acid seq code

#					if ((not(idNum is None)) and (idNum.span() != (0, 0))):

#						id = idNum.group()
#						print(idNum)
#						print("match:$" + id + "$")
#						idNum = None
#					else: 
#						id = ""
#					print(id)
#					print(idNum)
					if (seq_record.id== shortened_id):
						print("AG_TEST:"+hit.id)
						if hit.id in gene_ids:
#							print("hit in list")
#							print(hit.id)
#							print(gene_ids)
#							print("\n")
							break
						else:
							gene_ids.append(hit.id)
#							print("hit not in list")
#							print(hit.id)
							print(gene_ids)
#							print("\n")
							num1 = (int)(num1) - 1 #-1 for base pair error
							num2 = (int)(num2) - 1 #-1 for base pair error
							f.write(">Genome:" + genome_id + "_Contig:" + seq_record.id + "_$$_" + str(num1) + "_" + str(num2) + "_" + dir + "\n")
							startIndex = 0
							endIndex = len(str(seq_record.seq))
							s_num1 = num1 - 10000
							l_num2 = num2 + 10000
							if ((s_num1 > startIndex) and (l_num2 < endIndex)):
								f.write(str(seq_record.seq[num1-10000:num2+10000]) + "\n")
							elif ((s_num1 < startIndex) and (l_num2 < endIndex)):
								f.write(str(seq_record.seq[0:num2+10000]) + "\n")
							elif ((s_num1 > startIndex) and (l_num2 > endIndex)):
								f.write(str(seq_record.seq[num1-10000:endIndex]) + "\n")
							else: 
								f.write(str(seq_record.seq) + "\n")
							rt_file.write(">Genome:" + genome_id + "_Contig:" + seq_record.id + "_RT_" + str(num1) + "_" + str(num2) + "_" + dir + "\n") #writes RTs in lowercase if genome file given in lowercase
							rt_file.write(str(seq_record.seq[num1:num2]) + "\n") 
							writer.writerow([seq_record.id, num1, num2, dir, q_result.id]) 
