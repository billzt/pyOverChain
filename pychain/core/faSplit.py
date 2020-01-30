import os
import sys
import datetime

def run(file_new:str, chr_new:str, logfile='tmp.log'):
    #print(f'pyChain [{datetime.datetime.now()}]: Begin splitting new genomes: {chr_new} in {file_new}...', file=sys.stderr)

    os.system(f'faSplit -lift=pyChainTmp.NewGenome.lift.{file_new}/{chr_new}.lft \
        -oneFile size pyChainTmp.NewGenome.{file_new}/{chr_new}.fa 3000 \
            pyChainTmp.NewGenome.{file_new}/{chr_new}.split >>{logfile} 2>&1')

if __name__ == "__main__":
    run(file_new='JGI.fa',chr_new='D03')