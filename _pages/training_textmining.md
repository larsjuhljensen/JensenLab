---
title: Text-mining exercises
layout: single
permalink: /training/textmining/
sidebar:
  nav: "training-textmining"
---
## Learning objectives

In these exercises, we will use a variety of text-mining tools and databases based on text mining, to interpret the results from microbiome studies. The exercises will teach you how to:

* automatically highlight named entities in a web page
* use named entity recognition for synonym-aware information retrieval
* extract associations based on cooccurrence of entities in the literature
* discover novel, indirect associations between entities
* perform text-mining-based term enrichment analysis

## Prerequisites

Whereas exercise 1 requires only a web browser, parts of exercise 2 takes place on the command line and involves running Python scripts. To follow exercise 2, you thus need access to a Mac or Linux computer with Python installed, and you need basic knowledge of how to use the command line.

## Exercise 1

In this exercise we will first introduce the basics of text mining: 1) dictionary-based named entity recognition and 2) how this can used to help retrieve literature. Afterwards we will move on to how one can use the complete literature to 3) extract associations between entities and finally 4) how these associations can be used for knowledge discovery.

### 1.1 Named entity recognition

The goal of named entity recognition (NER) is to find names mentioned in text and resolve them to the underlying biomedical entities (document → A, B, C). To illustrate this, we will use the EXTRACT tool, which is designed to use NER to support manual database curation.

