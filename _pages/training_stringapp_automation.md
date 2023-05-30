---
title: Cytoscape stringApp automation exercises
layout: single
permalink: /training/stringapp/automation/
sidebar:
  nav: "training-stringapp-automation"
---
## Learning objectives

In these exercises, we will use the [stringApp](http://apps.cytoscape.org/apps/stringApp) for [Cytoscape](http://cytoscape.org/) to retrieve molecular networks from the [STRING](https://string-db.org/) database. The exercises will teach you how to:

* retrieve networks for proteins of interest
* retrieve networks for a disease
* layout and visually style the resulting networks
* import external data and map them onto a network
* perform enrichment analyses and visualize the results
* merge and compare networks
* select proteins by attributes
* identify functional modules through network clustering


## Prerequisites

To follow the exercises, please make sure that you have the latest version of Cytoscape installed. Then start Cytoscape and update the current apps if necessary by checking the **App Updates** icon in the right-most corner of the manubar. 

The exercises require you to have certain Cytoscape apps installed. Open the Cytoscape App Store and search for [stringApp](http://apps.cytoscape.org/apps/stringApp), select the app and press the **Install** button to install it. Similarly, make sure you have the [yFiles Layout Algorithms](https://apps.cytoscape.org/apps/yfileslayoutalgorithms) and [clusterMaker2](https://apps.cytoscape.org/apps/clustermaker2) apps installed before switching back to Cytoscape.

If you are not already familiar with the STRING database, we highly recommend that you go through the short [STRING exercises](/training/string/) to learn about the underlying data before working with them in these exercises.

## Exercise 1

In this exercise, we will perform some simple queries to retrieve molecular networks based on a protein, a small-molecule compound, a disease, and a topic in PubMed.

### 1.1 Protein queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: protein query** as **Data Source** and type your favorite protein into the **Enter protein names or identifiers** field (e.g. SORCS2). You can select the appropriate organism by typing the name (e.g. Homo sapiens). The **Maximum number of interactors** determines how many interaction partners of your protein(s) of interest will be added to the network. By default, if you enter only one protein name, the resulting network will contain 10 additional interactors. If you enter more than one protein name, the network will contain only the interactions among these proteins, unless you explicitly ask for additional proteins.

Unless the name(s) you entered give unambiguous matches, a disambiguation dialog will be shown next. It lists all the matches that the stringApp finds for each ambiguous query term and selects the first one for each. Select the right one(s) you meant and continue by pressing the **Import** button.

[Import SORCS2 network](cycmd:string protein query query=SORCS2 taxonID=9606){: .btn .btn--cybrowser .btn--primary}

_How many nodes are in the resulting network? How does this compare to the maximum number of interactors you specified? What types of information do the **Node** and **Edge Table** provide?_

### 1.2 Compound queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STITCH: protein/compound query** as **Data Source** and type your favorite compound into the **Enter protein or compound names or identifiers** field (e.g. imatinib). You can select the organism and number of additional interactors just like for the protein query above, and the disambiguation dialog also works the same way.

[Import imatinib network](cycmd:string compound query query=imatinib taxonID=9606){: .btn .btn--cybrowser .btn--primary}

_How is this network different from the protein-only network with respect to node types and the information provided in the **Node Table**?_

### 1.3 Disease queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: disease query** as **Data Source** and type a disease of interest into the **Enter disease term** field (e.g. Alzheimer's disease). The stringApp will retrieve a STRING network for the top-N proteins (by default 100) associated with the disease.

The next dialog shows all the matches that the stringApp finds for your disease query and selects the first one. Make sure to select the intended disease before pressing the **Import** button to continue.

[Import Alzheimer's disease network](cycmd:string disease query disease=DOID:10652 taxonID=9606 limit=100){: .btn .btn--cybrowser .btn--primary}

_Which additional attribute column do you get in the **Node Table** for a disease query compared to a protein query? Hint: check the last column._

### 1.4 PubMed queries

Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: PubMed query** as **Data Source** and type query representing a topic of interest into the **PubMed Query** field (e.g. jet-lag). You can use any query that would work on the PubMed website, but it should obviously a topic with related genes or proteins. The stringApp will query PubMed for the abstracts, find the top-N proteins (by default 100) associated with these abstracts, and retrieve a STRING network for them.

[Import jet-lag network](cycmd:string pubmed query pubmed=jet-lag taxonID=9606 limit=50){: .btn .btn--cybrowser .btn--primary}

_Which attribute column do you get in the **Node Table** for a PubMed query compared to a disease query? Hint: check the last columns._

### 1.5 Using the Cytoscape Search bar

The types of queries described above can alternatively be performed through the Cytoscape Search bar (located at the top of the **Network** panel in the **Control Panel**). Click on the drop-down menu with an icon for the different resources. Select one of the four possible STRING queries and directly enter your query in the text field. To change settings such as organism, click the ☰ button next to the text field. Finally, click the 🔍 button to retrieve a STRING network for your query.

## Exercise 2

In this exercise, we will work with a list of 541 proteins associated with epithelial ovarian cancer (EOC) as identified by phosphoproteomics in the study by [Francavilla et al.](https://doi.org/10.1016/j.celrep.2017.03.015). An adapted, simplified version of their results table can be downloaded [here in TSV format](/assets/Francavilla2017CellRep.tsv) and [here in XLSX format](/assets/Francavilla2017CellRep.xlsx).

### 2.1 Protein network retrieval

Close the current session in Cytoscape from the menu **File → Close**. Go to the menu **File → Import → Network from Public Databases**. In the import dialog, choose **STRING: protein query** as the **Data Source** and paste the list of UniProt accession numbers from the UniProt column in the table (first column) into the **Enter protein names or identifiers** field. Make sure that the option **maximum additional interactors** is set to **0** before pressing the **Import** button. 

Next, the disambiguation dialog shows all query terms that cannot be matched to a unique STRING protein, with the first matching STRING protein for each query term automatically selected. This default is fine for this exercise; click the **Import** button to continue. Check that **View → Always Show Graphics Details** for a detailed view of the network.

[Import network](cycmd:string protein query query="A6ND36,A6NKT7,B1AJR3,B4DY08,B4E106,O00161,O00192,O00264,O00499,O00767,O14578,O14607,O14647,O14681,O14683,O14745,O14828,O14924,O14974,O14979,O15014,O15027,O15164,O15231,O15320,O15439,O43166,O43172,O43290,O43395,O43399,O43491,O43719,O43731,O60551,O60716,O60784,O60841,O60885,O75113,O75179,O75351,O75369,O75376,O75400,O75427,O75448,O75569,O75643,O75909,O75925,O75970,O76021,O94979,O95049,O95071,O95171,O95218,O95248,O95249,O95365,O95391,O95400,O95453,O95674,O95772,O95785,O95831,O96013,O96017,O96019,P00533,P02538,P02545,P02686,P02765,P04920,P05386,P05412,P05783,P06748,P07199,P07910,P08238,P08559,P08670,P08727,P08729,P09601,P09651,P11137,P11388,P12694,P12931,P12956,P13639,P13647,P14923,P15056,P15336,P15408,P15923,P16104,P16949,P17096,P17181,P17480,P17844,P17980,P18583,P18615,P18669,P18887,P19174,P19338,P19634,P20042,P20700,P20810,P21127,P21333,P21796,P22087,P22626,P23193,P23246,P23588,P24928,P25205,P25445,P26368,P26373,P27816,P27824,P29590,P29692,P30414,P30622,P31930,P31943,P31949,P35269,P35579,P35611,P35613,P35658,P36578,P40123,P41212,P42166,P42696,P43243,P45880,P46821,P48634,P48681,P48960,P49207,P49321,P49585,P49736,P49756,P49757,P49792,P50613,P51608,P52594,P55287,P55884,P56181,P58107,P61247,P61313,P62328,P62753,P62979,P62995,P68363,P78332,P78527,P80723,P84103,P84157,P85037,P98175,Q00536,Q00839,Q01082,Q01105,Q01130,Q01167,Q02078,Q02241,Q02543,Q02818,Q02880,Q02952,Q03135,Q03164,Q04637,Q05397,Q05519,Q05655,Q05682,Q07157,Q07955,Q08945,Q09666,Q12769,Q12830,Q12872,Q12888,Q12906,Q12996,Q13112,Q13153,Q13177,Q13185,Q13242,Q13243,Q13247,Q13263,Q13286,Q13425,Q13427,Q13428,Q13443,Q13451,Q13459,Q13523,Q13796,Q13838,Q13946,Q14004,Q14008,Q14151,Q14156,Q14160,Q14207,Q14289,Q14498,Q14573,Q14669,Q14684,Q14694,Q14739,Q14764,Q14814,Q14865,Q14966,Q14978,Q14980,Q15019,Q15059,Q15061,Q15149,Q15154,Q15233,Q15390,Q15424,Q15459,Q15477,Q15678,Q16181,Q16204,Q16630,Q16647,Q16666,Q24JP5,Q27J81,Q2LD37,Q2M2I8,Q3KQU3,Q53EL6,Q53F19,Q53GS9,Q5HYI7,Q5JRA6,Q5JSH3,Q5JSZ5,Q5JTV8,Q5JVS0,Q5SNT6,Q5SSJ5,Q5SW79,Q5SYE7,Q5T200,Q5T4S7,Q5T5C0,Q5TAQ9,Q5TCQ9,Q5TCZ1,Q5VT52,Q5VTL8,Q5VUA4,Q5VZK9,Q5VZL5,Q658Y4,Q66K74,Q69YN4,Q6DD88,Q6KC79,Q6NYC8,Q6P4E1,Q6PD62,Q6PKG0,Q6WCQ1,Q6Y7W6,Q6ZRV2,Q71RC2,Q76M96,Q7KYR7,Q7KZ85,Q7KZF4,Q7L1V2,Q7L4E1,Q7L4I2,Q7L8J4,Q7Z3K3,Q7Z417,Q7Z460,Q7Z478,Q7Z4V5,Q7Z5L9,Q7Z6Z7,Q86UE4,Q86UP2,Q86VM9,Q86VR2,Q86W92,Q8IU81,Q8IVF2,Q8IWS0,Q8IX90,Q8IXQ4,Q8IYB3,Q8IYI6,Q8N201,Q8N3V7,Q8N4C8,Q8N554,Q8N684,Q8N720,Q8N8A6,Q8N8S7,Q8N9T8,Q8NB78,Q8NC51,Q8ND56,Q8ND76,Q8NDX5,Q8NEY1,Q8NHG8,Q8TAQ2,Q8TBE7,Q8TDB6,Q8TDM6,Q8TDY2,Q8TEB9,Q8TEU7,Q8WU90,Q8WUB8,Q8WUI4,Q8WUM9,Q8WUY3,Q8WVC0,Q8WVM0,Q8WWI1,Q8WWM7,Q8WWQ0,Q8WX93,Q8WY36,Q8WYL5,Q8WZ74,Q92466,Q92508,Q92522,Q92538,Q92543,Q92545,Q92585,Q92597,Q92599,Q92610,Q92922,Q92945,Q92974,Q969E4,Q96AQ6,Q96B36,Q96E09,Q96E39,Q96EB6,Q96EV2,Q96F86,Q96FV9,Q96G23,Q96GX8,Q96I25,Q96J92,Q96JM3,Q96L91,Q96PK6,Q96PY5,Q96QR8,Q96S55,Q96S94,Q96ST2,Q96ST3,Q96T23,Q96T37,Q96T58,Q96TA1,Q99442,Q99567,Q99569,Q99590,Q99700,Q99959,Q9BQQ3,Q9BRD0,Q9BRJ6,Q9BSQ5,Q9BST9,Q9BTA9,Q9BTX1,Q9BU76,Q9BW71,Q9BWF3,Q9BX95,Q9BXF6,Q9BXK5,Q9BXP5,Q9BYW2,Q9BZ71,Q9BZZ5,Q9C0C2,Q9GZY8,Q9H0C8,Q9H0D6,Q9H1E3,Q9H2H9,Q9H2U2,Q9H307,Q9H3R2,Q9H4L5,Q9H5H4,Q9H6F5,Q9H7F0,Q9H8Y8,Q9HAU0,Q9HB09,Q9HCD5,Q9HCG8,Q9HCM4,Q9NPH3,Q9NQC3,Q9NQG5,Q9NQG6,Q9NRA0,Q9NRA8,Q9NRG0,Q9NTI5,Q9NVM6,Q9NWB6,Q9NWV8,Q9NWW5,Q9NX40,Q9NX94,Q9NXD2,Q9NY27,Q9NY61,Q9NYF8,Q9NYM9,Q9NYV4,Q9NZ32,Q9NZJ7,Q9NZT2,Q9P0B6,Q9P0K7,Q9P1Y6,Q9P206,Q9P227,Q9P2E9,Q9P2N5,Q9P2R6,Q9UBC2,Q9UBI6,Q9UBV2,Q9UDY2,Q9UEY8,Q9UGU0,Q9UH62,Q9UHB6,Q9UHB7,Q9UHD8,Q9UHR4,Q9UHW9,Q9UID3,Q9UIG0,Q9UK61,Q9UKA4,Q9UKK3,Q9UKV3,Q9ULH0,Q9ULT0,Q9UMZ2,Q9UN86,Q9UNF1,Q9UNL2,Q9UP95,Q9UPN3,Q9UPU5,Q9UPU7,Q9UQ35,Q9UQE7,Q9Y222,Q9Y2D5,Q9Y2J2,Q9Y2K6,Q9Y2V2,Q9Y2W1,Q9Y2W2,Q9Y320,Q9Y385,Q9Y3T9,Q9Y490,Q9Y4G6,Q9Y4J8,Q9Y519,Q9Y5J1,Q9Y5Q9,Q9Y5S9,Q9Y618,Q9Y6D6,Q9Y6G9,Q9Y6I3,Q9Y6K1,Q9Y6M7,Q9Y6X9,Q9Y6Y8" taxonID=9606 limit=0){: .btn .btn--cybrowser .btn--primary}

_How many nodes and edges are there in the resulting network? Do the proteins all form a connected network? Why?_

Cytoscape provides several visualization options under the **Layout** menu. Try the **Degree Sorted Circle Layout**, the **Prefuse Force Directed Layout** with score as edge weight, and **yFiles Organic Layout**.

[Layout network](cycmd:layout kamada-kawai){: .btn .btn--cybrowser .btn--primary}

_Can you find a layout that allows you to easily recognize patterns in the network? What about the Edge-weighted Spring Embedded Layout with the attribute ‘score’, which is the combined STRING interaction score?_

### 2.2 Discrete color mapping

Cytoscape allows you to map attributes of the nodes and edges to visual properties such as node color and edge width. Here, we will map drug target family data from the [Pharos](https://pharos.nih.gov/idg/targets) database to the node color. This data is contained in the node attribute called **target family**.

Select **Style** from the side menu in the left panel (it is between **Network** and **Filter**). Click the **◀** button to the right of the property you want to change, in this case **Fill Color**, and change **Column** from name to **(T) family**, which is the node column containing the data that you want to use. The **Mapping Type** should remain set to **Discrete Mapping**. This action will remove the rainbow coloring of the nodes and present you with a list of all the different values of the attribute that exist in the network, in this case several protein target families.

To color the proteins in a given target family, first click the field to the **right** of an attribute value, i.e. **GPCR** or **IC**, then click the ⋯ button and choose a color from the color selection dialog. You can also set the default color for all nodes that do not have a target family annotation from Pharos by clicking on the **grey square** in the first column of the **Fill Color** row.

_How many of the proteins in the network are ion channels (IC) or GPCRs?_

There are many kinases in the network. We can avoid counting them manually by creating a selection filter in the **Filter** tab (located underneath **Style**). Click the **ᐩ** button and choose **Column filter** from the drop-down menu. Then, find and select the attribute **(T) Node: family**. Write **kinase** in the text field to select all nodes with this annotation.

<!-- [Create filter for kinases](cycmd:filter create name="myfilter" json='{ "id" : "ColumnFilter", "parameters" : { "criterion" : "Kinase", "columnName" : "target::family", "predicate" : "CONTAINS"} }'){: .btn .btn--cybrowser .btn--primary}
 -->

_How many kinases are in the network?_

### 2.3 Data import

Network nodes and edges can have additional information associated with them that we can load into Cytoscape and use for visualization. We will import the data from the [text file](/assets/Francavilla2017CellRep.tsv).

To import the node attributes file into Cytoscape, go to **File → Import → Table from File** and navigate to the directory that contains the **Francavilla** table file. In the resulting dialog entitled Import Columns From Table, use the drop-down menu next to **Where to Import Table Data** to choose the option **To a Network Collection**. Next, change the **Key Column for Network** from **shared name** to **query term** and click **OK**.

[Import table](cycmd:table import url url="https://jensenlab.org/assets/Francavilla2017CellRep.tsv" keyColumnForMapping="query term" keyColumnIndex=1 startLoadRow=1){: .btn .btn--cybrowser .btn--primary}

### 2.4 Continuous color mapping

Now, we want to color the nodes according to the quantitative phosphorylation data (log ratios) between disease (EOC) and the two healthy tissues distal fallopian tube epithelium (FTE) and ovarian surface epithelium (OSE) for the most significant site for each protein. From the left panel side menu, select **Style** (it is underneath **Network**). Then click on the **◀** button to the right of the property you want to change, for example **Fill Color**. Next, set **Column** to the node column containing the data that you want to use (EOC vs FTE&OSE). Since this is a numeric value, we will use the **Continuous Mapping** as the **Mapping Type**, and set a color gradient for how abundant each protein is. The default Cytoscape color gradient blue--white--red already gives a nice visualization of the log ratio.

_Are the up-regulated nodes grouped together? Do you see any issues with the color gradient?_

To change the colors, double click on the color gradient in order to bring up the **Continuous Mapping Editor** window and edit the colors for the continuous mapping. In the mapping editor dialog, the color that will be used for the minimum value is on the left, and the maximum is on the right. Double click on the triangles on the top and sides of the gradient to change the colors. The triangles on the top represent the values at which the data will be clipped; anything above the right triangle will be set to the max value. This is useful if you have a small number of values that are significantly higher than the median. As you move the triangles and change the color, the display in the network pane will automatically update -- this is all easier to do than to explain! If at any point it does not seem to work as expected, it is easiest to just delete the mapping and start again.

_Can you improve the color mapping such that it is easier to see which nodes have a log ratio below -4 and above 4?_

### 2.5 Save session

To keep all the networks, data, and visualizations you created, you can save them as a Cytoscape session and open them at a later time point. Go to **File → Save**, choose where to save the file, give it a proper name and click the **Save** button.

## Exercise 3

In this exercise, we will focus on clustering, a common network analysis task, as well as functional enrichment within the Cytoscape stringApp environment.

### 3.1 Network clustering

Starting from the network in Exercise 3, we will use the MCL algorithm to identify clusters of tightly connected proteins within the network. To do that, press the **Cluster network (MCL)** button in the **STRING Results panel** on the right side of the network view. Keep the default **granularity parameter (inflation value)** set to **4** and click **OK** to start the clustering. The clusterMaker app will now run the algorithm and automatically create a network showing the clusters.

[Cluster network](cycmd:cluster mcl attribute=score inflation_parameter=4 showUI=true){: .btn .btn--cybrowser .btn--primary}

_How many clusters have at least 10 nodes?_

### 3.2 Subnetworks and physical interactions

We will work with the largest cluster in the network (it should be in the upper left corner). Select the nodes of this cluster by holding down the modifier key (Shift on Windows, Ctrl or Command on Mac) and then left-clicking and dragging to select multiple nodes. The nodes will turn yellow if they are selected properly. Then, create a new network by clicking on the **New Network from Selection** button and choosing the option **From Selected Nodes, All Edges** or via the menu item **File → New Network → From Selected Nodes, All Edges**.

<!-- [Select cluster](cycmd:filter create name="myfiltercluster1" json='{ "id" : "ColumnFilter", "parameters" : { "criterion" : [ 1, 1 ], "columnName" : "__mclCluster", "predicate" : "BETWEEN"} }'){: .btn .btn--cybrowser .btn--primary}
[Create new network from selection](cycmd:network create excludeEdges=false nodeList=selected source=current){: .btn .btn--cybrowser .btn--primary}
 -->

_How many nodes and edges are there in this cluster?_

The cluster is very dense and almost fully connected, i.e. it has edges representing functional associations between almost all pairs of nodes. Change the network type to physical interactions by navigating to the **Edges tab** in the **STRING Results panel** and clicking the **Change network type** button. Leave the confidence cutoff at the default value, change the network type from **full STRING network** to **physical subnetwork** using the drop-down menu, and click **OK**. To better see the new set of edges, apply a layout of your choosing, e.g. the **yFiles Organic Layout**.

_How many edges does the resulting network contain and why are there now fewer edges?_

### 3.3 Functional enrichment

Next, we will retrieve functional enrichment for the proteins in our network of the largest cluster. After making sure that no nodes are selected in the network, go to the menu **Apps → STRING Enrichment → Retrieve functional enrichment** or use the **Functional Enrichment** button in the **Nodes tab** of the **STRING Panel** on the right side. Then, select the original, not clustered network ‘String Network’ as **Background** (instead of ‘genome’) and click **OK**. A new **STRING Enrichment tab** will appear in the **Table Panel** on the bottom. It contains a table of enriched terms and corresponding information for each enrichment category. You can see which proteins are annotated with a given term by selecting the term in the **STRING Enrichment panel** and you can see the terms annotating a given node by slecting it.

[Set as STRING network](cycmd:string make string){: .btn .btn--cybrowser .btn--primary}
[Retrieve functional enrichment](cycmd:string retrieve enrichment){: .btn .btn--cybrowser .btn--primary}
[Show functional enrichment](cycmd:string show enrichment){: .btn .btn--cybrowser .btn--primary}

_How many statistically significant terms are in the table? Which is the most significant term for each of the categories GO Biological Process, GO Molecular Function, and KEGG Pathways? Hint: Look at the FDR (false discovery rate) value column and use the **Filter** button to select individual categories._

<!-- To explore only specific types of terms, e.g. GO terms, and to remove redundant terms from the table, click on the filter icon in the **Table panel** (leftmost icon). Select the three types of GO terms, enable the option to **Remove redundant terms** and set **Redundancy cutoff** to 0.2. In this way, you will see only the statistically significant GO terms that do not represent largely the same set of proteins within the network. You can see which proteins are annotated with a given term by selecting the term in the **STRING Enrichment** panel.

[Filter functional enrichment](cycmd:string filter enrichment categories="GO Process,GO Component,GO Function" overlapCutoff=0.2 removeOverlapping=true){: .btn .btn--cybrowser .btn--primary}
 -->

Next, we will visualize the top-5 enriched terms in the network using split charts, click the colorful chart icon to show the terms as the charts on the network. You can manually change the layout of the network to improve the visualization. First apply the **yFiles Organic Layout** and then scale the network to reduce the overlap of the charts using the **Layout Tools (Layout → Layout Tools**).

To save the list of enriched terms and associated p-values as a text file, go to **Apps → STRING Enrichment → Export enrichment results**.

### 3.4 Enriched publications

To retrieve a list of publications that are enriched for the proteins in the network, go to the menu **Apps → STRING Enrichment → Retrieve enriched publications** or press the **Enriched Publications** button. A new tab called **STRING Publications** will appear in the **Table Panel** on the bottom. It contains a table of enriched publications and associated information such as how many of the network proteins were mentioned in each publication.

[Retrieve enriched publications](cycmd:string retrieve publications){: .btn .btn--cybrowser .btn--primary}
[Show enriched publications](cycmd:string show publications){: .btn .btn--cybrowser .btn--primary}

_What is the title of the most recent publication?_

## Exercise 4

In this exercise, we are going to use the stringApp to query the [DISEASES](https://diseases.jensenlab.org) database for proteins associated with epithelial ovarian cancer (EOC), retrieve a STRING network for them, and explore the resulting network.

### 4.1 Disease network retrieval

Use the menu **File → Import → Network from Public Databases** and the **STRING: disease query** option from the **Data Source** drop-down menu. Insert **ovary epithelial cancer** into the **Enter disease term** field, set the **Maximum number of proteins** option to **250** and press the **Import** button. Once the network appears, go to the menu **View → Always Show Graphics Details** to see the individual nodes and edges.

[Import EOC disease network](cycmd:string disease query disease=DOID:2152 taxonID=9606 limit=250){: .btn .btn--cybrowser .btn--primary}

### 4.2 Continuous color mapping

Cytoscape allows you to map attributes of the nodes and edges to visual properties such as node color and edge width. Here, we will map the subcellular localization data for nucleus to the node color.

From the left panel side menu, select **Style** (located underneath **Network** and above **Filter**). Click on the **◀** button to the right of the property you want to change, in this case **Fill Color** and set **Column** to the node column containing the data that you want to use (**nucleus**). Since this is a numeric value, we will use the **Continuous Mapping** as the **Mapping Type**, and set a color gradient for how likely each protein is located in the nucleus. The default Cytoscape yellow--purple color gradient already gives a nice visualization of the confidence of being located in this compartment.

_Does it look like the network contains many nuclear proteins?_

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
