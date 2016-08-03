#!/bin/bash -xe

python clean-up.py --fastq-file Aphid-cg_S5_L001_R1_001.fastq  --fastq-out-file Aphid-cg_S5_L001_R1_001-filtered.fastq --min-quality=20 --min-size=18 --max-size=25 --adaptor=TGGAATTC
python clean-up.py --fastq-file Aphid-H_S4_L001_R1_001.fastq  --fastq-out-file Aphid-H_S4_L001_R1_001-filtered.fastq --min-quality=20 --min-size=18 --max-size=25 --adaptor=TGGAATTC
