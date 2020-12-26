# Cute Ranking
> A cute little python module for calculating different ranking metrics. Based entirely on the gist from https://gist.github.com/bwhite/3726239.


## Install

Requires a minimum python installation of 3.6

`pip install cute_ranking`

## How to use

```python
from cute_ranking.core import mean_reciprocal_rank

relevancies = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
mean_reciprocal_rank(relevancies)
```




    0.611111111111111



The library current supports the following information retrieval ranking metrics:
1. Mean Reciprocal Rank - `mean_reciprocal_rank`
2. Relevancy Precision - `r_precision`
3. Precision at K - `precision_at_k`
4. Average Precision - `average_precision`
5. Mean Average Precision - `mean_average_precision`
6. Discounted Cumulative Gain at K - `dcg_at_k`
7. Normalized Discounted Cumulative Gain at K - `ndcg_at_k`

# Contributing
PRs and issues welcome! Please make sure to read through the `CONTRIBUTING.md` doc for how to contribute :).
