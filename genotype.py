import sympy as sp
from enum import Enum

from bayes import *

class GenePairValue(Enum):
  gg = 0
  Gg = 1
  GG = 2
  def __eq__(self,other):
    if not( isinstance( other, GenePairValue)):
      return NotImplemented
    return self.value == other.value
  def __lt__(self,other):
    if not( isinstance( other, GenePairValue)):
      return NotImplemented
    return self.value < other.value

class GenePair:
  def __init__(self, gvalue):
    if not( isinstance( gvalue, GenePairValue)):
      raise TypeError("gene value must be instance GenePairValue")
    self.gvalue = gvalue
  ## breeding two GenePairs
  def __mul__(self, other):
    if not( isinstance( other, type(self))):
      return NotImplemented
      #raise TypeError("incompatible type with {}: {}".format( type(self), type(other)))
    ## matching GG or gg
    if self.gvalue in [GenePairValue.GG, GenePairValue.gg] and self.gvalue == other.gvalue:
      return BayesObj([BayesProb(GenePair( self.gvalue),1)])
    ## GG and gg
    if (self.gvalue  in [GenePairValue.GG, GenePairValue.gg] and
        other.gvalue in [GenePairValue.GG, GenePairValue.gg] and
        self.gvalue != other.gvalue):
      return BayesObj([BayesProb(GenePair( GenePairValue.Gg),1)])
    ## both Gg
    if self.gvalue in [GenePairValue.Gg] and self.gvalue == other.gvalue:
      return BayesObj([
        BayesProb(GenePair( GenePairValue.GG),f14),
        BayesProb(GenePair( GenePairValue.Gg),f12),
        BayesProb(GenePair( GenePairValue.gg),f14)])
    ## others; Gg with GG or gg
    gvalue = (other.gvalue if self.gvalue == GenePairValue.Gg else self.gvalue)
    return BayesObj([
      BayesProb(GenePair( gvalue),f12),
      BayesProb(GenePair( GenePairValue.Gg),f12)])
  def __eq__(self,other):
    if not( isinstance( other, GenePair)):
      return NotImplemented
    return self.gvalue == other.gvalue
  def __lt__(self,other):
    if not( isinstance( other, GenePair)):
      return NotImplemented
    return self.gvalue < other.gvalue
  def __repr__(self):
    return '{}'.format( self.gvalue.name)
  def __str__(self):
    return self.__repr__()

basicPair0 = GenePair( GenePairValue.gg)
basicPair1 = GenePair( GenePairValue.Gg)
basicPair2 = GenePair( GenePairValue.GG)
basicPairs = [basicPair0,basicPair1,basicPair2]

