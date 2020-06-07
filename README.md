# Animal Crossing: New Horizons - Flower Breeder

Compute probabilities for flower parent and offspring genotypes in Animal Crossing: New Horizons.

## Prerequisites

Written in python v3.7.0

## Getting Started

Flower genotypes and phenotypes are pulled from the table on the [Animal Crossing Wiki Article on Flower Mechanics](https://animalcrossing.fandom.com/wiki/Flower/New_Horizons_mechanics).

Generic seed flower objects are predefined with names "<FlowerType>Seed<Color>", e.g. RoseSeedWhite.

Single offspring probabilities are evaluated by multiplying two parents together

```
>>> a0 = RoseSeedWhite * RoseSeedWhite
>>> print(a0)
BayesObj{
  (R:gg)(Y:gg)(W:GG)(B:gg)[Color.PURPLE]:1/4
  (R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]:1/2
  (R:gg)(Y:gg)(W:gg)(B:gg)[Color.WHITE]:1/4
 }
```

Offspring can be selected based on color by using the Pick() option with the lambda generator PickColor()

```
>>> a1 = a0.Pick(PickColor(Color.PURPLE))
>>> print(a1)
BayesObj{
  (R:gg)(Y:gg)(W:GG)(B:gg)[Color.PURPLE]:1
 }
```

The probability that a specific phenotype has been generated can be evaluated with Probability()

```
>>> print(a0)
BayesObj{
  (R:gg)(Y:gg)(W:GG)(B:gg)[Color.PURPLE]:1/4
  (R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]:1/2
  (R:gg)(Y:gg)(W:gg)(B:gg)[Color.WHITE]:1/4
 }
>>> print(a0.Probability(PickColor(Color.WHITE)))
3/4
```

Sometimes the parents' genotypes are not known. If one or more offspring have been created using a flower as a parent, then the colors of all these offspring can be used to update the posterior knowledge of the parents' genotypes. This is evaluated using Bayes' theorem.

```
a2 = a0.Pick(PickColor(Color.WHITE))
>>> print(a2)
BayesObj{
  (R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]:2/3
  (R:gg)(Y:gg)(W:gg)(B:gg)[Color.WHITE]:1/3
 }
>>> print(RoseSeedWhite)
BayesObj{
  (R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]:1
 }
>>> parent0 = a2
>>> parent1 = RoseSeedWhite
>>> child_colors = [Color.WHITE]
>>> a3 = BreedOutcome(parent0,parent1,child_colors)
>>> print(a3)
BayesObj{
  ((R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE], (R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]):3/5
  ((R:gg)(Y:gg)(W:gg)(B:gg)[Color.WHITE], (R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]):2/5
 }
```

If a flower has unknown genotype, you can also use a function to build a democratic probability for each possible genotype

```
>>> UnknownGenotype( ('R','Y','W','B'), RosePheno, Color.ORANGE)
BayesObj{
  (B:Gg)(R:GG)(W:Gg)(Y:GG)[Color.ORANGE]:1/9
  (B:Gg)(R:GG)(W:gg)(Y:GG)[Color.ORANGE]:1/9
  (B:Gg)(R:GG)(W:gg)(Y:Gg)[Color.ORANGE]:1/9
  (B:gg)(R:GG)(W:Gg)(Y:GG)[Color.ORANGE]:1/9
  (B:gg)(R:GG)(W:gg)(Y:GG)[Color.ORANGE]:1/9
  (B:gg)(R:GG)(W:gg)(Y:Gg)[Color.ORANGE]:1/9
  (B:gg)(R:Gg)(W:Gg)(Y:GG)[Color.ORANGE]:1/9
  (B:gg)(R:Gg)(W:gg)(Y:GG)[Color.ORANGE]:1/9
  (B:gg)(R:Gg)(W:gg)(Y:Gg)[Color.ORANGE]:1/9
 }
```

## Data Structure

Flower genotypes are saved in a Genotype class instance, which encodes the genes as GenePair class instances. Paired with the data is a dictionary describing the phenotype colors. GenePairs are given one GenePairValue to initialize, which encodes a single genepair ("gg", "Gg", or "GG"). Genotypes are passed as a class with each gene given a key value ("R", "Y", "W", or "B" in the predefined types).

```
>>> g0 = GenePair(GenePairValue.gg)
>>> print(g0)
gg
>>> print(gpRoseSeedWhite)
{'R': gg, 'Y': gg, 'W': Gg, 'B': gg}
>>> Genotype(gpRoseSeedWhite,pheno={})
(R:gg)(Y:gg)(W:Gg)(B:gg)[]
```

If the phenotype is defined, then that will show up in the string description too

```
>>> Genotype(gpRoseSeedWhite,pheno=RosePheno)
(R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]
```

To evaluate probabilities, the Genotype class is wrapped in a BayesProb class instance wrapper, which includes a probability with the class object (though the code is flexible enough to accept any object rather than only the Genotype class). The BayesProb are collected into a container class, BayesObj, which has a set of probabilities that sum to exactly 1.

```
>>> b0 = BayesProb(Genotype(gpRoseSeedWhite,pheno=RosePheno),1)
>>> print(b0)
(R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]:1
>>> b1 = BayesObj([b0])
>>> print(b1)
BayesObj{
  (R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]:1
 }
```

The BayesObj class objects can be accessed through the attribute ".objs". The BayesProb class object is accessed with the attribute ".obj".

```
>>> b1.objs
[(R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]:1]
>>> b1.objs[0]
(R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]:1
>>> b1.objs[0].obj
(R:gg)(Y:gg)(W:Gg)(B:gg)[Color.WHITE]
```

## Author

* **Aaron S. Meyer** - [asmeyer2012](https://github.com/asmeyer2012)

