#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     24/07/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
def replace_all():
    my_text = open('DNA.txt','r').read()
    reps = {'C':'g','T':'a', 'G':'c', 'A':'t',}
    for i, j in reps.items():
        text = my_text.replace(i, j)
    return my_text
    return text
"""
#gives the reverse compliment of a DNA text file
reps = {'A':'t', 'G':'c', 'T':'a', 'C':'g'}
my_text = open('DNA.txt', 'r').read()
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text.upper()
txt = replace_all(my_text, reps)[::-1]
print(txt)