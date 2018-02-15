#!/usr/bin/python
#
# Name:     disease_comentions.py
#
# Purpose:  Systematic retrieval of literature linking taxa to a disease
#
# Output:   Tab-delimited file with the following columns
#           1) NCBI TaxID
#           2) Space-separated list of PMIDs
#
# Authors:  Evangelos Pafilis (vagpafilis@gmail.com, http://epafilis.info)
#           Hellenic Center for Marine Research, Greece
#
#           Lars Juhl Jensen (lars.juhl.jensen@cpr.ku.dk)
#           Novo Nordisk Foundation Center for Protein Research, Denmark
#
# License:  2-clause BSD License

import sys

if len(sys.argv) < 2:
    print 'Usage: %s <disease_doid> [taxa file] [disease mentions file] [organism mentions file]' % __file__
    sys.exit(1)

# Read disease of interest from first argument.
disease_filter = sys.argv[1]

# Read organisms of interest, either from file specified as second argument or from stdin.
organisms_filter = set()
if (len(sys.argv) >= 3):
    for organism in open(sys.argv[2], 'r'):
        organisms_filter.add(organism.strip())
else:
    for organism in sys.stdin:
        organisms_filter.add(organism.strip())

# Read and store PMIDs for disease of interest.
disease_mentions_filename = 'disease_textmining_mentions.tsv'
if len(sys.argv) >= 4:
    disease_mentions_filename = sys.argv[3]
disease_mentions = set()
for line in open(disease_mentions_filename, 'r'):
    disease, pmids = line.strip().split('\t')
    if disease == disease_filter:
        for pmid in pmids.split(' '):
            disease_mentions.add(pmid)

# Print PMIDs of for disease and organisms of interest.
organism_mentions_filename   = 'organism_textmining_mentions.tsv'
if len(sys.argv) >= 5:
    organism_mentions_filename = sys.argv[4]
for line in open(organism_mentions_filename, 'r'):
    organism, pmids = line.strip().split('\t')
    if organism in organisms_filter:
        filtered_pmids = []
        for pmid in pmids.split(' '):
            if pmid in disease_mentions:
                filtered_pmids.append(pmid)
        print organism+'\t'+' '.join(filtered_pmids)
