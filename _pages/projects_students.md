---
title: Student projects
layout: single
permalink: /projects/students/
sidebar:
  nav: "projects"
---
We are always looking for Master's students to join the lab to work on projects. All projects are estimated to last between three and six months and basic programming knowledge is required. Please contact us if you are interested in doing a project with us.

## Deep learning of peptide fragmentation

Tandem mass-spectrometry (MS/MS) has become a method of choice for high-throughput, quantitative analysis in proteomics. Proteins in a sample are isolated and cleaved into peptides, which are then subjected to ionization, mass analysis, fragmentation, and a second step of mass analysis. Identification of the peptides relies on matching of the fragmentation spectra (MS2) to theoretical spectra of possible candidate peptides. Algorithms typically score the concordance between the theoretical and the experimental spectra by evaluating the number of theoretically possible fragment ions observed in the experimental spectra. However, this assumes that each theoretical fragment is equally likely to be observed, which is not the case. On the contrary, MS2 spectra typically have a few dominant fragments, and it would make sense to only look for these to improve identification.

We have a large pool of identified spectra, which can be used to train machine-learning methods to predict the relative intensities of fragments originating from a peptide sequence, in a specific charge state. There is an existing predictor based on a hidden Markov model, which we would like to compare to recursive neural network (RNN) and "long short-term memory" (LSTM) models.

The goal of the project is to evaluate different machine-learning methods on this task to find out which work best and to investigate their pros and cons to understand why. The project requires that you are well versed in Python, since most existing code and libraries are written in Python, and it is a great chance to practice using deep-learning frameworks like Keras as well as data visualization packages.

*Project advisors: [Ufuk Kirik](/people/ufukkirik/) and [Lars Juhl Jensen](/people/larsjuhljensen/)*

## Text mining beyond PubMed

Text mining of the biomedical literature has been successful in extracted interactions between a broad spectrum of biomedical entities. The JensenLab co-develops a range of widely used [resources](/resources/) that catalog association, such as STRING for protein--protein interactions and DISEASES for disease--gene associations. A central component of all resources is the automatic mining of abstracts and open access full-text articles available in PubMed.

[Recent work](https://doi.org/10.1371/journal.pcbi.1005962) showed that using full-text articles yields considerable improvements compared to PubMed abstracts alone. Motivated by these results, the main focus of this project is to explore resources for text mining beyond PubMed and to study the effect of incorporating additional text sources on the quality of the extracted associations. The quality will be measured by comparing them to a gold standard of expert-curated associations. Potential sources of text include the 10000+ relevant preprints available in bioRxiv, patents available via USPTO, clinical trial records, and proposals of funded research grants.

The project is ideal to get started with co-occurrence-based text mining, improve your skills on the command line for handling and cleaning large data files, and become more proficient in a programming language used for data analysis (such as Python).

*Project advisors: [Alexander Junge](/people/alexanderjunge/) and [Lars Juhl Jensen](/people/larsjuhljensen/)*
