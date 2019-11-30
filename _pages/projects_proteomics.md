---
title: Proteomics projects
layout: single
permalink: /projects/proteomics/
sidebar:
  nav: "projects"
---
Tandem mass-spectrometry has become a method of choice for high-throughput, quantitative analysis in proteomics. Being located next to a world-leading mass-spectrometry facility, we have a keen interest in applying bioinformatics methods to proteomics data and developing new methods.

## Phosphorylation site localization

Phosphorylation-driven cell signaling governs most biological functions and is widely studied using mass spectrometry-based phosphoproteomics. Identifying the peptides and localizing the phosphorylation sites within them from the raw data is challenging and can be performed by several algorithms that return scores that are not directly comparable. This increases the heterogeneity among published phosphoproteomics data sets, prevents their direct integration, and introduces false positives in the dedicated databases. By evaluating the performances of different bioinformatics pipelines for MS-based proteomic analysis of complex phospho-peptide mixtures, we aim to normalize their scores by converting the to estimated false positive rates.

## Network Visualization

Data such as proteomics data on individual post-translational modification (PTM) sites, which have multiple values per protein, are not easy to visualize onto protein networks using existing tools. To address this, we develop the [Omics Visualizer](http://apps.cytoscape.org/apps/omicsvisualizer) app for [Cytoscape](https://cytoscape.org/), a popular open-source tool for network analysis and visualization. The app allows users to import data tables with several rows referring to the same node and to visualize such data on networks; while designed with omics data in mind, the app is data agnostic. These values can be shown directly on the nodes of the networks as pie or donut visualizations, in which the color of each slice represents a different value for the same node.

## Analysis of in-house data

We collaborate with all groups in the [Proteomics program](http://www.cpr.ku.dk/research/proteomics/) to perform advanced analyses of the mass-spectrometry datasets that they produce. The projects are too many and too frequently changing to list here, but most related to analysis of post-translational modifications, including their regulation, evolutionary conservation, and structural context. Besides numerous joint publications, such collaborations have resulted in several of the [proteomics tools](/resources/proteomics/) developed within the group.
