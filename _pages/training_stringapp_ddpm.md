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

To follow the exercises, please make sure that you have the latest version of Cytoscape installed. Then start Cytoscape and update the current apps if necessary by checking the **App Updates** icon in the right-most corner of the manubar. 

The exercises require you to have certain Cytoscape apps installed. Go to the [Cytoscape App Store](https://apps.cytoscape.org/) in your web browser and search for [stringApp](http://apps.cytoscape.org/apps/stringApp), select the app and press the **Install** button to install it.

Troubleshooting: If your browser does not allow you to install the app directly from the App Store, you will see a **Download** button that you can press to download the app file. After that, switch to Cytoscape and go to **Apps → App Store → Install apps from file**. Find the downloaded app in your files, select it and press the Open button to let Cytoscape install it.

## Exercise 1

In this exercise, we will perform a simple query to retrieve molecular networks based on a protein of interest.

### Protein queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: protein query** as **Data Source** and type your favorite protein into the **Enter protein names or identifiers** field (e.g. SORCS2 or INSR). You can select the appropriate organism by typing the name (e.g. Homo sapiens). The **Maximum number of interactors** determines how many interaction partners of your protein(s) of interest will be added to the network. By default, if you enter only one protein name, the resulting network will contain 10 additional interactors. If you enter more than one protein name, the network will contain only the interactions among these proteins, unless you explicitly ask for additional proteins.

_How many nodes are in the resulting network? How does this compare to the maximum number of interactors you specified? What types of information do the **Node Table** and **Edge Table** provide?_

## Exercise 2

In this exercise, we are going to use the stringApp to query the [DISEASES](https://diseases.jensenlab.org) database for proteins associated with type 1 diabetes, retrieve a STRING network for them, and explore the resulting network.

### 2.1 Disease query

Go to <https://diseases.jensenlab.org/>, type **type 1 diabetes** in the search field, and click the **search** button. The web interface will now show the search results, which include all diseases and protein names starting with the search term. Click **Type 1 diabetes mellitus** to get to the results page showing proteins associated with the disease.

Like STRING, the DISEASES database integrates several types of evidence, in this case automatic text mining, manually curated knowledge, and experimental evidence from genome-wide association studies.

_Is the protein INS supported by all three types of evidence? If yes, how confident is each source (in number of stars)?_

### 2.2 Disease network retrieval

Now go to Cytoscape and close the current session from the menu **File → Close**. Use the menu **File → Import → Network from Public Databases** and the **STRING: disease query** option from the **Data Source** drop-down menu. Insert **type 1 diabetes mellitus** into the **Enter disease term** field and press the **Import** button. The next dialog shows all possible matches and the correct one should be chosen by default, so just press **Import** again. The stringApp will retrieve a STRING network for the top-N proteins (by default 100) associated with the disease. Once the network appears, go to the menu **View → Always Show Graphics Details** to see the individual nodes and edges.

Note that the retrieved network contains a lot of additional information associated with the nodes and edges, such as the protein sequence, tissue expression data, subcellular localization, disease score (**Node Table**) as well as the confidence scores for the different interaction evidences (**Edge Table**). In the following, we will explore these data using Cytoscape.

Find the **disease score** column in the node attributes table (look at the last columns). Sort it by values to see the highest and lowest confidence scores. You can highlight the corresponding nodes by selecting the rows in the table, bringing up the context menu (right-click the selected rows) and choosing the **Select nodes from selected rows** option. You can also use the **Fit Selected** icon in the menu bar to zoom into the selected node (**View → Fit Selected**).

_How many nodes and edges are there in the resulting network? How many nodes have the highest disease score? Give at least one example._

### 2.3 Discrete color mapping and filters

Cytoscape allows you to map attributes of the nodes and edges to visual properties such as node color and edge width. Here, we will map drug target family data from the [Pharos](https://pharos.nih.gov/idg/targets) database to the node color. This data is contained in the node attribute called **target family**.

Select **Style** from the side menu in the left panel (it is between **Network** and **Filter**). Click the **◀** button to the right of the property you want to change, in this case **Fill Color**, and change **Column** from name to **(T) family**, which is the node column containing the data that you want to use. The **Mapping Type** should remain set to **Discrete Mapping**. This action will remove the rainbow coloring of the nodes and present you with a list of all the different values of the attribute that exist in the network, in this case several protein target families.

To color the proteins in a given target family, first click the field to the **right** of an attribute value, i.e. **GPCR** or **Ion channel**, then click the ⋯ button and choose a color from the color selection dialog. You can also set the default color for all nodes that do not have a target family annotation from Pharos by clicking on the **grey square** in the first column of the **Fill Color** row.

_How many of the proteins in the network are ion channels or GPCRs?_

There are many transcription factors in the network. We can avoid counting them manually by creating a selection filter in the **Filter** tab (located underneath **Style**). Click the **ᐩ** button and choose **Column filter** from the drop-down menu. Then, find and select the attribute **(T) Node: family**. Write **Transcription factor** in the text field to select all nodes with this annotation. Note that the current selection criterion is set to **contains**, but you can change it to other values, such as **is** or **doesn't contain**.

_How many transcription factors are in the network?_

### 2.4 Inspect tissue expression data [optional]

The stringApp automatically retrieves information about tissues, in which the proteins are expressed, from the [TISSUES](https://tissues.jensenlab.org/) database. We will take a look at it first to better understand the data.

Go to [TISSUES](https://tissues.jensenlab.org/) and enter **INS** into the search box. The resulting page will show all matches for the query INS. After selecting the human gene, you will see a schematic of where in the body it is expressed and tables containing the specific lines of evidence that contribute to the overall score.

_What tissues is INS present in with a high confidence? What source do these associations come from?_

In Cytoscape, we can identify all the proteins in our network that are expressed in the pancreas with highest confidence of 5 by using the tissue sliders in the **STRING** results panel on the right side. In the **Nodes** tab expand the group of **Tissue filters** by clicking the small triangle and find the slider for **pancreas**. To hide all nodes with a confidence score below 5, set the low bound to 5.0 by typing the number in the text field and pressing **Enter**.

_How many proteins are expressed in pancreas with a confidence score of 5?_

Important: Move the filter back to 0.0 to see all nodes again before continuing with the next exercise.

### 2.5 Continuous color mapping [optional]

Finally, we will map the tissue expression data for pancreas to the node color. From the left panel side menu, select **Style** (located underneath **Network** and above **Filter**). Click on the **◀** button to the right of the property you want to change, in this case **Fill Color** and set **Column** to the node column containing the data that you want to use (**(T) pancreas**). Since this is a numeric value, we will use the **Continuous Mapping** as the **Mapping Type**, and set a color gradient for how likely each protein is expressed in pancreas. The default Cytoscape yellow--purple color gradient already gives a nice visualization of the confidence of being expressed in this tissue.

_Does it look like the network contains many proteins expressed in pancreas?_

## Supporting lectures

The theoretical background for these exercises is covered in these short online lectures:

[![STRING](training_string.png)](https://youtu.be/o208DwyFbNk)
[![Cytoscape](training_cytoscape.png)](https://youtu.be/Ohf9IPUJ82w)
[![stringApp](training_stringapp.png)](https://youtu.be/MXmzXxNqmnI)
[![stringApp tutorial](training_stringapp_tutorial.png)](https://youtu.be/kRQyPDMF_8k)
[![DISEASES](training_diseases.png)](https://youtu.be/xkYixhO2CJQ)

## Supporting literature

Doncheva NT, Morris JH, Gorodkin J and Jensen LJ (2019). Cytoscape stringApp: Network analysis and visualization of proteomics data. *Journal of Proteome Research*, **18**:623-632.  
[Abstract](https://www.ncbi.nlm.nih.gov/pubmed/30450911) [Full text](https://doi.org/10.1021/acs.jproteome.8b00702) [Preprint](https://doi.org/10.1101/358283)

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
