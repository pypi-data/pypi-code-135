#delete general DGR_module in VB_shared after

from Bio import SeqIO
from Bio import SearchIO
import DGR_package.DGR_module as DGR_module
import re
import copy
import csv
import pandas as pd

def getContigID(genome_file, line):
#	print(line)
	isHeader = False
	if line[0] == ">":
		isHeader = True
	idNum = 0
	record_list = []
	for seq_record in SeqIO.parse(genome_file, "fasta"):
		record_list.append(seq_record)
	contig_RT_id = ""
	if (isHeader):
		for n in range(0, len(line)-6):
			if(line[n:n+7] == "Contig:"):
				idNum = n+7
		if (idNum != 0):
			for num in range(idNum, len(line)): 
				if (line[num:num+4] == "_$$_"):
#					print()
#					print(line[idNum:num] + "\n")
					contig_id = line[idNum:num]
			for record in record_list:
##				print("record id: " + record.id)
#				contigInRT = re.search(record.id, contig_id)
#				if not (contigInRT is None):
				if (contig_id == record.id):
#					print("contig identified: " + record.id)
					contig_RT_id = record.id
	return(contig_RT_id)
	return("none")

def getRT(line):
	if line[0] == ">":
		isHeader = True
	underscoreCount = 0
	startNum = 0
	num1 = ""
	num2 = ""
	if (isHeader):
		for num in range(0, len(line)-2): 
			char = line[num]
			secondChar = line[num + 1]
			thirdChar = line[num + 2]
			if (char == "$" and secondChar == "$" and thirdChar == "_"): 
				startNum = num+3
		if (startNum != 0): 
			hash_count = 0
			for num in range(startNum, len(line)):
				if line[num] != "_" and hash_count < 1: 
					num1 += line[num]
				elif line[num] != "_" and hash_count < 2:
					num2 += line[num]
				if line[num] == "_":
					if hash_count < 1: 
						num1 = num1.strip()
					elif hash_count < 2:
						num2 = num2.strip()
					hash_count = hash_count + 1
#			print("num1 is " + num1)
#			print("num2 is " + num2)
#			print()
	return(int(num1), int(num2))

def getDict(genome_file, type):
	contig_dict = {}
	fileDir = DGR_module.getFileDir(genome_file)
	fileName = DGR_module.getFileName(genome_file)
	fileOutputDir = DGR_module.getOutputFileDir(DGR_module.getFileDir(genome_file), DGR_module.getFileName(genome_file))
	target_file = fileOutputDir + "/" + fileName + "_clustered_" + type + "_sequences.fasta"
	Lines = ""
	with open(target_file, "r") as file: 
		Lines = file.readlines()
	contig_id = ""
	RT_counter = 1
	target_counter = 1
	for line in Lines:
		isHeader = False
		if line[0] == ">":
			isHeader = True
		if(isHeader):
			contig_id = getContigID(genome_file, line)
#			print("returned id: " + contig_id)
			if (not(contig_id in contig_dict)):
				contig_dict[contig_id] = {}
			RT_coords = getRT(line)
#			print(RT_coords)
			for contig_key in contig_dict:
#				print("key: " + contig_key)
				typeKeyExists = False
				RT_counter = 1
				for type_key in contig_dict[contig_key]:
					if (type_key[0:2] == "RT" and RT_counter > 0):
						if (contig_dict[contig_key][type_key] == RT_coords):
							typeKeyExists = True
						if ((RT_counter < int(type_key[2]) + 1) and not(typeKeyExists)):
							RT_counter = int(type_key[2]) + 1
#			print(RT_counter)
			if(not(typeKeyExists)):
				contig_dict[contig_id]["RT" + str(RT_counter)] = RT_coords
		else:
			target_seq = line.strip()
#			print(target_seq)
			for seq_record in SeqIO.parse(genome_file, "fasta"):
#				print(seq_record.id)
				idNum = None
				if (seq_record.id == contig_id): 
					idNum = re.search(target_seq.upper(), str(seq_record.seq).upper()) #added upper for string comparison
					print(idNum)
				start = ""
				end = ""
				target_coords = ()
				if not(idNum is None):
#					print(seq_record.id)
					start = idNum.start()
					end = idNum.end()
					target_coords = idNum.span()
					print(target_coords)
					for contig_key in contig_dict:
#						print("key: " + contig_key)
						target_counter = 1
						for target_key in contig_dict[contig_key]:
							if (target_key[0:2] == type and target_counter > 0):
								if (target_counter < int(target_key[2]) + 1):
#									print(target_key)
#									print(contig_dict)
									target_counter = int(target_key[2]) + 1
#									print(target_counter)
					contig_dict[contig_id][type + str(target_counter)] = target_coords
#					print()
#	print(contig_dict)
	return(contig_dict)

