---
title: Cytoscape Omics Visualizer exercises
layout: single
permalink: /training/omicsvisualizer/
sidebar:
  nav: "training-omicsvisualizer"
---
## Learning objectives

In these exercises, we will use the [Omics Visualizer](http://apps.cytoscape.org/apps/omicsvisualizer) app for [Cytoscape](http://cytoscape.org/) to retrieve molecular networks from the [STRING](https://string-db.org/) database and visualize site-specific information on the nodes. The exercises will teach you how to:

* load a table with site-specific data
* filter the data within the table
* retrieve a STRING network for a table
* visualize site-specific data onto networks

## Prerequisites

To follow the exercises, please make sure that you have the latest version of Cytoscape installed. Then start Cytoscape and go to **Apps → App Manager** to check for new apps, install them and update the current ones if necessarily. The exercises require you to have certain Cytoscape apps installed. Search for the **Omics Visualizer** in the search field; if it is not already installed, select it and press the **Install** button to install it. Similarly, make sure you have the **stringApp**, **enhancedGraphics**, and their dependencies installed before closing the App Manager.

## Exercise 1

In this exercise, we will load a data table with proteomics data, filter it, retrieve a STRING network for the proteins, and visualize site-specific information onto the protein network.

We will work with phosphoproteomics data from an ovarian cancer study ([Francavilla et al., 2017](https://doi.org/10.1016/j.celrep.2017.03.015)). The study used mass spectrometry to compare the phosphoproteome of primary cells derived from epithelial ovarian cancer (EOC) to those of two healthy tissues, namely distal fallopian tube epithelium (FTE) and ovarian surface epithelium (OSE). Each protein can have multiple significantly regulated phosphorylation sites, each of which is associated with two log-fold change values (one for each control tissue), a Benjamini–Hochberg adjusted p-value, and a cluster assignment that groups sites with similar behavior across samples. An adapted and simplified table with the data from this study is available [here](/assets/omicsvisualizer/Francavilla2017CellRep.tsv).

### 1.1 Table import

Start Cytoscape or close the current session from the menu **File → Close**. Go to the menu **Apps → Omics Visualizer → Import table from file**. Download and open the [text file](/assets/omicsvisualizer/Francavilla2017CellRep.tsv) with the data described above. The import dialog gives you the option to name the table, shows how the file is interpreted given the current settings, and allows you to change these as needed. As no changes should be needed for this file, simply click **OK** to complete the import.

### 1.2 Table row filtering

Omics Visualizer allows you to filter the rows in the table before visualizing them on a network. Click the filter button above the network or go to the menu **Apps → Omics Visualizer → Filter table rows**. In the filter dialog, you can build logical rules that take into account multiple columns in the table. However, here we will create a simple filter to keep only the phosphorylation sites that are statistically significant at a 1% false discovery rate.

Select **Adj p-value** as the column to use for filtering, choose **<=** as the operator, enter **0.01** as the value, and click **Apply**. The filter button above the table should turn green to show that you have an active filter, and the table will only show the rows that passed the filter.

[Filter table](cycmd:ov filter filter="(Adj p-value,EQUALS,0.01)"){: .btn .btn--cybrowser .btn--primary}

_How many rows do you have in the table? How many rows are shown after you applied the filter?_

### 1.3 STRING network retrieval

Before we can make a network visualization of the data, we obviously need to obtain a network from somewhere. While Omics Visualizer is designed to be able to work well with networks from any source, it integrates nicely with [stringApp](http://apps.cytoscape.org/apps/stringapp), which you can learn more about [here](/training/stringapp/).

Click the STRING button above the table or go to the menu **Apps → Omics Visualizer → Retrieve STRING network**. In the dialog, you can specify the species your data is from, the table column that holds the gene/protein identifiers that we want to query with, and the confidence score cutoff for the interactions retrieved from STRING. Here, we want to retrieve a **Homo sapiens** network based on the accession numbers in the **UniProt** column with a STRING confidence score cutoff of **0.7**. Select those values, click **Retrieve network**, and you should obtain a STRING network for the proteins in the filtered data table.

[Retrieve a STRING network](cycmd:ov retrieve queryColumn="UniProt" cutoff=0.7 taxonID=9606){: .btn .btn--cybrowser .btn--primary}

_How many nodes do you have in your network? Does it corresponds to the number of rows you queried?_

### 1.4 Donut visualization

We are now ready to start mapping the site-specific phosphoproteomics data onto the network. Specifically, we will visualize the two log-fold change values for each site as concentric rings around the nodes in the network.

Click the donut button above the table or go to the menu **Apps → Omics Visualizer → Create donut visualization**. In the first dialog you choose the data to visualize; select **EOC vs FTE** as the first value set, click the **+** to add a second, select **EOC vs OSE** as the second value set, and choose **Continuous** as mapping. To label the visualization with the modified position(s) in the protein, select **AA position** as labels. Click **Next >** to get to the second dialog, which allows you to select the color palette and fine-tune the color gradient; as the default values are fine, simply click **Draw** to produce the visualization.

_How are multiple sites on the same protein shown? Do different different within a protein always show similar changes?_

### 1.5 Pie visualization

With the donut visualization we showed the quantitative changes in phosphorylation of each site. The study by Francavilla and coworkers also used this information to assign each site to one of three clusters (A, B and C) based on its behavior across samples. We will add this qualitative information to the network as a pie visualization.

Click the pie button above the table or go to **Apps → Omics Visualizer → Create pie visualization.**. In the first dialog, select **Cluster** as values and do not select any labels. The mapping has automatically changed to **Discrete** and cannot be changed because the column does not contain numeric data. Click **Next >** to get to the second dialog and then **Draw** to create the visualization.

The nodes themselves have now been replaced with pie visualizations that color each site depending which cluster it belongs to. Looking at the colors, it is clear that cluster assignments very well summarize the quantitative data on regulation; one cluster A are the down-regulated sites, cluster C are the up-regulated sites, and cluster B mostly contains sites that show different behavior in the two control tissues. However, the colors assigned to the clusters do not show this in an intuitive way.

To change the colors open the pie visualization dialog again and click **Next >**. Customize the colors so that cluster A is blue, cluster B is yellow, and cluster C is red. Click **Draw** to update the visualization. You should now clearly see the consistency the log-fold change values shown as donuts and the cluster assignments shown as pies.

Since the two visualizations are now redundant, we can simplify the figure by deleting the detailed donut visualization. Open the donut dialog and click **Delete Visualization** to remove it.

_What are the advantages and disadvantages of donut vs. pie visualizations? Which would be best suited for a big network with several hundreds of proteins?_
