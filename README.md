# Helpful Scripts for BIOL435

## translate.py

Translates protein coding DNA information into amino acids.  
Usage:  
`translate.py <DNA.fas> > <PROT.fas>`

## reverseTranslateAlignment.py 

Reverse translates a protein alignment into a codon alignment.  
The fasta headers must be **identical** in **both** files.  
Usage:  
`reverseTranslateAlignment.py <PROTALN.fas> <DNA.fas> > <CODON.fas>`

## drawTree.py  

This one is a weird one, it's held together by duct tape, definitely test it. 
You will still have to call this script from its "home" and you'll have to call 'xvfb-run'.
Usage:  
`xvfb-run python ~/software/BIOL435/drawTree.py <bipartitions_file> <outfile prefix>`  

Example:

`xvfb-run python ~/software/BIOL435/drawTree.py RAxML_bipartitions.codon ADRA_codon`    
