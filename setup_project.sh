#!/bin/bash

#Create project directory
mkdir -p bioinformatics_project

#Create subdirectories
mkdir -p bioinformatics_project/data bioinformatics_project/scripts bioinformatics_project/results

#Create the empty Python scripts
touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

#Create empty files in the data and results directories
touch bioinformatics_project/data/random_sequence.fasta
touch bioinformatics_project/results/cutsite_summary.txt

#Create a README.md file 
echo "## Bioinformatics Project" > bioinformatics_project/README.md
echo "This is a bioinformatics project for DNA sequence analysis." >> bioinformatics_project/README.md
echo "The project directory structure is as follows:" >> bioinformatics_project/README.md

#Create Project structure details into readme
echo "bioinformatics_project/" >> bioinformatics_project/README.md
echo "├── README.md" >> bioinformatics_project/README.md
echo "├── data/" >> bioinformatics_project/README.md
echo "│   └── random_sequence.fasta #Generates random fasta format dna sequence." >> bioinformatics_project/README.md>> bioinformatics_project/README.md 
echo "├── results/" >> bioinformatics_project/README.md
echo "│   └── cutsite_summary.txt    #Stores the analysis results such as cut site summaries." >> bioinformatics_project/README.md
echo "└── scripts/" >> bioinformatics_project/README.md
echo "    ├── generate_fasta.py      #Script to generate random FASTA sequences." >> bioinformatics_project/README.md
echo "    ├── dna_operations.py      #Script for performing DNA-related operations." >> bioinformatics_project/README.md
echo "    └── find_cutsites.py       #Script for finding restriction enzyme cut sites." >> bioinformatics_project/README.md


#Run the tree command to display the directory structure
echo "Project directory structure created successfully:"
tree bioinformatics_project/




