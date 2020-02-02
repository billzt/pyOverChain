import os
import sys
import datetime

def run(file_new:str, chr_new:str, logfile='tmp.log'):
    os.system(f'liftUp -pslQ pyOverChainTmp.NewGenome.liftUp.{file_new}/{chr_new}.psl \
        pyOverChainTmp.NewGenome.lift.{file_new}/{chr_new}.lft warn \
            pyOverChainTmp.NewGenome.blat.{file_new}/{chr_new}.psl >>{logfile} 2>&1')

if __name__ == "__main__":
    run(file_new='JGI.fa',chr_new='D03')