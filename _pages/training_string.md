---
title: STRING exercises
layout: single
permalink: /training/string/
sidebar:
  nav: "training-string"
---
## Learning objectives

In these exercises, we will use the [STRING](https://string-db.org/), [STITCH](http://stitch-db.org/), and [DISEASES](https://diseases.jensenlab.org/) databases through their respective web interfaces. The exercises will teach you how to:

* retrieve a STRING network for a protein of interest
* interpret the different visual representations
* inspect the evidence behind an interaction
* retrieve a STITCH network for chemical compound of interest
* use DISEASES to find proteins associated with a disease of interest

## Exercise 1

### 1.1 Single protein query

We will first retrieve a STRING network for human insulin receptor (INSR). Go to <https://string-db.org/>, open the **Protein by name** search interface, and type **INSR** in the field **Protein Name**. You can either specify **Homo sapiens** in the **Organism** field leave it on **auto-detect**. Click **SEARCH**. If you specified the organism, you will immediately receive a protein network; otherwise you will first be presented with a disambiguation page on which you can specify that you meant the human protein.

### 1.2 Visual representations

The STRING web interface provides several different visual representations of the network. The **Settings** tab below the network view allows you to change between different visual representations of the same network. Try changing between the **confidence** and **evidence** views; do not forget to press the **UPDATE** button.

_Which information is shown for the edges in each representation? Why are there sometimes multiple lines connecting the same two proteins in the evidence representation?_

### 1.3 Evidence viewers

A key feature of the STRING web interface is the evidence viewers. One should not rely purely on the confidence scores; it is important to inspect the actual evidence underlying an interaction before relying on it, for example, for designing experiments.

_Which types of evidence support the interaction between insulin receptor (INSR) and insulin receptor substrate 1 (IRS1)?_

Further detail on the evidence of an interaction can be seen in a popup by clicking on the corresponding edge in the network. Click on the edge between INSR and IRS1 to view its popup; you may need to move the nodes to make this easier.

_Which type of evidence gives the largest contribution to the confidence score?_

Click on the **Show** button to view the experimental evidence for the interaction.

_Which types of experiments support this interaction?_

### 1.4 Query parameters

The **Settings** tab also allows you to modify detailed parameters for the search, such as the types of evidence to use (**active interaction sources**), the **minimum required interaction score**, and the **max number of interactors to show**.

Change the **minimum required interaction score** to high confidence (0.700).

_Does this change the set of proteins shown? Does it change the interactions shown?_

Turn off all evidence types except experiments.

_Does this change the set of proteins shown in the network?_

Increase the **max number of interactors to show** to 20.

_How many interaction partners of INSR do you get in the network?_

Change the **minimum required interaction score** back to 0.400.

_How many INSR interactors do you now get?_

Turn on all evidence types back on.

_Does this change the set of proteins shown in the network?_

## Exercise 2

### 2.1 Chemical compound query

To retrieve for a chemical compound, go to <http://stitch-db.org/>, type **aspirin** in the **Item Name** field, type **Homo sapiens** in **Organism**, and click the **SEARCH** button. You should now see a network of proteins associated with aspirin, including PTGS1 and PTGS2, which are the direct targets of aspirin.

### 2.2 Binding assay data

Click the interaction between aspirin and PTGS1 and then the **Show** button next to **Experimental/Biochemical Data** in the popup. The evidence viewer now shows all the available binding assay data for this interaction, including the binding affinities (IC50 values).

## Exercise 3

### 3.1 Disease query

Go to <https://diseases.jensenlab.org/>, type **Parkinson** in the search field, and click the **search** button. The web interface will now show the search results, which include all diseases and protein names starting with the search term. Click **Parkinson's disease** to get to the results page showing proteins associated with the disease.

Like STRING and STITCH, the DISEASES database integrates several types of evidence, in this case automatic text mining, manually curated knowledge, and experimental evidence from genome-wide association studies.

_Are there any proteins that are supported by all three types of evidence?_

### 3.2 Validation of text mining

The DISEASES database too allows you to inspect the underlying evidence for an association. Since the predominant source of evidence is automatic text mining, it is always wise to read the underlying text to manually validate the results. Click on **SNCA** in the **Text mining** table to view the text based on which it was associated with the disease. Click **View abstract** for a given entry to see the complete abstract rather than only the title.

_Do the abstracts all mention both the protein and the disease? Do they all use the same name for the protein?_

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
