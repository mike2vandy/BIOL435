#! /usr/bin/env python

import sys

seqs = {}
with open(sys.argv[1]) as f:
  for line in f:
    line = line.strip()
    if line.startswith('>'):
      head = line
      seqs[head] = ''
    else:
      seqs[head] += line

for i, j in seqs.items():
  end = j[-3:]
  if end == 'TAG' or end == 'TAA' or end == 'TGA':
    print "{}\n{}".format(i, j[:-3])
  else:
    print "{}\n{}".format(i, j)
 

 
