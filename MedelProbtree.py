#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      zaj3
#
# Created:     08/02/2018
# Copyright:   (c) zaj3 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


k = ["A","A"]
m = ["A", "a"]
n = ["a","a"]

kNum = 2
mNum = 2
nNum = 2

size = int(kNum + mNum + nNum)

# Creates breeding pool
def space(k,m,n):
    pool = []
    for i in range(kNum):
        pool.append(k)
    for i in range(mNum):
        pool.append(m)
    for i in range(nNum):
        pool.append(n)

    # iterate through pool non-inclusive to select Dad
    cohort = range(len(pool))
    for i in cohort:
        pair = []
        pair.append(i)
       # pair = pair.append(cohort[i])
    return pair, cohort, pool


print(space(k,m,n))





