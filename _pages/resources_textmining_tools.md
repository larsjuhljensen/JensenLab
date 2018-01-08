---
title: Text-mining tools
layout: single
permalink: /resources/textmining/tools
sidebar:
  nav: "resources"
---
The group has together with collaborators developed two real-time text-mining tools, namely [Reflect](http://reflect.ws/) and [EXTRACT](https://extract.jensenlab.org/), which can be used within a web browser to augment the functionality. Both tools identify named entities such as genes/proteins within web pages, highlight the identified names, and provide popups with information and functionality related to entities. Whereas Reflect aims to augment pages with information relevant to typical readers, EXTRACT was designed primarily with database curators in mind. We currently recommend using EXTRACT as it is most up-to-date.

We also make available precomputed text-mining results, which are updated weekly and include both the direct results from named entity recognition and derived co-occurrence statistics. Users can access many of these through the topic-specific web resources [ORGANISMS](https://organisms.jensenlab.org/), [COMPARTMENTS](https://compartments.jensenlab.org/), [TISSUES](https://tissues.jensenlab.org/), and [DISEASE](https://diseases.jensenlab.org/). The text-mining results can also be accessed through a [RESTful API](https://api.jensenlab.org/).

The source code for the underlying tagger software is available at [Bitbucket](https://bitbucket.org/larsjuhljensen/tagger/), along with a detailed README describing how to use the tagger. If you prefer to not have to compile it yourself, you can also access it as a Docker container at [Docker Hub](https://hub.docker.com/r/larsjuhljensen/tagger/).
