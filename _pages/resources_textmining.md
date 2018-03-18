---
title: Text-mining resources
layout: single
permalink: /resources/textmining/
sidebar:
  nav: "resources"
---
Many of the other resources developed in the group rely heavily on dictionary-based named entity recognition (NER) of genes/proteins and other entities and concepts of biomedical relevance. We have thus developed a wide range of biomedical dictionaries, which have been tuned to work well with the associated open-source NER software.

## Dictionaries

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

## Tools

The group has together with collaborators developed two real-time text-mining tools, namely [Reflect](http://reflect.ws/) and [EXTRACT](https://extract.jensenlab.org/), which can be used within a web browser to augment the functionality. Both tools identify named entities such as genes/proteins within web pages, highlight the identified names, and provide popups with information and functionality related to entities. Whereas Reflect aims to augment pages with information relevant to typical readers, EXTRACT was designed primarily with database curators in mind. We currently recommend using EXTRACT as it is most up-to-date.

We also make available precomputed text-mining results, which are updated weekly and include both the direct results from named entity recognition and derived co-occurrence statistics. Users can access many of these through the topic-specific web resources [ORGANISMS](https://organisms.jensenlab.org/), [COMPARTMENTS](https://compartments.jensenlab.org/), [TISSUES](https://tissues.jensenlab.org/), and [DISEASES](https://diseases.jensenlab.org/). The text-mining results can also be accessed through a [RESTful API](https://api.jensenlab.org/).

The source code for the underlying tagger software is available at [Bitbucket](https://bitbucket.org/larsjuhljensen/tagger/), along with a detailed README describing how to use the tagger. If you prefer to not have to compile it yourself, you can access it as a Docker container at [Docker Hub](https://hub.docker.com/r/larsjuhljensen/tagger/).

To further improve the quality of the text-mining results, we are developing a context-aware co-occurrence scoring system named CoCoScore. Although this is not yet implemented in the resources listed above, it is already available as open-source software on [GitHub](https://github.com/JungeAlexander/cocoscore).
