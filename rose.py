
from bayes import *
from genotype import *

## build the list of phenotypes for roses
RosePheno = {}
for bp0 in basicPairs:
  ## no red
  RosePheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':basicPair0,'B':bp0}).ShortSeq()] = Color.WHITE
  RosePheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':basicPair1,'B':bp0}).ShortSeq()] = Color.WHITE
  RosePheno[Genotype({
    'R':basicPair0,'Y':basicPair0,'W':basicPair2,'B':bp0}).ShortSeq()] = Color.PURPLE
  RosePheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':basicPair0,'B':bp0}).ShortSeq()] = Color.YELLOW
  RosePheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':basicPair1,'B':bp0}).ShortSeq()] = Color.WHITE
  RosePheno[Genotype({
    'R':basicPair0,'Y':basicPair1,'W':basicPair2,'B':bp0}).ShortSeq()] = Color.PURPLE
  RosePheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':basicPair0,'B':bp0}).ShortSeq()] = Color.YELLOW
  RosePheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':basicPair1,'B':bp0}).ShortSeq()] = Color.YELLOW
  RosePheno[Genotype({
    'R':basicPair0,'Y':basicPair2,'W':basicPair2,'B':bp0}).ShortSeq()] = Color.WHITE

## one red
for bp0 in basicPairs:
  RosePheno[Genotype({
    'R':basicPair1,'Y':basicPair0,'W':bp0,'B':basicPair0}).ShortSeq()] = Color.RED
  RosePheno[Genotype({
    'R':basicPair1,'Y':basicPair0,'W':bp0,'B':basicPair1}).ShortSeq()] = Color.PINK
  RosePheno[Genotype({
    'R':basicPair1,'Y':basicPair0,'W':bp0,'B':basicPair2}).ShortSeq()] = Color.WHITE
  #
  RosePheno[Genotype({
    'R':basicPair1,'Y':basicPair1,'W':bp0,'B':basicPair0}).ShortSeq()] = Color.RED
  RosePheno[Genotype({
    'R':basicPair1,'Y':basicPair1,'W':bp0,'B':basicPair1}).ShortSeq()] = Color.PINK
  RosePheno[Genotype({
    'R':basicPair1,'Y':basicPair1,'W':bp0,'B':basicPair2}).ShortSeq()] = Color.WHITE
  #
  RosePheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0,'B':basicPair0}).ShortSeq()] = Color.ORANGE
  RosePheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0,'B':basicPair1}).ShortSeq()] = Color.YELLOW
  RosePheno[Genotype({
    'R':basicPair1,'Y':basicPair2,'W':bp0,'B':basicPair2}).ShortSeq()] = Color.YELLOW

RosePheno[Genotype({
  'R':basicPair1,'Y':basicPair0,'W':basicPair2,'B':basicPair2}).ShortSeq()] = Color.PURPLE
#
RosePheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair0,'B':basicPair0}).ShortSeq()] = Color.ORANGE
RosePheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair0,'B':basicPair1}).ShortSeq()] = Color.YELLOW
RosePheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair0,'B':basicPair2}).ShortSeq()] = Color.YELLOW
RosePheno[Genotype({
  'R':basicPair1,'Y':basicPair1,'W':basicPair2,'B':basicPair2}).ShortSeq()] = Color.PURPLE
#
RosePheno[Genotype({
  'R':basicPair1,'Y':basicPair2,'W':basicPair2,'B':basicPair0}).ShortSeq()] = Color.RED
RosePheno[Genotype({
  'R':basicPair1,'Y':basicPair2,'W':basicPair2,'B':basicPair1}).ShortSeq()] = Color.PINK
RosePheno[Genotype({
  'R':basicPair1,'Y':basicPair2,'W':basicPair2,'B':basicPair2}).ShortSeq()] = Color.WHITE

## two red
for bp0 in basicPairs:
  RosePheno[Genotype({
    'R':basicPair2,'Y':basicPair0,'W':bp0,'B':basicPair0}).ShortSeq()] = Color.BLACK
  RosePheno[Genotype({
    'R':basicPair2,'Y':basicPair0,'W':bp0,'B':basicPair1}).ShortSeq()] = Color.RED
  RosePheno[Genotype({
    'R':basicPair2,'Y':basicPair0,'W':bp0,'B':basicPair2}).ShortSeq()] = Color.PINK
  #
  RosePheno[Genotype({
    'R':basicPair2,'Y':basicPair1,'W':basicPair0,'B':bp0}).ShortSeq()] = Color.ORANGE
  RosePheno[Genotype({
    'R':basicPair2,'Y':basicPair1,'W':basicPair1,'B':bp0}).ShortSeq()] = Color.RED
  #
  RosePheno[Genotype({
    'R':basicPair2,'Y':basicPair2,'W':basicPair0,'B':bp0}).ShortSeq()] = Color.ORANGE
  RosePheno[Genotype({
    'R':basicPair2,'Y':basicPair2,'W':basicPair1,'B':bp0}).ShortSeq()] = Color.ORANGE

RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair1,'W':basicPair0,'B':basicPair2}).ShortSeq()] = Color.YELLOW
RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair1,'W':basicPair1,'B':basicPair2}).ShortSeq()] = Color.WHITE
RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair1,'W':basicPair2,'B':basicPair0}).ShortSeq()] = Color.BLACK
RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair1,'W':basicPair2,'B':basicPair1}).ShortSeq()] = Color.RED
RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair1,'W':basicPair2,'B':basicPair2}).ShortSeq()] = Color.PURPLE
#
RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair2,'W':basicPair0,'B':basicPair2}).ShortSeq()] = Color.YELLOW
RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair2,'W':basicPair1,'B':basicPair2}).ShortSeq()] = Color.YELLOW
RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair2,'W':basicPair2,'B':basicPair0}).ShortSeq()] = Color.BLUE
RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair2,'W':basicPair2,'B':basicPair1}).ShortSeq()] = Color.RED
RosePheno[Genotype({
  'R':basicPair2,'Y':basicPair2,'W':basicPair2,'B':basicPair2}).ShortSeq()] = Color.WHITE

gpRoseSeedWhite  = {'R':basicPair0,'Y':basicPair0,'W':basicPair1,'B':basicPair0}
gpRoseSeedYellow = {'R':basicPair0,'Y':basicPair1,'W':basicPair0,'B':basicPair0}
gpRoseSeedRed    = {'R':basicPair2,'Y':basicPair0,'W':basicPair0,'B':basicPair1}
geRoseSeedWhite  = Genotype(gpRoseSeedWhite, pheno=RosePheno)
geRoseSeedYellow = Genotype(gpRoseSeedYellow,pheno=RosePheno)
geRoseSeedRed    = Genotype(gpRoseSeedRed,   pheno=RosePheno)
RoseSeedWhite  = BayesObj([ BayesProb( geRoseSeedWhite,  1)])
RoseSeedYellow = BayesObj([ BayesProb( geRoseSeedYellow, 1)])
RoseSeedRed    = BayesObj([ BayesProb( geRoseSeedRed,    1)])

#for bp0 in basicPairs:
# for bp1 in basicPairs:
#  for bp2 in basicPairs:
#   for bp3 in basicPairs:
#    g0 = Genotype({'R':bp0,'Y':bp1,'W':bp2,'B':bp3},pheno=RosePheno)
#    print(g0)

