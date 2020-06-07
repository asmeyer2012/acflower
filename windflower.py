
from bayes import *
from genotype import *

WindflowerPheno = {}
for bp0 in basicPairs:
  WindflowerPheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.WHITE
  WindflowerPheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.ORANGE
  WindflowerPheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.ORANGE
  WindflowerPheno[Genotype({
    'R':basicPair1,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.RED
  WindflowerPheno[Genotype({
    'R':basicPair1,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.PINK
  WindflowerPheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.ORANGE
  WindflowerPheno[Genotype({
    'R':basicPair2,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.RED
  WindflowerPheno[Genotype({
    'R':basicPair2,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.RED
  WindflowerPheno[Genotype({
    'R':basicPair2,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.PINK

for bp0 in basicPairs:
  WindflowerPheno[Genotype({
    'R':basicPair2,'Y':bp0,'W':basicPair2}).ShortSeq()] = Color.PURPLE

WindflowerPheno[Genotype({
  'R':basicPair0,'Y':basicPair0,'W':basicPair2}).ShortSeq()] = Color.BLUE
WindflowerPheno[Genotype({
  'R':basicPair0,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.BLUE
WindflowerPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair2}).ShortSeq()] = Color.BLUE

gpWindflowerSeedWhite  = {'R':basicPair0,'Y':basicPair0,'W':basicPair1}
gpWindflowerSeedOrange = {'R':basicPair0,'Y':basicPair2,'W':basicPair0}
gpWindflowerSeedRed    = {'R':basicPair2,'Y':basicPair0,'W':basicPair0}
geWindflowerSeedWhite  = Genotype(gpWindflowerSeedWhite, pheno=WindflowerPheno)
geWindflowerSeedOrange = Genotype(gpWindflowerSeedOrange,pheno=WindflowerPheno)
geWindflowerSeedRed    = Genotype(gpWindflowerSeedRed,   pheno=WindflowerPheno)
WindflowerSeedWhite  = BayesObj([ BayesProb( geWindflowerSeedWhite,  1)])
WindflowerSeedOrange = BayesObj([ BayesProb( geWindflowerSeedOrange, 1)])
WindflowerSeedRed    = BayesObj([ BayesProb( geWindflowerSeedRed,    1)])

#for bp0 in basicPairs:
# for bp1 in basicPairs:
#  for bp2 in basicPairs:
#   g0 = Genotype({'R':bp0,'Y':bp1,'W':bp2},pheno=WindflowerPheno)
#   print(g0)


