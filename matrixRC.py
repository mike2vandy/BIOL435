#! /usr/bin/env python

import sys, os, glob

genes = {}
fNs = []

for fi in glob.glob("*.genes.results"):
  fN = fi.split('.')[0]
  fNs.append(fN)
  with open(fi) as f:
    for line in f:
      line = line.strip()
      fields = line.split()
      if line.startswith('gene'):
        pass
      else:
        iD, RC = fields[0], round(float(fields[-3]),0)
        if iD in genes:
          genes[iD][fN] = RC
        else:
          genes[iD] = {fN: RC}

print "gene,{}".format(','.join(fNs))
for gene, fns in genes.items():
  expression = [gene]
  for i in fNs:
    expression.append(fns[i])
  print ','.join(map(str, expression))

