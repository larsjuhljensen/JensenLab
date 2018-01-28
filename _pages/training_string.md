---
title: STRING exercises
layout: single
permalink: /training/string/
sidebar:
  nav: "training-string"
---
## Learning objectives

In these exercises, we will use the [STRING](https://string-db.org/), [STITCH](https://stitch-db.org/), and [DISEASES](https://diseases.jensenlab.org/) databases through their respective web interfaces. The exercises will teach you how to:

* retrieve a STRING network for a protein of interest
* interpret the different visual representations
* inspect the evidence behind an interaction
* retrieve a STITCH network for a protein or chemical compound of interest
* use DISEASES to find proteins associated with a disease of interest

## Exercise 1

### 1.1 Single protein query

We will first retrieve a STRING network for human insulin receptor (INSR). Go to http://string-db.org/, open the **Protein by name** search interface, and type **INSR** in the field **Protein Name**. You can either specify **Homo sapiens** in the **Organism** field leave it on **auto-detect**. Click **SEARCH**. If you specified the organism, you will immediately receive a protein network; otherwise you will first be presented with a disambiguation page on which you can specify that you meant the human protein.

## 1.2 Visual representations

The STRING web interface provides several different visual representations of the network. The **Settings** tab below the network view allows you to change between different visual representations of the same network. Try changing between the **confidence** and **evidence** views; do not forget to press the **UPDATE** button.

_Which information is shown for the edges in each representation? Why are there sometimes multiple lines connecting the same two proteins in the evidence representation?_

## 1.3 Evidence viewers

A key feature of the STRING web interface is the evidence viewers. One should not rely purely on the confidence scores; it is important to inspect the actual evidence underlying an interaction before relying on it, for example, for designing experiments.

_Which types of evidence support the interaction between insulin receptor (INSR) and insulin receptor substrate 1 (IRS1)?_

Further detail on the evidence of an interaction can be seen in a popup by clicking on the corresponding edge in the network. Click on the edge between INSR and IRS1 to view its popup; you may need to move the nodes to make this easier.

_Which type of evidence gives the largest contribution to the confidence score?_

Click on the **Show** button to view the experimental evidence for the interaction.

_Which types of experiments support this interaction?_

Go back to the network and similarly inspect the text-mining evidence for the same interaction.

_Do the documents indeed co-mention INSR and IRS1?_

## Exercise 2

STITCH exercise to be added.

## Exercise 3

DISEASES exercise to be added.
