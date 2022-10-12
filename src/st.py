import argparse
from sequence_generator import (genome_sequence_generator,
                                random_sequence_generator)
from elv import match
from fasta_dict import fasta_func
from fastq_dict import fastq_func


def tree_runner(fasta_dict, fastq_dict):
    print('test1')
    print(fastq_dict)
    print(fasta_dict)
    l = []
    for p_key, p_val in fastq_dict.items():
        print('test2')
        for x_key, x_val in fasta_dict.items():
            print('test3')
            matches = match(p_val, x_val)
            for i in matches:
                l.append('\t'.join([p_key, x_key, str(i), f'{str(len(p_val))}M', p_val]))
    
    return '\n'.join(l)


def main():
    # argparser = argparse.ArgumentParser(
    #     description="Exact matching using a suffix tree")
    # argparser.add_argument("genome", type=argparse.FileType('r'))
    # argparser.add_argument("reads", type=argparse.FileType('r'))
    # args = argparser.parse_args()
    # print(f"Find every reads in {args.reads.name} " +
    #       f"in genome {args.genome.name}")

    # #translate files into dicts
    # fasta_dict = fasta_func(args.genome)
    # fastq_dict = fastq_func(args.reads)

    # print(tree_runner(fasta_dict, fastq_dict))



    a1_fastq = fastq_func(random_sequence_generator(1, 0, 'fastq', 'a1_fastq', True))
    a10_fasta = fasta_func(random_sequence_generator(10, 0, 'fasta', 'a10_fasta', True))
    print('a')
    print(tree_runner(a10_fasta, a1_fastq))
    print('b')


if __name__ == '__main__':
    main()
