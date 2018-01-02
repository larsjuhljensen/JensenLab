---
title: Dictionaries
layout: single
permalink: /resources/textmining/dictionaries
sidebar:
  nav: "resources"
---
Many of the other resources developed in the group rely heavily on dictionary-based named entity recognition (NER) of genes/proteins and other entities and concepts of biomedical relevance. We have thus developed a wide range of biomedical dictionaries, which have been tuned to work well with our open source NER software.

The gene/protein dictionary is based on the alias file of the [STRING](https://string-db.org/) database. For convenience, we make available separate dictionaries for human and selected eukaryotic model organisms:
* [Homo sapiens](http://download.jensenlab.org/human_dictionary.tar.gz)
* [Mus musculus](http://download.jensenlab.org/mouse_dictionary.tar.gz)
* [Rattus norwegicus](http://download.jensenlab.org/rat_dictionary.tar.gz)
* [Sus scrofa](http://download.jensenlab.org/pig_dictionary.tar.gz)
* [Drosophila melanogaster](http://download.jensenlab.org/fly_dictionary.tar.gz)
* [Caenorhabditis elegans](http://download.jensenlab.org/worm_dictionary.tar.gz)
* [Saccharomyces cerevisiae](http://download.jensenlab.org/yeast_dictionary.tar.gz)

Most of our other dictionaries are built based on existing taxonomy and ontology resources:
* [Organisms](http://download.jensenlab.org/organisms_dictionary.tar.gz)
* [Compartments](http://download.jensenlab.org/compartments_dictionary.tar.gz)
* [Tissues](http://download.jensenlab.org/tissues_dictionary.tar.gz)
* [Diseases](http://download.jensenlab.org/diseases_dictionary.tar.gz)
* [Phenotypes](http://download.jensenlab.org/phenotypes_dictionary.tar.gz)
* [Environments](http://download.jensenlab.org/environments_dictionary.tar.gz)

In addition to the dictionaries listed above, we also provide the combined [full dictionary](http://download.jensenlab.org/tagger_dictionary.tar.gz), which is used for text-mining in our databases, as well as the reduced [tagger dictionary](http://download.jensenlab.org/tagger_dictionary.tar.gz), which is used by the Tagger web service.
