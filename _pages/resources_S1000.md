---
title: S1000 corpus
layout: single
permalink: /resources/s1000/
sidebar:
  nav: "s1000"
---

The S1000 corpus is a comprehensive manual reannotation and extension of the S800 corpus that allows highly accurate recognition of species names, both for machine learning and dictionary-based methods. 
In this page we have gathered links to the publication, the corpus, datasets and codebases related to this project 

## Publication

* Publication Preprint: [Title for publication](link/to/biorxiv)

* [The S1000 Corpus](/assets/s1000/S1000-corpus.tar.gz) in [BRAT standoff format](https://brat.nlplab.org/standoff.html)

## Datasets

* The S1000 corpus, the dictionary used by [Jensenlab tagger](https://github.com/larsjuhljensen/tagger), results from large scale tagging with both the Jensenlab tagger and the transformer-based method, and the annotation guidelines are available at [Zenodo](https://zenodo.org/deposit/7064902). 
* The input documents for Jensenlab tagger are hosted [here](https://a3s.fi/s1000/PubMed-input.tar.gz) and [here](https://a3s.fi/s1000/PMC-OA-input.tar.gz) and for the transformer-based method [here](https://a3s.fi/s1000/database_documents.tsv.gz)

## Code

* Useful scripts to reproduce the results presented in the publication can be found in this [Github repo](https://github.com/katnastou/various-scripts-for-S1000)

* The codebase used for training the deep learning-based model can be found in this [Github repo](/link/to/github) together with the model used for large-scale tagging of the literature.
