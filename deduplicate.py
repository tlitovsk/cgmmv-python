'''
Program to search for sequnces in blast
'''

import argparse
from Bio import SeqIO
from Bio.SeqUtils.CheckSum import seguid
from progress.counter import Counter


def is_equal(a, b):
    if seguid(a.seq) == seguid(b.seq):
        return True
    return False


def get_deduplicated(records):
    disp = Counter("Records processed:")
    tested_record = records[0]
    for record in records:
        if not is_equal(tested_record, record):
            yield tested_record
            tested_record = record
        disp.next()


def main():
    parser = argparse.ArgumentParser(
        description='Searches for sequnce in sequence')
    parser.add_argument(
        '--fastq-file',
        type=str,
        required=True,
        dest='fastq_file',
        help='input')

    parser.add_argument(
        '--fasta-out-file',
        type=str,
        required=True,
        dest='fasta_output_file',
        help='output')

    args = parser.parse_args()
    records = list(SeqIO.parse(args.fastq_file, 'fastq'))
    sorted_rec = sorted(records, key=lambda x: seguid(x.seq))
    SeqIO.write(get_deduplicated(sorted_rec), args.fasta_output_file, 'fasta')

if __name__ == "__main__":
    main()
