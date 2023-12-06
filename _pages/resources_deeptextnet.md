---
title: DeepTextNet 
layout: single
permalink: /resources/deeptextnet/
sidebar:
  nav: "deeptextnet"
---

# Results produced by DeepTextNet

This project is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Sklodowska-Curie (grant number: 101023676)

![Photo of EU flag](/assets/complextome/EUflag.jpg)  

## Publications and corpora

* Publication in Oxford Bioinformatics: [S1000: A better taxonomic name corpus for biomedical information extraction](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btad369/7192170)
* Preprint for ComplexTome and related resources: [STRING-ing together protein complexes: extracting physical protein interactions from the literature]()
* Preprint for the Automatic Blocklist generation paper: [Improving dictionary-based named entity recognition with deep learning]()

* [The S1000 Corpus](/assets/s1000/S1000-corpus.tar.gz) in [BRAT standoff format](https://brat.nlplab.org/standoff.html)
* [The ComplexTome Corpus](/assets/complextome/ComplexTome.tar.gz) in BRAT standoff format

## Datasets

* The [Zenodo](https://doi.org/10.5281/zenodo.7064902) project related to S1000 that contains: 
  * The S1000 corpus split in training, development and test sets in BRAT and CoNLL formats
  * The guidelines used during annotation of the corpus (also available as an annodoc [here](https://katnastou.github.io/s1000-corpus-annotation-guidelines/))
  * the dictionary used by [Jensenlab tagger](https://github.com/larsjuhljensen/tagger)
  * results from large scale tagging with the Jensenlab tagger 
  * the model used for the large scale run of the transformer-based method and
  * results from large scale tagging with the transformer-based method

* The [Zenodo](https://doi.org/10.5281/zenodo.8139717) project related to ComplexTome contains:
  * The Complextome corpus in BRAT format. The corpus is provided in two different directory organizations. The directory "splits" has the corpus split based on the train/dev/test used for the training of the relation extraction system, and the "data_source" directory has the corpus split based on the source of the data as described in the Methods section of the manuscript. The annotation guidelines along with the annotation configuration files for BRAT are provided in the root directory.
  * The trigger word corpus in BRAT format. The corpus is split in devel and test set. The annotation guidelines for trigger word detection are at the bottom of the relation annotation guidelines provided above.
  * The dictionary used by [Jensenlab tagger](https://github.com/larsjuhljensen/tagger)
  * Tagger output: we filter the results of the tagger run down to gene/protein hits, and documents with more than 1 hit (since we are doing relation extraction) before feeding it to our RE system. The filtered output is available in tagger_matches_ggp_only_gt_1_hit.tsv.gz
  * Relation extraction system input: combined_input_for_re.tar.gz: these are the directories with all the .ann and .txt files used as input for the large scale execution of the relation extraction pipeline. The files are generated from the tagger tsv output (see above, tagger_matches_ggp_only_gt_1_hit.tsv.gz) using the tagger2standoff.py script from the string-db-tools repository.
  * Relation extraction models: The TensorFlow model used for large-scale relation extraction for STRING v12 is at relation_extraction_string_v12_best_model.tar.gz, while the PyTorch model used to do the relation extraction for trigger word detection is at relation_extraction_for_trigger_detection_best_model.tar.gz
  * Relation extraction system output: large_scale_relation_extraction_results.tar.gz: this is the output of the relation extraction system, which includes both negative and positive predictions. The file has 5 columns: PMID, Entity BRAT ID1, Entity BRAT ID2, prediction (positive or negative) and a list of the positive and negative score coming from the relation extraction model. E.g.: 10092099 T1 T2 neg [1.0, 5.017947320683225e-13]
  * Trigger word detection system input: combined_input_for_triggers.tar.gz these are the directories with all the .ann and .txt files used as input for the large scale execution of the trigger word detection system. These are only pairs predicted as positive from the relation extraction system's large scale predictions. 
  * Trigger word detection system output: trigger_word_model_predictions.tar.gz contains the output of the large scale execution pipeline, with 9 columns: PubMed id, Entity ID1, Entity ID2, Negative logit for complex formation relationship, Positive logit for complex formation relationship, trigger score, start offset, end offset, trigger word match.


* The [Zenodo](https://doi.org/10.5281/zenodo.10008720) project related to blocklist generation contains:
  * all the dictionary files used for the tagger runs for all Jensenlab resources (including STRINGv12). It also contains files only relevant for this work, namely: curated_local.tsv & curated_global.tsv which are used for running tagger only with curated blocklists, blacklist_terms_over_10M.txt & blacklist_terms_over_10M+auto_only_list.txt which are used for the automatic blocklist runs only, and empty_global.tsv which is used for the run without blocklists and regex.
  * A version of the Jensenlab tagger with the tagger_core.h header updated so as not to use a regex to block things. This version of the tagger has been used only for the no-blocklist run of the paper. I
  * A small dataset with 125,000 training and 62,500 development examples used to perform a grid search to detect the best set of hyperparameters
  * A large dataset of 12.5 million training and 62,500 testing examples to train the model used for prediction with the set of best hyperparameters identified above 
  * A TensorFlow model fine-tuned on the large dataset (12.5M) that is used for all the prediction runs. The model is finetuned starting from the BioBERT base v1.1 model. 
  * The combined automatically generated and manually curated blocklist used for the curated+auto runs in the paper. This is the list currently used for the tagger runs for all Jensenlab resources
  * The manually curated blocklist used for the curated_only runs in the paper
  * The automatically generated blocklist used for the auto_only runs in the paper


* The input documents for the large scale runs with:
  * Jensenlab tagger are hosted [here](https://a3s.fi/s1000/PubMed-input.tar.gz) and [here](https://a3s.fi/s1000/PMC-OA-input.tar.gz)
  * the transformer-based method are hosted [here](https://a3s.fi/s1000/database_documents.tsv.gz)
_(Note: the pre-processed input documents are the same, the difference is in the document format for the two methods)_

## Code

* Useful scripts to reproduce the results presented in the S1000 publication can be found in this [Github repo](https://zenodo.org/record/7650251#.Y--QPrTMJR4)
* The codebase for the transformer-based NER tagger can be found [here](https://zenodo.org/record/8034112) and the codebase used for the large scale run [here](https://zenodo.org/record/8034152)
* The codebase for the entity type classification system can be found [here](https://github.com/katnastou/BioBERT-based-entity-type-classifier)
* The codebase for the relation extraction and trigger word detection system can be found [here](https://github.com/farmeh/STRINGDB_cf_extraction)


