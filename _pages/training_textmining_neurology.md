---
title: Text-mining exercises
layout: single
permalink: /training/textmining/neurology/
---
## Learning objectives

In these exercises, we will use a variety of text-mining tools and databases based on text mining to interpret the results from microbiome studies. The exercises will teach you how to:

* automatically highlight named entities in a web page
* use named entity recognition for synonym-aware information retrieval
* extract associations based on cooccurrence of entities in the literature

## Prerequisites

All exercises are purely web-based.

## Exercise 1

In this exercise we will first introduce the basics of text mining: 1) dictionary-based named entity recognition and 2) how this can used to help retrieve literature. Afterwards we will move on to how one can use the complete literature to 3) extract associations between entities and finally 4) how these associations can be used for knowledge discovery.

### 1.1 Named entity recognition

The goal of named entity recognition (NER) is to find names mentioned in text and resolve them to the underlying biomedical entities (document → A, B, C). To illustrate this, we will use the EXTRACT tool, which is designed to use NER to support manual database curation.

Install the EXTRACT bookmarklet as described on the [EXTRACT website](https://extract.jensenlab.org/).

Open the paper "Age-Dependent Brain Gene Expression and Copy Number Anomalies in Autism Suggest Distinct Pathological Processes at Young Versus Mature Ages" ([Chow et al., 2012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3310790/)) and click the **EXTRACT** bookmarklet. After a short time, terms should be highlighted in the text.

_What do the different colors mean?_

By clicking or hovering over a tagged term, you will get a popup that includes its standard name, entity type, database or ontology identifier, and a link to its reference record. Click or hover over **autism** and **NFBD1**.

_What is the main name for autism in Disease Ontology? What is the difference between NFBD1 and MDC1?_

Select the **Author Summary** paragraph in the paper and click the **EXTRACT** bookmarklet. Hover over terms in the text or lines in the table.

_What happens?_

Use the buttons in the popup to copy the data into a spreadsheet/text file or save it in tabular format.

_Which information is then provided in addition to what is shown in the popup?_

### 1.2 Information retrieval

The goal of information retrieval (IR) is to find the documents pertaining to a topic of interest. When the topic is a biological entity (A), NER can be used to index the literature and thereby support retrieval of relevant documents (A → documents).

We run the same NER system used in EXTRACT on entire PubMed every week and make the results available through a suite of web resources. One such resource is [DISEASES](https://diseases.jensenlab.org/). While primarily intended to view disease–gene associations extracted from literature, it can also be used for information retrieval.

Click the following link to retrieve abstracts that mention the gene LRRK2:

<https://diseases.jensenlab.org/Entity?documents=10&type1=9606&id1=ENSP00000298910>

_Do the abstracts shown all mention LRRK2?_

You can similarly use NER to retrieve abstracts for any disease in the Disease Ontology. For example, the following query will retrieve abstracts for **neurodegenerative disease** (DOID:1289):

<https://diseases.jensenlab.org/Entity?documents=10&type1=-26&id1=DOID:1289>

_Which diseases are highlighted in the abstracts?_

### 1.3 Information extraction

The goal of cooccurrence-based information extraction (IE) is to link entities (A, B, C) to each other based on them being mentioned together in documents (A → documents → B; B → documents → C).

Go to <https://diseases.jensenlab.org/> and query for **LRRK**. You are now presented with two options, since there are two gene names starting with LRRK, namely LRRK1 and LRRK2. Click on the **LRRK2** row to view the disease associations for this gene.

_Which disease is most strongly associated with LRRK2 according to text mining?_

Click on **Parkinson's disease** in the text-mining table.

_Do the abstracts in fact support an association between epilepsy disease and SCN1A?_

Cooccurrence-based IE is a very generic approach, which can be used to find associations between any two types of entities for which we can do NER. For example, we can use the same approach to extract LRRK2-associated terms from the mammalian phenotype:

<https://phenotypes.jensenlab.org/Entity?textmining=20&type1=9606&type2=-36&id1=ENSP00000298910>

## Exercise 2

In this exercise, we will focus on how one can utilize the text-mining tools used in exercise 1 to analyze an observed association between epilepsy and autism spectrum disorders.

### 2.1 Using NER to dig deeper

The SCN2A gene is well known to be involved in epilepsy. To check if it has also been implicated autism spectrum disorder, we will perform a systematic search for literature linking the two. A simple PubMed search retrieves only seven publications:

<https://www.ncbi.nlm.nih.gov/pubmed/?term=%22SCN2A%22+%22autism+spectrum+disorders%22>

Since SCN2A (ENSP00000283256) and autism spectrum disorder (DOID:0060041) are both named entities in our dictionary, we can instead use the results of NER to retrieve relevant documents:

<https://diseases.jensenlab.org/Entity?documents=50&type1=9606&type2=-26&id1=ENSP00000283256&id2=DOID:0060041>

The NER-based approach retrieves several many publications. Inspect these abstracts.

_Are they relevant and why were they were not found by the initial search?_

### 2.2 Linking diseases via genes

Above, we saw how existing text-mining resources can be used to retrieve abstracts connecting entities of interest and to extract associations. We will now use this in a few different ways to attempt to find genes that link two diseases of interest.

The first idea is to use NER-based information retrieval to find abstracts that mention both epilepsy (DOID:1826) and autism spectrum disorder (DOID:0060041). Click the link below to view these abstracts:

<https://diseases.jensenlab.org/Entity?documents=10&type1=-26&&type2=-26&id1=DOID:1826&id2=DOID:0060041>

_Which, if any, genes do you see mentioned in these abstracts_

This approach obviously only works when the association between the two diseases is sufficiently well described in the literature for there to be abstracts that mention both diseases as well as the genes of interest. If that is not the case, but one has a candidate gene in mind, one can instead use information extraction to obtain a list of diseases for the gene in question to see if it is in fact associated with both diseases in the literature. Go to <https://diseases.jensenlab.org/>, query for **SCN2A**, and view the disease associations obtained from text mining.

_Is SCN2A associated with both diseases of interest?_

When one does not have a candidate gene, the best solution is to obtain two gene lists, one for each disease, and then identify the ones that rank high on both lists. This is a variant of the closed knowledge discovery problem. It is unfortunately not currently possible to perform such an analysis via a web interface, but it can be done by downloading the complete set disease–gene association from the [DISEASES downloads page](https://diseases.jensenlab.org/Downloads) and analyzing them in Python or R. Alternatively, the analysis can be performed through Cytoscape as illustrated in the [Cytoscape stringApp exercises](https://jensenlab.org/training/stringapp/).

## Supporting literature

Jensen LJ, Saric S and Bork P (2006). Literature mining for the biologist: from information retrieval to biological discovery. *Nature Reviews Genetics*, **7**:119–129.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/16418747) [Full text](https://doi.org/10.1038/nrg1768)

Fleuren WWM and Wynand Alkema W (2015). Application of text mining in the biomedical domain. Methods, **74**:97–106.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/25641519) [Full text](https://doi.org/10.1016/j.ymeth.2015.01.015)

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
