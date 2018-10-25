#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     28/08/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/python
#Biopython alignment test

import os
from Bio import pairwise2

## Show menu ##
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Template file path")
print ("2. Alignment sequence")
print (os.getcwd() + "    <-- current working directory")
print (30 * '-')
print ("Remeber you can press Crtl+C to stop process if shit goes down")

Seq1 = os.path.join(os.getcwd(), input('Template file name: '))
Seq2 = os.path.join(os.getcwd(), input('Sequence file name: '))

print ("This first path looks like this:  " + Seq1)


#class RNAseq:
def SeqAlign(outputSeq,Seq1,Seq2):
    with open(outputSeq,'w') as output, open(Seq1, 'r') as Seq1read, open(Seq2, 'r') as Seq2read:
        Seq1R = Seq1read.read()
        Seq2R = Seq2read.read()
        align = pairwise2.align.globalxx(Seq1R,Seq2R,score_only = True)
        output.write(str(align))
        print(align)

SeqAlign('Alignment_output.txt',Seq1,Seq2)
