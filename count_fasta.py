#!/usr/bin/env python

import sys
import subprocess
from Bio import SeqIO

# Count the number of sequences in a multifasta file

# Checks if in proper number of arguments are passed gives instructions on proper use.
def argsCheck(numArgs):
	if len(sys.argv) < numArgs or len(sys.argv) > numArgs:
		print "\nConcatenates multifasta files to one unique file and create a dictionary"
		print "Developed by: Felipe Lira\n"
		print "\nUsage:\n\t" + sys.argv[0] + " [file.fasta]\n"
		exit(1) # Aborts program. (exit(1) indicates that an error occurred)

argsCheck(2) # Checks if the number of arguments are correct.


inFile = open(sys.argv[1], "r") # fasta file

listFasta = [] # store the records in fasta file

for record in SeqIO.parse(inFile, "fasta"):
	listFasta.append(record.id)

#print "\nYour file <<", sys.argv[1], ">> has",len(listFasta), "sequences.\n"

print sys.argv[1], len(listFasta)
