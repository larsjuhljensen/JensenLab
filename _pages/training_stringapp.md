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

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: protein query** as **Data Source** and type your favorite protein into the **Enter protein names or identifiers** field (e.g. SORCS2). You can select the appropriate organism by typing the name (e.g. Homo sapiens). The **Maximum number of interactors** determines how many interaction partners of your protein(s) of interest will be added to the network. By default, if you enter only one protein name, the resulting network will contain 10 additional interactors. If you enter more than one protein name, the network will contain only the interactions among these proteins, unless you explicitly ask for additional proteins.

Unless the name(s) you entered give unambiguous matches, a disambiguation dialog will be shown next. It lists all the matches that the stringApp finds for each query term and selects the first one for each. Select the right one(s) you meant and continue by pressing the **Import** button.

[Import SORCS2 network](cycmd:string protein query query=SORCS2 taxonID=9606){: .btn .btn--cybrowser .btn--primary}

_How many nodes are in the resulting network? How does this compare to the maximum number of interactors you specified? What types of information does the **Node Table** provide?_

### 1.2 Compound queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STITCH: protein/compound query** as **Data Source** and type your favorite compound into the **Enter protein or compound names or identifiers** field (e.g. imatinib). You can select the organism and number of additional interactors just like for the protein query above, and the disambiguation dialog also works the same way.

[Import imatinib network](cycmd:string compound query query=imatinib taxonID=9606){: .btn .btn--cybrowser .btn--primary}

_How is this network different from the protein-only network with respect to node types and the information provided in the **Node Table**?_

### 1.3 Disease queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: disease query** as **Data Source** and type a disease of interest into the **Enter disease term** field (e.g. Alzheimer's disease). The stringApp will retrieve a STRING network for the top-N proteins (by default 100) associated with the disease.

The next dialog shows all the matches that the stringApp finds for your disease query and selects the first one. Make sure to select the intended disease before pressing the **Import** button to continue.

