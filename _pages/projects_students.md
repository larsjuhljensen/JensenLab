---
title: Student projects
layout: single
permalink: /projects/students/
sidebar:
  nav: "projects"
---
We are always looking for Master's students to join the lab to work on projects. All projects are estimated to last between three and six months and basic programming knowledge is required. Please contact us if you are interested in doing a project with us.

Text mining of the biomedical literature has been successful in extracted interactions between a broad spectrum of biomedical entities. The JensenLab co-develops a range of widely used [resources](/resources/) that catalog association, such as STRING for protein--protein interactions and DISEASES for disease--gene associations. A central component of all resources is the automatic mining of abstracts and open access full-text articles available in PubMed. We have several open student projects related to this.

## Detecting "paper-mill publications"

Scientific fraud is a growing concern in research and has important implications for text mining. The scientific community is fighting against it, exemplified by databases like [Retraction Watch](https://retractionwatch.com) and [PubPeer](https://pubpeer.com). In this project you will implement a machine learning-based method to detect fraud in the biomedical literature. The method that you will develop during this project should be able using the text and metadata from these publications, to detect those originating from so-called ["paper mills"](https://scienceintegritydigest.com/2020/02/21/the-tadpole-paper-mill/) [of](https://scienceintegritydigest.com/2020/07/05/the-stock-photo-paper-mill/) [already](https://scienceintegritydigest.com/2020/07/23/the-effect-paper-mill/) [discovered](https://scienceintegritydigest.com/2020/07/28/the-48-mini-mill/) and, ideally, detect yet unknown “paper mills”. Succeeding in developing this method would allow automatic detection of a list of publications, which should not be text mined for associations between biological entities. This information will feed into the text-mining pipeline that is used to update databases like [STRING](https://string-db.org) and [DISEASES](https://diseases.jensenlab.org), which serve thousands of scientists every day.

The project a great opportunity to work with text classification and clustering methods and to become familiar with the machine/deep-learning frameworks used in text mining.

*Project advisors: [Katerina Nastou](/people/katerinanastou/) and [Lars Juhl Jensen](/people/larsjuhljensen/)*

## Text mining beyond PubMed

[Earlier work](https://doi.org/10.1371/journal.pcbi.1005962) showed that using full-text articles yields considerable improvements compared to PubMed abstracts alone. Motivated by these results, the main focus of this project is to explore resources for text mining beyond PubMed and to study the effect of incorporating additional text sources on the quality of the extracted associations. The quality will be measured by comparing them to a gold standard of expert-curated associations. Potential sources of text include the 10000+ relevant preprints available in bioRxiv, patents available via USPTO, clinical trial records, and proposals of funded research grants.

The project is ideal to get started with co-occurrence-based text mining, improve your skills on the command line for handling and cleaning large data files, and become more proficient in a programming language used for data analysis (such as Python).

*Project advisors: [Dhouha Grissa](https://dgrissa.wixsite.com/dhouha-grissa) and [Lars Juhl Jensen](/people/larsjuhljensen/)*

## Connecting lifestyle and diseases

To adress the challenging task of extracting information on lifestyle from text, we have developed a prototype lifestyle-factor ontology. The goals of this project are to enhance this prototype to produce a vocabulary and to subsequently use it in combination with existing disease vocabularies to extract associations between diseases and lifestyle factors from the biomedical literature. To enrich the lifestyle factors ontology you will train deep learning-based language models to detect terms from the scientific literature and evaluate whether these are synonyms of existing terms or new terms, which are currently missing in the ontology. Moreover, you will use the results from pre-trained models to resolve cases of ambiguity with other entity types. Following the creation of the novel lifestyle vocabulary, you will use the in-house dictionary-based tagger to extract associations between these factors and diseases from the entire biomedical literature.

This project allows you to learn how to apply text-mining techniques to new knowledge domains, combining existing dictionary-based tools and deep learning-based frameworks.

*Project advisors: [Katerina Nastou](/people/katerinanastou/) and [Lars Juhl Jensen](/people/larsjuhljensen/)*
