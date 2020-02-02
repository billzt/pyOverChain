import os
import sys
import datetime

def run(file_new:str, chr_new:str, logfile='tmp.log'):
    os.system(f'netChainSubset pyOverChainTmp.NewGenome.net.{file_new}/{chr_new}.net \
         pyOverChainTmp.NewGenome.chain.{file_new}/{chr_new}.chain \
              pyOverChainTmp.NewGenome.over.{file_new}/{chr_new}.chain >>{logfile} 2>&1')

if __name__ == "__main__":
    run(file_new='JGI.fa',chr_new='D03')