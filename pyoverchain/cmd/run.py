#!/usr/bin/env python3

'''pyOverChain: a python pipeline to generate chain files between different genome assemblies for LiftOver.
Github: https://github.com/billzt/pyOverChain
'''

__author__ = 'Tao Zhu'
__copyright__ = 'Copyright 2020'
__license__ = 'GPL'
__version__ = '0.1'
__email__ = 'taozhu@mail.bnu.edu.cn'
__status__ = 'Development'

import argparse
import re
import sys
import shutil
import os

from distutils.version import LooseVersion
from operator import itemgetter

from pyoverchain.core import version
from pyoverchain.core import pipeline_multiple

def make_args():
    parser = argparse.ArgumentParser(description='pyOverChain: a python pipeline to generate \
        chain files between different genome assemblies for LiftOver.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+version.get())
    parser.add_argument('old_genome', help='Old genome file in FASTA format')
    parser.add_argument('new_genome', help='New genome file in FASTA format')
    parser.add_argument('chr_map', help='A chromosome-mapping-file in TSV format', type=argparse.FileType('r'))
    parser.add_argument('-n', '--num-chromosome-tasks', help='number of parallel tasks to run different \
        chromosomes', type=int, default=2)
    parser.add_argument('-p', '--num-threads-pblat', help='number of threads for pblat. \
        Only useful if pblat were available', type=int, default=2)
    parser.add_argument('--disable-progress', help='Disable progress displaying. Useful if you want to \
        run it in background', action='store_true')
    args = parser.parse_args()
    return args

def check_environments():
    for i in ['samtools', 'faSplit', 'liftUp', 'axtChain', 'chainMergeSort', 'chainNet', 'netChainSubset']:
        if shutil.which(i) is None:
            raise Exception(f'No {i} detected in your system')
    blat_binary = ''
    if shutil.which('pblat') is not None:
        blat_binary = 'pblat'
    elif shutil.which('blat') is not None:
        blat_binary = 'blat'
    if blat_binary=='':
        raise Exception(f'Neither blat nor pblat detected in your system')
    return blat_binary


def main():
    args = make_args()
    blat_binary = check_environments()

    # chr_map
    chr_map = {}
    for line in args.chr_map:
        if line.startswith('#'):
            continue
        (chr_old, chr_new) = line.strip().split()
        chr_map[chr_old] = chr_new

    # make directories
    os.system("rm -rf pyOverChainTmp.*")
    os.system(f"mkdir pyOverChainTmp.log pyOverChainTmp.NewGenome.axtChain.{args.new_genome} \
        pyOverChainTmp.NewGenome.blat.{args.new_genome} pyOverChainTmp.NewGenome.chain.{args.new_genome} \
            pyOverChainTmp.NewGenome.{args.new_genome} pyOverChainTmp.NewGenome.lift.{args.new_genome} \
                pyOverChainTmp.NewGenome.liftUp.{args.new_genome} pyOverChainTmp.NewGenome.net.{args.new_genome} \
                    pyOverChainTmp.NewGenome.over.{args.new_genome} pyOverChainTmp.OldGenome.{args.old_genome}")

    # run
    pipeline_multiple.run(file_old=args.old_genome, file_new=args.new_genome, chr_map=chr_map, \
        num_parallel_chr=args.num_chromosome_tasks, num_thread_blat=args.num_threads_pblat, \
            binary=blat_binary, noprogress=args.disable_progress)
    
    # remove directories
    os.system("rm -rf pyOverChainTmp.*")

if __name__ == "__main__":
    main()