
from bayes import *
from genotype import *

PansyPheno = {}
for bp0 in basicPairs:
  PansyPheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.WHITE
  PansyPheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.YELLOW
  PansyPheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  PansyPheno[Genotype({
    'R':basicPair1,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.RED
  PansyPheno[Genotype({
    'R':basicPair1,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.ORANGE
  PansyPheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  PansyPheno[Genotype({
    'R':basicPair2,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.RED
  PansyPheno[Genotype({
    'R':basicPair2,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.RED
  PansyPheno[Genotype({
    'R':basicPair2,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.ORANGE

for bp0 in basicPairs:
  PansyPheno[Genotype({
    'R':basicPair2,'Y':bp0,'W':basicPair2}).ShortSeq()] = Color.PURPLE

PansyPheno[Genotype({
  'R':basicPair0,'Y':basicPair0,'W':basicPair2}).ShortSeq()] = Color.BLUE
PansyPheno[Genotype({
  'R':basicPair0,'Y':basicPair1,'W':basicPair2}).ShortSeq()] = Color.BLUE
PansyPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair2}).ShortSeq()] = Color.BLUE

gpPansySeedWhite  = {'R':basicPair0,'Y':basicPair0,'W':basicPair1}
gpPansySeedYellow = {'R':basicPair0,'Y':basicPair2,'W':basicPair0}
gpPansySeedRed    = {'R':basicPair2,'Y':basicPair0,'W':basicPair0}
gePansySeedWhite  = Genotype(gpPansySeedWhite, pheno=PansyPheno)
gePansySeedYellow = Genotype(gpPansySeedYellow,pheno=PansyPheno)
gePansySeedRed    = Genotype(gpPansySeedRed,   pheno=PansyPheno)
PansySeedWhite  = BayesObj([ BayesProb( gePansySeedWhite,  1)])
PansySeedYellow = BayesObj([ BayesProb( gePansySeedYellow, 1)])
PansySeedRed    = BayesObj([ BayesProb( gePansySeedRed,    1)])

#for bp0 in basicPairs:
# for bp1 in basicPairs:
#  for bp2 in basicPairs:
#   g0 = Genotype({'R':bp0,'Y':bp1,'W':bp2},pheno=PansyPheno)
#   print(g0)


