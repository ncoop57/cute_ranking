# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.ipynb (unless otherwise specified).

__all__ = ['hit_rate_at_k', 'mean_rank', 'mean_reciprocal_rank', 'r_precision', 'r_recall', 'precision_at_k',
           'average_precision', 'mean_average_precision', 'dcg_at_k', 'ndcg_at_k']

# Cell
import numpy as np

# Cell
def hit_rate_at_k(rs, k):
    """Score is percentage of first relevant item in list that occur
    at rank k or lower. First element is 'rank 1'.  Relevance is binary (nonzero is relevant).

    Args:
        rs: Iterator of relevance scores (list or numpy) in rank order
            (first element is the first item)
        k: the largest rank position to consider
    Returns:
        Hit Rate @k
    """
    if k < 1 or k > len(rs[0]):
        raise ValueError('k value must be >=1 and < Max Rank')
    hits = 0
    for r in rs:
        if np.sum(r[:k]) > 0: hits += 1

    return hits / len(rs)

# Cell
def mean_rank(rs):
    """Score is mean rank of the first relevant item in list
    First element is 'rank 1'.  Relevance is binary (nonzero is relevant).

    Args:
        rs: Iterator of relevance scores (list or numpy) in rank order
            (first element is the first item)
    Returns:
        Mean rank
    """
    _rs = []
    for r in rs:
        ids = np.asarray(r).nonzero()[0]
        if len(ids) == 0:
            _rs.append(0)
        else:
            _rs.append(ids[0] + 1)
    return np.mean(_rs)

# Cell
def mean_reciprocal_rank(rs):
    """Score is reciprocal of the rank of the first relevant item
    First element is 'rank 1'.  Relevance is binary (nonzero is relevant).
    Example from http://en.wikipedia.org/wiki/Mean_reciprocal_rank

    Args:
        rs: Iterator of relevance scores (list or numpy) in rank order
            (first element is the first item)
    Returns:
        Mean reciprocal rank
    """
    rs = (np.asarray(r).nonzero()[0] for r in rs)
    return np.mean([1. / (r[0] + 1) if r.size else 0. for r in rs])

# Cell
def r_precision(r):
    """Score is precision after all relevant documents have been retrieved
    Relevance is binary (nonzero is relevant).

    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
    Returns:
        R Precision
    """
    r = np.asarray(r) != 0
    z = r.nonzero()[0]
    if not z.size:
        return 0.
    return np.mean(r[:z[-1] + 1])

# Cell
def r_recall(r, max_rel):
    """Score is recall after all relevant documents have been retrieved
    Relevance is binary (nonzero is relevant).

    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
        max_rel: Maximum number of documents that can be relevant
    Returns:
        R Recall
    """
    r = np.asarray(r) != 0
    z = r.nonzero()[0]
    if not z.size:
        return 0.
    if np.sum(r) > max_rel:
        raise ValueError('Number of relevant documents retrieved > max_rel')
    return np.sum(r) / max_rel

# Cell
def precision_at_k(r, k):
    """Score is precision @ k
    Relevance is binary (nonzero is relevant).

    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
    Returns:
        Precision @ k
    Raises:
        ValueError: len(r) must be >= k
    """
    assert k >= 1
    r = np.asarray(r)[:k] != 0
    if r.size != k:
        raise ValueError('Relevance score length < k')
    return np.mean(r)

# Cell
def average_precision(r):
    """Score is average precision (area under PR curve)
    Relevance is binary (nonzero is relevant).

    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
    Returns:
        Average precision
    """
    r = np.asarray(r) != 0
    out = [precision_at_k(r, k + 1) for k in range(r.size) if r[k]]
    if not out:
        return 0.
    return np.mean(out)

# Cell
def mean_average_precision(rs):
    """Score is mean average precision
    Relevance is binary (nonzero is relevant).

    Args:
        rs: Iterator of relevance scores (list or numpy) in rank order
            (first element is the first item)
    Returns:
        Mean average precision
    """
    return np.mean([average_precision(r) for r in rs])


# Cell
def dcg_at_k(r, k, method=0):
    """Score is discounted cumulative gain (dcg)
    Relevance is positive real values.  Can use binary
    as the previous methods.
    Example from
    http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per.pdf

    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
        k: Number of results to consider
        method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
                If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    Returns:
        Discounted cumulative gain
    """
    r = np.asfarray(r)[:k]
    if r.size:
        if method == 0:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
        elif method == 1:
            return np.sum(r / np.log2(np.arange(2, r.size + 2)))
        else:
            raise ValueError('method must be 0 or 1.')
    return 0.

# Cell
def ndcg_at_k(r, k, method=0):
    """Score is normalized discounted cumulative gain (ndcg)
    Relevance is positive real values.  Can use binary
    as the previous methods.
    Example from
    http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per.pdf

    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
        k: Number of results to consider
        method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
                If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    Returns:
        Normalized discounted cumulative gain
    """
    dcg_max = dcg_at_k(sorted(r, reverse=True), k, method)
    if not dcg_max:
        return 0.
    return dcg_at_k(r, k, method) / dcg_max