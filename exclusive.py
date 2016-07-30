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


def get_exclusive(set_a, set_b):
    disp = Counter("Records processed:")
    for record_a in set_a:
        found = False
        for record_b in set_b:
            if is_equal(record_a, record_b):
                found = True
                break

        if not found:
            yield record_a
        else:
            found = False

        disp.next()


def main():
    parser = argparse.ArgumentParser(
        description='Searches for sequnce in sequence')
    parser.add_argument(
        '--fasta-file-a',
        type=str,
        required=True,
        dest='fasta_file_a',
        help='input A')

    parser.add_argument(
        '--fasta-file-b',
        type=str,
        required=True,
        dest='fasta_file_b',
        help='input B')

    parser.add_argument(
        '--output',
        type=str,
        required=True,
        dest='output',
        help='exclusibve records to a')

    args = parser.parse_args()
    set_a = list(SeqIO.parse(args.fasta_file_a, 'fasta'))
    set_b = list(SeqIO.parse(args.fasta_file_b, 'fasta'))
    SeqIO.write(get_exclusive(set_a, set_b), args.output, 'fasta')

if __name__ == "__main__":
    main()
