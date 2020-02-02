import os
import sys
import datetime

def run(file_old:str, file_new:str, chr_map:dict):
    for (chr_old, chr_new) in chr_map.items():
        print(f'[pyoverchain:{datetime.datetime.now()}] Begin separating {chr_old} from {file_old}...', file=sys.stderr)
        os.system(f'samtools faidx {file_old} {chr_old} >pyOverChainTmp.OldGenome.{file_old}/{chr_old}.fa')

        print(f'[pyoverchain:{datetime.datetime.now()}] Begin separating {chr_new} from {file_new}...', file=sys.stderr)
        os.system(f'samtools faidx {file_new} {chr_new} >pyOverChainTmp.NewGenome.{file_new}/{chr_new}.fa')

if __name__ == "__main__":
    run(file_old='ISR.fa', file_new='JGI.fa', chr_map={'D03':'D03'})
