---
title: Text-mining tools
layout: single
permalink: /resources/textmining/tools
sidebar:
  nav: "resources"
---
The group has together with collaborators developed two interactive text-mining tools, namely [Reflect](http://reflect.ws/) and [EXTRACT](https://extract.jensenlab.org/), which can be used within a web browser to augment the functionality. Both tools identify named entities such as genes/proteins within web pages, highlight the identified names, and provide popups with information and functionality related to entities. Whereas Reflect aims to augment pages with information relevant to typical readers, EXTRACT was designed primarily with database curators in mind. We currently recommend using EXTRACT as it is most up-to-date.

The source code for the tagger software is available at [Bitbucket](https://bitbucket.org/larsjuhljensen/tagger/), along with a detailed README describing how to use the tagger. If you prefer to not have to compile it yourself, you can also access it as a Docker container at [Docker Hub](https://hub.docker.com/r/larsjuhljensen/tagger/).
