jdjdj#-------------------------------------------------------------------------------
# Name:        ori test
# Purpose:
#
# Author:      zaust
#
# Created:     08/08/2017
# Copyright:   (c) zaust 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Copy your FrequentWords function (along with all required subroutines) from Replication.py
# You will need to copy FrequentWords, CountDict, and PatternCount

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
# HINT:   This code should be identical to when you last implemented CountDict
def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
# Then, call your FrequentWords function, passing in "GATCCAGATCCCCATAC" for Text and 2 for k,
# and store the result as a variable named words.
Text = "GATCCAGATCCCCATAC"
k = 2
print (FrequentWords(Text, k))
# Finally, print the words variable.
