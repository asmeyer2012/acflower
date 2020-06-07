# Animal Crossing: New Horizons - Flower Breeder

Compute probabilities for flower parent and offspring genotypes in Animal Crossing: New Horizons.

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

### Prerequisites

Written in python v3.7.0

## Authors

* **Aaron S. Meyer** - [asmeyer2012](https://github.com/asmeyer2012)

