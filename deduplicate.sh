#!/bin/bash -xe

python deduplicate.py --fastq-file Aphid-cg_S5_L001_R1_001-filtered.fastq --fasta-out-file Aphid-cg_S5_L001_R1_001-single.fasta
python deduplicate.py --fastq-file Aphid-H_S4_L001_R1_001-filtered.fastq --fasta-out-file Aphid-H_S4_L001_R1_001-single.fasta
