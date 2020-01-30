import os
import sys
import datetime

def run(file_old:str, file_new:str, chr_old:str, chr_new:str, logfile='tmp.log'):
    os.system(f'axtChain -linearGap=medium -psl pyChainTmp.NewGenome.liftUp.{file_new}/{chr_new}.psl \
        -faT pyChainTmp.OldGenome.{file_old}/{chr_old}.fa \
            -faQ pyChainTmp.NewGenome.{file_new}/{chr_new}.fa \
                pyChainTmp.NewGenome.axtChain.{file_new}/{chr_new}.chain >>{logfile} 2>&1')

if __name__ == "__main__":
    run(file_old='ISR.fa', file_new='JGI.fa', chr_old='D03', chr_new='D03')