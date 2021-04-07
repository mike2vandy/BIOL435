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
    query, hit, evalue, bit = fields[0], fields[1], fields[10], fields[11]
    main = [hit, float(evalue), float(bit)]
    if query in hits:
      hits[query].append(main)
    else:
      hits[query] = [main]

#go through parsed blast output
#for each query, sort hits by evalue: low to high
#use hit with lowest evalue
#Will only return orfs with a blast hit
#unannotated ORFs will be discarded
for i, j in hits.items():
  j.sort(key = lambda x: x[1])
  best = j[0]
  anno = best[0].split('|')
  swiss, gene = anno[1], anno[2].split('_')[0]
  better = swiss + '|' + gene
  print ">{}.{}\n{}".format(i, better, seqs[i])

