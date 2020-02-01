#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     04/02/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def DNAtoRNA(Text):
    Text = Text.replace("T","U")
    return Text

Text = ""

print (DNAtoRNA(Text))