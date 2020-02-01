#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      zaust
#
# Created:     06/02/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

TRANS = { "T": "A", "A": "T", "G": "C", "C": "G" }

def revComp(strand):
    strand = strand[::-1]
    newstrand =[]
    for base in strand.upper():
        newstrand.append(TRANS[base])
    newstrand = ''.join(newstrand)
    return newstrand

strand = "AGTGGAGCAGCCT"
print (revComp(strand))