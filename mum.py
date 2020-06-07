
from bayes import *
from genotype import *

MumPheno = {}
for bp0 in basicPairs:
  MumPheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.WHITE
  MumPheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.YELLOW
  MumPheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  MumPheno[Genotype({
    'R':basicPair1,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.PINK
  MumPheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.PURPLE
  MumPheno[Genotype({
    'R':basicPair2,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.RED
  MumPheno[Genotype({
    'R':basicPair2,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.PURPLE
  MumPheno[Genotype({
    'R':basicPair2,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.GREEN

for bp0 in basicPairs:
  MumPheno[Genotype({
    'R':basicPair2,'Y':bp0,'W':basicPair2}).ShortSeq()] = Color.RED

MumPheno[Genotype({
  'R':basicPair0,'Y':basicPair0,'W':basicPair2}).ShortSeq()] = Color.PURPLE
MumPheno[Genotype({
  'R':basicPair0,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.WHITE
MumPheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair0}).ShortSeq()] = Color.YELLOW
MumPheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair1}).ShortSeq()] = Color.RED
MumPheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.PINK

gpMumSeedWhite  = {'R':basicPair0,'Y':basicPair0,'W':basicPair1}
gpMumSeedYellow = {'R':basicPair0,'Y':basicPair2,'W':basicPair0}
gpMumSeedRed    = {'R':basicPair2,'Y':basicPair0,'W':basicPair0}
geMumSeedWhite  = Genotype(gpMumSeedWhite, pheno=MumPheno)
geMumSeedYellow = Genotype(gpMumSeedYellow,pheno=MumPheno)
geMumSeedRed    = Genotype(gpMumSeedRed,   pheno=MumPheno)
MumSeedWhite  = BayesObj([ BayesProb( geMumSeedWhite,  1)])
MumSeedYellow = BayesObj([ BayesProb( geMumSeedYellow, 1)])
MumSeedRed    = BayesObj([ BayesProb( geMumSeedRed,    1)])

#for bp0 in basicPairs:
# for bp1 in basicPairs:
#  for bp2 in basicPairs:
#   g0 = Genotype({'R':bp0,'Y':bp1,'W':bp2},pheno=MumPheno)
#   print(g0)


