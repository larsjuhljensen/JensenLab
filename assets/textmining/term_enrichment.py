#!/usr/bin/python
#
# Name:     term_enrichment.py
#
# Purpose:  Counting and enrichment analysis of terms (e.g. tissues or
#           diseases) associated with organisms through text mining
#
# Inputs:   1) File of text-mined organism-term associations
#           2) Z-score cutoff
#           3) File with NCBI TaxIDs of foreground organisms
#           4) File with NCBI TaxIDs of background organisms (optional)
#           5) P-value cutoff
#
# Output:   Tab-delimited file with the following columns
#           1) Term identifier
#           2) Term Name
#           3) Foreground count
#           4) Background count (optional)
#           5) P-value
#
# Author:   Lars Juhl Jensen (lars.juhl.jensen@cpr.ku.dk)
#           Novo Nordisk Foundation Center for Protein Research, Denmark
#
# License:  2-clause BSD License

import scipy.stats
import sys

if len(sys.argv) < 2:
    print 'Usage: %s <associations file> [z-score cutoff] [foreground file] [background file] [p-value cutoff]' % __file__
    sys.exit(1)

# Read z-score cutoff from second argument.
z_cutoff = 5
if len(sys.argv) >= 3:
    z_cutoff = float(sys.argv[2])

# Read foreground organisms.
foreground_organisms = set()
if len(sys.argv) >= 4:
    for organism in open(sys.argv[3], 'r'):
        foreground_organisms.add(organism.strip())
else:
    for organism in sys.stdin:
        foreground_organisms.add(organism.strip())

# Read background organisms.
background_organisms = None
if len(sys.argv) >= 5:
    background_organisms = set()
    for organism in open(sys.argv[4], 'r'):
        background_organisms.add(organism.strip())

# Read p-value cutoff from fifth argument.
p_cutoff = 1.0
if len(sys.argv) >= 6:
    p_cutoff = float(sys.argv[5])

# Read and count associations above cutoff for foreground and background.
foreground_counts = {}
background_counts = {}
term_names = {}
for line in open(sys.argv[1], 'r'):
    fields = line.strip().split('\t')
    z_score = fields[4]
    if float(z_score) >= z_cutoff:
        organism = fields[0]
        term = fields[2]
        name = fields[3]
        if organism in foreground_organisms:
            if term in foreground_counts:
                foreground_counts[term] += 1
            else:
                foreground_counts[term] = 1
                if term not in term_names:
                    term_names[term] = name
        if background_organisms is not None and organism in background_organisms:
            if term in background_counts:
                background_counts[term] += 1
            else:
                background_counts[term] = 1

# Loop over counted terms, calculate statistics, and print results.
for term in foreground_counts.keys():
    name = term_names[term]
    foreground_count = foreground_counts[term]
    if background_organisms is None:
        print '%s\t%s\t%d' % (term, name, foreground_count)
    else:
        background_count = 0
        if term in background_counts:
            background_count = background_counts[term]-foreground_count
        foreground_size = len(foreground_organisms)
        background_size = len(background_organisms)-foreground_size
        table = [[foreground_count,foreground_size-foreground_count],[background_count,background_size-background_count]]
        ratio, p_value = scipy.stats.fisher_exact(table, alternative='greater')
        if p_value < p_cutoff:
            print '%s\t%s\t%d\t%d\t%f' % (term, name, foreground_count, background_count, p_value)
