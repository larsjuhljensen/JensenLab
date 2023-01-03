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

* Publication Preprint: [Title for publication](link/to/biorxiv)

* [The S1000 Corpus](/assets/s1000/S1000-corpus.tar.gz) in [BRAT standoff format](https://brat.nlplab.org/standoff.html)

## Datasets

* There is a [Zenodo](https://zenodo.org/deposit/7064902) project related to S1000 that contains: 
  * the dictionary used by [Jensenlab tagger](https://github.com/larsjuhljensen/tagger)
  * results from large scale tagging with the Jensenlab tagger 
  * results from large scale tagging with the transformer-based method and 
* The input documents for the large scale runs with
  * Jensenlab tagger are hosted [here](https://a3s.fi/s1000/PubMed-input.tar.gz) and [here](https://a3s.fi/s1000/PMC-OA-input.tar.gz)
  * the transformer-based method are hosted [here](https://a3s.fi/s1000/database_documents.tsv.gz)
* the S1000 corpus and
* the guidelines used during annotation of the corpus

_(Note: the input documents are the same, the difference is in the input format)_

## Code

* Useful scripts to reproduce the results presented in the publication can be found in this [Github repo](https://github.com/katnastou/various-scripts-for-S1000)

* The codebase used for training the deep learning-based model can be found in this [Github repo](/link/to/github) together with a link to the model used for large-scale tagging of the literature.