Install the EXTRACT bookmarklet as described on the [EXTRACT website](https://extract.jensenlab.org/).

Open the paper "Intestinal Microbiota and the Efficacy of Fecal Microbiota Transplantation in Gastrointestinal Disease" ([Aroniadis et al., 2014](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4073534/)) and click the **EXTRACT** bookmarklet. After a short time, terms should be highlighted in the text.

_What do the different colors mean?_

By clicking or hovering over a tagged term, you will get a popup that includes its standard name, entity type, database or ontology identifier, and a link to its reference record. Click or hover over **Micrococcus pyogenes**.

_What is the difference between Micrococcus pyogenes and Staphylococcus aureus?_

Select the **Keywords** line and click the **EXTRACT** bookmarklet. Hover over terms in the text or lines in the table.

_What happens?_

Use the buttons in the popup to copy the data into a spreadsheet/text file or save it in tabular format.

_Which information is then provided in addition to what is shown in the popup?_

### 1.2 Information retrieval

The goal of information retrieval (IR) is to find the documents pertaining to a topic of interest. When the topic is a biological entity (A), NER can be used to index the literature and thereby support retrieval of relevant documents (A → documents).

We run the same NER system used in EXTRACT on entire PubMed every week and make the results available through a suite of web resources. One such resource is [ORGANISMS](https://organisms.jensenlab.org/). It allows users to retrieve abstracts that mention any organism of interest (specified by an NCBI TaxID) based on the NER results.

Go to <https://organisms.jensenlab.org/> and query for **S. aureus**. You are now presented with several options, since there are many genera starting with S that include an aureus species. Click on the **Staphylococcus aureus** (taxid:1280) row to view the abstracts for this species.

_Do the abstracts shown all mention Staphylococcus aureus?_

Go back to the search page (e.g. by clicking **ORGANISMS** in the header) and query for **Firmicutes**. You are again presented with many options including the **Firmicutes** phylum itself (taxid:1239) as well as numerous species and strains. Click on the row for the phylum to view abstracts.

_Which taxa do you see abstracts for?_

### 1.3 Information extraction

The goal of cooccurrence-based information extraction (IE) is to link entities (A, B, C) to each other based on them being mentioned together in documents (A → documents → B; B → documents → C).

Go to <https://diseases.jensenlab.org/> and query for **Crohn disease**. Again, click on it on the disambiguation page (like in the ORGANISMS resource).

_Which gene is most strongly associated with Crohn's disease according to text mining?_

Click on **NOD2** in the text-mining table.

_Do the abstracts in fact support an association between Crohn's disease and NOD2?_

Cooccurrence-based IE is a very generic approach, which can be used to find associations between any two types of entities for which we can do NER. For example, we can use the same approach to link Staphylococcus aureus together with the gene NOD2:

<https://organisms.jensenlab.org/Entity?documents=10&type1=-2&id1=1280&type2=9606&id2=ENSP00000300589>

### 1.4 Knowledge discovery

The goal of knowledge discovery is to find indirect associations between entities (A, C) via other entities (B). In the so-called closed discovery problem, we search for B entities that can explain an observed association between A and C (A → B ← C), which may never have been mentioned together in the literature. For example, we saw above that both Crohn's disease and Staphylococcus aureus have links to NOD2, which could mechanistically explain an observed association between Staphylococcus aureus and Crohn’s disease.

[ARROWSMITH](http://arrowsmith.psych.uic.edu/cgi-bin/arrowsmith_uic/start.cgi) is a tool for discovering such associations in a systematic manner; its Two-Node Literature Search corresponds to the closed discovery problem.

Open ARROWSMITH and do a basic two-node literature search using **Staphylococcus aureus** as A-literature and **Crohn's disease** as C-literature. After some minutes you should see a ranked list of B-terms that were mentioned in both the A-literature and the C-literature.

_Which is the top-ranking B-term?_

Inspect some of the literature supporting the A–B and the B–C associations.

_Does B provide a plausible connection between A and C?_

## Exercise 2

In this exercise, we will focus on how one can utilize the text-mining tools used in exercise 1 to interpret the results from a microbiome analysis. To this end, we will start from the results published on the human colorectal cancer microbiome ([Zeller et al., 2014](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4299606/)).

It is important to note that there are currently no dedicated text-mining tools that have been designed to aid microbiome analysis. What we will do is thus to (ab)use existing text-mining tools and resources, to illustrate what is already now possible with text-mining and which will hopefully be possible to do in a more user-friendly manner in the future.

### 2.1 Using NER to dig deeper into the literature

Colorectal cancer studies have revealed a strong cooccurrence pattern between the proinflammatory Fusobacterium nucleatum and Parvimonas micra. This led to a systematic search for literature linking also the latter bacterial species to inflammatory response. A simple PubMed search retrieves only three publications:

<https://www.ncbi.nlm.nih.gov/pubmed/?term=%22Parvimonas+micra%22+%22inflammatory+response%22>

Of these, only one had been published when the colorectal cancer microbiome was being analyzed, and it sheds no light on the topic. However, since Parvimonas micra has an NCBI Taxon ID (taxid:33033) and inflammatory response is a GO term (GO:0006954), we can instead use the results of NER to retrieve relevant documents:

<http://organisms.jensenlab.org/Entity?documents=10&type1=-2&id1=33033&type2=-21&id2=GO:0006954>

Because NER makes use of synonyms, this retrieves several additional publications. Inspect these abstracts.

_Are they relevant and why were they were not found by the initial search?_

One of the abstracts (Yoshioka et al., 2005) reveals a possible link between the two bacteria and oral inflammatory response: Parvimonas micra can bind to lipopolysaccharides on Gram-negative bacteria such as Fusobacterium nucleatum and thereby induce inflammatory response. This publication was missed by the PubMed query, because Parvimonas micra is referred to under its older name Peptostreptococcus micros. The species is thus mentioned, but a search for its current name will not retrieve it.

Open the abstract by Yoshioka et al. in PubMed and run EXTRACT on it. Inspect the tagging of Peptostreptococcus micros.

_Which name is listed for the species in the popup?_

### 2.2 Retrieval of literature linking taxa to a disease

Above, we saw how existing text-mining resources can be used to retrieve abstracts that mention a species of interest with a disease of interest. Very similar to the previous exercise, we can easily look up the abstracts that mention, for example, Fusobacterium nucleatum (taxid:851) together with colorectal cancer (DOID:9256):

<https://organisms.jensenlab.org/Entity?documents=10&type1=-2&id1=851&type2=-26&id2=DOID:9256>

To do this systematically for all taxa found in a microbiome study, automation is desirable. One could obviously very easily produce a web page with links like the one above for a list of organisms. However, we will instead directly produce a list of PMIDs for each organism, in which the organism is co-mentioned with the disease of interest.

The first step in such an information retrieval task is to find the set of documents that mention the disease of interest. The PMIDs of all abstracts that mention a given disease, including colorectal cancer, can be found in this file:

<http://download.jensenlab.org/disease_textmining_mentions.tsv>

The second step is to similarly retrieve the PMIDs that mention each organism, which can be found in this file:

<http://download.jensenlab.org/organism_textmining_mentions.tsv>

All we now need is a script that does the following steps:
1.	Load the PMIDs associated with the disease of interest into memory
2.	Read the NCBI TaxIDs for each organisms of interest.
3.	For each PMID, check if it is associated with the disease and print it if this is the case

We have made a [Python script]({{ site.baseurl }}/assets/textmining/disease_comentions.py) that does this and prepared a [file with NCBI TaxIDs]({{ site.baseurl }}/assets/textmining/organisms.txt) of the organisms of interest from the colorectal cancer microbiome study. Download both and run:

```
python disease_comentions.py DOID:9256 organisms.txt
```

The script writes its output to the terminal, which you can redirect to a file with the > operator if desired. The format of the tab-delimited output is the same as the input file with organism mentions: the first column contains the NCBI TaxID and the second column contains a space-delimited list of PMIDs. These PMIDs are the abstracts that mention the organism as well as the disease of interest.

These PMIDs can serve as a starting point for a variety of downstream analyses, including calculating simple count statistics, manually inspecting/curating all the associated articles, or retrieving all abstract texts for additional automatic text-mining analyses. The script can trivially be modified to retrieve PMIDs associating organisms with other types of named entities than diseases, such as tissues or environmental descriptors.

### 2.3 Characterization of microbiomes

Already prior to the microbiome study analyzed here, it had been noted that several bacteria associated with colorectal cancer were first described as oral pathogens. It had also been suggested that their invasion of the gut might cause or contribute to tumorigenesis (Warren et al., 2013).

To explore this in a systematic manner, we will investigate text-mined associations between bacteria identified in the colorectal cancer microbiome study and tissues.

The first step is thus to download the complete sets of text-mined associations between organisms (NCBI TaxIDs) and tissues (BTO terms):

<http://download.jensenlab.org/organism_tissue_textmining_full.tsv>

With this file at hand, we can count how many of the bacteria linked to colorectal cancer are associated with each tissue in the literature. We have made a [Python script]({{ site.baseurl }}/assets/textmining/term_enrichment.py) that does this and prepared a [file with NCBI TaxIDs]({{ site.baseurl }}/assets/textmining/organisms.txt) from the colorectal cancer microbiome study. Download both and run this command:

```
python term_enrichment.py organism_tissue_textmining_full.tsv 5 organisms.txt
```

The arguments for this command are the file with organism–term associations, the z-score cutoff to be applied to these, and the file of organisms for which to count term associations. The results show that even at this very stringent z-score cutoff, three of the organisms are associated with each of the terms **Dental plaque**, **Mouth**, and **Saliva**.

You can also count for both a foreground and a background set of organisms and test each tissue term for statistically significant overrepresentation in the foreground set. To do so also download the [file with all bacteria identified in the study]({{ site.baseurl }}/assets/textmining/background.txt) for use as background and run:

```
python term_enrichment.py organism_tissue_textmining_full.tsv 5 organisms.txt background.txt 0.005
```

In this command, the additional last two arguments are the file with the background set of organisms and the p-value threshold. The output for each term includes its identifier, its name, the counts for both sets of organisms, and the uncorrected p-value. The results show that oral bacteria indeed appear to be overrepresented among the set of organisms associated with colorectal cancer, although the p-values should obviously must be corrected for multiple testing before claiming significance.

These types of analyses are by no means limited to tissues. If the task asks for it, equivalent analyses can be done for, e.g., diseases or environmental descriptors.

Test for a link to oral diseases using the following file of organism–disease associations:  
<http://download.jensenlab.org/organism_disease_textmining_full.tsv>

### 2.4 Mining for indirect associations

After Fusobacterium nucleatum, the most overrepresented bacterial species in samples from colorectal cancer patients is Peptostreptococcus stomatis. A search for abstracts linking Peptostreptococcus stomatis to colorectal cancer retrieves a few publications; however, none of these shed any light on the association:

<https://organisms.jensenlab.org/Entity?documents=10&type1=-2&id1=341694&type2=-26&id2=DOID:9256>

Use ARROWSMITH to search for B-terms that connect the A-term **Peptostreptococcus stomatis** to the C-term **colorectal cancer**. Look through the list of suggested B-terms.

Most of the top terms are very general terms related to microbiome sequencing. However, multiple terms related to oral squamous cell carcinomas are also found to be linked both to the species in question and to colorectal cancer. Inspect the underlying literature for this indirect association in ARROWSMITH.

_Does this indirect association appear to hold up to closer scrutiny?_

Similarly, query ARROWSMITH for terms connecting **Lactobacillus ruminis** to **colorectal cancer**. This should suggest inflammation as a possible (if somewhat vague) connection between the two.

## Supporting literature

Jensen LJ, Saric S and Bork P (2006). Literature mining for the biologist: from information retrieval to biological discovery. *Nature Reviews Genetics*, **7**:119–129.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/16418747) [Full text](https://doi.org/10.1038/nrg1768)

Fleuren WWM and Wynand Alkema W (2015). Application of text mining in the biomedical domain. Methods, **74**:97–106.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/25641519) [Full text](https://doi.org/10.1016/j.ymeth.2015.01.015)

Brbic M, Piskorec M, Vidulin V, Krisko A, Smuc T and Supek F (2017). The landscape of microbial phenotypic traits and associated genes. *Nucleic Acids Research*, **44**:10074–10090.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/27915291) [Full text](https://doi.org/10.1093/nar/gkw964)

[![CC By 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
