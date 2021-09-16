---
title: Text-mining exercises
layout: single
permalink: /training/textmining/hb/
sidebar:
  nav: "training-textmining-hb"
---
## Learning objectives

In these exercises, we will use a variety of text-mining tools and databases based on text mining to interpret the results from microbiome studies. The exercises will teach you how to:

* automatically highlight named entities in a web page
* use named entity recognition for synonym-aware information retrieval
* extract associations based on cooccurrence of entities in the literature
* perform text-mining-based term enrichment analysis

## Prerequisites

All exercises are purely web-based. We recommend using [Firefox](http://getfirefox.org/), as some functionality will not work in the latest Chrome and Chrome-based browsers.

## Exercise 1

In this exercise we will first introduce the basics of text mining: 1) dictionary-based __named entity recognition__ and 2) how this can used to help __retrieve literature__. Afterwards we will move on to how one can use the complete literature to 3) __extract associations between entities__.

### 1.1 Named Entity Recognition

The goal of named entity recognition (NER) is to find names mentioned in text and resolve them to the underlying biomedical entities (document → entity A, entity B, entity C). To illustrate this, we will use the EXTRACT tool, which is designed to use NER to support manual database curation.

Install the EXTRACT bookmarklet as described on the [EXTRACT website](https://extract.jensenlab.org/). We recommend using [Firefox](http://getfirefox.org/), as some functionality will not work in the latest Chrome and Chrome-based browsers.

_Hint: If the bookmarks toolbar is not showing in Firefox then go the File menu bar and select View → Toolbars → Bookmarks Toolbar → Always show_

Open the paper "Binding of _Actinobacillus actinomycetemcomitans_ lipopolysaccharides to _Peptostreptococcus micros_ stimulates tumor necrosis factor alpha production by macrophage-like cells" ([Yoshioka et al., 2005](https://pubmed.ncbi.nlm.nih.gov/15720573/)) and click the **EXTRACT** bookmarklet. After a short time, terms should be highlighted in the text.

_1. What do the different colors mean?_

By clicking or hovering over a tagged term, you will get a popup that includes its standard name, entity type, database or ontology identifier, and a link to its reference record. Click or hover over **_Peptostreptococcus micros_** and **inflammatory response**.

_2. What is an alternative name for Peptostreptococcus micros? What is the difference between Peptostreptococcus micros and Parvimonas micra?_

_3. What is the NCBI Taxonomy ID of Peptostreptococcus micros and what is the Gene Ontology identifier of inflammatory response?_

Select the **Title** in the paper and click the **EXTRACT** bookmarklet. Hover over terms in the text or lines in the table.

_4. What happens when you hover over the terms under the selected text section?_

Use the buttons in the popup to copy the data into a spreadsheet (e.g. Microsoft excel/[Google sheets](https://docs.google.com/spreadsheets/u/0/)) or text file (e.g. Notepad/[Notepad++](https://notepad-plus-plus.org/downloads/)) or save it in tabular (tsv/csv) format.

_5. Which information is then provided in addition to what is shown in the popup?_

### 1.2 Information retrieval

The goal of information retrieval (IR) is to find the documents pertaining to a topic of interest. When the topic is a biological entity (A), NER can be used to index the literature and thereby support retrieval of relevant documents (A → documents).

We run the same NER system used in EXTRACT on entire PubMed every week and make the results available through a suite of web resources. One such resource is [ORGANISMS](https://organisms.jensenlab.org/). It allows users to retrieve abstracts that mention any organism of interest (specified by an NCBI TaxID) based on the NER results.

Go to <https://organisms.jensenlab.org/> and query for **P. micra**. You are now presented with several options, since there are several genera starting with P that include a micra species. Click on the **Parvimonas micra** (taxid: 33033) row to view the papers for this species.

_6. Do the papers shown on the second page all mention Parvimonas micra?_ (Hint: Press _Next>_ on the top of the table to move to the second page and _[View Text]_ to see the text from the paper)

Go back to the search page (e.g. by clicking **ORGANISMS** in the header) and query for **Firmicutes**. You are again presented with many options including the **Firmicutes** phylum itself (taxid:1239) as well as numerous species and strains. Click on the row for the phylum to view papers.

_7. Which taxa do you see papers for on the first page?_

You can similarly use NER to retrieve abstracts for any disease in the Disease Ontology. For example, the following query will retrieve abstracts for **cancer** (DOID:162):

<https://diseases.jensenlab.org/Entity?documents=10&type1=-26&id1=DOID:162>

_8. Which diseases are highlighted in the first five abstracts?_

### 1.3 Relation extraction

The goal of cooccurrence-based relation extraction (RE) is to link entities (A, B) to each other based on them being mentioned together in documents (A → documents → B).

Go to <https://diseases.jensenlab.org/> and query for **colorectal cancer**. Again, click on it on the Search results page (like in the ORGANISMS resource).

_9. Which gene is most strongly associated with colorectal cancer according to text mining?_

Click on **TP53** in the text-mining table.

_10. Do the abstracts in fact support an association between colorectal cancer and TP53? Comparing it with KRAS which disease-gene association seems to be more clearly stated in the text? Can you think of a reason why?_

Cooccurrence-based relation extraction is a very generic approach, which can be used to find associations between any two types of entities for which we can do NER. For example, we can use the same approach to link the species **_Fusobacterium nucleatum_** together with **colorectal cancer** (DOID:9256):

<https://organisms.jensenlab.org/Entity?documents=10&type1=-2&id1=851&type2=-26&id2=DOID:9256>

_11. Is this association supported by only few papers or is it well established in the literature?_

## Exercise 2

Now we will focus on how one can utilize text-mining tools to interpret the results from a microbiome analysis. To this end, we will start from the results published on the human colorectal cancer microbiome ([Zeller et al., 2014](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4299606/)).

It is important to note that there are currently no dedicated text-mining tools that have been designed to aid microbiome analysis. What we will do is thus to (ab)use existing text-mining tools and resources, to illustrate what is already now possible with text-mining and which will hopefully be possible to do in a more user-friendly manner in the future.

### 2.1 Microbiome characterization with text mining

Now that we've seen what can be generally done let's switch our focus to microbiome data.

Studies on the colorectal cancer microbiome (e.g. [Zeller et al., 2014](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4299606/)) have revealed a strong co-occurrence pattern between the proinflammatory bacterium _Fusobacterium nucleatum_ and _Parvimonas micra_. This led to a systematic search for literature linking also the latter bacterial species to inflammatory response. A simple PubMed search retrieves only four publications:

<https://www.ncbi.nlm.nih.gov/pubmed/?term=%22Parvimonas+micra%22+%22inflammatory+response%22>

Of these, only one had been published when the colorectal cancer microbiome was being analyzed ([Rutger Persson et al., 2014](https://pubmed.ncbi.nlm.nih.gov/18517068/)), and it sheds no light on the topic. However, since, as we saw before, _Parvimonas micra_ has an NCBI Taxonomy ID (taxid:33033) and inflammatory response is a GO term (GO:0006954), we can instead use the results of NER to retrieve relevant documents by plugging in these identifiers in the URL of our database with textmining results:

<http://organisms.jensenlab.org/Entity?documents=100&type1=-2&id1=33033&type2=-21&id2=GO:0006954>

Inspect some of these abstracts (Hint: focus on those where terms are higlighted in blue and red).

_12. Are they relevant and why were they not found by the initial search?_ 

[comment]: # (Because NER makes use of synonyms, this retrieves several additional publications.)

In the results list you can find the abstract we analyzed above ([Yoshioka et al., 2005](https://pubmed.ncbi.nlm.nih.gov/15720573/)) 

_13. Can you find the possible link between Parvimonas micra, Fusobacterium nucleatum and inflammatory response by looking at this abstract?_ (Hint: _Fusobacterium nucleatum_ is a Gram-negative bacterium).

[comment]: # (possible link between the two bacteria and oral inflammatory response: _Parvimonas micra_ can bind to lipopolysaccharides on Gram-negative bacteria such as _Fusobacterium nucleatum_ and thereby induce inflammatory response. This publication was missed by the PubMed query, because _Parvimonas micra_ is referred to under its older name _Peptostreptococcus micros_. The species is thus mentioned, but a search for its current name will not retrieve it. As you saw before, on the popup its current official name shows up.)

Above, we saw how existing text-mining resources can be used to retrieve abstracts that mention a species of interest with a disease of interest. To do this systematically for all taxa found in a microbiome study, automation is desirable. One could obviously partially automate this by producing a web page with links like the one above for a list of organisms. Alternatively, one can download the full results from named entity recognition and write a simple script to identify all abstracts that mention organisms of interest with diseases of interest, which can then serve as a starting point for either manual curation of the associated articles or statistical analyses.

### 2.2 Text mining-based enrichment analysis

Already prior to the microbiome study analyzed here, it had been noted that several bacteria associated with **colorectal cancer** were first described as **oral pathogens**. It had also been suggested that their invasion of the gut might cause or contribute to tumorigenesis ([Warren et al., 2013](https://microbiomejournal.biomedcentral.com/articles/10.1186/2049-2618-1-16)). We will explore this in a systematic manner by investigating the text-mined associations between bacteria identified in the colorectal cancer microbiome study and human tissues.

In that context, the simplest possible characterization is to just count how many of the bacteria associated with colorectal cancer can be associated with each tissue (tissue terms as defined in [Brenda Tissue Ontology (BTO)](https://www.ebi.ac.uk/ols/ontologies/bto)) through text mining. 

To perform such an analysis: 

1) Go to the [SimpleCount](https://simplecount.jensenlab.org/) web server

2) As **Foreground** paste in the list of NCBI TaxIDs corresponding to the bacteria of interest; we have prepared a file with the [colorectal cancer-associated NCBI TaxIDs]({{ site.baseurl }}/assets/textmining/organisms.txt). We leave the **Background** empty for now. 

3) Next select the **Dictionary** that you want counts for (i.e. **Tissues**)

4) Specify a **[Z-score](https://en.wikipedia.org/wiki/Standard_score) cutoff** for the text-mining association (leave at default for now), and 

5) Click the **Count** button. 

After a few seconds, you will see a table with the results of the analysis; you can sort the table by clicking on the column headings.

_14. Which are the most frequent tissue terms? Are these terms specific or very broad?_

Go back to the input page, lower the **Z-score cutoff** to **3.0** and rerun the analysis.

_15. How does this change the results?_

The [SimpleCount](https://simplecount.jensenlab.org/) server also allows you to count terms in both a foreground and a background set of organisms and test each tissue term for statistically significant overrepresentation in the foreground set. 

This type of analysis yields terms that are frequent in the foreground set but not in the background set, as opposed to the terms identified above, which are merely frequent in the foreground set. 

To perform this analysis:

1) Use the same **Foreground** set as in the previous analysis

2) Paste in the [full list of bacteria identified in the study]({{ site.baseurl }}/assets/textmining/background.txt) into **Background**

3) Set the **Z-score cutoff** to **5.0** 

4) set the **P-value cutoff** to **0.001** 

5) and click **Count**

The results table now includes two additional columns, namely the **background count** and the **p-value**. (_Note that the reported p-values are not corrected for multiple testing. If you want to correct for multiple testing you can do Bonferroni correction or calculate the false discovery rate (this is typically done by enrichment tools)_).

_16. Are the overrepresented terms more specific than those with the highest counts?_

These types of analyses are by no means limited to tissues. If the task asks for it, equivalent analyses can be done for, e.g., diseases or environmental descriptors. 

Perform an enrichment analysis for diseases using a **Z-score cutoff** of **5.0**.

_17. Which is the most significantly overrepresented disease?_

## Further questions
Post them on this [Padlet](https://ucph.padlet.org/katerinanastou/2dghxogasnybwh47)

(just double click in the background to add your question) 

## Supporting Lectures

[Biomedical text mining: A short introduction to the core concepts](https://www.youtube.com/watch?v=NcntH0WYp1M)

[Named entity recognition: A deeper dive into methods for finding things mentioned in papers](https://www.youtube.com/watch?v=Uxfedtto8Fo)

[Information retrieval: A deeper dive into methods for finding relevant papers](https://www.youtube.com/watch?v=hCju07CkgNs)

[Relation extraction: A deeper dive into methods for extracting information from text](https://www.youtube.com/watch?v=25u7ZmczdI8)

[Enrichment analysis: A short introduction to the core concepts of gene set enrichment analysis](https://www.youtube.com/watch?v=2NC1QOXmc5o)

## Supporting literature

Jensen LJ, Saric S and Bork P (2006). Literature mining for the biologist: from information retrieval to biological discovery. *Nature Reviews Genetics*, **7**:119–129.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/16418747) [Full text](https://doi.org/10.1038/nrg1768)

Fleuren WWM and Wynand Alkema W (2015). Application of text mining in the biomedical domain. Methods, **74**:97–106.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/25641519) [Full text](https://doi.org/10.1016/j.ymeth.2015.01.015)

Brbic M, Piskorec M, Vidulin V, Krisko A, Smuc T and Supek F (2017). The landscape of microbial phenotypic traits and associated genes. *Nucleic Acids Research*, **44**:10074–10090.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/27915291) [Full text](https://doi.org/10.1093/nar/gkw964)

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
