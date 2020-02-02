import datetime

from pyoverchain.core import axtchain, blat, chainMergeSort, chainNet, faSplit, liftUp, netChainSubset

def run(args:dict):
    logfile = 'pyOverChainTmp.log/'+args['file_old']\
        +args['chr_old']+'-to-'+args['file_new']+args['chr_new']+'.log'

    flog = open(logfile, mode='w')

    print(f'[pyoverchain:{datetime.datetime.now()}] Begin faSplit...', file=flog, flush=True)
    faSplit.run(file_new=args['file_new'], chr_new=args['chr_new'], logfile=logfile)

    print(f'[pyoverchain:{datetime.datetime.now()}] Begin BLAT...', file=flog, flush=True)
    blat.run(file_old=args['file_old'], file_new=args['file_new'], \
        chr_old=args['chr_old'], chr_new=args['chr_new'], cpu=args['cpu'], binary=args['binary'], logfile=logfile)
    
    print(f'[pyoverchain:{datetime.datetime.now()}] Begin liftUp...', file=flog, flush=True)
    liftUp.run(file_new=args['file_new'], chr_new=args['chr_new'], logfile=logfile)

    print(f'[pyoverchain:{datetime.datetime.now()}] Begin axtchain...', file=flog, flush=True)
    axtchain.run(file_old=args['file_old'], file_new=args['file_new'], \
        chr_old=args['chr_old'], chr_new=args['chr_new'], logfile=logfile)
    
    print(f'[pyoverchain:{datetime.datetime.now()}] Begin chainMergeSort...', file=flog, flush=True)
    chainMergeSort.run(file_new=args['file_new'], chr_new=args['chr_new'], logfile=logfile)

    print(f'[pyoverchain:{datetime.datetime.now()}] Begin chainNet...', file=flog, flush=True)
    chainNet.run(file_old=args['file_old'], file_new=args['file_new'], \
        chr_new=args['chr_new'], logfile=logfile)

    print(f'[pyoverchain:{datetime.datetime.now()}] Begin netChainSubset...', file=flog, flush=True)
    netChainSubset.run(file_new=args['file_new'], chr_new=args['chr_new'], logfile=logfile)
    

if __name__ == "__main__":
    run({
        'file_old': 'ISR.fa',
        'file_new': 'JGI.fa', 
        'chr_old': 'D03', 
        'chr_new': 'D03', 
        'cpu': 50, 
        'binary': 'pblat'
    })