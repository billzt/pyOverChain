import os
import sys
import datetime

def run(file_old:str, file_new:str, chr_old:str, chr_new:str,  cpu=1, binary='blat', logfile='tmp.log'):
    if binary=='pblat':
        cmd = f'pblat pyOverChainTmp.OldGenome.{file_old}/{chr_old}.fa \
            pyOverChainTmp.NewGenome.{file_new}/{chr_new}.split.fa \
                pyOverChainTmp.NewGenome.blat.{file_new}/{chr_new}.psl -threads={cpu} \
                    -tileSize=12 -minScore=100 -minIdentity=98 -fastMap'
    else:
        cmd = f'blat pyOverChainTmp.OldGenome.{file_old}/{chr_old}.fa \
            pyOverChainTmp.NewGenome.{file_new}/{chr_new}.split.fa \
                pyOverChainTmp.NewGenome.blat.{file_new}/{chr_new}.psl \
                    -tileSize=12 -minScore=100 -minIdentity=98 -fastMap'
    os.system(cmd+f' >>{logfile} 2>&1')

if __name__ == "__main__":
    run(file_old='ISR.fa', file_new='JGI.fa', chr_old='D03', chr_new='D03', cpu=50, binary='pblat')