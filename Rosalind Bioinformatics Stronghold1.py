#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     23/07/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Rosalind Bioinformatics stronghold#

#Counting nucleic acids in DNA string

import collections as coll
import pandas as pd
import itertools


sequence = '/home/zacjohnson/OneDrive/School-dj-Ubuntu/DataScience/Sequences/Per2AS_clone21.txt'



#prints how many ATCG is in a DNA string as a vertical table
def coolCount():
    with open(sequence) as f:
        for k, v in coll.Counter(list(str(f.readlines()))).items(): print(k, v)
print(coolCount())

#transcribes DNA to RNA
def DNAtoRNA():
    with open('C57PER2_mouse_full_DNA.txt', 'r') as f, open('C:/School/C57PER2_mouse_full_RNA.txt', 'w+') as g:
        RNA = ''.join([w.replace('T', 'U') for w in f]).split('>')[1::]
        g.write(str(RNA))
        return RNA
#print(DNAtoRNA())


"""
#Reverse Compliment of DNA (Switch T to u for RNA)  MUST REPLACE WITH LOWER CASE FIRST
reps = {'A':'u', 'G':'c', 'U':'a', 'C':'g'}
my_text = open('C:/School/C57PER2_mouse_full_RNA.txt', 'r').read()
RevComp = open('C:/School/C57PER2_mouse_full_AS_RNA.txt', 'w+')
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text.upper()
txt = replace_all(my_text, reps)[::-1]
RevComp.write(txt)
"""

import collections as coll
import pandas as pd
import itertools


sequence = '/home/zacjohnson/OneDrive/School-dj-Ubuntu/DataScience/Sequences/Per2AS_clone3.txt'
#calculates GC content of DNA text file regardless of spaces in sequence
def GCcontent():
    totals = []
    with open(sequence, 'r') as g:
        new = g.read().replace('\n','').split('>')[1::]
        for i in new:
            totals.append(round(((i.count('G') + i.count('C') )/(i.count('G') + i.count('C')+i.count('T') + i.count('A'))*100),6))
    GCratio = list(zip(new, totals))
    HighGC = max(GCratio, key=lambda x: x[1])
    for i in HighGC: print(i)
    g.close()
print(GCcontent())


#Counting hammond distance in two sequences
def PointmutCount():
    SeqList,count=[],0
    with open('DNA.txt', 'r') as f:
        for line in f.read().split(): SeqList.append(line)
        count = sum(1 for a, b in list(zip(SeqList[0], SeqList[1])) if a != b)
        return SeqList, count
#print (PointmutCount())

#Converts bi-column RNA codon table to dictionary
def RNAdict():
    with open('RNAdict.txt', 'w') as f :
        CodonList = []
        ProteinList = []
        df = pd.read_table('RNAcodontable.txt', "\s+", names = ['codon', 'protein',
        'codon1', 'protein1','codon2', 'protein2','codon3', 'protein3'])
        df = df.astype(str)
        for i in range(len(df.columns)):
            if i % 2 == 0 or i == 0:
                ProteinList.append(list(df.iloc[:,i])  )
            else:
                CodonList.append(list(df.iloc[:,i]))
        f.write(str(dict(zip(list(itertools.chain.from_iterable(CodonList)),
        list(itertools.chain.from_iterable(ProteinList))) )))
    f.close()
#print(RNAdict())

# USE .read()   TO CONVERT INTO STRINGS!!!!!
def RNAtoProtein():
    ProteinList = []
    with open('RNAdict.txt') as f, open('RNA.txt') as s:
        RNA = s.read()
        Protein = eval(f.read())
        RNAList = [RNA[i:i+3] for i in range(0, len(RNA), 3)]
        for i in RNAList:
            ProteinList.append((list(Protein.keys())[list(Protein.values()).index(i)]))
    return  ProteinList, RNAList
    f.close()
#print(RNAtoProtein())
"""
