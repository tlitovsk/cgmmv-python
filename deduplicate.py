'''
Program to search for sequnces in blast
'''

import argparse
from Bio import SeqIO
from Bio.SeqUtils.CheckSum import seguid
#from progress.counter import Counter


def is_inside(a, b):
    if b.seq.find(a.seq) is not -1:
        return True
    return False


def main():
    parser = argparse.ArgumentParser(
        description='Searches for sequnce in sequence')
    parser.add_argument(
        '--fastq-file',
        type=str,
        required=True,
        dest='fastq_file',
        help='input')

    '''
    parser.add_argument(
        '--fastq-out-file',
        type=str,
        required=True,
        dest='fastq_output_file',
        help='output')
    '''

    args = parser.parse_args()
    records = list(SeqIO.parse(args.fastq_file, 'fastq'))
    records.sort(cmp=lambda x, y: cmp(len(x), len(y)))
    result = dict()

    while True:
        tested_record = records[0]
        counts = 0
        leftover = list()
        for record in records:
            if is_inside(tested_record, record):
                counts = counts + 1
            else:
                leftover.append(record)

        records = leftover
        print "Count for {}:{}".format(tested_record.seq, counts)

        if len(leftover) is 0:
            break

if __name__ == "__main__":
    main()
