# Acetylcholinesterase_Bioinfomatics



This repository contains the code and data for the Acetylcholinesterase Bioinformatics project, which is a part of a series on Computational Drug Discovery.

## Bioinformatics Project - Computational Drug Discovery [Part 1]
*****
ChEMBL Database
The ChEMBL Database is a database that contains curated bioactivity data of more than 2 million compounds. It is compiled from more than 76,000 documents, 1.2 million assays and the data spans 13,000 targets and 1,800 cells and 33,000 indications. [Data as of March 25, 2020; ChEMBL version 26].

## Bioinformatics Project - Computational Drug Discovery [Part 2]

Install conda and rdkit
RDKit is a popular open-source cheminformatics software toolkit that is widely used by chemists, biologists, and other researchers in drug discovery, materials science, and other areas of chemistry. It provides a set of powerful and efficient tools for working with molecular structures, including molecules, reactions, and fragments. RDKit is a powerful and versatile toolkit that provides a range of tools and capabilities for chemists and other researchers working with molecular structures. Its ease of use and broad range of applications have made it a popular choice for cheminformatics and drug discovery research.

Interpretation of Statistical Results

Box Plots
pIC50 values

Taking a look at pIC50 values, the actives and inactives displayed statistically significant difference, which is to be expected since threshold values (IC50 < 1,000 nM = Actives while IC50 > 10,000 nM = Inactives, corresponding to pIC50 > 6 = Actives and pIC50 < 5 = Inactives) were used to define actives and inactives.

### Lipinski's descriptors

All of the 4 Lipinski's descriptors exhibited statistically significant difference between the actives and inactives.

## Bioinformatics Project - Computational Drug Discovery [Part 3]

Descriptor Calculation and Dataset Preparation
In Part 3, we will be calculating molecular descriptors that are essentially quantitative description of the compounds in the dataset. Finally, we will be preparing this into a dataset for subsequent model building in Part 4.
Load bioactivity data

Download the curated ChEMBL bioactivity data that has been pre-processed from Parts 1 and 2 of this Bioinformatics Project series. Here we will be using the acetylcholinesterase_bioactivity_data_with_descipator.csv file that essentially contain the pIC50 values that we will be using for building a regression model.
