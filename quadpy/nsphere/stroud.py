# -*- coding: utf-8 -*-
#
from __future__ import division

import math

import numpy

from ..helpers import untangle, fsd, fsd2, pm_array0, pm

from .stroud1967 import Stroud1967
from .helpers import integrate_monomial_over_unit_nsphere


class Stroud(object):
    '''
    Arthur Stroud,
    Approximate Calculation of Multiple Integrals,
    Prentice Hall, 1971.
    '''
    def __init__(self, n, index):
        self.dim = n
        if index == 'Un 3-1':
            self.degree = 3
            data = [
                (0.5/n, fsd(n, 1.0, 1)),
                ]
            self.points, self.weights = untangle(data)
            self.weights *= integrate_monomial_over_unit_nsphere(n * [0])
        elif index == 'Un 3-2':
            self.degree = 3
            data = [
                (0.5**n, pm(n, math.sqrt(1.0/n))),
                ]
            self.points, self.weights = untangle(data)
            self.weights *= integrate_monomial_over_unit_nsphere(n * [0])
        elif index == 'Un 5-1':
            self.degree = 5

            B1 = (4.0 - n) / (2.0*n*(n+2))
            B2 = 1.0 / n / (n+2)

            data = [
                (B1, fsd(n, 1.0, 1)),
                (B2, fsd(n, math.sqrt(0.5), 2)),
                ]

            self.points, self.weights = untangle(data)
            self.weights *= integrate_monomial_over_unit_nsphere(n * [0])
        elif index == 'Un 5-2':
            self.degree = 5

            B1 = 1.0 / n / (n+2)
            B2 = n / 2**n / (n+2)

            data = [
                (B1, fsd(n, 1.0, 1)),
                (B2, pm(n, math.sqrt(1.0/n))),
                ]

            self.points, self.weights = untangle(data)
            self.weights *= integrate_monomial_over_unit_nsphere(n * [0])
        elif index == 'Un 5-3':
            self.degree = 5

            s = math.sqrt(1.0 / (n+2))
            B = [
                2.0**(k-n) * (n+2) / n / (k+1) / (k+2)
                for k in range(1, n+1)
                ]
            r = [
                math.sqrt((k+2) / (n+2))
                for k in range(1, n+1)
                ]
            data = [
                (B[k], pm_array0(n, [r[k]] + (n-k-1)*[s], range(k, n)))
                for k in range(n)
                ]

            self.points, self.weights = untangle(data)
            self.weights *= integrate_monomial_over_unit_nsphere(n * [0])
        elif index == 'Un 5-4':
            self.degree = 5

            s = math.sqrt(2*(n+2))
            u = math.sqrt((n + 2 + (n-1)*s) / n / (n+2))
            v = math.sqrt((n + 2 - s) / n / (n+2))

            data = [
                (1.0/2**n/n, fsd2(n, u, v, 1, n-1)),
                ]

            self.points, self.weights = untangle(data)
            self.weights *= integrate_monomial_over_unit_nsphere(n * [0])
        elif index == 'Un 7-1':
            self.set_data(Stroud1967(n))
        elif index == 'Un 7-2':
            self.degree = 7

            A = -n**2 / 2.0**(n+3) / (n+2)
            B = (n+4)**2 / 2.0**(n+3) / n / (n+2)

            r = math.sqrt(1.0 / n)
            s = math.sqrt(5.0 / (n+4))
            t = math.sqrt(1.0 / (n+4))

            data = [
                (A, pm(n, r)),
                (B, fsd2(n, s, t, 1, n-1))
                ]

            self.points, self.weights = untangle(data)
            self.weights *= integrate_monomial_over_unit_nsphere(n * [0])
        else:
            assert index == '11-1'
            assert n >= 5
            self.degree = 11

            plus_minus = numpy.array([+1, -1])
            sqrt3 = math.sqrt(3.0)

            t = math.sqrt(1.0 / n)
            r1, r2 = numpy.sqrt(
                    (n + 6 - plus_minus*4*sqrt3) / (n**2 + 12*n - 12)
                    )
            s1, s2 = numpy.sqrt(
                    (7*n - 6 + plus_minus*4*(n-1)*sqrt3) / (n**2 + 12*n - 12)
                    )
            u1, u2 = numpy.sqrt(
                    (n + 12 + plus_minus*8*sqrt3) / (n**2 + 24*n - 48)
                    )
            v1, v2 = numpy.sqrt(
                    (7*n - 12 - plus_minus*4*(n-2)*sqrt3) / (n**2 + 24*n - 48)
                    )
            # TODO continue here

        return

    def set_data(self, scheme):
        self.degree = scheme.degree
        self.weights = scheme.weights
        self.points = scheme.points
        return
