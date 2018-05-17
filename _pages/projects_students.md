---
title: Student projects
layout: single
permalink: /projects/students/
sidebar:
  nav: "projects"
---
We are always looking for Master's students to join the lab to work on projects. All projects are estimated to last between three and six months and basic programming knowledge is required. Please contact us if you are interested in doing a project with us.

## Network-based label diffusion

The aim of functional association networks like [STRING](https://string-db.org/) is to link proteins that function together. It is thus an obvious idea to use such networks to infer functional labels of proteins, e.g. involvement in a disease of interest, based on the labels of neighboring proteins. Indeed many algorithms have been proposed for doing this, which either use only the direct neighbors or allow functional labels to diffuse like heat across the network.

We would like to implement such functionality into [stringApp](http://apps.cytoscape.org/apps/stringApp) and possibly also as a new evidence channel in the [COMPARTMENTS](https://compartments.jensenlab.org/), [TISSUES](https://tissues.jensenlab.org/), and [DISEASES](https://diseases.jensenlab.org/)databases. However, it is currently not clear which of the many algorithms is best suited for use on the STRING network. The project is thus to use several existing implementations to diffusion labels, such as disease annotations, across the STRING network and assess which of them yield the best results, both in terms of quality and speed.

*Project advisors: Nadezhda Tsankova Doncheva and [Lars Juhl Jensen](/people/larsjuhljensen/)*

## Phosphoproteome visualization

Post-translational modification (PTM) of proteins is an important mechanism in regulation of biochemical reactions in biological systems. Phosphorylation is one of the most studied PTMs since it acts as an on/off switch for many proteins. Surveys of the phosphoproteome quantitatively analyze tens of thousands of phosphorylation sites on thousands of proteins across multiple conditions or time points. All in all, visualization of the phosphoproteome data is far from trivial.

Given that proteins work together in complexes and pathways, it is desirable to view phosphoproteomics data in the context of protein networks. We would thus like to create a framework for visualizing such data within the open-source Cytoscape platform. This can be done either by developing a Cytoscape app in Java or by using JavaScript frameworks like D3.js within the built-in web browser in Cytoscape.

The aim of the project is not to develop a final software package for this, but rather to explore and evaluate different avenues for visualizing phosphoproteomics data. However, a successful project should provide means for to upload new datasets and obtain network-based interactive visualizations.

*Project advisors: Ufuk Kirik and [Lars Juhl Jensen](/people/larsjuhljensen/)*

## Text mining beyond PubMed

Text mining of the biomedical literature has been successful in extracted interactions between a broad spectrum of biomedical entities. The JensenLab co-develops a range of widely used [resources](/resources/) that catalog association, such as STRING for protein--protein interactions and DISEASES for disease--gene associations. A central component of all resources is the automatic mining of abstracts and open access full-text articles available in PubMed.

[Recent work](https://doi.org/10.1371/journal.pcbi.1005962) showed that using full-text articles yields considerable improvements compared to PubMed abstracts alone. Motivated by these results, the main focus of this project is to explore resources for text mining beyond PubMed and to study the effect of incorporating additional text sources on the quality of the extracted associations. The quality will be measured by comparing them to a gold standard of expert-curated associations. Potential sources of text include the 10000+ relevant preprints available in bioRxiv, patents available via USPTO, clinical trial records, and proposals of funded research grants.

The project is ideal to get started with co-occurrence-based text mining, improve your skills on the command line for handling and cleaning large data files, and become more proficient in a programming language used for data analysis (such as Python).

*Project advisors: [Alexander Junge](/people/alexanderjunge/) and [Lars Juhl Jensen](/people/larsjuhljensen/)*

## Text mining for rare diseases

The goals of this project are to perform text mining for rare human diseases and to assess the results so that they can be integrated into the [DISEASES](https://diseases.jensenlab.org/) database. Approximately 6--7000 rare diseases have been identified, each affecting less than 1 in 2000 people. However, collectively they affect around 10% of the population and many are chronic, progressive diseases with genetic causes.

Due to their collective importance to human health, we would like to develop computational methods to study them as a group. One approach is to use text mining to automatically read the literature and to extract information about which genes are associated with which rare diseases. This enables the information found in free form scientific articles to be automatically structured and included in a searchable and reusable database.

The DISEASES database created by the JensenLab in 2015 uses text mining and experimental evidence to expose connections between diseases and the underlying genes but does not yet include rare diseases. This project involves conducting the text mining to enable rare diseases to be added to the database, starting from the rare diseases in the [Monarch Disease Ontology](https://monarchinitiative.org/disease) or the [Orphanet Ontology](https://bioportal.bioontology.org/ontologies/ORDO). Because we expect that many fewer articles are written about rare diseases than about common diseases, we must first test that that text-mining approach will provide useful information also about rare diseases.

*Project advisors: [Alexander Junge](/people/alexanderjunge/) and [Lars Juhl Jensen](/people/larsjuhljensen/)*
