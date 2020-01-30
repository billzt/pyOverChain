import os
import sys
import datetime

def run(file_new:str, chr_new:str, logfile='tmp.log'):
    os.system(f'chainMergeSort pyChainTmp.NewGenome.axtChain.{file_new}/{chr_new}.chain \
         | chainSplit pyChainTmp.NewGenome.chain.{file_new} stdin >>{logfile} 2>&1')

if __name__ == "__main__":
    run(file_new='JGI.fa',chr_new='D03')