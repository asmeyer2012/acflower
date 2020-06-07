import sympy as sp
from enum import Enum
from copy import deepcopy

f12 = sp.Rational(1,2)
f14 = sp.Rational(1,4)

class BayesProb:
  def __init__(self,obj,prob):
    self.obj = obj
    if (prob < 0) or (prob > 1):
      raise ValueError("invalid probability")
    self.prob = prob
  def Copy(self):
    return BayesProb(deepcopy(self.obj),self.prob)
  ## apply a function to the object and build a new BayesProb out of it
  def Apply(self, fn):
    return BayesProb( fn( self.obj), self.prob)
  ## ensure that result is list of BayesProb instances
  def TypeConvertResult(self,res):
    if isinstance(res,list):
      xres = []
      for term in res:
        xres.extend( self.TypeConvertResult( term))
      return xres
    if isinstance(res,BayesObj):
      return res.objs
    if isinstance(res,BayesProb):
      return [res]
    return [BayesProb(res,1)]
  def __rmul__(self, other):
    return self.__mul__(other)
  def __mul__(self, other):
    if isinstance( other, type(self.obj)):
      return self *BayesProb( other, 1)
    if not( isinstance( other, type(self))):
      return NotImplemented
    if not( isinstance( self.obj, type(other.obj))):
      raise TypeError(
        "BayesProb objects of incompatible types: {}, {}".format(
        type(self.obj), type(other.obj)))
    res = self.TypeConvertResult( self.obj *other.obj)
    for term in res:
      term.prob *= self.prob *other.prob
    ## always returns a list of BayesProb class objects
    return res
  ## only tests equality of objects, not probabilities
  def __eq__(self,other):
    return self.obj == other.obj
  def __lt__(self,other):
    return self.obj < other.obj
  def __repr__(self):
    return '{}:{}'.format( self.obj, self.prob)
  def __str__(self):
    return self.__repr__()

class BayesObj:
  def __init__(self,objs):
    for obj in objs:
      if not( isinstance( obj, BayesProb)):
        raise TypeError(
          "BayesObj initialized with non-BayesProb instance of type: {}".format(
          type( obj)))
    self.objs = sorted( objs, key=lambda x: x.__repr__())
    ## check that probabilities sum to 1
    prob = 0
    for obj in self.objs:
      prob += obj.prob
    if prob != 1:
      raise ValueError("BayesObj probability sums to nonunity: {}".format( prob))
  def Copy(self):
    return BayesObj([ obj.Copy() for obj in self.objs ])
  def __rmul__(self, other):
    return self.__mul__(other)
  def __mul__(self, other):
    if isinstance( other, type(self.objs[0].obj)):
      return self *BayesObj([ BayesProb(other,1) ])
    if not( isinstance( other, type(self))):
      return NotImplemented
    objs = []
    for obj0 in self.objs:
      for obj1 in other.objs:
        objs.extend( obj0*obj1)
    ret = BayesObj(objs)
    ret.Reduce()
    return ret
  def Reduce(self):
    N = len( self.objs)
    for i0,obj0 in enumerate( self.objs[::-1]):
      i0 = N-1-i0
      for i1,obj1 in enumerate( self.objs[:i0]):
        if obj0 == obj1:
          obj0.prob += obj1.prob
          self.objs.pop(i1)
          self.Reduce()
          return
  ## if self.objs are also BayesObjs, then flatten to top level
  def Flatten(self):
    if isinstance( self.objs[0].obj, BayesObj):
      ret = []
      for obj0 in self.objs:
        _obj0 = obj0.Copy().obj.objs
        for obj1 in _obj0:
          obj1.prob *= obj0.prob
        ret.extend( _obj0)
      bobj = BayesObj( ret)
      bobj.Reduce()
      return bobj
    raise ValueError("Flatten() got non-BayesObj object")
  ## apply a function to the objects and build a new BayesObj out of it
  def Apply(self, fn):
    return BayesObj([ obj.Apply( fn) for obj in self.objs ])
  ## concatenate two BayesObjs together to create new
  ## objects are tuples containing one from each of previous
  def Concatenate(self, other):
    objs = []
    for obj0 in self.objs:
      for obj1 in other.objs:
        if not( isinstance( obj0.obj, tuple)):
          _obj0 = ( obj0.obj,)
        else:
          _obj0 = obj0.obj
        if not( isinstance( obj1.obj, tuple)):
          _obj1 = ( obj1.obj,)
        else:
          _obj1 = obj1.obj
        obj2 = _obj0 +_obj1
        prob2 = obj0.prob *obj1.prob
        objs.append( BayesProb( obj2, prob2))
    return BayesObj( objs)
  ## only keep the objects that satisfy fn(obj) == True
  ## rescale the probabilities to sum to 1
  def Pick(self, fn):
    objs = [ obj.Copy() for obj in self.objs if fn(obj) ]
    marg = sum([ obj.prob for obj in self.objs if fn(obj) ])
    if ((len( objs) == 0) or (marg == 0)):
      raise ValueError("Pick() found zero probability")
    for obj in objs:
      obj.prob /= marg
    return BayesObj( objs)
  ## give the sum of probabilities for objects that satisfy fn(obj) == True
  def Probability(self, fn):
    return sum([ obj.prob for obj in self.objs if fn(obj) ])
  ## use Bayes theorem to compute probability based on outcome
  ## P(A|B) = P(B|A) P(A) / P(B)
  ## P(A) is probability in each obj of self.objs
  ## P(B) is sum of probabilities from all outcomes where test_fn(obj) == True
  ## compute P(B|A) by applying test_fn to each outcome_fn(obj) in self.objs
  ## return a BayesObj with probs for each A in P(A|B)
  def Posterior(self, outcome_fn, test_fn):
    ## apply fn to each obj => BayesObj outcome for each
    ## compute relevant probabilities
    PB = self.Apply( outcome_fn).Flatten().Probability( test_fn)
    if PB == 0:
      raise ValueError("Posterior() found zero probability")
    PAall  = [ obj.prob for obj in self.objs ]
    PBAall = [ obj.obj.Probability( test_fn) for obj in self.Apply( outcome_fn).objs ]
    PABall = [ (PBAi *PAi /PB) for (PBAi,PAi) in zip( PBAall, PAall) ]
    bobj = BayesObj([ BayesProb( obj.obj, PABi) for (obj,PABi) in zip( self.objs, PABall) ])
    return bobj
  def __repr__(self):
    ostr = 'BayesObj{\n'
    for obj in self.objs:
      ostr = ostr +'  ' +obj.__repr__() +'\n'
    return ostr +' }'
  def __str__(self):
    return self.__repr__()