[Import Alzheimer's disease network](cycmd:string disease query disease=DOID:10652 taxonID=9606 limit=100){: .btn .btn--cybrowser .btn--primary}

_Which additional attribute column do you get in the **Node Table** for a disease query compared to a protein query? (Hint: check the last column.)_

### 1.4 PubMed queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: PubMed query** as **Data Source** and type query representing a topic of interest into the **PubMed Query** field (e.g. jet-lag). You can use any query that would work on the PubMed website, but it should obviously a topic with related genes or proteins. The stringApp will query PubMed for the abstracts, find the top-N proteins (by default 100) associated with these abstracts, and retrieve a STRING network for them.

[Import jet-lag network](cycmd:string pubmed query pubmed=jet-lag taxonID=9606 limit=50){: .btn .btn--cybrowser .btn--primary}

_Which attribute column do you get in the **Node Table** for a PubMed query compared to a disease query? (Hint: check the last columns.)_

### 1.5 New search interface

The types of queries described above can alternatively be performed through the new Cytoscape search interface. Click on the drop-down menu with an icon on it, located on the left side below the **Network** tab in the **Control Panel**. Select one of the four possible STRING queries and directly enter your query in the text field. To change settings such as organism, click the ☰ button next to the text field. Finally, click the 🔍 button to retrieve a STRING network for your query.

## Exercise 2

In this exercise, we will work with a list of 78 proteins that interact with TrkA (tropomyosin-related kinase A) in neuroblastoma cells 10 min after stimulation with NGF (nerve growth factor) ([Emdal et al., 2015](http://stke.sciencemag.org/content/8/374/ra40)). An adapted table with the data from this study is available [here](/assets/stringapp/Emdal2015SciSignal.tsv).

### 2.1 Protein network retrieval

Start Cytoscape or close the current session from the menu **File → Close**. Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: protein query** as the **Data Source** and paste the list of UniProt accession numbers from the first column in the table into the **Enter protein names or identifiers** field.

Next, the disambiguation dialog shows all STRING proteins that match the query terms, with the first protein for each query term automatically selected. This default is fine for this exercise; click the **Import** button to continue.

[Import network](cycmd:string protein query query="Q75VX8,P29353,O14492,P19174,Q07890,P62993,P42336,Q9H706,O00750,Q8TER5,P27986,O00459,Q07889,Q92529,P42338,P29590,P62987,Q9UKV5,Q13191,Q13480,Q9Y6I3,O00443,Q8IZ07,Q8N1I0,O75962,O75473,Q96S55,Q15276,P16234,Q63ZY3,Q9UJ41,P52735,Q8TC07,Q06124,O14976,Q9Y4H2,Q9UN70,P42566,Q9H3W5,Q7Z6Z7,P36896,Q86YT6,O75665,Q8WXW3,Q6ZNH5,P10599,P04040,P05413,P14923,Q02413,P22735,P23528,P31025,P62805,P15924,P07737,Q08380,Q99880,P02788,P06702,B9A064,Q08188,Q08554,P61626,P81605,Q6ZMV7,P09104,P62937,Q13410,P13010,P12956,P30512,P09211,O75027,Q9UQ80,Q06830,P51858,O95757" taxonID=9606 limit=0){: .btn .btn--cybrowser .btn--primary}

_How many nodes and edges are there in the resulting network? Do the proteins all form a connected network? Why?_

Cytoscape provides several visualization options under the **Layout** menu. Experiment with these and find one that allows you to see the shape of the network easily. For example, you can try the **Degree Sorted Circle Layout**, the **Prefuse Force Directed Layout**, and the **Edge-weighted Spring Embedded Layout**.

[Layout network](cycmd:layout fruchterman-rheingold){: .btn .btn--cybrowser .btn--primary}

_Can you find a layout that allows you to easily recognize patterns in the network? What about the Edge-weighted Spring Embedded Layout with the attribute ‘score’, which is the combined STRING interaction score._

### 2.2 Discrete color mapping

Cytoscape allows you to map attributes of the nodes and edges to visual properties such as node color and edge width. Here, we will map drug target family data from the [Pharos](https://pharos.nih.gov/idg/targets) database to the node color.

Select **Style** from the top menu in the left panel (it is between **Network** and **Select**). Click the **◀** button to the right of the property you want to change, in this case **Fill Color**, and set **Column** to the node column containing the data that you want to use (i.e. **target family**). This action will remove the rainbow coloring of the nodes and present you with a list of all the different values of the attribute that are exist in the network.

_Which target families are present in the network?_

To color the corresponding proteins, first click the field to the right of an attribute value, i.e. **GPCR** or **Kinase**, then click the **⋯** button and choose a color from color selection dialog. You can also set a default color, e.g. for all nodes that do not have a target family annotation from Pharos, by clicking on the white button in the first column of the same row.

_How many of the proteins in the network are kinases?_

Note that the retrieved network contains a lot of additional information associated with the nodes and edges, such as the protein sequence, tissue expression data (Node Table) as well as the confidence scores for the different interaction evidences (Edge Table). In the following, we will explore these data using Cytoscape.

### 2.3 Data import

Network nodes and edges can have additional information associated with them that we can load into Cytoscape and use for visualization. We will import the data from the [text file](/assets/stringapp/Emdal2015SciSignal.tsv).

To import the node attributes file into Cytoscape, go to **File → Import → Table from File**. The preview in the import dialog will show how the file is interpreted given the current settings and will update automatically when you change them. To change the default selection chosen by Cytoscape, click on the arrow in the column heading. For example, you can decide whether the column is imported or not by changing the **Meaning** of the column (hover over each symbol with the mouse to see what they mean). This column-specific dialog will also allow you to change the column name and type.

Now you need to map unique identifiers between the entries in the data and the nodes in the network. The key point of this is to identify which nodes in the network are equivalent to which entries in the table. This enables mapping of data values into visual properties like Fill Color and Shape. This kind of mapping is typically done by comparing the unique Identifier attribute value for each node (Key Column for Network) with the unique Identifier value for each data value (key symbol). As a default, Cytoscape looks for an attribute value of ‘ID’ in the network and a user-supplied Key in the dataset.

The **Key Column** for Network can be changed using a combo box and allows you to set the node attribute column that is to be used as key to map to. In this case it is **query term** because this attribute contains the UniProt accession numbers you entered when retrieving the network. You can also change the Key by pressing the key button for the column that is to be used as key for mapping values in the dataset.

If there is a match between the value of a Key in the dataset and the value the Key Column for Network field in the network, all attribute--value pairs associated with the element in the dataset are assigned to the matching node in the network. You will find the imported columns at the end of the Node Table.

[Import table](cycmd:table import url url="https://jensenlab.org/assets/stringapp/Emdal2015SciSignal.tsv" keyColumnForMapping="query term" keyColumnIndex=1 startLoadRow=1){: .btn .btn--cybrowser .btn--primary}

### 2.4 Continuous color mapping

Now, we want to color the nodes according to the protein abundance (log ratio) compared to the cells before NGF treatment. From the left panel top menu, select **Style** (it is to the right of **Network**). Then click on the **◀** button to the right of the property you want to change, for example **Fill Color**. Next, set **Column** to the node column containing the data that you want to use (10 min log ratio). Since this is a numeric value, we will use the **Continuous Mapping** as the **Mapping Type**, and set a color gradient for how abundant each protein is. The default Cytoscape color gradient blue-white-red already gives a nice visualization of the negative-to-positive abundance ratio.

_Are the up-regulated nodes grouped together?_

To change the colors, double click on the color gradient in order to bring up the **Continuous Mapping Editor** window and edit the colors for the continuous mapping. In the mapping editor dialog, the color that will be used for the minimum value is on the left, and the max is on the right. Double click on the triangles on the top and sides of the gradient to change the colors. The triangles on the top represent the values at which the data will be clipped; anything above the right triangle will be set to the max value. This is useful if you have a small number of values that are significantly higher than the median. To have three colors, you need to add a new triangle (for the white color) by pressing the Add button and set the Handle position value to 0. As you move the triangles and change the color, the display in the network pane will automatically update — so this is all easier to do than to explain! If at any point it doesn't seem to work as expected, it is easiest to just delete the mapping and start again.

_Can you improve the color mapping such that it is easier to see which nodes have a log ratio below -2 and above 2?_

### 2.5 Functional enrichment

Next, we will retrieve functional enrichment for the proteins in our network. After making sure that no nodes are selected in the network, go to the menu **Apps → STRING Enrichment → Retrieve functional enrichment** and keep the default p-value of 0.05. A new STRING Enrichment tab will appear in the Table Panel on the bottom. It contains a table of enriched terms and corresponding information for each enrichment category.

[Retrieve functional enrichment](cycmd:string retrieve enrichment cutoff=0.05){: .btn .btn--cybrowser .btn--primary}

_Which are the three most statistically significant terms?_

To explore only specific types of terms, e.g. GO terms, and to remove redundant terms from the table, click on the filter icon in the **Table panel** (leftmost icon). Select the three types of GO terms, enable the option to **Remove redundant terms** and set **Redundancy cutoff** to 0.2. In this way, you will see only the statistically significant GO terms that do not represent largely the same set of proteins within the network. You can see which proteins are annotated with a given term by selecting the term in the **STRING Enrichment** panel.

_Do the functional terms assigned to a protein correlate with whether it is up- or down-regulated?_

Next, we will visualize the top-3 enriched terms in the network by using split charts. Click the settings icon (rightmost icon) and set the **Number of terms** to chart to 3; you can optionally also **Change Color Palette** before clicking **OK** to confirm the new settings. Click the colorful chart icon to show the terms as the charts on the network.

_Do these terms give good coverage of the proteins in network?_

Finally, save the list of enriched terms and associated p-values as a text file by going to **File → Export → Export STRING Enrichment**.

## Exercise 3

We are going to use the stringApp to query the [DISEASES](https://diseases.jensenlab.org) database for proteins associated with Parkinson’s disease and with Alzheimer's disease, retrieve STRING networks for both, created a combined network for the two neurodegenerative diseases, identify clusters in the network, and color it to compare the diseases.

### 3.1 Disease network retrieval

Close the current session in Cytoscape from the menu **File → Close**. Use the menu **File → Import → Network from Public Databases** and the **STRING: disease query** option. Retrieve a network for **Parkinson's disease** and another for **Alzheimer's disease**.

[Import Parkinson's disease network](cycmd:string disease query disease=DOID:14330 taxonID=9606 limit=100){: .btn .btn--cybrowser .btn--primary} [Import Alzheimer's disease network](cycmd:string disease query disease=DOID:10652 taxonID=9606 limit=100){: .btn .btn--cybrowser .btn--primary}

### 3.2. Working with node attributes

Browse through the node attributes table and find the disease score column. Sort it descending by values to see the highest disease scores. You can highlight the corresponding nodes by selecting the rows in the table, bringing up the context menu (right-click the selected rows) and choosing the ‘Select nodes from selected rows’ option. You can also use one of the icons in the menu to zoom into the selected node.

Look for an example for a node with a disease score of 5 and one with a disease score below 4.

Rename the **disease score** columns in the two networks to **PD score** and **AD score**, respectively, by right-clicking the name and choosing the **Rename column** option.

[Rename disease score to PD score](cycmd:table rename column columnName="disease score" newColumnName="PD score" table="String Network - Parkinson's disease default node){: .btn .btn--cybrowser .btn--primary} [Rename disease score to AD score](cycmd:table rename column columnName="disease score" newColumnName="AD score" table="String Network - Alzheimer's disease default node){: .btn .btn--cybrowser .btn--primary}

### 3.3 Merging networks

Cytoscape provides functionality to merge two or more networks, building either their union, intersection or difference. To merge the two disease networks go to the menu **Tools → Merge → Networks**. Select the two disease networks in the **Available Networks** list and move them to the **Networks to Merge** list by clicking the **>** button. Make sure the **Union** button is selected and click the **Merge** button.

_How many nodes and edges are there in the merged network compared to the two individual disease networks?_

Because the merged network was not created by the stringApp, but rather by Cytoscape's merge tool based on two separately retrieved STRING networks, we now have two problems. First, Cytoscape does not know the merged network is a STRING network, and most menu points in the stringApp menu are thus grayed out; fix this by going to the menu **Apps → STRING → Set as STRING network**. Second, because the two disease networks were retrieved separately, the merged network does not contain any interactions between proteins involved only in Parkinson's disease and proteins involved only in Alzheimer's disease, even if the proteins interact according to STRING. To solve this, first go to the menu **Apps → STRING → Change confidence menu**, set the **New confidence cutoff** to 1, and press **OK**; this will remove all STRING interactions, leaving only the proteins. Then bring up the same dialog and lower the confidence cutoff back down to 0.4; the stringApp will now query the server again to retrieve interactions among all the proteins.

_How many nodes and edges does the network contain compared to before?_

### 3.4 Network clustering

Next, we will use the MCL algorithm to find identify clusters of tightly connected proteins within the combined network. Go to the menu **Apps → clusterMaker → MCL Cluster**. Set the **Granularity parameter (inflation value)** to 4 and choose the **score** attribute (i.e. the overall STRING confidence score) as **Array Sources**, select the option **Create new clustered network**, and click **OK** to start the clustering. The app will now run the algorithm and automatically create a network showing the clusters.

[Cluster network](cycmd:cluster mcl attribute=score inflation_parameter=4 showUI=true){: .btn .btn--cybrowser .btn--primary}

_How many clusters have at least 4 nodes?_

### 3.5 Selection filters and style bypass

Finally, we want to color the nodes based on which disease(s) the proteins are involved in. To do so we will make use of selection filters to select nodes based on their attributes and the visual style bypass to explicitly specify the colors of individual nodes.

First, to select all proteins associated with Alzheimer's disease, go to the **Select** tab, click the **+** button, and choose **Column Filter**. Select **Node: AD score** in the drop-down menu and the 100 nodes associated with Alzheimer's disease will be highlighted yellow in the network. Next, go to the **Style** tab and click the square just left of **Fill color** to set a bypass color for the selected nodes (e.g. red). Repeat this process for the node attribute column **Node: PD score** and choose different color (e.g. blue).

To select the nodes that are shared between the diseases, go to the **Select** tab and create two column filters, one for **Node: AD score** and one for **Node: PD score**. Since the filters by default are combined using the **Match all (AND)** rule, only the nodes that have both scores will be selected. Go to the **Style** tab to set a third bypass color for this last group.

_How are the two diseases distributed across the clusters?_

## Exercise 4

In this exercise, we will retrieve virus-host networks for two closely related viruses, merge them into a single network, and then will retrieve the functional enrichment for the host proteins in this network.

### 4.1 Virus queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: protein query** as the **Data Source**. As of version 1.4 of the STRING app, 236 virus species are included in the species dropdown menu. Since most viruses are small (they have a median of 9 proteins in their genomes) it is reasonable to import **all proteins of this species** for a given virus, so select this checkbox underneath the species dropdown. For this example we will query all proteins of "Human papillomavirus type 16 (HPV 16)". Simply type HPV 16 and select the species from the resulting shorter dropdown menu.

_How many virus proteins are encoded for by this virus? What node information is imported along with the names of the proteins?_

### 4.2 Expand with host interactors

To retrieve interactions with host proteins, go to **Apps → STRING → Expand network**. In the resulting dialog, enter the number of desired host proteins, and select the host species from **Type of interactors to expand network by**. All host species for which we have interactions with the currently imported virus genes, will be shown in the dropdown menu. The **selectivity of interactors** can also be specified -- we recommend a default value of 0.5, but you can move the slider towards 0 to decrease the number of network-sepcific interactors or towards 1 to increase it. In this example, we will import 50 human proteins, and keep the default selectivity.

The resulting network will be automatically re-styled such that the nodes representing virus proteins are red and host proteins are green-blue. These attributes can be changed from the Cytoscape Style menu.

_Which human protein has the highest interaction score to one of the virus proteins? What cellular functions is this protein involved in? (Hint: open the results panel under **Apps → STRING → Show results** panel.)_

Additional viruses or hosts can be added to the network by iterating on this procedure, but this will only add proteins that interact with the proteins that are already in the network. This will work fine when adding new hosts, since all virus proteins are already in the network. However to add new viruses, we recommend merging the expanded networks for each virus.

### 4.3 Add specific host proteins

If a specific host protein is desired, it can also be included in the network from the **Apps → STRING → Query for additional nodes** menu option. In this example, p53 is not one of the proteins that was included in the network in the previous step, however it is known that the HPV E6 protein mediates ubiquitination of p53. To include this protein, choose "Homo sapiens" for the species (you may have to scroll up in the list), and enter "tp53" into the text area box in the dialog, then click **Import**.

_Which HPV proteins does p53 interact with?_

Note that p53 will be added to the network in the previous step if a selectivity of 0.1 is chosen. Choosing a lower selectivity will include more hub proteins (such as p53) that are connected to many proteins, and that do not interact specifically with proteins in your network. Conversely, choosing a higher selectivity will include more proteins that are more specific to your network, but these interactions will have lower confidence (since any higher confidence hub proteins will be filtered out). Further, be aware that changing the selectivity parameter will change the enrichment results in step 4.5, since different proteins will be included in the host network.

### 4.4 Merge two host-virus networks

Let us now compare the networks for HPV 16 and HPV 1a. Create a new host-virus network for "Human papillomavirus type 1a (HPV 1a)" by repeating steps 4.1 and 4.2. Merge the two networks using **Tools → Merge → Networks**. Move both the HPV 16 and HPV 1a networks into the **Networks to merge** box and otherwise use the defaults for the merge. In the resulting network, use the menu option **Apps → STRING → Set as STRING network** to manipulate the network as a STRING network again. To show any interactions between host nodes that were present in one source network but not the other, first set the confidence to 1, then set the confidence to the desired confidence (0.4) to retrieve any missing interactions.

The resulting network can be styled to give the nodes of each species a distinct color so that the proteins of the two viruses can be distinguished from each other.

_How many host proteins interact with E6 from both HPV species?_

### 4.5 Functional enrichment

We will now examine the human proteins to see what pathways are enriched in this network.

Next, we will retrieve functional enrichment for the human proteins. Go to the menu **Apps → STRING Enrichment → Retrieve functional enrichment** and keep the default p-value of 0.05. Homo sapiens will be selected by default in the species dropdown. It is currently only possible to retrieve enrichment for host proteins. A new STRING Enrichment tab will appear in the Table Panel. It contains a table of enriched terms and corresponding information for each enrichment category. Use the filter button in the top left of the STRING Enrichment panel to show only **KEGG Pathways**. Click on the draw charts icon to the right of the filter icon to plot the enrichment values on the network.

_Which two KEGG pathways have the lowest p-values? Which host proteins are associated with the KEGG pathways "cell cycle"? (Hint: click on the associated row in the enrichment table to select the proteins with this term.)_

## Supporting literature

Doncheva NT, Morris JH, Gorodkin J and Jensen LJ (2018). Cytoscape stringApp: Network analysis and visualization of proteomics data.  
[Preprint](https://doi.org/10.1101/358283)

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
