#!/bin/bash -xe

python exclusive.py --fasta-file-a Aphid-cg_S5_L001_R1_001-single.fasta  --fasta-file-b Aphid-H_S4_L001_R1_001-single.fasta --output Aphid-cg_S5_L001_R1_001-exclusive.fasta
python exclusive.py --fasta-file-a Aphid-H_S4_L001_R1_001-single.fasta  --fasta-file-b Aphid-cg_S5_L001_R1_001-single.fasta --output Aphid-H_S4_L001_R1_001-exclusive.fasta

