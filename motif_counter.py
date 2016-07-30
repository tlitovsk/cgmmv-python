'''
Program to search for sequnces in blast
'''

import argparse
from Bio import SeqIO
import xml.etree.ElementTree as ET


def get_motif_string(element):
    seq = ""
    for matrix in element.findall('probabilities/alphabet_matrix/alphabet_array'):
        max_probability = 0.0
        selected_letter = ''
        for letter in matrix.findall('value'):
            if float(letter.text) > max_probability:
                max_probability = float(letter.text)
                selected_letter = letter.attrib['letter_id']
        seq = seq + selected_letter

    return seq


def count_seq(seq, file):
    records = SeqIO.parse(file, 'fastq')
    counter = 0
    for record in records:
        if record.seq.find(seq) is not -1:
            counter = counter + 1
    return counter


def main():
    parser = argparse.ArgumentParser(
        description='Searches for sequnce in sequence')
    parser.add_argument(
        '--motif',
        type=str,
        required=True,
        dest='motif',
        help='the file with motifes we want to count')

    parser.add_argument(
        '--fastq-file',
        type=str,
        required=True,
        dest='fastq_file',
        help='the file we searching motifs in')

    parser.add_argument(
        '--min-motif-length',
        type=int,
        required=True,
        dest='min_length',
        help='the minimum motif length in seq')

    args = parser.parse_args()

    tree = ET.parse(args.motif)
    root = tree.getroot()

    #lets get to motifs tree

    for motif in root.findall("./motifs/motif"):
        if int(motif.attrib['width']) >= args.min_length:
            seq = get_motif_string(motif)
            counter = count_seq(seq, args.fastq_file)
            print motif.attrib['id'] + ":" + seq + " Counted:" + str(counter)

if __name__ == "__main__":
    main()
