---
title: Enrichment analysis
layout: single
permalink: /resources/proteomics/enrichment
sidebar:
  nav: "resources"
---
Enrichment analysis is frequently used to examine "-omics" data sets for enriched functional terms in a subset of the data set, such as regulated genes or modified proteins. It involves a statistical test to find significant differences in the frequency of GO-terms associated with e.g. modified proteins relative to their frequency in the genome. [a GO tool](https://agotool.sund.ku.dk/) is *a Gene Ontology enrichment tool*. This site can be used for functional annotation enrichment for proteomics data. It contains tools for abundance corrected GO-term, UniProt-keyword, and KEGG-pathway enrichment.

There are many GO enrichment tools freely available, so why would I want to use aGOtool instead? aGOtool stands out, because it was specifically designed for the abundance bias in Mass Spectrometry (MS) based proteomics data. This bias exists, since proteins can't be amplified, and abundant proteins are more likely to be detected by MS. This effect is even more pronounced when investigating post-translationally-modified (PTM) proteins, due to the fact that site occupancy is usually not as high as 100%. Meaning, that not every single copy of a given protein will have the PTM of interest at the same location. Therefore, it will be easier to detect PTMs on abundant proteins compared to low abundant proteins.

A GO-enrichment analyses comparing post-translationally modified proteins to unmodified proteins is likely to reveal enriched GO-terms associated with abundant proteins, rather than modified proteins specifically. We have developed a method to correct for this bias (see publication or explanation below) and this freely accessible web-tool, which you are most welcome to use.

This will result in
* a comparison to an appropriate control group
* increased specificity
* fewer significantly enriched, but more accurate and biologically meaningful terms
