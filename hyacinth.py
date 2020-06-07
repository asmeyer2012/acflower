
from bayes import *
from genotype import *

HyacinthPheno = {}
for bp0 in basicPairs:
  HyacinthPheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.WHITE
  HyacinthPheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.YELLOW
  HyacinthPheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  HyacinthPheno[Genotype({
    'R':basicPair1,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.YELLOW
  HyacinthPheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  HyacinthPheno[Genotype({
    'R':basicPair2,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.RED
  HyacinthPheno[Genotype({
    'R':basicPair2,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.BLUE
  HyacinthPheno[Genotype({
    'R':basicPair2,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.PURPLE

HyacinthPheno[Genotype({
  'R':basicPair0,'Y':basicPair0,'W':basicPair2}).ShortSeq()] = Color.BLUE
HyacinthPheno[Genotype({
  'R':basicPair0,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.WHITE
HyacinthPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair0}).ShortSeq()] = Color.RED
HyacinthPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair1}).ShortSeq()] = Color.PINK
HyacinthPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair2}).ShortSeq()] = Color.WHITE
HyacinthPheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair0}).ShortSeq()] = Color.ORANGE
HyacinthPheno[Genotype({
  'R':basicPair1,'Y':basicPair2,'W':basicPair0}).ShortSeq()] = Color.ORANGE
HyacinthPheno[Genotype({
  'R':basicPair2,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.RED

gpHyacinthSeedWhite  = {'R':basicPair0,'Y':basicPair0,'W':basicPair1}
gpHyacinthSeedYellow = {'R':basicPair0,'Y':basicPair2,'W':basicPair0}
gpHyacinthSeedRed    = {'R':basicPair2,'Y':basicPair0,'W':basicPair1}
geHyacinthSeedWhite  = Genotype(gpHyacinthSeedWhite, pheno=HyacinthPheno)
geHyacinthSeedYellow = Genotype(gpHyacinthSeedYellow,pheno=HyacinthPheno)
geHyacinthSeedRed    = Genotype(gpHyacinthSeedRed,   pheno=HyacinthPheno)
HyacinthSeedWhite  = BayesObj([ BayesProb( geHyacinthSeedWhite,  1)])
HyacinthSeedYellow = BayesObj([ BayesProb( geHyacinthSeedYellow, 1)])
HyacinthSeedRed    = BayesObj([ BayesProb( geHyacinthSeedRed,    1)])

#for bp0 in basicPairs:
# for bp1 in basicPairs:
#  for bp2 in basicPairs:
#   g0 = Genotype({'R':bp0,'Y':bp1,'W':bp2},pheno=HyacinthPheno)
#   print(g0)


