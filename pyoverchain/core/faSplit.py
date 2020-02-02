import os
import sys
import datetime

def run(file_new:str, chr_new:str, logfile='tmp.log'):

    os.system(f'faSplit -lift=pyOverChainTmp.NewGenome.lift.{file_new}/{chr_new}.lft \
        -oneFile size pyOverChainTmp.NewGenome.{file_new}/{chr_new}.fa 3000 \
            pyOverChainTmp.NewGenome.{file_new}/{chr_new}.split >>{logfile} 2>&1')

if __name__ == "__main__":
    run(file_new='JGI.fa',chr_new='D03')