import argparse
from sequence_generator import (genome_sequence_generator,
                                random_sequence_generator)
from elv import match                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
from fasta_dict import fasta_func
from fastq_dict import fastq_func


def tree_runner(fasta_dict, fastq_dict):
    l = []
    for p_key, p_val in fastq_dict.items():
        for x_key, x_val in fasta_dict.items():
            matches = match(p_val, x_val)
            for i in matches:
                l.append('\t'.join([p_key, x_key, str(i+1), f'{str(len(p_val))}M', p_val]))
    
    return '\n'.join(l)


def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching using a suffix tree")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()

    #translate files into dicts
    fasta_dict = fasta_func(args.genome)
    fastq_dict = fastq_func(args.reads)

    print(tree_runner(fasta_dict, fastq_dict))




if __name__ == '__main__':
    main()
