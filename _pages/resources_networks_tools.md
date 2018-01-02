---
title: Visualization tools
layout: single
permalink: /resources/networks/tools
sidebar:
  nav: "resources"
---
Whereas web interfaces are well suited for working with individual or small groups of proteins, more powerful tools are needed when working with large networks resulting from, for example, proteomics or other omics technologies. To this end, we collaborate with the [Cytoscape](http://cytoscape.org/) to develop [stringApp](http://apps.cytoscape.org/apps/stringapp), which imports protein-protein and protein-chemical interaction data from [STRING](https://string-db.org/) and [STITCH](http://stitch.embl.de/) into Cytoscape.

Users provide a list of one or more gene, protein or compound identifiers, the species, and a confidence score and stringApp will query the database and return the matching network. Currently, four different queries are supported:

* STRING: protein query -- enter a list of protein names (e.g. gene symbols or UniProt identifiers/accession numbers) to obtain a STRING network for the proteins
* STRING: PubMed query -- enter a PubMed query and utilize text mining to get a STRING network for the top N proteins associated with the query
* STRING: disease query -- enter a disease name to retrieve a STRING network of the top N proteins associated with the specified disease
* STITCH: protein/compound query -- enter a list of protein or compound names to obtain a network for them from STITCH

stringApp also allows users to expand the resulting network by adding an arbitrary number of nodes (protein or chemical compounds), change the confidence score, and expand the network by adding new nodes. In addition, stringApp v1.1 can retrieve functional enrichment for Gene Ontology terms, KEGG Pathways, and protein domains at a user-specified significance threshold and show the results in a new table in the Table Panel. All STRING networks are visualized using a new "String Style" custom graphic, which closely resembles the networks on the STRING web site.
