# -*- coding: utf-8 -*-
#
import numpy
import pytest
import quadpy
from quadpy.nsimplex.helpers import integrate_monomial_over_unit_simplex

from helpers import check_degree


@pytest.mark.parametrize(
    "scheme",
    [quadpy.nsimplex.grundmann_moeller(dim, k) for dim in range(3, 7) for k in range(5)]
    #
    + [quadpy.nsimplex.stroud_tn_1_1(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_1_2(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_2_1a(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_2_1b(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_2_2(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_1(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_2(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_3(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_4(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_5(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_6a(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_6b(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_7(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_8(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_9(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_4_1(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_5_1(dim) for dim in range(3, 7)]
    + [quadpy.nsimplex.stroud_tn_3_10(dim) for dim in [3, 4, 6, 7]]
    + [quadpy.nsimplex.stroud_tn_3_11(dim) for dim in [3, 4, 6, 7]]
    + [quadpy.nsimplex.stroud_tn_52(dim) for dim in range(4, 8)]
    #
    + [quadpy.nsimplex.walkington_3(k) for k in [1, 2, 3, 5, 7]]
    + [quadpy.nsimplex.walkington_4(k) for dim in range(4, 7) for k in [1, 2, 3]],
)
def test_scheme(scheme):
    assert scheme.points.dtype in [numpy.float64, numpy.int64], scheme.name
    assert scheme.weights.dtype in [numpy.float64, numpy.int64], scheme.name

    n = scheme.dim
    simplex = numpy.zeros((n + 1, n))
    for k in range(n):
        simplex[k + 1, k] = 1.0
    degree = check_degree(
        lambda poly: quadpy.nsimplex.integrate(poly, simplex, scheme),
        integrate_monomial_over_unit_simplex,
        n,
        scheme.degree + 1,
    )
    assert degree >= scheme.degree, "Observed: {}, expected: {}".format(
        degree, scheme.degree
    )
    return


if __name__ == "__main__":
    n_ = 3
    scheme_ = quadpy.nsimplex.Stroud(n_, "Tn 5-1")
    test_scheme(scheme_)
