#! /usr/bin/env python

import sys
from ete3 import Tree, TreeStyle

#read tree
tr = Tree(sys.argv[1])

#set root at midpoint (think it works)
root = tr.get_midpoint_outgroup()
tr.set_outgroup(root)

#TreeStyle stuff
ts = TreeStyle()
ts.show_branch_support = True
ts.branch_vertical_margin = 15

outName = sys.argv[2]
tr.render(outName +'.png', dpi = 300, tree_style = ts)


