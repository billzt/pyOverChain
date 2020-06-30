import os
import sys
import datetime

def run(file_new:str, chr_new:str, file_old:str, chr_old:str, logfile='tmp.log'):
    os.system(f'netChainSubset pyOverChainTmp.NewGenome.net.{file_new}/{chr_new}.net \
         pyOverChainTmp.OldGenome.chain.{file_old}/{chr_old}.chain \
              pyOverChainTmp.NewGenome.over.{file_new}/{chr_new}.chain >>{logfile} 2>&1')

if __name__ == "__main__":
    run(file_new='JGI.fa',chr_new='D03', file_old='ISR.fa', chr_old='D03')