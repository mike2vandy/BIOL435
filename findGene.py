#! /usr/bin/python

import sys

data = []
count = 0
piwi = 0

with open(sys.argv[2]) as f:
  for line in f:
    line = line.upper().strip()
    fields = line.split()
    chrm, start = fields[0], int(fields[3])
    data.append(line)
    if sys.argv[1] in line:
      piwi = count
    count += 1

locus = data[piwi-10:piwi+10]

for i in locus:
  i = i.replace('"', '').replace(';', '')
  fields = i.split()
  if "GENE_NAME" in fields:
    print fields[0], fields[3], fields[4], fields[6], fields[9], fields[13]
  else:
    print fields[0], fields[3], fields[4], fields[6], fields[9]
