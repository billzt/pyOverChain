# pyChain
a python pipeline to generate chain files between different genome assemblies for [LiftOver](https://genome.ucsc.edu/cgi-bin/hgLiftOver).

## External Dependencies
This pipeline can only be used under Linux.
These softwares must be in your system PATH
* [Samtools](https://www.htslib.org/).
* [BLAT](http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/) or [pblat](https://github.com/icebert/pblat) (**preferred**)
* [UCSC tool kits](http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/), including:
    * liftUp
    * axtChain
    * chainMergeSort
    * chainSplit
    * chainNet
    * netChainSubset

## Installation
### Via pip (release only)
```
pip3 install pyoverchain
```

### Via Github
```
git clone https://github.com/billzt/pyOverChain.git
cd pyOverChain
python3 setup.py install
```

## Usage
```
pyoverchain [-h] [-v] [-n NUM_CHROMOSOME_TASKS] [-p NUM_THREADS_PBLAT]
               [--disable-progress]
               old_genome new_genome chr_map

positional arguments:
  old_genome            Old genome file in FASTA format
  new_genome            New genome file in FASTA format
  chr_map               A chromosome-mapping-file in TSV format

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -n NUM_CHROMOSOME_TASKS, --num-chromosome-tasks NUM_CHROMOSOME_TASKS
                        number of parallel tasks to run different chromosomes
                        (default: 2)
  -p NUM_THREADS_PBLAT, --num-threads-pblat NUM_THREADS_PBLAT
                        number of threads for pblat. Only useful if pblat were
                        available (default: 2)
  --disable-progress    Disable progress displaying. Useful if you want to run
                        it in background (default: False)
```

## chromosome-mapping-file
It is a plain text file in TSV format showing the relationship between genome assemblies. Corresponding
chromosomes usually have the same or similar names. However, this is not always the case.
```
#old_genome_chr new_genome_chr
chr1    chr1
chr2    chr2
chr3    chr3
```

## Some useful documents
* [Document from kent](https://hgwdev.gi.ucsc.edu/~kent/src/unzipped/hg/doc/liftOver.txt)
* [Minimal Steps For LiftOver](http://genomewiki.ucsc.edu/index.php/Minimal_Steps_For_LiftOver)

## Warning
This pipeline can only liftOver ***different assemblies*** of ***the same species***.
