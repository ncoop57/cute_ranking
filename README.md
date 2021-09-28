# Cute Ranking
> A cute little python module for calculating different ranking metrics. Based entirely on the gist from https://gist.github.com/bwhite/3726239.


[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cute-ranking)](https://pypi.org/project/cute-ranking/)
[![PyPI Status](https://badge.fury.io/py/cute-ranking.svg)](https://badge.fury.io/py/cute-ranking)
[![PyPI Status](https://pepy.tech/badge/cute-ranking)](https://pepy.tech/project/cute-ranking)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/ncoop57/cute-ranking/blob/main/LICENSE)

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
4. Recall at K - `recall_at_k`
5. F1 score at K - `f1_score_at_k`
6. Average Precision - `average_precision`
7. Mean Average Precision - `mean_average_precision`
8. Discounted Cumulative Gain at K - `dcg_at_k`
9. Normalized Discounted Cumulative Gain at K - `ndcg_at_k`
10. Mean Rank - `mean_rank`
11. Hit@k - `hit_rate_at_k`

# Contributing
PRs and issues welcome! Please make sure to read through the `CONTRIBUTING.md` doc for how to contribute :).
