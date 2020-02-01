#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     11/07/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import collections as coll
import pandas as pd

# Combines characters in single string from a:b to c:d
def parse(a,b,c,d):
    string = 'vJ9Oy2b5Uu6vIpmv2iYTZniJHVm7Theloderma7AjgJpQEI16ydKG3kPYfO6PSr4FtzLP50SnpfSkMGMGc5vndesertiSVFw2bSw3pxrXAra2sNwBWTSgIoRMIRaGlwj7c2c6Jv2iInzzFkRr3DdunHLXJqVpfaU3W9c7zYO.'
    x = string[a:b+1]
    y = string[c:d+1]
    z = x + ' ' + y
    return z
# Sums all odd numbers in from integer e to f
def sum_of_odd(e,f):
    h, mem = list(range(e,f+1)), 0
    print(len(h))
    while i < len(h):
        if h[i] % 2 == 1:
            mem += h[i]
        i += 1
    return mem
# parses even numbered lines of list together
def even_list(data):
    new = []
    for line in data:
        new.append(datalist[i])
        i += 2
    return new

# Parses all even lines from a text document together, saves in new document
def evenLines():
    results, evenresults, i, x = [], [], 1, 0
    f = open('change.txt', 'w')
    with open('BravesirRobin.txt','r') as inputf:
        for line in inputfile:
            results.append(line.strip().splitlines())
    evenresults = results[1::2]
    for x in evenresults:
        f.write(str(x)[2:-2] + '\n')
    return results, evenresults
    f.close()

# Returns table of word:#of repeats  from string # more effcient
def DNAseqCount():
    with open('TriedZen.txt') as f:
        for k, v in coll.Counter(str(f.readlines()).split()).items(): print(k, v)
print(DNAseqCount())



