#! /usr/bin/env python

import sys

#import fasta file 
seqs = {}
with open(sys.argv[1]) as f:
  for line in f:
    line = line.strip()
    if line.startswith('>'):
      head = line.split()[0].replace('>', '')
      seqs[head] = ''
    else:
      seqs[head] += line

#import BLAST output
#For each query, save the hits and associated evalue and bit scores
hits = {}
with open(sys.argv[2]) as f:
  for line in f:
    line = line.strip()
    fields = line.split()
    que, db, evalu, bit = fields[0], fields[1], float(fields[-2]), float(fields[-1])
    specific = db.split('|')[2].split('_')[0]
    if specific in hits:
      hits[specific].append([que,evalu, bit])
    else:
      hits[specific] = [[que, evalu, bit]]

#go through parsed blast output
#for each query, sort hits by evalue: low to high
#use hit with lowest evalue
#Will only return orfs with a blast hit
#unannotated ORFs will be discarded
for i, j in hits.items():
  j.sort(key = lambda x: x[2], reverse = True)
  best = j[0][0]
  print ">{}|{}\n{}".format(best, i, seqs[best])

