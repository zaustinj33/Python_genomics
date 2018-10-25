#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      zaust
#
# Created:     04/02/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def NucCount(Text):
    Count = Text.count("A"), Text.count("C"), Text.count("G"), Text.count("T")
    return Count


print(NucCount(Text))