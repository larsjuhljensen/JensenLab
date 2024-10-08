---
title: Cytoscape stringApp diseases exercises
layout: single
permalink: /training/stringapp/diseases/
sidebar:
  nav: "training-stringapp-diseases"
---
## Learning objectives

In these exercises, we will use the [stringApp](http://apps.cytoscape.org/apps/stringApp) for [Cytoscape](http://cytoscape.org/) to retrieve molecular networks from the [STRING](https://string-db.org/) database for genes associated with diseases according to the [DISEASES](https://diseases.jensenlab.org/Search) database. The exercises will teach you how to:

* retrieve networks for a disease
* merge and compare networks
* select proteins by attributes
* layout and visually style the resulting networks
* perform enrichment analyses and visualize the results
* identify functional modules through network clustering

## Prerequisites

To follow the exercises, please make sure that you have the latest version of Cytoscape installed. Then start Cytoscape and update the current apps if necessary by checking the **App Updates** icon in the right-most corner of the menu bar. 

The exercises require you to have certain Cytoscape apps installed. Go to the [Cytoscape App Store](https://apps.cytoscape.org/) in your web browser and search for [stringApp](http://apps.cytoscape.org/apps/stringApp), select the app and press the **Install** button to install it. Similarly, make sure you have the [Omics Visualizer](https://apps.cytoscape.org/apps/OmicsVisualizer), [yFiles Layout Algorithms](https://apps.cytoscape.org/apps/yfileslayoutalgorithms) and [clusterMaker2](https://apps.cytoscape.org/apps/clustermaker2) apps installed before switching back to Cytoscape.

If you are not already familiar with the STRING database or stringApp, we highly recommend that you go through the [STRING exercises](/training/string/) to learn about the underlying data and the [stringApp exercises](/training/stringapp/) to get familiarized with Cytoscape and stringApp.

## Exercise 1

In this exercise, we will retrieve several different disease networks and compare them by creating the union of their nodes and edges as well as by visualizing which nodes belong to which diseases.

### 1.1 Disease queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: disease query** as **Data Source**, type _Pancreatic cancer_ into the **Enter disease term** field and set the **Confidence (score) cutoff** to **0.7**. When you press **Import**, stringApp will retrieve a STRING network for the top-100 proteins associated with the chosen disease. Repeat this for **two** of the following diseases: _Acute pancreatitis_, _Anxiety disorder_, _Sleep disorder_, _Intestinal disease_, or _Diabetes mellitus_.

_Which diseases did you choose and what is the lowest and highest stringdb::disease score for each of them? Are the scores in a similar range or not?_

Now, go to the _stringdb::disease score_ column, click on the column name and choose **Rename column**. For each network, rename the column to reflect the name of the disease, e.g. _Pancreatic cancer_ or _disease PC_. Note that you can remove _stringdb::_ from the name. 

### 1.2 Integrate disease networks

Cytoscape provides functionality to merge two or more networks, building either their union, intersection or difference. We will now merge the disease networks so that we can identify the overlap and differences between them. Use the Merge tool (**Tools → Merge → Networks...**) and make sure the **Union** tab is chosen. Then, select the disease networks from **Available Networks** list (for example ‘String Network - Pancreatic cancer’, ‘String Network - Acute pancreatitis’, and ‘String Network - Anxiety disorder’). Click on **>** to add them to the list of **Networks to Merge** and click **Merge**.

_How many nodes and edges are in the merged network? If you pick one protein from each disease and check if they are connected in the merged network, what do you observe?_

In the next step, we need to retrieve all the interactions between the nodes that were not in the same disease network since those are not yet included in the network. To do so, we first remove all edges by choosing **Apps → STRING → Change confidence or type** from the Cytoscape menu. In the dialog, we set the **Confidence cutoff** to **1.0** and press **OK**. Then, we open the same dialog again, change the **Confidence cutoff** back to **0.7** and press *OK*. In this way, we make sure that all interactions above the confidence cutoff between **all** proteins in the current network are retrieved. Note that if you get an error while setting the confidence to 0.7, you can avoid it by switching to another network in the **Network** panel, and then back to the **Merged Network** before changing the confidence. 

_How many edges do we have now in the merged network? Can you think of a reason for why the number of edges increased? Are the proteins you selected from different disease now connected?_

To better see the nodes and their names, make sure the graphics details are enabled (**View → Always Show Graphics Details**) and to improve the layout of the merged network, go to **Layout → Apply Preferred Layout** and then to **Layout → yFiles Remove Overlaps** (skip the last step if the menu item is not visible on your screen due to screen size or resolution).

We can change the visualization of the merged network to look like a STRING network by changing the style. Go to **Style** in the **Control Panel** (beneath **Network**) and click on the drop-down menu to change the style from **default** to **STRING - Pancreatic cancer**. Disable the **STRING style colors** and **STRING style labels** from the **STRING Results panel** (right side) to remove the colors of the proteins associated with Pancreatic cancer, make all nodes grey and center the node labels. 

### 1.3 Use selection filters

Now, we can explore the disease scores and check how many proteins are associated with more than one disease by using Cytoscape's built-in selection filters (**Filter** tab located underneath the **Style** tab). Click the **ᐩ** button, choose **Column filter** from the drop-down menu, and select one of the disease score columns you renamed in Exercise 1.1. The filtering criteria will automatically bet set to **is** and then a range for the score. Add a filter for the other two diseases in the network by clicking on the **ᐩ** button and selecting the respective disease score column. All three filters are connected with an _AND_ logic, which means that a node is selected only if it fulfills all three conditions. 

_How many nodes (proteins) are common to all three diseases? And how many are common to some of the pairs of diseases? Note that you can see the nodes common to a pair by either deleting one of the three filters or by setting the third filter to **is not**._

Depending on which option you choose, you will get slightly different numbers because in the first case (having only two filters) the set of proteins associated with the two disease might contain proteins associated with the third disease, while in the second case, you specifically set the third filter to choose proteins that are associated with the first two diseases but **not** with the third one. 

### 1.4 Visualize disease associations

In the next step, we will import the disease scores into a different table using the _Omics Visualizer_ app. Go to **Apps → Omics Visualizer → Import form node table**. In the resulting dialog, we will see all node attribute columns, including the ones created in Exercise 1.1. Note that if you kept _stringdb::_ in the column names, you will find the columns under the _strigndb_ namespace. Move the three columns containing the disease scores from **Available columns** to **Selected columns** using the **>** button and then click **Next** and **Import**. 

A new table should appear in the Cytoscape _Node Panel_ in the **Omics Visualizer Tables** tab. This table contains three columns (_shared name_, _value_, and _source_ or _stringdb_) and for each node, one row for each column we selected in the previous step, in this case three. Since not all nodes are associated with all three diseases, in some cases the _value_ column is empty. We can filter the table to show only the rows that contain any disease score, since this would be useful for the visualization we want to make. Press the **filter icon** (second icon just above the table), choose the **_value_** column and the **_is not null_** criteria. Now you can press **Apply** and then the **Close** button. 

_How many rows remain after filtering? Out of how many? Do you have an idea why the number of filtered rows is such a round number?_

To visualize which nodes are associated with which disease, you can use the **donut chart icon** (6th icon in the row above the table). In the resulting dialog, choose **_source_** (or **stringdb**) in the **Values** column, keep the **Mapping** to _Discrete_ and **Labels** to _NONE_. Pressing the **Next** button will show the next page of settings. We can pick other colors or keep the defaults and press **Draw**. As a result, the nodes are colored based on their association with one, two or all three diseases we combined in this network. Press the **Legend** icon (last icon) and confirm with the **Create** button to let Omics Visualizer create a legend of the visualization. 

_Do you observe an overlap between the three diseases? If yes, list a few of the overlapping proteins and briefly explain their biological role or function (see their description in the **STRING Results Panel** on the right). Would you have expected these proteins to overlap between the diseases you chose?_

## Exercise 2

In this exercise, we will analyze the integrated disease network by performing network clustering and functional enrichment. 

### 2.1 Network clustering

Starting from the merged network, we will use the MCL algorithm to identify clusters of tightly connected proteins within the network. To do that, press the **Cluster network (MCL)** button in the **STRING Results panel** on the right side of the network view. Set the **granularity parameter (inflation value)** to **5** and click **OK** to start the clustering. The _clusterMaker_ app will now run the algorithm and automatically create a network showing the clusters. To remove the node overlaps, go to **Layout → yFiles Remove Overlaps**.

_How many big clusters are there (with more than 10 nodes)? Are any of the clusters related mostly to one or two diseases or do they contain proteins associated with all three diseases?_

<details>
<summary><em>Alternative instructions for clustering</em></summary>

<p>Go to the menu <b>Apps → clusterMaker → ClusterMaker Cluster Network → MCL Cluster</b>>. Set the <b>Granularity parameter (inflation value)</b> to 5 and choose the <b>stringdb::score</b> attribute (i.e. the overall STRING confidence score) as <b>Array Sources</b>, select the option <b>Create new clustered network</b>, and click OK to start the clustering. The app will now run the algorithm and automatically create a network showing the clusters.</p>
</details>

### 2.2 Group-wise functional enrichment

Now we will perform functional enrichment analysis on each of the bigger clusters separately. Sometimes stringApp does not detect the clustered network as STRING network, so switch to the unclustered network and back to the clustered one. Now, select the menu **Apps → STRING Enrichment → Retrieve group-wise functional enrichment**. In the resulting dialog, press **Advanced** to show the advanced options and set the **minimum group size** to **10**, in order to retrieve enrichment results only for clusters with at least 10 nodes. Press **OK** and the **STRING enrichment** table will be populated with several tables, one for each cluster (look at the bottom right, next to the *Node* and *Edge Table*). You can explore the results of each of them separately. Note that if you only see enriched DISEASES, you need to reset the filter by pressing the filter icon, choosing **Select all** for including all categories, and pressing **OK**.

_Can you briefly characterize the three largest clusters in terms of their functionality? What distinguishes them?_

### 2.3 Group-wise annotations

Finally, you can automatically annotate all clusters by going to **Apps → STRING Enrichment → Retrieve group-wise annotations**. In the resulting dialog, you can again set the **minimum group size** to **10** under **Advanced** setting if you want to only get annotations for the bigger clusters. Press **OK** and you will see several new annotations being places close to the clusters. 

_Do the automatic annotations agree with what you wrote up for the three biggest clusters in the previous question?_

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