def combineDicts(dict1, dict2):
	RT_dict = {}
	RT_counter = 1
	for contig1 in dict1:
		for target1 in dict1[contig1]:
			if (not(contig1 in RT_dict)):
				RT_dict[contig1] = {}
			RTExists = False
			for RT_key in RT_dict[contig1]:
				if (RT_dict[contig1][RT_key] == dict1[contig1][target1]):
					RTExists = True
			if (target1[0:2] == "RT" and not(RTExists)):
				RT_counter = len(RT_dict[contig1]) + 1
				RT_dict[contig1]["RT" + str(RT_counter)] = dict1[contig1][target1]
	for contig2 in dict2:
		for target2 in dict2[contig2]:
			if (not(contig2 in RT_dict)):
				RT_dict[contig2] = {}
			RTExists = False
			for RT_key in RT_dict[contig2]:
				if (RT_dict[contig2][RT_key] == dict2[contig2][target2]):
					RTExists = True
			if (target2[0:2] == "RT" and not(RTExists)):
				RT_counter = len(RT_dict[contig2]) + 1
				RT_dict[contig2]["RT" + str(RT_counter)] = dict2[contig2][target2]
#	print("RT Dict")
#	print(RT_dict)

#	print("TR VR Dict ")
	cdict = {} #only TRs and VRs --> any RTs removed
	for contig1 in dict1:
		for contig2 in dict2:
			if (contig1 == contig2):
				cdict[contig1] = {**dict1[contig1], **dict2[contig2]}
#	print(cdict)
	combined_dict = copy.deepcopy(cdict) #loop and copy
	for contig in cdict:
		for target in cdict[contig]:
			if (target[0:2] == "RT"):
				combined_dict[contig].pop(target)


#	for contig1 in dict1: 

#	dict2_copy = copy.deepcopy(dict2)
#	for contig2 in dict2: 
#		for target in dict2[contig2]: 
#			if (target[0:2] == "RT"


#	print()
#	print("final combined dictionary")
	final_dict = {} #combining final TR and VR dictionaries
	for contig1 in combined_dict:
		for contig2 in RT_dict:
			if (contig1 == contig2):
				final_dict[contig1] = {**combined_dict[contig1], **RT_dict[contig2]}
	print(final_dict)
	return(final_dict)

def writeTableToFile(genome_file, full_dict, summary_file):
	fileName = DGR_module.getFileName(genome_file)
	fileOutputFolder = fileName + "_output"
	with open(summary_file, "a", newline = "") as csvfile:
		TR_VR_RT_writer = csv.writer(csvfile)
		dictNotEmpty = bool(full_dict)
		print("DICT NOT EMPTY: " + str(dictNotEmpty))
		if (dictNotEmpty):
			print("in loop")
			for contig in full_dict:
				for target in full_dict[contig]: 
					print("writing to csv file")
					TR_VR_RT_writer.writerow([fileName, contig, target, full_dict[contig][target][0], full_dict[contig][target][1]])

def checkForOverlap(num1, tuple1): 
	overlapExists = num1 in range(tuple1[0]-1, tuple1[1]+2)
	return overlapExists

def combineTuples(tuple1, tuple2): 
	if (tuple1[0] > tuple2[0]):
		num1 = tuple2[0]
	else:
		num1 = tuple1[0]
	if (tuple1[1] > tuple2[1]): 
		num2 = tuple1[1]
	else:
		num2 = tuple2[1]
	combinedTuple = (num1, num2)
	return combinedTuple

def checkForSplit(dict):
	overlapsExist = True
	fixed_dict = copy.deepcopy(dict)
#	print(fixed_dict)
	target_counter = 1
	while (overlapsExist):
#		print("BACK TO TOP")
		overlapsLoopCounter = 0
		for contig in dict:
			usedTargets = []
			for target in dict[contig]:
				for check_target in dict[contig]:
#					print(str(dict[contig][target][0]))
					if (dict[contig][target] != dict[contig][check_target]):
#						print(str(dict[contig][target][0]))
#						print(str(dict[contig][target][1]))
#						print(str(dict[contig][check_target]))
#						print(dict[contig][target][0] in range(dict[contig][check_target][0], dict[contig][check_target][1]))
#						print(dict[contig][target][1] in range(dict[contig][check_target][0], dict[contig][check_target][1]))
						targetNotRT = target[0:2] != "RT" and check_target[0:2] != "RT"
						targetNotUsed = not(dict[contig][target] in usedTargets)
						#note: range numbers will cause an issue if the first coordinate is 0
						firstNumInTuple = checkForOverlap(dict[contig][target][0], dict[contig][check_target])
						secondNumInTuple = checkForOverlap(dict[contig][target][1], dict[contig][check_target])
						if ((targetNotRT and targetNotUsed) and (firstNumInTuple or secondNumInTuple)):
							overlapsLoopCounter = overlapsLoopCounter + 1
