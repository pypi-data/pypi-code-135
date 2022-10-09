from __future__ import division
from itertools import product
from Bio.Blast import NCBIXML
import sys
import getopt
import os
import csv
import DGR_package.DGR_module as DGR_module

def find_between(s, first, last ):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return "ValueError"

def compare(s1,s2,fileoutTR,fileoutVR,names1,names2):
    Ls1= len(s1)
    Abase=0
    Amismatch=0
    Tbase=0
    Tmismatch=0
    Gbase=0
    Gmismatch=0
    Cbase=0
    Cmismatch=0
    A2base=0
    A2mismatch=0
    T2base=0
    T2mismatch=0
    G2base=0
    G2mismatch=0
    C2base=0
    C2mismatch=0
    s1=s1.upper()
    s2=s2.upper()
    if len(s1) != len(s2):
        return False
    else:
        for c1, c2 in zip(s1, s2):

            if c1 == "A":
                Abase+=1
                if c1 != c2:
                    Amismatch+=1
            if c2 == "A":
                A2base+=1
                if c1 != c2:
                    A2mismatch+=1
            if c1 == "T":
                Tbase+=1
                if c1 != c2:
                    Tmismatch+=1
            if c2 == "T":
                T2base+=1
                if c1 != c2:
                    T2mismatch+=1
            if c1 == "G":
                Gbase+=1
                if c1 != c2:
                    Gmismatch+=1
            if c2 == "G":
                G2base+=1
                if c1 != c2:
                    G2mismatch+=1
            if c1 == "C":
                Cbase+=1
                if c1 != c2:
                    Cmismatch+=1
            if c2 == "C":
                C2base+=1
                if c1 != c2:
                    C2mismatch+=1

    varA1=0
    varT1=0
    varA2=0
    varT2=0
    if Amismatch>0:
        varA1= Amismatch/(Amismatch+Tmismatch+Gmismatch+Cmismatch)
    if Tmismatch >0:
        varT1= Tmismatch/(Amismatch+Tmismatch+Gmismatch+Cmismatch)
    if A2mismatch>0:
        varA2= A2mismatch/(A2mismatch+T2mismatch+G2mismatch+C2mismatch)
    if T2mismatch>0:
        varT2= T2mismatch/(A2mismatch+T2mismatch+G2mismatch+C2mismatch)
    else:
        False

    if Ls1>60:
        if Amismatch > 5 or Tmismatch > 5 or A2mismatch > 5 or T2mismatch > 5:
            if find_between(names1, names1[:1],"_$$_") in names2:
#            if find_between(names1,"fold_","_-_B") == find_between(names2,"fold_","_-_B"):
                if varA1 > 0.8 or varT1 > 0.8:
                    output = open(fileoutTR, "a")
                    output.write('>TR '+names1 +'\n' + s1 + '\n')
                    output = open(fileoutVR, "a")
                    output.write('>VR '+names2 +'\n' + s2 + '\n')

         
                elif varA2 > 0.8 or varT2 > 0.8:
                    output = open(fileoutTR, "a")
                    output.write('>TR '+names2 +'\n' + s2 + '\n')
                    output = open(fileoutVR, "a")
                    output.write('>VR '+names1 +'\n' + s1 + '\n')
            
    if Ls1>60:
            if Amismatch > 5 or Tmismatch > 5 or A2mismatch > 5 or T2mismatch > 5:
                if varA1 > 0.8 or varT1 > 0.8 or varA2 > 0.8 or varT2 > 0.8:
                    return True

def findVRTRs(file):
    fileDir = DGR_module.getFileDir(file)
    fileName = DGR_module.getFileName(file)

    result = open(fileDir + "/" + fileName + "_alignments.xml","r")
    records= NCBIXML.parse(result)

    VRTRs = 0

    with open(fileDir + "/" + fileName + "_DGR_csv.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequence", "Query", "Length", "Score", "Gaps", "E Value", "HSP Query", "HSP Match", "HSP Subject", "VRTR Count"])

    for item in records:
        for alignment in item.alignments:
                  for hsp in alignment.hsps:
                         if hsp.score <100:
                            if compare(hsp.query,hsp.sbjct, fileDir + "/" + fileName + "_path_to_TR_sequences_file_for_output.fasta", fileDir + "/" + fileName + "_path_to_VR_sequences_file_for_output.fasta",item.query, alignment.title):
#line from initial script
#                           if find_between(item.query,item.query[:4],"_-_B") == find_between(alignment.title,alignment.title[:4],"_-_B"):
                                if find_between(item.query,item.query[:1],"_$$_") in alignment.title:
                                    VRTRs+=1
                                    with open(fileDir + "/" + fileName + "_DGR_csv.csv", "a", newline = "") as csvfile:
                                        writer = csv.writer(csvfile)
                                        writer.writerow([item.query, alignment.title, alignment.length, hsp.score, hsp.gaps, hsp.expect, hsp.query, hsp.match, hsp.sbjct, VRTRs])
                                    print('****Alignment****')
                                    print('sequence:', item.query)
                                    print('query:', alignment.title)
                                    print('length:', alignment.length)
                                    print('score:', hsp.score)
                                    print('gaps:', hsp.gaps)
                                    print('e value:', hsp.expect)
                                    print(hsp.query)
                                    print(hsp.match)
                                    print(hsp.sbjct)
                                    print("%%%%%%   VRTR Count:", VRTRs, "   %%%%%%")


    print(VRTRs)

