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

Renders a PNG image of a provided newick file.  
This one is a weird one, it's held together by duct tape, definitely test it. 
You will still have to call this script from its "home" and you'll have to call 'xvfb-run' first.  
Usage:  
`xvfb-run python ~/software/BIOL435/drawTree.py <bipartitions_file> <outfile prefix>`  

Example:

`xvfb-run python ~/software/BIOL435/drawTree.py RAxML_bipartitions.codon ADRA_codon`    

## calcSeqLen.py  

Measures the length of sequences in a fasta file, outputs a tab delimited format with seq name and the length

Usage:  
`calcSeqLen.py <fasta> > <out.tab>`

Example:

calcSeqLen.py Trinity.fasta > trinityLens.tab

## fas2phy.py  

Converts a FASTA file into a PHYLIP format. 

Usage:  
`fas2phy.py <fasta> > <phylip>`

Example:  

fas2phy.py piwi.aln.fas > piwi.aln.phy

## findGene.py

Finds a gene of interest in an ensembl GTF, will print 5 genes up and downstream as a bed file for synteny purposes  

Usage:  
`findGene.py <gene name> <GTF file> > <region.bed>`

Example:  

findGene.py PIWIL4 Homo_sapiens.GRCh38.100.gtf.gz > homo.piwil4.region.bed

## makeConfig.py

Makes a config.nex file needed for ExaBayes.  

Usage:  
makeConfig.py 
