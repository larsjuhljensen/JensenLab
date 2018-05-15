---
title: Student projects
layout: single
permalink: /projects/students/
sidebar:
  nav: "projects"
---
We are always looking for Master's students to join the lab to work on projects. All projects are estimated to last between three and six months and basic programming knowledge is required. Please contact us if you are interested in doing a project with us.

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
