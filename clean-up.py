'''
Program to search for sequnces in blast
'''

import argparse
from Bio import SeqIO
from progress.counter import Counter


def trim_adaptor(record, adaptor):
    """Trims perfect adaptor sequences, checks read length.
       Returns the the trimmed record or none
    """
    len_adaptor = len(adaptor)
    if record is not None:
        index = record.seq.find(adaptor)
        if index is not -1:
            #adaptor not found, so won't trim
            return record[index+len_adaptor:]
    return None


def validate_quality(record, quality):
    """ Check the record for minimum quality value
    """
    if record is not None:
        if min(record.letter_annotations["phred_quality"]) >= quality:
            return record
    return None


def validate_size(record, min, max):
    """ Check the record for minimum quality value
    """
    if record is not None:
        len_record = len(record.seq)
        if min <= len_record <= max:
            return record
    return None


def main():
    parser = argparse.ArgumentParser(
        description='Searches for sequnce in the blast gen e database')
    parser.add_argument(
        '--fastq-file',
        type=str,
        required=True,
        dest='fastq_file',
        help='input')

    parser.add_argument(
        '--fastq-out-file',
        type=str,
        required=True,
        dest='fastq_output_file',
        help='output')

    parser.add_argument(
        '--min-quality',
        type=int,
        required=True,
        dest='quality',
        help='minimum quality required')

    parser.add_argument(
        '--min-size',
        type=int,
        required=True,
        dest='min_size',
        help='minimum size required')

    parser.add_argument(
        '--max-size',
        type=int,
        required=True,
        dest='max_size',
        help='maximum size allowed')

    parser.add_argument(
        '--adaptor',
        type=str,
        required=True,
        dest='adaptor',
        help='adaptor')

    args = parser.parse_args()
    records = SeqIO.parse(args.fastq_file, 'fastq')
    out = list()
    disp = Counter("Records processed:")

    for record in records:
        record = validate_quality(record, args.quality)
        record = trim_adaptor(record, args.adaptor)
        record = validate_size(record, args.min_size, args.max_size)
        if record is not None:
            out.append(record)
        disp.next()

    SeqIO.write(out, args.fastq_output_file, 'fastq')


if __name__ == "__main__":
    main()
