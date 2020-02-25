#! /usr/bin/env python2.7

import sys

def fasDict(i_f):
  seq_dict = {}
  with open(i_f) as infile:
    for line in infile:
      line = line.strip()
      if line.startswith('>'):
        header = line.split()[0].replace('>', '')
        seq_dict[header] = ''
      else:
        seq_dict[header] += line

    return seq_dict

def printSeq(seq):
  count = 0
  while count <= len(seq):
    print seq[count: count + 70]
    count += 70

aa_seqs = fasDict(sys.argv[1])
nucl_seqs = fasDict(sys.argv[2])

for head in nucl_seqs:
  n_seq = nucl_seqs[head]
  if head in aa_seqs:
    aligned = aa_seqs[head]
    raw_aa = aligned.replace('-', '')
    count = 0
    nucl_aligned = ''
    for letter in aligned:
      if letter == '-':
        nucl_aligned += '---'
      elif letter == '?':
        nucl_aligned += '---'
        count += 1
      elif letter == raw_aa[count]:
        nucl = count * 3
        nucl_aligned += n_seq[nucl:nucl + 3]
        count += 1
    print '>' + head
    printSeq(nucl_aligned)

