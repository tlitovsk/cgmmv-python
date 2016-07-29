#!/bin/bash -xe

python deduplicate.py --fastq-file Aphid-cg_S5_L001_R1_001-filtered.fastq
python deduplicate.py --fastq-file Aphid-H_S4_L001_R1_001-filtered.fastq
