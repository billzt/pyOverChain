import os
import sys
import datetime

def run(file_new:str, chr_new:str, file_old:str, logfile='tmp.log'):
    os.system(f'cut -f 1,2 {file_old}.fai >pyOverChainTmp.OldGenome.{file_old}/chr.sizes')
    os.system(f'cut -f 1,2 {file_new}.fai >pyOverChainTmp.NewGenome.{file_new}/chr.sizes')
    os.system(f'chainNet pyOverChainTmp.NewGenome.chain.{file_new}/{chr_new}.chain \
        pyOverChainTmp.OldGenome.{file_old}/chr.sizes pyOverChainTmp.NewGenome.{file_new}/chr.sizes \
            pyOverChainTmp.NewGenome.net.{file_new}/{chr_new}.net /dev/null >>{logfile} 2>&1')

if __name__ == "__main__":
    run(file_new='JGI.fa',chr_new='D03', file_old='ISR.fa')