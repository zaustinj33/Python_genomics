#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     16/07/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def importfile():
    results, evenresults, i, x = [], [], 1, 0
    f = open('change.txt', 'w')
    with open('BravesirRobin.txt','r') as inputfile:
        for line in inputfile:
            results.append(line.strip().splitlines())
    evenresults =  results[1::2]
    for x in evenresults:
        f.write(str(x)[2:-2] + '\n')
    return results, evenresults
    f.close()
print(importfile())