---
title: Text-mining projects
layout: single
permalink: /projects/textmining/
sidebar:
  nav: "projects"
---
The group works on a number of projects related to biomedical text mining. Because text-mining technologies are broadly applicable, these projects span a number of application areas within biomedicine. All of the projects described below make use of the JensenLab tagger software to recognize named entities such as proteins or diseases in text.

## Microbiome interpretation

Together with the [Pafilis group](http://epafilis.info/) we apply text mining to analysis of microbial ecosystems. In this context we have developed the [SPECIES](https://species.jensenlab.org/) and [ENVIRONMENTS](https://environments.jensenlab.org/) tools adapted them for tagging of viruses and bacterial biotopes.

Studying microbiomes using metagenomic sequence data is a topic of major interest due to the impact of microbiota on human health and environments; however, interpretation of the data is a major bottleneck. We work to develop text-mining tools that can help by systematically annotating the literature with organisms, diseases, processes, environmental descriptors, and associations among them. Our [text-mining exercises](/training/textmining/) give an overview of what is already possible today.

## Challenges and shared tasks

The text-mining community organizes many so-called challenges and shared tasks in which research groups around the world try to solve the same problems with the goal to find out which approaches work best. We have participated in several [BioCreative](http://www.biocreative.org/) and [BioNLP](http://www.bionlp-st.org/) challenges with excellent results. However, we only participate in such challenges when they naturally align with the research projects in the group.

[EXTRACT](https://extract.jensenlab.org/) came out as the best scoring tool in the BioCreative V Interactive Annotation Task, which evaluated utility and user experience of annotation tools. TagIt, an adapted version of the tagger software used for all our text-mining projects, produced the best quality results for named entity recognition of both bacteria and habitats in the BioNLP Bacteria Biotope 3 task. Finally, our public tagging web service was one of several servers to manage perfect uptime and performance bottlenecked only by the evaluation servers in the BioCreative V.5 Technical Interoperability and Performance of annotation Servers track.

## Understudied drug targets

The JensenLab is part of the Knowledge Management Central of the NIH program [Illuminating the Druggable Genome](https://druggablegenome.net/). In this project the [text-mining resources](/resources/textmining) developed within the group are used to identify proteins from targetable classes (kinases, G-protein-coupled receptors, and ion channels) in text from the scientific literature as well as funding and patent records. This in turn allows us to help quantify how well studied each protein is, and thereby prioritize the so-called dark targets, about which very little is known.

## Adverse drug reactions

The [SIDER](http://sideeffects.embl.de/) database, which we develop in collaboration with the [Bork group](http://www.bork.embl.de/), uses the JensenLab tagger to extract structured data on side effects and indications of drugs from the unstructured text in the packet inserts describing the drugs.

We also collaborate with the [Brunak group](http://www.cpr.ku.dk/research/disease-systems-biology/brunak/) to apply text-mining to the clinical narrative in Danish electronic health records. This can, for example, be used to link drugs to adverse events, which were not discovered during clinical trials and are not yet described in the package inserts.