class Genotype:
  def __init__(self,gpairs,pheno={}):
    self.gpairs = dict( gpairs)
    self.pheno = dict( pheno)
  def Copy(self):
    return Genotype( dict( self.gpairs), pheno=dict( self.pheno))
  def AddGene(self,gtag,gpair):
    cp = self.Copy()
    if gtag in cp.gpairs.keys(): 
      raise KeyError("gtag \"{}\" in gene tags".format(gtag))
    cp.gpairs[gtag] = gpair
    return cp
  ## breeding single GenePairs
  def MultiplyGenePair(self, other, gtags, ret):
    if len( gtags) == 0:
      return BayesObj(ret)
    gtag = gtags[0]
    gtags = gtags[1:]
    prod = self.gpairs[gtag] *other.gpairs[gtag]
    xret = []
    for bobj0 in ret:
      for bobj1 in prod.objs:
        gtype = bobj0.obj.AddGene(gtag,bobj1.obj)
        prob = bobj0.prob *bobj1.prob
        xret.append( BayesProb(gtype,prob))
    return self.MultiplyGenePair( other, gtags, ret=xret)
  ## return a short string
  def ShortSeq(self):
    otag = tuple()
    for gtag in sorted( list( self.gpairs.keys())):
      otag += (self.gpairs[ gtag].gvalue.value,)
    return otag
  ## return the phenotype as defined in self.pheno
  def Phenotype(self):
    return self.pheno.get( self.ShortSeq(), '')
  ## breeding two Genotypes, returns BayesObj class instance
  def __mul__(self, other):
    if not( isinstance( other, type(self))):
      return NotImplemented
    if not( self.gpairs.keys() == other.gpairs.keys()):
      print( self.gpairs.keys())
      print( other.gpairs.keys())
      raise TypeError("incompatible genotype genes")
    return self.MultiplyGenePair( other, list(self.gpairs.keys()),
      ret=[BayesProb(Genotype({},pheno=self.pheno),1)])
  def __eq__(self,other):
    if not( isinstance( other, Genotype)):
      return False
    if set( self.gpairs.keys()) != set( other.gpairs.keys()):
      return False
    ret = True
    for gtag in self.gpairs.keys():
      ret = ret and (self.gpairs[gtag] == other.gpairs[gtag])
    return ret
  def __lt__(self,other):
    if not( isinstance( other, Genotype)):
      return NotImplemented
    if set( self.gpairs.keys()) != set( other.gpairs.keys()):
      raise TypeError("GenePairs do not match")
    for gtag in sorted( list( self.gpairs.keys())):
      if (self.gpairs[gtag] < other.gpairs[gtag]):
        return True
    return False
  def __repr__(self):
    ostr = ''
    for gtag in self.gpairs.keys():
      otag = '({}:{})'.format(gtag,self.gpairs[gtag])
      ostr = ostr +otag
    ptag = '[{}]'.format( self.Phenotype())
    return ostr +ptag
  def __str__(self):
    return self.__repr__()

class Color(Enum):
  RED = 0
  YELLOW = 1
  WHITE = 2
  PINK = 3
  ORANGE = 4
  PURPLE = 5
  BLACK = 6
  BLUE = 7
  GREEN = 8
  def __eq__(self,other):
    if not( isinstance( other, Color)):
      return NotImplemented
    return self.value == other.value
  def __lt__(self,other):
    if not( isinstance( other, Color)):
      return NotImplemented
    return self.value < other.value

## lambda function for use with Pick() and Probability()
def PickColor( color):
  if not( isinstance( color, Color)):
    raise TypeError("PickColor must take Color type")
  return (lambda g: (g.obj.Phenotype() == color))

## update parent probabilities based on child color phenotypes after breeding
## result is a posterior in BayesObj
def BreedOutcome( parent0, parent1, child_colors):
  child_colors = sorted( child_colors)
  Nchild = len(child_colors)
  parents = parent0.Concatenate( parent1)
  ## breed the colors
  def outcome_fn(x):
    ret = x[0]*x[1]
    if Nchild < 2:
      ## need to make output shape consistent
      ret = ret.Concatenate(BayesObj([BayesProb(tuple(),1)]))
    else:
      for i in range(Nchild-1):
        ret = ret.Concatenate(x[0]*x[1])
    return ret.Apply( sorted)
  def test_fn(ocm):
    return (child_colors == sorted([ x.Phenotype() for x in ocm.obj ]))
  return parents.Posterior( outcome_fn, test_fn)

## build a BayesObj with democratic genotype from a flower with known color
## has equal probability for all genotypes with a specific phenotype
def UnknownGenotype( gpair_keys, pheno, color):
  gpair_keys = sorted( list( gpair_keys))
  objs = []
  for (gpv,clr) in pheno.items():
    if clr == color:
      gdict = dict(zip(gpair_keys,[GenePair( GenePairValue(x)) for x in gpv]))
      objs.append( Genotype( gdict, pheno=pheno))
  Nobj = len( objs)
  bobjs = [ BayesProb( obj, sp.Rational(1,Nobj)) for obj in objs ]
  return BayesObj( bobjs)

