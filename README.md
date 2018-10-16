EASY21-NOTEBOOK
===============
Easy21 Reinforcement Learning Exercise.

Provides jupyter notebook documents that solve
[Easy21](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/Easy21-Johannes.pdf) excersise for
David Silver's [Reinforcement Learning course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html).

This repository covers following methodologies (items with * are not in the original assignment):

## Tabular methods
 
* [Dynamic programming](https://nbviewer.jupyter.org/github/kota7/easy21-notebook/blob/master/notebook/1_dynamic-programming.ipynb)*
* [Monte carlo control](https://nbviewer.jupyter.org/github/kota7/easy21-notebook/blob/master/notebook/3_montecarlo.ipynb)
* [Temporal difference learning](https://nbviewer.jupyter.org/github/kota7/easy21-notebook/blob/master/notebook/4_temporal-difference.ipynb)*
* [TD(&#955;)](https://nbviewer.jupyter.org/github/kota7/easy21-notebook/blob/master/notebook/5_td-lambda.ipynb)


## Function approximation method

* Linear function approximation (TBA)
* Deep Q-network* (TBA)
* Policy gradient* (TBA)


## Tree search method

* [Monte carlo tree search](https://nbviewer.jupyter.org/github/kota7/easy21-notebook/blob/master/notebook/6_monte-carlo-tree-search.ipynb)


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
