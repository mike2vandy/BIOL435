#! /usr/bin/env python2.7

import sys

with open(sys.argv[1]) as f:
  for line in f:
    if line.startswith('#'):
      pass
    else:
      line = line.strip()
      fields = line.split()
      main = fields[-1]
      info = fields[7]
      dp = info.split(';')[0]
      dp = dp.split('=')[1]
      dp = int(dp)
      gd, etc, ad = main.split(':')
      if gd == '0/1' and dp >= 10:
        chrm, pos, refA, altA = fields[0], fields[1], fields[3], fields[4]
        ref, alt = ad.split(',')
        ref, alt = int(ref), int(alt)
        total = ref + alt
        refFreq = alt/float(total) *100
        print "{}\t{}\t{}\t{}\t{}".format(chrm, pos, refA, altA, refFreq)
