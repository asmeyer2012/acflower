
from bayes import *
from genotype import *

LilyPheno = {}
for bp0 in basicPairs:
  LilyPheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':bp0}).ShortSeq()] = Color.WHITE
  LilyPheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.WHITE
  LilyPheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  LilyPheno[Genotype({
    'R':basicPair1,'Y':basicPair1,'W':bp0}).ShortSeq()] = Color.YELLOW
  LilyPheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.YELLOW
  LilyPheno[Genotype({
    'R':basicPair2,'Y':bp0,'W':basicPair0}).ShortSeq()] = Color.BLACK
  LilyPheno[Genotype({
    'R':basicPair2,'Y':bp0,'W':basicPair1}).ShortSeq()] = Color.RED
  LilyPheno[Genotype({
    'R':basicPair2,'Y':bp0,'W':basicPair2}).ShortSeq()] = Color.PINK

for bp0 in basicPairs:
  LilyPheno[Genotype({
    'R':basicPair2,'Y':basicPair2,'W':bp0}).ShortSeq()] = Color.ORANGE

LilyPheno[Genotype({
  'R':basicPair0,'Y':basicPair1,'W':basicPair0}).ShortSeq()] = Color.YELLOW
LilyPheno[Genotype({
  'R':basicPair0,'Y':basicPair2,'W':basicPair2}).ShortSeq()] = Color.WHITE
LilyPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair0}).ShortSeq()] = Color.RED
LilyPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair1}).ShortSeq()] = Color.PINK
LilyPheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair2}).ShortSeq()] = Color.WHITE
LilyPheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair0}).ShortSeq()] = Color.ORANGE
LilyPheno[Genotype({
  'R':basicPair1,'Y':basicPair2,'W':basicPair0}).ShortSeq()] = Color.ORANGE
LilyPheno[Genotype({
  'R':basicPair2,'Y':basicPair2,'W':basicPair2}).ShortSeq()] = Color.WHITE

gpLilySeedWhite  = {'R':basicPair0,'Y':basicPair0,'W':basicPair2}
gpLilySeedYellow = {'R':basicPair0,'Y':basicPair2,'W':basicPair0}
gpLilySeedRed    = {'R':basicPair2,'Y':basicPair0,'W':basicPair1}
geLilySeedWhite  = Genotype(gpLilySeedWhite, pheno=LilyPheno)
geLilySeedYellow = Genotype(gpLilySeedYellow,pheno=LilyPheno)
geLilySeedRed    = Genotype(gpLilySeedRed,   pheno=LilyPheno)
LilySeedWhite  = BayesObj([ BayesProb( geLilySeedWhite,  1)])
LilySeedYellow = BayesObj([ BayesProb( geLilySeedYellow, 1)])
LilySeedRed    = BayesObj([ BayesProb( geLilySeedRed,    1)])

#for bp0 in basicPairs:
# for bp1 in basicPairs:
#  for bp2 in basicPairs:
#   g0 = Genotype({'R':bp0,'Y':bp1,'W':bp2},pheno=LilyPheno)
#   print(g0)


