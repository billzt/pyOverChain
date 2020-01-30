mkdir axtchain blat.psl chain liftUp.psl net over
faSplit -lift=lift/D03.lft -oneFile size query/D03.ISR.fa 3000 split/D03.split
blat D03.JGI.fa split/D03.split.fa split/D03.split.fa.psl -tileSize=12 -minScore=100 -minIdentity=98 -fastMap &
liftUp -pslQ liftUp.psl/D03.psl lift/D03.lft warn blat.psl/D03.psl
axtChain -linearGap=medium -psl liftUp.psl/D03.psl -faT D03.JGI.fa -faQ D03.ISR.fa axtchain/D03.chain
chainMergeSort axtchain/D03.chain | chainSplit chain stdin
chainNet chain/D03.chain D03.JGI.fa.fai D03.ISR.fa.fai net/D03.net /dev/null
netChainSubset net/D03.net chain/D03.chain over/D03.chain
