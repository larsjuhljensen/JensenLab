---
title: Cytoscape stringApp exercises
layout: single
permalink: /training/stringapp/
sidebar:
  nav: "training-stringapp"
---
In these exercises, we will use the [stringApp](http://apps.cytoscape.org/apps/stringApp) for [Cytoscape](http://cytoscape.org/) to retrieve molecular networks from the [STRING](https://string-db.org/) and [STITCH](https://stitch-db.org/) databases. The exercises will teach you how to:

* retrieve networks for proteins or small-molecule compounds of interest
* retrieve networks for a disease or an arbitrary topics in PubMed
* layout and visually style the resulting networks
* import external data and map them onto a network
* perform enrichment analyses and visualize the results
* identify functional modules through network clustering
* merge and compare networks

## Prerequisites

To follow the exercises, please make sure that you have the latest version of Cytoscape installed. Then start Cytoscape and go to **Apps → App Manager** to check for new apps, install them and update the current ones if necessarily. The exercises require you to have certain Cytoscape apps installed. Search for the **stringApp** in the search field; if it is not already installed, select it and press the **Install** button to install it. Similarly, make sure you have the **enhancedGraphics** and **clusterMaker2** apps installed before closing the App Manager.

## Exercise 1

In this exercise, we will perform some simple queries to retrieve molecular networks based on a protein, a small-molecule compound, a disease, and a topic in PubMed.

### 1.1 Query for your favorite protein(s)

Go to the menu **File → Import → Network → Public Databases**. In the import dialog, choose **STRING: protein query** as **Data Source** and type your favorite protein(s) into the **Enter protein names or identifiers** field. You can select the appropriate organism by typing the name. The **Maximum number of interactors** determines how many interaction partners of your protein(s) of interest will be added to the network. By default, if you enter only one protein name, the resulting network will contain 10 additional interactors. If you enter more than one protein name, the network will contain only the interactions among these proteins, unless you explicitly ask for additional proteins.

Unless the name(s) you entered give unambiguous matches, a disambiguation dialog will be shown next. It lists all the matches that the stringApp finds for each query term and selects the first one for each. Select the right one(s) you meant and continue by pressing the **Import** button.

_How many nodes are in the resulting network? How does this compare to the maximum number of interactors you specified? What types of information does the **Node Table** provide?_

### 1.2 Query for your favorite compound(s)

Go to the menu **File → Import → Network → Public Databases**. In the import dialog, choose **STITCH: protein/compound query** as **Data Source** and type your favorite compound(s) into the **Enter protein or compound names or identifiers** field. You can select the organism and number of additional interactors just like for the protein query above, and the disambiguation dialog also works the same way.

_How is this network different from the protein-only network with respect to node types and the information provided in the **Node Table**?_

### 1.3 Query for a disease of interest

Go to the menu **File → Import → Network → Public Databases**. In the import dialog, choose **STRING: disease query** as **Data Source** and type a disease of interest into the **Enter disease term** field (e.g. Alzheimer's disease). The stringApp will retrieve a STRING network for the top-N proteins (by default 100) associated with the disease.

The next dialog shows all the matches that the stringApp finds for your disease query and selects the first one. Make sure to select the intended disease before pressing the **Import** button to continue.

_Which additional attribute column do you get in the **Node Table** for a disease query compared to a protein query? (Hint: check the last column.)_

### 1.4 Query for a topic in PubMed

Go to the menu **File → Import → Network → Public Databases**. In the import dialog, choose **STRING: PubMed query** as **Data Source** and type query representing a topic of interest into the **PubMed Query** field (e.g. jet-lag). You can use any query that would work on the PubMed website, but it should obviously a topic with related genes or proteins. The stringApp will query PubMed for the abstracts, find the top-N proteins (by default 100) associated with these abstracts, and retrieve a STRING network for them.

_Which attribute column do you get in the **Node Table** for a PubMed query compared to a disease query? (Hint: check the last columns.)_

### 1.5 Try the new Cytoscape search interface

Click on the drop-down menu with an icon on it, located on the left side below the **Network** tab in the **Control Panel**. Select one of the four possible STRING queries and directly enter your query in the text field. To change settings such as organism, click the ☰ button next to the text field. Finally, click the 🔍 button to retrieve a STRING network for your query.

## Exercise 2

In this exercise, we will work with a list of 78 proteins that interact with TrkA (tropomyosin-related kinase A) in neuroblastoma cells 10 min after stimulation with NGF (nerve growth factor) ([Emdal et al., 2015](http://stke.sciencemag.org/content/8/374/ra40)). The adapted table with data is available for download from here: https://goo.gl/zjDa81

### 2.1 Retrieve network for a set of proteins

Start Cytoscape or open a new session from the menu **File → New → Session. Go to the menu File → Import → Network → Public Databases**. In the import dialog, choose **STRING: protein query** as the **Data Source** and insert the list of UniProt accession numbers from the first column in the table into the **Enter protein names or identifiers** field.

The next dialog shows all the matches that the stringApp finds for your query and selects the first one. Select the right one and continue with the import by pressing the Import button.

_How many nodes and edges are in the resulting network? Are they all connected to each other and if not why?_

Cytoscape provides several visualization options under the Layout menu. Experiment with these and find one that allows you to see the shape of the network easily. For example, you can try the ‘Degree Sorted Circle Layout’ and the ‘Prefuse Force Directed Layout’ with the ‘score’ as edge weight.
Can you find a layout that allows you to easily recognize patterns in the network? What about the Edge-weighted Spring Embedded Layout with the attribute ‘score’, which is the combined STRING interaction score.

### 2.2 Browse the node attributes and select nodes

Note that the retrieved network contains a lot of additional information associated with the nodes and edges, such as the protein sequence, tissue expression data (Node Table) as well as the confidence scores for the different interaction evidences (Edge Table). In the following, we will explore these data using Cytoscape.

Browse through the node attributes table and find the target family column (hint: the additional attributed are sorted alphabetically). This column contains target information from the Pharos database (https://pharos.nih.gov/idg/targets).

_Which families are represented?_

You can highlight nodes that belong to a certain family by selecting the rows in the table, bringing up the context menu (right-click the selected rows) and choosing the ‘Select nodes from selected rows’ option. You can also use the icon in the menu to zoom into the selected node.

To select all nodes that are in the Kinase target family, you can create a selection filter in the Select tab (it iss to the right of ‘Style’). Click the ➕ button and choose ‘Column filter’ from the drop-down menu. Then, find and select the attribute ‘Node: target family’. Type Kinase in the text field and all nodes with this attribute value will be highlighted.

_How many proteins from the network are in the Kinase target family?_

### 2.3 Style the network I

Cytoscape allows you to map properties of the nodes and edges to visual parameters such as node color and edge width. We will map the target family data to the node shape. From the left panel top menu, select 'Style' (it is between 'Network' and ‘Select’). Then click ◀ button to the right of the property you want to change, for example ‘Fill Color’. Next, set the 'Column' to the node column containing the data that you want to use (target family). This action will remove the rainbow coloring of the nodes. Click the field next to each different attribute value, e.g. Kinase and GPCR and choose a different color by clicking the ⋯ button. You can also set a color for the default field, e.g., for all nodes that do not have a target family annotation from Pharos by clicking on the white colored button in the first column of the same row.

### 2.4 Import own data from a table

Network nodes and edges can have additional information associated with them that we can load into Cytoscape and use for visualization. We will import the data from the text file (https://goo.gl/zjDa81).

To import the node attributes file into Cytoscape, go to File → Import → Table → File. The preview in the import dialog will show how the file is interpreted given the current settings and will update automatically when you change them. To change the default selection chosen by Cytoscape, click on the arrow in the column heading. For example, you can decide whether the column is imported or not by selecting one of the two options: for imported and for not imported. This column-specific dialog will also allow you to change the column name and type.

Now you need to map unique identifiers between the entries in the data and the nodes in the network. The key point of this is to identify which nodes in the network are equivalent to which entries in the table. This enables mapping of data values into visual properties like Fill Color and Shape. This kind of mapping is typically done by comparing the unique Identifier attribute value for each node (Key Column for Network) with the unique Identifier value for each data value (). As a default, Cytoscape looks for an attribute value of ‘ID’ in the network and a user-supplied Key in the dataset.

The Key Column for Network can be changed using a combo box and allows you to set the node attribute column that is to be used as key to map to. In this case it is the ‘query term’ because this attribute contains the UniProt accession numbers you entered when retrieving the network. You can also change the Key by pressing the key button () for the column that is to be used as key for mapping values in the dataset.

If there is a match between the value of a Key in the dataset and the value the Key Column for Network field in the network, all attribute-value pairs associated with the element in the dataset are assigned to the matching node in the network. You will find the imported columns at the end of the Node Table.

### 2.5 Style the network II

Now, we want to color the nodes according to the protein abundance (log ratio) compared to the cells before NGF treatment. From the left panel top menu, select 'Style' (it is to the right of 'Network'). Then click on the ◀button to the right of the property you want to change, for example ‘Fill Color’. Next, set the 'Column' to the node column containing the data that you want to use (10 min log ratio). Since this is a numeric value, we will use the 'Continuous Mapping' as the ‘Mapping Type’, and set a color gradient for how abundant each protein is. The default Cytoscape color gradient blue-white-red already gives a nice visualization of the negative-to-positive abundance ratio.

If you want to change the colors, double click on the color gradient in order to bring up the 'Continuous Mapping Editor' window and edit the colors for the continuous mapping. In the mapping editor dialog, the color that will be used for the minimum value is on the left, and the max is on the right. Double click on the triangles on the top and sides of the gradient to change the colors. The triangles on the top represent the values at which the data will be clipped — anything above the right triangle will be set to the max value. This is useful if you have a small number of values that are significantly higher than the median. To have three colors, you need to add a new triangle (for the white color) by pressing the Add button and set the Handle position value to 0. As you move the triangles and change the color, the display in the network pane will automatically update — so this is all easier to do than to explain! If at any point it doesn't seem to work as expected, it is easiest to just delete the mapping and start again.

_What do you observe? Are up- and down-regulated nodes connected to each other or not?_

_Can you improve the color mapping such that it is easier to see which nodes have a log ratio below -2 and above 2?_

### 2.6 Retrieve and explore functional enrichment

Next, we will retrieve functional enrichment for the proteins in our network. After making sure that no nodes are selected in the network, go to the menu Apps → STRING Enrichment → Retrieve functional enrichment and keep the default p-value of 0.05. A new STRING Enrichment tab will appear in the Table Panel on the bottom. It contains a table of enriched terms and corresponding information for each enrichment category.
Explore the enrichment results. Which are the top three enriched terms? What happens when you click some of the terms you find interesting?

To explore the terms of only one specific category, e.g. all GO terms, you can click on the filter icon on the most left in the Table panel. Select the three types of GO terms, enable the option to Remove redundant terms and set the redundancy cutoff to 0.2. In this way, you will only see the significant GO terms that do not represent largely the same set of proteins within the network.

_Which are the top 3 enriched terms now (lowest p-values)?_

Next, we are going to visualize the top-3 enriched terms in the network by using split charts. Click the Settings icon (rightmost one) and set the Number of terms to chart to 3. You can choose your favorite color palette by clicking on the Change Color Palette button. Click OK to confirm the Settings and click the colorful chart icon to draw the charts onto the network. If no charts are drawn on the nodes, you need to install the **EnhancedGraphics** app from the App Manager.

_Do the top three terms annotate the network well in your opinion?_

### 2.7 Cluster the network

Next, we will use clusterMaker to find clusters in the network using the MCL clustering algorithm. Install clusterMaker from the AppManager (go to Apps → AppManager, search for the app name and press the Install button). The MCL clustering algorithm can be found in the menu Apps → clusterMaker → MCL Cluster. Set the granularity parameter (inflation value) to 4 and choose the ‘score’ attribute as **Array Sources** (this is the overall confidence score for each interaction from STRING). Select both options in the **Visualization Options** section at the bottom of the window and the app will automatically create a new clustered network and restore all edges between the clusters.

_How many clusters with at least 4 nodes are generated? Do you notice something particular about how the nodes are distributed in the clusters?_

You can now run the functional enrichment analysis on one of the clusters by first selecting the nodes in the cluster and then using the menu **Apps → STRING Enrichment → Retrieve functional enrichment**. If the menu item is grayed out, you need to first tell stringApp that this is a STRING network by choosing the menu point **Apps → STRING → Set as STRING network**.

_Is there a difference in the most enriched terms for the whole network and for only one cluster? Does it depend on the choice of cluster?_

## Exercise 3

We are going to use the stringApp for Cytoscape (http://apps.cytoscape.org/apps/stringapp) to query the DISEASES database (http://diseases.jensenlab.org) and retrieve a network of proteins that are associated with Parkinson’s disease and compare it to another related disease (Alzheimer’s disease).

### 3.1 Retrieve disease networks

Open a new session in Cytoscape from the menu **File → New → Session. Use the menu File → Import → Network → Public Databases** and the **STRING: disease query** option. Retrieve a network for ‘Parkinson’s disease’ and another for ‘Alzheimer’s disease’.

### 3.2. Browse the node attributes table

Browse through the node attributes table and find the disease score column. Sort it by descending values to see the highest disease scores. You can highlight the corresponding nodes by selecting the rows in the table, bringing up the context menu (right-click the selected rows) and choosing the ‘Select nodes from selected rows’ option. You can also use one of the icons in the menu to zoom into the selected node. Look for an example for a node with a disease score of 5 and one with a disease score below 4.
Rename the ‘disease score’ column to ‘alzheimer’s score’ and ‘parkinson’s score’, respectively, by right-clicking the name and choosing the **Rename column** option.

### 3.3 Merge two related diseases

Cytoscape provides functionality to merge two or more networks by building their union, intersection or difference, which can be found in the menu **Tools → Merge → Networks**. Select the two disease networks in the ‘Available Networks’ list and move them to the **Networks to Merge** list by clicking the > button. Make sure the Union button is selected and click the Merge button to initiate the network merge.

_How does the resulting network look and why? Note that you can select one of the many layouts to visualize the merged network better._

### 3.4 Complement the merged network

Since the merged network was not created by the stringApp, we have to manually set it to be a String network from the stringApp menu (Apps -> STRING -> Set as STRING network). Next, we will use the Apps -> STRING -> Change confidence menu to increase the confidence to 1, which will effectively remove all edges from the network. Then, we will bring up the Change confidence window again and set the confidence to 0.4, which will prompt the stringApp to retrieve all interactions with a confidence score above 0.4 between all proteins in the current network from STRING.

_How many nodes and edges are in the new network and why? Is the number bigger or smaller than before changing the confidence?_

### 3.5 Run clusterMaker to identify clusters

Next, we will use clusterMaker to find clusters in the merged network using the MCL clustering algorithm (**Apps → clusterMaker → MCL Cluster**). Set the granularity parameter to 4. To include an edge weight in the cluster identification, choose the **score** attribute as **Array Sources** (this is the overall confidence score for each interaction from STRING). Note that the app will automatically create a new clustered network and restore all edges if you select both options in the **Visualization Options** section at the bottom of the window.

_How many clusters have at least 4 nodes?_

### 3.6 Selection filters and visual style bypass

Finally, we want to highlight the nodes that are associated with each disease and to easily see to which cluster they belong. First, we will select all nodes that have an alzheimer’s score by creating a selection filter. Go to the ‘Select’ tab, click the + button and select the ‘Column filter’ option. Find the ‘Node: alzheimer’s score’ in the drop-down menu and the 100 nodes associated with Alzheimer’s disease will be highlighted yellow in the network. Next, go to the ‘Style’ tab and click the square next to ‘Fill color’ to set a color bypass for the selected nodes (for example red). Repeat the same action for the node attribute column ‘Node: parkinson’s score’ and choose another color.

To select all nodes that are shared between the diseases, create a second filter in the ‘Select’ tab. If the first filter is for Alzheimer’s disease, the second should be for Parkinson’s disease or the other way around. Since the filters are connected with an ‘AND’ relationship, only nodes that have both scores will be selected. Go to the ‘Style’ tab to set a color for this last group.

_In which clusters are the shared nodes? Are there clusters that contain nodes associated with both diseases?_
