---
title: Cytoscape stringApp exercises
layout: single
permalink: /training/stringapp/ddpm/
sidebar:
  nav: "training-stringapp-ddpm"
---
## Learning objectives

In these exercises, we will use the [stringApp](http://apps.cytoscape.org/apps/stringApp) for [Cytoscape](http://cytoscape.org/) to retrieve molecular networks from the [STRING](https://string-db.org/) database. The exercises will teach you how to:

* retrieve networks for proteins of interest
* retrieve networks for a disease
* layout and visually style the resulting networks
* select proteins by attributes

## Prerequisites

To follow the exercises, please make sure that you have the latest version of Cytoscape installed. Then start Cytoscape and go to **Apps → App Manager** to check for new apps, install them and update the current ones if necessary. The exercises require you to have certain Cytoscape apps installed. Search for the **stringApp** in the search field; if it is not already installed, select it and press the **Install** button to install it. Similarly, make sure you have the **yFiles Layout Algorithms** app installed before closing the App Manager.

If you are not already familiar with the STRING and DISEASES databases, we highly recommend that you go through the short [STRING exercises](/training/string/) to learn about the underlying data before working with them in these exercises.

## Exercise 1

In this exercise, we will perform some simple queries to retrieve molecular networks based on a protein and a topic in PubMed.

### 1.1 Protein queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: protein query** as **Data Source** and type your favorite protein into the **Enter protein names or identifiers** field (e.g. SORCS2). You can select the appropriate organism by typing the name (e.g. Homo sapiens). The **Maximum number of interactors** determines how many interaction partners of your protein(s) of interest will be added to the network. By default, if you enter only one protein name, the resulting network will contain 10 additional interactors. If you enter more than one protein name, the network will contain only the interactions among these proteins, unless you explicitly ask for additional proteins.

Unless the name(s) you entered give unambiguous matches, a disambiguation dialog will be shown next. It lists all the matches that the stringApp finds for each ambiguous query term and selects the first one for each. Select the right one(s) you meant and continue by pressing the **Import** button.

[Import SORCS2 network](cycmd:string protein query query=SORCS2 taxonID=9606){: .btn .btn--cybrowser .btn--primary}

_How many nodes are in the resulting network? How does this compare to the maximum number of interactors you specified? What types of information do the **Node Table** and **Edge Table** provide?_

### 1.2 PubMed queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: PubMed query** as **Data Source** and type query representing a topic of interest into the **PubMed Query** field (e.g. jet-lag). You can use any query that would work on the PubMed website, but it should obviously a topic with related genes or proteins. The stringApp will query PubMed for the abstracts, find the top-N proteins (by default 100) associated with these abstracts, and retrieve a STRING network for them.

[Import jet-lag network](cycmd:string pubmed query pubmed=jet-lag taxonID=9606 limit=50){: .btn .btn--cybrowser .btn--primary}

_Which attribute column do you get in the **Node Table** for a PubMed query compared to a protein query? Hint: check the last columns._

## Exercise 2

In this exercise, we are going to use the stringApp to query the [DISEASES](https://diseases.jensenlab.org) database for proteins associated with diabetes, retrieve a STRING network for them, and explore the resulting network.

### 2.1 Disease network retrieval

Close the current session in Cytoscape from the menu **File → Close**. Use the menu **File → Import → Network from Public Databases** and the **STRING: disease query** option from the **Data Source** drop-down menu. Insert **Diabetes mellitus** into the **Enter disease term** field and press the **Import** button. The stringApp will retrieve a STRING network for the top-N proteins (by default 100) associated with the disease. Once the network appears, go to the menu **View → Always Show Graphics Details** to see the individual nodes and edges.

Note that the retrieved network contains a lot of additional information associated with the nodes and edges, such as the protein sequence, tissue expression data, subcellular localization, disease score (**Node Table**) as well as the confidence scores for the different interaction evidences (**Edge Table**). In the following, we will explore these data using Cytoscape.

Find the **disease score** column in the node attributes table (look at the last columns). Sort it by values to see the highest and lowest confidence scores. You can highlight the corresponding nodes by selecting the rows in the table, bringing up the context menu (right-click the selected rows) and choosing the **Select nodes from selected rows** option. You can also use the **Fit Selected** icon in the menu bar to zoom into the selected node (**View → Fit Selected**).

_Give an example for a node with the highest and lowest disease score._

Cytoscape provides several visualization options under the **Layout** menu. Try the **Degree Sorted Circle Layout**, the **Prefuse Force Directed Layout** and the **Edge-weighted Spring Embedded Layout** with the attribute **score**, which is the combined STRING interaction scorewith **score**. If you have installed the **yFiles Layout Algorithms** app, you can also try the **yFiles Organic Layout**.

_Does any of the suggested layouts make patterns in the network easy to recognize?_

### 2.2 Discrete color mapping

Cytoscape allows you to map attributes of the nodes and edges to visual properties such as node color and edge width. Here, we will map drug target family data from the [Pharos](https://pharos.nih.gov/idg/targets) database to the node color. This data is contained in the node attribute called **target family**.

Select **Style** from the side menu in the left panel (it is between **Network** and **Filter**). Click the **◀** button to the right of the property you want to change, in this case **Fill Color**, and change **Column** from name to **(T) family**, which is the node column containing the data that you want to use. The **Mapping Type** should remain set to **Discrete Mapping**. This action will remove the rainbow coloring of the nodes and present you with a list of all the different values of the attribute that exist in the network, in this case several protein target families.

To color the proteins in a given target family, first click the field to the **right** of an attribute value, i.e. **GPCR** or **IC**, then click the ⋯ button and choose a color from the color selection dialog. You can also set the default color for all nodes that do not have a target family annotation from Pharos by clicking on the **grey square** in the first column of the **Fill Color** row.

_How many of the proteins in the network are ion channels (IC) or GPCRs?_

There are many kinases in the network. We can avoid counting them manually by creating a selection filter in the **Filter** tab (located underneath **Style**). Click the **ᐩ** button and choose **Column filter** from the drop-down menu. Then, find and select the attribute **(T) Node: family**. Write **kinase** in the text field to select all nodes with this annotation. Note that the current selection criterium is set to **contains**, but you can change it other values, such as **is** or **doesn't contain**.

_How many kinases are in the network?_


### 2.3 Inspect subcellular localization data

The stringApp automatically retrieves information about in which compartments the proteins are located from the [COMPARTMENTS](https://compartments.jensenlab.org/) database, which we will take a look at first to better understand the data.

Go to [COMPARTMENTS](https://compartments.jensenlab.org/) and enter **HNF1A** into the search box. The resulting page will show all matches for the query HNF1A. After selecting the human gene, you will see a schematic of where in the cell it is located and below it tables containing the specific lines of evidence that contribute to the overall score.

_What compartments is HNF1A present in with a confidence of 5 (stars)? What source do these associations come from? Hint: you can see what the abbreviations for different evidence types mean [here](http://geneontology.org/docs/guide-go-evidence-codes/)._

In Cytoscape, we can identify all the proteins in our network that are located in the nucleus with highest confidence of 5 by using the COMPARTMENTS sliders in the **STRING** results panel on the right side. In the **Nodes** tab expand the group of compartment filters by clicking the small triangle and find the slider for **nucleus**. To hide all nodes with a confidence score below 5, set the low bound to 5.0 by typing the number in the text field and pressing **Enter**.

Select all remaining nodes in the network view by holding down the modifier key (Shift on Windows, Ctrl or Command on Mac) and then left-clicking and dragging to select multiple nodes. The nodes will turn yellow if they are selected properly. The number of selected nodes is shown in the light grey panel bar on the bottom-right part of the network view panel, just above the **Table panel**.

_How many proteins are found in the nucleus with a confidence score of 5? In mitochondrion? In both nucleus and mitochondrion?_

Important: Move the filter back to 0.0 to see all nodes again before continuing with the next exercise.

### 2.4 Continuous color mapping

Finally, we will map the subcellular localization data for nucleus to the node color. From the left panel side menu, select **Style** (located underneath **Network** and above **Filter**). Click on the **◀** button to the right of the property you want to change, in this case **Fill Color** and set **Column** to the node column containing the data that you want to use (**nucleus**). Since this is a numeric value, we will use the **Continuous Mapping** as the **Mapping Type**, and set a color gradient for how likely each protein is located in the nucleus. The default Cytoscape yellow--purple color gradient already gives a nice visualization of the confidence of being located in this compartment.

_Does it look like the network contains many nuclear proteins?_

<!-- ### 2.5 Functional enrichment

After making sure that no nodes are selected in the current network, go to the menu **Apps → STRING Enrichment → Retrieve functional enrichment** or use the **Functional Enrichment** button in the **Nodes tab** of the **STRING Panel** on the right side. Use the default settings and click **OK**. A new **STRING Enrichment tab** will appear in the **Table Panel** on the bottom. It contains a table of enriched terms and corresponding information for each enrichment category. You can see which proteins are annotated with a given term by selecting the term in the **STRING Enrichment panel** and you can see the terms annotating a given node by slecting it.

[Set as STRING network](cycmd:string make string){: .btn .btn--cybrowser .btn--primary}
[Retrieve functional enrichment](cycmd:string retrieve enrichment){: .btn .btn--cybrowser .btn--primary}
[Show functional enrichment](cycmd:string show enrichment){: .btn .btn--cybrowser .btn--primary}

_How many statistically significant terms are in the table? Which is the most significant term for each of the categories GO Biological Process and KEGG Pathways? Hint: Look at the FDR (false discovery rate) value column and use the **Filter** button to select individual categories._

To save the list of enriched terms and associated p-values as a text file, go to **Apps → STRING Enrichment → Export enrichment results**. -->

## Supporting lectures

The theoretical background for these exercises is covered in these short online lectures:

[![STRING](training_string.png)](https://youtu.be/o208DwyFbNk)
[![Cytoscape](training_cytoscape.png)](https://youtu.be/Ohf9IPUJ82w)
[![stringApp](training_stringapp.png)](https://youtu.be/MXmzXxNqmnI)
[![stringApp tutorial](training_stringapp_tutorial.png)](https://youtu.be/kRQyPDMF_8k)
[![DISEASES](training_diseases.png)](https://youtu.be/xkYixhO2CJQ)
[![Enrichment analysis](training_enrichment_analysis.png)](https://youtu.be/2NC1QOXmc5o)
[![stringApp enrichment analysis](training_stringapp_enrichment_analysis.png)](https://youtu.be/AUEyZw-iJHg)

## Supporting literature

Doncheva NT, Morris JH, Gorodkin J and Jensen LJ (2019). Cytoscape stringApp: Network analysis and visualization of proteomics data. *Journal of Proteome Research*, **18**:623-632.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/30450911) [Full text](https://doi.org/10.1021/acs.jproteome.8b00702) [Preprint](https://doi.org/10.1101/358283)

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
