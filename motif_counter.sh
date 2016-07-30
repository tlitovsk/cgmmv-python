#!/bin/bash -xe

#python motif_counter.py --fastq-file Aphid-cg_S5_L001_R1_001.fastq  --motif Aphid-cg_S5_L001_R1_001-meme.xml --min-motif-length 18
python motif_counter.py --fastq-file Aphid-H_S4_L001_R1_001.fastq  --motif Aphid-H_S4_L001_R1_001-meme.xml --min-motif-length 16

