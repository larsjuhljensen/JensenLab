---
title: Proteomics resources
layout: single
permalink: /resources/proteomics/
sidebar:
  nav: "resources"
---
Being located next to a world-leading mass spectrometry-based proteomics facility, the group has been involved in the development of several tools for analysis of such data.

## Enrichment analysis

Enrichment analysis is frequently used to examine "-omics" data sets for enriched functional terms in a subset of the data set, such as regulated genes or modified proteins. It involves a statistical test to find significant differences in the frequency of GO-terms associated with e.g. modified proteins relative to their frequency in the genome. [a GO tool](https://agotool.sund.ku.dk/) is *a Gene Ontology enrichment tool*. This site can be used for functional annotation enrichment for proteomics data. It contains tools for abundance corrected GO-term, UniProt-keyword, and KEGG-pathway enrichment.

There are many GO enrichment tools freely available, so why would I want to use aGOtool instead? aGOtool stands out, because it was specifically designed for the abundance bias in Mass Spectrometry (MS) based proteomics data. This bias exists, since proteins can't be amplified, and abundant proteins are more likely to be detected by MS. This effect is even more pronounced when investigating post-translationally-modified (PTM) proteins, due to the fact that site occupancy is usually not as high as 100%. Meaning, that not every single copy of a given protein will have the PTM of interest at the same location. Therefore, it will be easier to detect PTMs on abundant proteins compared to low abundant proteins.

A GO-enrichment analysis comparing post-translationally modified proteins to unmodified proteins is likely to reveal enriched GO-terms associated with abundant proteins, rather than modified proteins specifically. We have developed a method to correct for this bias (see publication or explanation below) and this freely accessible web-tool, which you are most welcome to use.

This will result in a comparison to an appropriate control group, increased specificity, and fewer significantly enriched, but more accurate and biologically meaningful terms.

## Phosphorylation

The lab jointly developed the kinase-substrate interaction resources [NetworKIN](http://networkin.info/), [NetPhorest](http://netphorest.info/), and [KinomeXplorer](http://kinomexplorer.info/) with the [LindingLab](http://lindinglab.org/) who now maintains them. These resources provide an atlas of the sequence specificities of kinases and kinase families, which is combined with the STRING network to predict the kinases that are most likely to be responsible for the phosphorylation of observed phosphorylation sites. We also developed [DoReMi](http://doremi.jensenlab.org/), which is a generalization of NetworKIN that allows users search with a user-specified sequence motif and prioritize the matches based on their network context.

Building upon this, we developed the [Phomics](http://phomics.jensenlab.org/) toolset, which can perform kinase enrichment analysis based on NetworKIN predictions as well as kinase activation loop analysis and site-based term enrichment analysis.
