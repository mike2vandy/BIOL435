#! /usr/bin/env python

import sys

seqs = {}

with open(sys.argv[1]) as f:
  for line in f:
    line = line.strip()
    if line.startswith('>'):
      head = line.replace('>', '')
      seqs[head] = 0
    else:
      seqs[head] += len(line)

for i, j in seqs.items():
  print "{}\t{}".format(i, j)

