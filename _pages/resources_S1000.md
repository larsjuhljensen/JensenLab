---
title: S1000 corpus
layout: single
permalink: /resources/s1000/
sidebar:
  nav: "s1000"
---

The S1000 corpus is a comprehensive manual reannotation and extension of the S800 corpus that allows highly accurate recognition of species names, both for machine learning and dictionary-based methods. 
In this page we have gathered links to the publication, the corpus, datasets and codebases related to this project.

## Publication and Corpus

* Publication in Oxford Bioinformatics: [S1000: A better taxonomic name corpus for biomedical information extraction](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btad369/7192170)

* [The S1000 Corpus](/assets/s1000/S1000-corpus.tar.gz) in [BRAT standoff format](https://brat.nlplab.org/standoff.html)

## Datasets

* The [Zenodo](https://doi.org/10.5281/zenodo.7064902) project related to S1000 that contains: 
  * The S1000 corpus split in training, development and test sets in BRAT and CoNLL formats
  * The guidelines used during annotation of the corpus (also available as an annodoc [here](https://katnastou.github.io/s1000-corpus-annotation-guidelines/))
  * the dictionary used by [Jensenlab tagger](https://github.com/larsjuhljensen/tagger)
  * results from large scale tagging with the Jensenlab tagger 
  * the model used for the large scale run of the transformer-based method and
  * results from large scale tagging with the transformer-based method

* The input documents for the large scale runs with:
  * Jensenlab tagger are hosted [here](https://a3s.fi/s1000/PubMed-input.tar.gz) and [here](https://a3s.fi/s1000/PMC-OA-input.tar.gz)
  * the transformer-based method are hosted [here](https://a3s.fi/s1000/database_documents.tsv.gz)
_(Note: the pre-processed input documents are the same, the difference is in the document format for the two methods)_

## Code

* Useful scripts to reproduce the results presented in the publication can be found in this [Github repo](https://zenodo.org/record/7650251#.Y--QPrTMJR4)

* The codebase for the transformer-based NER tagger can be found [here](https://zenodo.org/record/8034112) and the codebase used for the large scale run [here](https://zenodo.org/record/8034152)