#							print("overlap")
							num1 = ""
							num2 = ""
#							print(str(dict[contig][target]))
#							print(str(dict[contig][check_target]))
							if (target in fixed_dict[contig] and fixed_dict[contig][target] == dict[contig][target]):  #line added
								fixed_dict[contig].pop(target)
							if (check_target in fixed_dict[contig] and fixed_dict[contig][check_target] == dict[contig][check_target]): #line added
								fixed_dict[contig].pop(check_target)

							combinedTuple = combineTuples(dict[contig][target], dict[contig][check_target])

							existingTarget = ""
							for existing_target in fixed_dict[contig]:
								if (existing_target[0:2] != "RT"): 
									firstNumInTuple = checkForOverlap(combinedTuple[0], fixed_dict[contig][existing_target])
									secondNumInTuple = checkForOverlap(combinedTuple[1], fixed_dict[contig][existing_target])
									if (firstNumInTuple or secondNumInTuple): 
										existingTarget = existing_target
										combinedTuple = combineTuples(combinedTuple, fixed_dict[contig][existing_target])
#										print(combinedTuple)
							if (existingTarget != ""):
								fixed_dict[contig].pop(existingTarget)

							target_counter = 1
							fixed_dict_copy = copy.deepcopy(fixed_dict)
							for number_target in fixed_dict_copy[contig]:
								if (number_target[0:2] != "RT"):
									fixed_dict[contig].pop(number_target)
									fixed_dict[contig][number_target[0:2] + str(target_counter)] = fixed_dict_copy[contig][number_target]
									target_counter = target_counter + 1

#							combinedTuple = combineTuples(dict[contig][target], dict[contig][check_target])
							target_counter = 1
							for fixed_target in fixed_dict[contig]: 
								if (fixed_target[0:2] != "RT"): 
									target_counter = target_counter + 1
#							print("combined tuple to add")
#							print(combinedTuple)

							fixed_dict[contig][target[0:2] + str(target_counter)] = combinedTuple

#							print("dict after adding")
#							print(fixed_dict)
							target_counter = target_counter + 1
							usedTargets.append(dict[contig][target])
							usedTargets.append(dict[contig][check_target])
#		print("fixed_dict")
#		print(fixed_dict)
		if (overlapsLoopCounter == 0):
			overlapsExist = False
#			print("EXIT LOOP")
		else:
			overlapsExist = True
#			print("RERAN CHECK")
#		overlapsExist = False
		dict = fixed_dict
		fixed_dict = copy.deepcopy(dict)
	return(fixed_dict)

#def returnContig(hitID):
#	id = ""
#	hash_count = 0
#	for char in hitID: #takes out ending number >
#		if char == "_":
#			hash_count += 1
#			if hash_count >= 2:
#				break
#		id += char
#	return(id)


def checkDGRInRT(RT_file, TR_VR_RT_file):
	RT_df = pd.read_csv(RT_file)
	print(RT_df)
	full_df = pd.read_csv(TR_VR_RT_file)
	print("full_df")
	print(full_df)
	numsEqual = False
	for index1, row1 in RT_df.iterrows(): 
#		RT_contig = returnContig(row1["ID"])
		RT_contig = row1["ID"]
		print("RT ID: " + "$" + RT_contig + "$")
		print(type(RT_contig))
		RT_num1 = row1["Start_Pos"]
		RT_num2 = row1["Stop_Pos"]
#		print("done" + "\n")
		for index2, row2 in full_df.iterrows():
			full_contig = row2["Contig"]
			print("Full Contig ID: $" + full_contig + "$")
			full_num1 = row2["Start"]
			full_num2 = row2["Stop"]
			print("full contig == RT contig:" + str(full_contig.strip() == RT_contig.strip()))
			if ((row2["Feature"][0:2] == "RT") and (full_contig == RT_contig)): 
#			fullInRTContig = re.search(full_contig, RT_contig) #switched order worked for matches
#			print(fullInRTContig)
#			print(type(RT_contig))
#			if ((row2["Feature"][0:2] == "RT") and not(fullInRTContig is None)): 
				print(row2["Feature"][0:2]) #rethink for folder vs. file (numsEqual placement)
				numsEqual = (RT_num1 == full_num1) and (RT_num2 == full_num2)
				print(numsEqual)
				if (numsEqual): 
					print("RT num 1: " + str(RT_num1) + " full num 1: " + str(full_num1))
					print("RT num 2: " + str(RT_num2) + " full num 2: " + str(full_num2))
					print("nums equal!")
				print("Full Table ID: " + full_contig)
		RT_df.at[index1, "Contains DGR"] = numsEqual
		numsEqual = False #rethink for folder vs. file (numsEqual placement)
	RT_df.to_csv(RT_file, index = False)
