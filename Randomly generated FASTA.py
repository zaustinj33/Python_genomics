#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     07/08/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#RANDOMLY GENERATED FASTA SEQUENCES

import Bio
from Bio import SeqI0
import random
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def make_shuffle_record(record, new_id):
    nuc_list = list(record.seq)
    random.shuffle(nuc_list)
    return SeqRecord(Seq("".join(nuc_list),record.seq.alphabet), id=newid, description="Based on %s" % original_rec.id)
original_rec = SeqI0.read("NC_005816.gb", "genbank")
shuffled_recs = (make_shuffle_record(original_rec, "Shuffled%i" % (i+1)) for i in range(30))
SeqI0.write(shuffled_recs, "shuffled.fasta", "fasta")

