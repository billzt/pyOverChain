import multiprocessing as mp
import time
import datetime
import sys
import os

from glob import glob

import progressbar

from pyoverchain.core import pipeline_single, chr_separation

def run(file_old:str, file_new:str, chr_map:dict, num_parallel_chr:int, \
    num_thread_blat:int, binary:str, noprogress=False):
    # separate chromosomes
    chr_separation.run(file_old=file_old, file_new=file_new, chr_map=chr_map)

    # distribute tasks
    print(f'[pyoverchain:{datetime.datetime.now()}] Begin building chains by {num_parallel_chr} parallel tasks...', \
        file=sys.stderr)
    pool = mp.Pool(processes=num_parallel_chr)
    multi_res = []
    for (chr_old, chr_new) in chr_map.items():
        args = {
            'file_old': file_old,
            'file_new': file_new, 
            'chr_old': chr_old, 
            'chr_new': chr_new, 
            'cpu': num_thread_blat, 
            'binary': binary
        }
        multi_res.append(pool.apply_async(pipeline_single.run, (args,)))
    
    # monitor
    if noprogress is False:
        widgets = ['Running: ', progressbar.Counter(),\
                    ' chromosomes Finished', ' (', progressbar.Percentage(), ')', \
                        progressbar.Bar(), progressbar.ETA()]
        bar = progressbar.ProgressBar(widgets=widgets, max_value=len(chr_map)).start()
    while True:
        complete_count = sum([1 for x in multi_res if x.ready()])
        if complete_count == len(chr_map):
            if noprogress is False:
                bar.finish()
            break
        if noprogress is False:
            bar.update(complete_count)
        time.sleep(1)
    
    # Combine
    print(f'[pyoverchain:{datetime.datetime.now()}] Combining Results...', file=sys.stderr)
    chain_files = ' '.join(glob(f'pyOverChainTmp.NewGenome.over.{file_new}/*.chain'))
    os.system(f'cat {chain_files} >{file_old}.to.{file_new}.over.chain')



if __name__ == "__main__":
    run(file_old='ISR.fa', file_new='JGI.fa', chr_map={'D03':'D03', 'D02':'D02'}, \
        num_parallel_chr=2, num_thread_blat=50, binary='pblat')