
from bayes import *
from genotype import *

TulipPheno = {}
for bp0 in basicPairs:
  TulipPheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.WHITE
  TulipPheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.YELLOW
  TulipPheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  TulipPheno[Genotype({
    'R':basicPair1,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.YELLOW
  TulipPheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  TulipPheno[Genotype({
    'R':basicPair2,'Y':bp0,'W':basicPair0}).ShortSeq()] = Color.BLACK
  TulipPheno[Genotype({
    'R':basicPair2,'Y':bp0,'W':basicPair1}).ShortSeq()] = Color.RED
  TulipPheno[Genotype({
    'R':basicPair2,'Y':bp0,'W':basicPair2}).ShortSeq()] = Color.RED

for bp0 in basicPairs:
  TulipPheno[Genotype({
    'R':basicPair2,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.PURPLE

TulipPheno[Genotype({
  'R':basicPair0,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.WHITE
TulipPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair0}).ShortSeq()] = Color.RED
TulipPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair1}).ShortSeq()] = Color.PINK
TulipPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair2}).ShortSeq()] = Color.WHITE
TulipPheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair0}).ShortSeq()] = Color.ORANGE
TulipPheno[Genotype({
  'R':basicPair1,'Y':basicPair2,'W':basicPair0}).ShortSeq()] = Color.ORANGE

gpTulipSeedWhite  = {'R':basicPair0,'Y':basicPair0,'W':basicPair1}
gpTulipSeedYellow = {'R':basicPair0,'Y':basicPair2,'W':basicPair0}
gpTulipSeedRed    = {'R':basicPair2,'Y':basicPair0,'W':basicPair1}
geTulipSeedWhite  = Genotype(gpTulipSeedWhite, pheno=TulipPheno)
geTulipSeedYellow = Genotype(gpTulipSeedYellow,pheno=TulipPheno)
geTulipSeedRed    = Genotype(gpTulipSeedRed,   pheno=TulipPheno)
TulipSeedWhite  = BayesObj([ BayesProb( geTulipSeedWhite,  1)])
TulipSeedYellow = BayesObj([ BayesProb( geTulipSeedYellow, 1)])
TulipSeedRed    = BayesObj([ BayesProb( geTulipSeedRed,    1)])

#for bp0 in basicPairs:
# for bp1 in basicPairs:
#  for bp2 in basicPairs:
#   g0 = Genotype({'R':bp0,'Y':bp1,'W':bp2},pheno=TulipPheno)
#   print(g0)


