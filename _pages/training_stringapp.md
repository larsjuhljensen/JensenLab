---
title: Cytoscape stringApp exercises
layout: single
permalink: /training/stringapp/
sidebar:
  nav: "training-stringapp"
---
## Learning objectives

In these exercises, we will use the [stringApp](http://apps.cytoscape.org/apps/stringApp) for [Cytoscape](http://cytoscape.org/) to retrieve molecular networks from the [STRING](https://string-db.org/) and [STITCH](http://stitch-db.org/) databases. The exercises will teach you how to:

* retrieve networks for proteins or small-molecule compounds of interest
* retrieve networks for a disease or an arbitrary topics in PubMed
* layout and visually style the resulting networks
* import external data and map them onto a network
* perform enrichment analyses and visualize the results
* merge and compare networks
* select proteins by attributes
* identify functional modules through network clustering

## Prerequisites

To follow the exercises, please make sure that you have the latest version of Cytoscape installed. Then start Cytoscape and go to **Apps → App Manager** to check for new apps, install them and update the current ones if necessarily. The exercises require you to have certain Cytoscape apps installed. Search for the **stringApp** in the search field; if it is not already installed, select it and press the **Install** button to install it. Similarly, make sure you have the **yFiles Layout Algorithms**, **enhancedGraphics**, and **clusterMaker2** apps installed before closing the App Manager.

If you are not already familiar with the STRING database, we highly recommend that you go through the short [STRING exercises](/training/string/) to learn about the underlying data before working with them in these exercises.

## Exercise 1

In this exercise, we will perform some simple queries to retrieve molecular networks based on a protein, a small-molecule compound, a disease, and a topic in PubMed.

### 1.1 Protein queries

Go to the menu **File → Import → Network → Public Databases**. In the import dialog, choose **STRING: protein query** as **Data Source** and type your favorite protein into the **Enter protein names or identifiers** field. You can select the appropriate organism by typing the name. The **Maximum number of interactors** determines how many interaction partners of your protein(s) of interest will be added to the network. By default, if you enter only one protein name, the resulting network will contain 10 additional interactors. If you enter more than one protein name, the network will contain only the interactions among these proteins, unless you explicitly ask for additional proteins.

Unless the name(s) you entered give unambiguous matches, a disambiguation dialog will be shown next. It lists all the matches that the stringApp finds for each query term and selects the first one for each. Select the right one(s) you meant and continue by pressing the **Import** button.

_How many nodes are in the resulting network? How does this compare to the maximum number of interactors you specified? What types of information does the **Node Table** provide?_

### 1.2 Compound queries

Go to the menu **File → Import → Network → Public Databases**. In the import dialog, choose **STITCH: protein/compound query** as **Data Source** and type your favorite compound into the **Enter protein or compound names or identifiers** field. You can select the organism and number of additional interactors just like for the protein query above, and the disambiguation dialog also works the same way.

_How is this network different from the protein-only network with respect to node types and the information provided in the **Node Table**?_

### 1.3 Disease queries

Go to the menu **File → Import → Network → Public Databases**. In the import dialog, choose **STRING: disease query** as **Data Source** and type a disease of interest into the **Enter disease term** field (e.g. Alzheimer's disease). The stringApp will retrieve a STRING network for the top-N proteins (by default 100) associated with the disease.

The next dialog shows all the matches that the stringApp finds for your disease query and selects the first one. Make sure to select the intended disease before pressing the **Import** button to continue.

[Import Alzheimer's disease network](cycmd:string disease query disease=DOID:10652 taxonID=9606){: .btn .btn--primary cybrowser}

_Which additional attribute column do you get in the **Node Table** for a disease query compared to a protein query? (Hint: check the last column.)_

### 1.4 PubMed queries

Go to the menu **File → Import → Network → Public Databases**. In the import dialog, choose **STRING: PubMed query** as **Data Source** and type query representing a topic of interest into the **PubMed Query** field (e.g. jet-lag). You can use any query that would work on the PubMed website, but it should obviously a topic with related genes or proteins. The stringApp will query PubMed for the abstracts, find the top-N proteins (by default 100) associated with these abstracts, and retrieve a STRING network for them.

_Which attribute column do you get in the **Node Table** for a PubMed query compared to a disease query? (Hint: check the last columns.)_

### 1.5 New search interface

The types of queries described above can alternatively be performed through the new Cytoscape search interface. Click on the drop-down menu with an icon on it, located on the left side below the **Network** tab in the **Control Panel**. Select one of the four possible STRING queries and directly enter your query in the text field. To change settings such as organism, click the ☰ button next to the text field. Finally, click the 🔍 button to retrieve a STRING network for your query.

## Exercise 2

In this exercise, we will work with a list of 78 proteins that interact with TrkA (tropomyosin-related kinase A) in neuroblastoma cells 10 min after stimulation with NGF (nerve growth factor) ([Emdal et al., 2015](http://stke.sciencemag.org/content/8/374/ra40)). An adapted table with the data from this study is available [here](https://goo.gl/8HkRb4).

### 2.1 Protein network retrieval

Start Cytoscape or open a new session from the menu **File → New → Session**. Go to the menu **File → Import → Network → Public Databases**. In the import dialog, choose **STRING: protein query** as the **Data Source** and paste the list of UniProt accession numbers from the first column in the table into the **Enter protein names or identifiers** field.

Next, the disambiguation dialog shows all STRING proteins that match the query terms, with the first protein for each query term automatically selected. This default is fine for this exercise; click the **Import** button to continue.

_How many nodes and edges are there in the resulting network? Do the proteins all form a connected network? Why?_

Cytoscape provides several visualization options under the **Layout** menu. Experiment with these and find one that allows you to see the shape of the network easily. For example, you can try the **Degree Sorted Circle Layout**, the **Prefuse Force Directed Layout** with **score** as edge weight, and **yFiles Organic Layout**.

_Can you find a layout that allows you to easily recognize patterns in the network? What about the Edge-weighted Spring Embedded Layout with the attribute ‘score’, which is the combined STRING interaction score._

### 2.2 Discrete color mapping

Cytoscape allows you to map attributes of the nodes and edges to visual properties such as node color and edge width. Here, we will map drug target family data from the [Pharos](https://pharos.nih.gov/idg/targets) database to the node color.

Select **Style** from the top menu in the left panel (it is between **Network** and **Select**). Click the **◀** button to the right of the property you want to change, in this case **Fill Color**, and set **Column** to the node column containing the data that you want to use (i.e. **target family**). This action will remove the rainbow coloring of the nodes and present you with a list of all the different values of the attribute that are exist in the network.

_Which target families are present in the network?_

To color the corresponding proteins, first click the field to the right of an attribute value, i.e. **GPCR** or **Kinase**, then click the **⋯** button and choose a color from color selection dialog. You can also set a default color, e.g. for all nodes that do not have a target family annotation from Pharos, by clicking on the white button in the first column of the same row.

_How many of the proteins in the network are kinases?_

Note that the retrieved network contains a lot of additional information associated with the nodes and edges, such as the protein sequence, tissue expression data (Node Table) as well as the confidence scores for the different interaction evidences (Edge Table). In the following, we will explore these data using Cytoscape.

### 2.3 Data import

Network nodes and edges can have additional information associated with them that we can load into Cytoscape and use for visualization. We will import the data from the text file (https://goo.gl/zjDa81).

To import the node attributes file into Cytoscape, go to **File → Import → Table → File**. The preview in the import dialog will show how the file is interpreted given the current settings and will update automatically when you change them. To change the default selection chosen by Cytoscape, click on the arrow in the column heading. For example, you can decide whether the column is imported or not by changing the **Meaning** of the column (hover over each symbol with the mouse to see what they mean). This column-specific dialog will also allow you to change the column name and type.

Now you need to map unique identifiers between the entries in the data and the nodes in the network. The key point of this is to identify which nodes in the network are equivalent to which entries in the table. This enables mapping of data values into visual properties like Fill Color and Shape. This kind of mapping is typically done by comparing the unique Identifier attribute value for each node (Key Column for Network) with the unique Identifier value for each data value (key symbol). As a default, Cytoscape looks for an attribute value of ‘ID’ in the network and a user-supplied Key in the dataset.

The **Key Column** for Network can be changed using a combo box and allows you to set the node attribute column that is to be used as key to map to. In this case it is **query term** because this attribute contains the UniProt accession numbers you entered when retrieving the network. You can also change the Key by pressing the key button for the column that is to be used as key for mapping values in the dataset.

If there is a match between the value of a Key in the dataset and the value the Key Column for Network field in the network, all attribute--value pairs associated with the element in the dataset are assigned to the matching node in the network. You will find the imported columns at the end of the Node Table.

### 2.4 Continuous color mapping

Now, we want to color the nodes according to the protein abundance (log ratio) compared to the cells before NGF treatment. From the left panel top menu, select **Style** (it is to the right of **Network**). Then click on the **◀** button to the right of the property you want to change, for example **Fill Color**. Next, set **Column** to the node column containing the data that you want to use (10 min log ratio). Since this is a numeric value, we will use the **Continuous Mapping** as the **Mapping Type**, and set a color gradient for how abundant each protein is. The default Cytoscape color gradient blue-white-red already gives a nice visualization of the negative-to-positive abundance ratio.

_Are the up-regulated nodes grouped together?_

To change the colors, double click on the color gradient in order to bring up the **Continuous Mapping Editor** window and edit the colors for the continuous mapping. In the mapping editor dialog, the color that will be used for the minimum value is on the left, and the max is on the right. Double click on the triangles on the top and sides of the gradient to change the colors. The triangles on the top represent the values at which the data will be clipped; anything above the right triangle will be set to the max value. This is useful if you have a small number of values that are significantly higher than the median. To have three colors, you need to add a new triangle (for the white color) by pressing the Add button and set the Handle position value to 0. As you move the triangles and change the color, the display in the network pane will automatically update — so this is all easier to do than to explain! If at any point it doesn't seem to work as expected, it is easiest to just delete the mapping and start again.

_Can you improve the color mapping such that it is easier to see which nodes have a log ratio below -2 and above 2?_

### 2.5 Functional enrichment

Next, we will retrieve functional enrichment for the proteins in our network. After making sure that no nodes are selected in the network, go to the menu **Apps → STRING Enrichment → Retrieve functional enrichment** and keep the default p-value of 0.05. A new STRING Enrichment tab will appear in the Table Panel on the bottom. It contains a table of enriched terms and corresponding information for each enrichment category.

_Which are the three most statistically significant terms?_

To explore only specific types of terms, e.g. GO terms, and to remove redundant terms from the table, click on the filter icon in the **Table panel** (leftmost icon). Select the three types of GO terms, enable the option to **Remove redundant terms** and set **Redundancy cutoff** to 0.2. In this way, you will see only the statistically significant GO terms that do not represent largely the same set of proteins within the network. You can see which proteins are annotated with a given term by selecting the term in the **STRING Enrichment** panel.

_Do the functional terms assigned to a protein correlate with whether it is up- or down-regulated?_

Next, we will visualize the top-3 enriched terms in the network by using split charts. Click the settings icon (rightmost icon) and set the **Number of terms** to chart to 3; you can optionally also **Change Color Palette** before clicking **OK** to confirm the new settings. Click the colorful chart icon to show the terms as the charts on the network.

_Do these terms give good coverage of the proteins in network?_

Finally, save the list of enriched terms and associated p-values as a text file by going to **File → Export → Export STRING Enrichment**.

## Exercise 3

We are going to use the stringApp to query the [DISEASES](https://diseases.jensenlab.org) database for proteins associated with Parkinson’s disease and with Alzheimer's disease, retrieve STRING networks for both, created a combined network for the two neurodegenerative diseases, identify clusters in the network, and color it to compare the diseases.

### 3.1 Disease network retrieval

Open a new session in Cytoscape from the menu **File → New → Session**. Use the menu **File → Import → Network → Public Databases** and the **STRING: disease query** option. Retrieve a network for **Parkinson's disease** and another for **Alzheimer's disease**.

### 3.2. Working with node attributes

Browse through the node attributes table and find the disease score column. Sort it descending by values to see the highest disease scores. You can highlight the corresponding nodes by selecting the rows in the table, bringing up the context menu (right-click the selected rows) and choosing the ‘Select nodes from selected rows’ option. You can also use one of the icons in the menu to zoom into the selected node.

Look for an example for a node with a disease score of 5 and one with a disease score below 4.

Rename the **disease score** columns in the two networks to **PD score** and **AD score**, respectively, by right-clicking the name and choosing the **Rename column** option.

### 3.3 Merging networks

Cytoscape provides functionality to merge two or more networks, building either their union, intersection or difference. To merge the two disease networks go to the menu **Tools → Merge → Networks**. Select the two disease networks in the **Available Networks** list and move them to the **Networks to Merge** list by clicking the **>** button. Make sure the **Union** button is selected and click the **Merge** button.

_How many nodes and edges are there in the merged network compared to the two individual disease networks?_

Because the merged network was not created by the stringApp, but rather by Cytoscape's merge tool based on two separately retrieved STRING networks, we now have two problems. First, Cytoscape does not know the merged network is a STRING network, and most menu points in the stringApp menu are thus grayed out; fix this by going to the menu **Apps → STRING → Set as STRING network**. Second, because the two disease networks were retrieved separately, the merged network does not contain any interactions between proteins involved only in Parkinson's disease and proteins involved only in Alzheimer's disease, even if the proteins interact according to STRING. To solve this, first go to the menu **Apps → STRING → Change confidence menu**, set the **New confidence cutoff** to 1, and press **OK**; this will remove all STRING interactions, leaving only the proteins. Then bring up the same dialog and lower the confidence cutoff back down to 0.4; the stringApp will now query the server again to retrieve interactions among all the proteins.

_How many nodes and edges does the network contain compared to before?_

### 3.4 Network clustering

Next, we will use the MCL algorithm to find identify clusters of tightly connected proteins within the combined network. Go to the menu **Apps → clusterMaker → MCL Cluster**. Set the **Granularity parameter (inflation value)** to 4 and choose the **score** attribute (i.e. the overall STRING confidence score) as **Array Sources**, select the option **Create new clustered network**, and click **OK** to start the clustering. The app will now run the algorithm and automatically create a network showing the clusters.

_How many clusters have at least 4 nodes?_

### 3.5 Selection filters and visual style bypass

Finally, we want to color the nodes based on which disease(s) the proteins are involved in. To do so we will make use of selection filters to select nodes based on their attributes and the visual style bypass to explicitly specify the colors of individual nodes.

First, to select all proteins associated with Alzheimer's disease, go to the **Select** tab, click the **+** button, and choose **Column Filter**. Select **Node: AD score** in the drop-down menu and the 100 nodes associated with Alzheimer's disease will be highlighted yellow in the network. Next, go to the **Style** tab and click the square just left of **Fill color** to set a bypass color for the selected nodes (e.g. red). Repeat this process for the node attribute column **Node: PD score** and choose different color (e.g. blue).

To select the nodes that are shared between the diseases, go to the **Select** tab and create two column filters, one for **Node: AD score** and one for **Node: PD score**. Since the filters by default are combined using the **Match all (AND)** rule, only the nodes that have both scores will be selected. Go to the **Style** tab to set a third bypass color for this last group.

_How are the two diseases distributed across the clusters?_
