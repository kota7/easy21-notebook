EASY21-NOTEBOOK
===============
Easy21 Reinforcement Learning Exercise.

Provides jupyter notebook documents that solve
[Easy21](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/Easy21-Johannes.pdf) excersise for
David Silver's [Reinforcement Learning course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html).

This repository covers following methodologies (items with * are not in the original assignment):

1. [Dynamic programming*](./notebook/1_dynamic-programming.ipynb)
1. [Monte Carlo](./notebook/3_montecarlo.ipynb)
1. [Temporal Difference](./notebook/4_temporal-difference.ipynb)
1. TD-lambda (TBA)
1. Linear function approximation (TBA)
1. Deep Q-network* (TBA)
1. Policy gradient* (TBA)


## Setup

Create anaconda environment with the yaml file.

```bash
$ conda create env -f environment.yml
```

## Run notebook

Start jupyter and open notebooks.

```bash
$ conda activate easy21
$ jupyter notebook
```
