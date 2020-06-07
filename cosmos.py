
from bayes import *
from genotype import *

CosmosPheno = {}
for bp0 in basicPairs:
  CosmosPheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.WHITE
  CosmosPheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.YELLOW
  CosmosPheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  CosmosPheno[Genotype({
    'R':basicPair1,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.PINK
  CosmosPheno[Genotype({
    'R':basicPair1,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.ORANGE
  CosmosPheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.ORANGE
  CosmosPheno[Genotype({
    'R':basicPair2,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.RED
  CosmosPheno[Genotype({
    'R':basicPair2,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.ORANGE
  CosmosPheno[Genotype({
    'R':basicPair2,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.BLACK

CosmosPheno[Genotype({
  'R':basicPair0,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.WHITE
CosmosPheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.PINK
CosmosPheno[Genotype({
  'R':basicPair2,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.RED
CosmosPheno[Genotype({
  'R':basicPair2,'Y':basicPair2,'W':basicPair2}).ShortSeq()] = Color.RED

gpCosmosSeedWhite  = {'R':basicPair0,'Y':basicPair0,'W':basicPair1}
gpCosmosSeedYellow = {'R':basicPair0,'Y':basicPair2,'W':basicPair1}
gpCosmosSeedRed    = {'R':basicPair2,'Y':basicPair0,'W':basicPair0}
geCosmosSeedWhite  = Genotype(gpCosmosSeedWhite, pheno=CosmosPheno)
geCosmosSeedYellow = Genotype(gpCosmosSeedYellow,pheno=CosmosPheno)
geCosmosSeedRed    = Genotype(gpCosmosSeedRed,   pheno=CosmosPheno)
CosmosSeedWhite  = BayesObj([ BayesProb( geCosmosSeedWhite,  1)])
CosmosSeedYellow = BayesObj([ BayesProb( geCosmosSeedYellow, 1)])
CosmosSeedRed    = BayesObj([ BayesProb( geCosmosSeedRed,    1)])

#for bp0 in basicPairs:
# for bp1 in basicPairs:
#  for bp2 in basicPairs:
#   g0 = Genotype({'R':bp0,'Y':bp1,'W':bp2},pheno=CosmosPheno)
#   print(g0)


