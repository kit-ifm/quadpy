<p align="center">
  <a href="https://github.com/nschloe/quadpy"><img alt="quadpy" src="https://nschloe.github.io/quadpy/logo-with-text.svg" width="60%"></a>
  <p align="center">Your one-stop shop for numerical integration in Python.</p>
</p>

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/quadpy/master.svg?style=flat-square)](https://circleci.com/gh/nschloe/quadpy/tree/master)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/quadpy.svg?style=flat-square)](https://codecov.io/gh/nschloe/quadpy)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![awesome](https://img.shields.io/badge/awesome-yes-brightgreen.svg?style=flat-square)](https://github.com/nschloe/quadpy)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/quadpy.svg?style=flat-square)](https://pypi.org/pypi/quadpy/)
[![PyPi Version](https://img.shields.io/pypi/v/quadpy.svg?style=flat-square)](https://pypi.org/project/quadpy)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1173132.svg?style=flat-square)](https://doi.org/10.5281/zenodo.1173132)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/quadpy.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/quadpy)
[![PyPi downloads](https://img.shields.io/pypi/dm/quadpy.svg?style=flat-square)](https://pypistats.org/packages/quadpy)
[![Slack](https://img.shields.io/static/v1?logo=slack&label=slack&message=chat&color=4a154b&style=flat-square)](https://app.slack.com/client/TTL6Q54A3/CT865V1QR)

More than 1500 numerical integration schemes for
[line segments](#line-segment),
[circles](#circle),
[disks](#disk),
[triangles](#triangle),
[quadrilaterals](#quadrilateral),
[spheres](#sphere),
[balls](#ball),
[tetrahedra](#tetrahedron),
[hexahedra](#hexahedron),
[wedges](#wedge),
[pyramids](#pyramid),
[n-spheres](#n-sphere),
[n-balls](#n-ball),
[n-cubes](#n-cube),
[n-simplices](#n-simplex),
[the 1D half-space with weight functions exp(-r)](#1d-half-space-with-weight-function-exp-r),
[the 2D space with weight functions exp(-r)](#2d-space-with-weight-function-exp-r),
[the 3D space with weight functions exp(-r)](#3d-space-with-weight-function-exp-r),
[the nD space with weight functions exp(-r)](#nd-space-with-weight-function-exp-r),
[the 1D space with weight functions exp(-r<sup>2</<sup>)](#1d-space-with-weight-function-exp-r2),
[the 2D space with weight functions exp(-r<sup>2</<sup>)](#2d-space-with-weight-function-exp-r2),
[the 3D space with weight functions exp(-r<sup>2</<sup>)](#3d-space-with-weight-function-exp-r2),
and
[the nD space with weight functions exp(-r<sup>2</<sup>)](#nd-space-with-weight-function-exp-r2),
for fast integration of real-, complex-, and vector-valued functions.

For example, to numerically integrate any function over any given interval, install
quadpy [from the Python Package Index](https://pypi.org/project/quadpy/) with
```
pip install quadpy
```
and do
```python
import numpy
import quadpy

def f(x):
   return numpy.sin(x) - x

val, err = quadpy.quad(f, 0.0, 6.0)
```
This is just like
[scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html)
with the addition that quadpy handles complex-, vector-, matrix-valued integrands,
and "intervals" in spaces of arbitrary dimension.

To integrate over a _triangle_ with [Strang's rule](https://bookstore.siam.org/wc08/) of
degree 6, do
```python
import numpy
import quadpy

def f(x):
    return numpy.sin(x[0]) * numpy.sin(x[1])

triangle = numpy.array([[0.0, 0.0], [1.0, 0.0], [0.7, 0.5]])

val = quadpy.triangle.strang_fix_cowper_09().integrate(f, triangle)
```

All schemes have
```python
scheme.points
scheme.weights
scheme.degree
scheme.citation

scheme.show()
scheme.integrate(
    # ...
)
```
and many have
```python
scheme.points_symbolic
scheme.weights_symbolic
```

quadpy is fully vectorized, so if you like to compute the integral of a function on many
domains at once, you can provide them all in one `integrate()` call, e.g.,
```python
# shape (3, 5, 2), i.e., (corners, num_triangles, xy_coords)
triangles = numpy.stack([
    [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]],
    [[1.2, 0.6], [1.3, 0.7], [1.4, 0.8]],
    [[26.0, 31.0], [24.0, 27.0], [33.0, 28]],
    [[0.1, 0.3], [0.4, 0.4], [0.7, 0.1]],
    [[8.6, 6.0], [9.4, 5.6], [7.5, 7.4]]
    ], axis=-2)
```
The same goes for functions with vectorized output, e.g.,
```python
def f(x):
    return [numpy.sin(x[0]), numpy.sin(x[1])]
```

More examples under [test/examples_test.py](https://github.com/nschloe/quadpy/blob/master/test/examples_test.py).

Read more about the dimensionality of the input/output arrays [in the
wiki](https://github.com/nschloe/quadpy/wiki#dimensionality-of-input-and-output-arrays).

Advanced topics:

  * [Adaptive quadrature](https://github.com/nschloe/quadpy/wiki/Adaptive-quadrature)
  * [Creating your own Gauss scheme](https://github.com/nschloe/quadpy/wiki/Creating-your-own-Gauss-quadrature-in-two-simple-steps)
  * [tanh-sinh quadrature](https://github.com/nschloe/quadpy/wiki/tanh-sinh-quadrature)


## Schemes

### Line segment
<img src="https://nschloe.github.io/quadpy/line-segment-gauss-legendre-20.svg" width="50%">

 * [Chebyshev-Gauss](quadpy/line_segment/_chebyshev_gauss.py) (type 1 and 2, arbitrary degree)
 * [Clenshaw-Curtis](quadpy/line_segment/_clenshaw_curtis.py) (arbitrary degree)
 * [Fejér](quadpy/line_segment/_fejer.py) (type 1 and 2, arbitrary degree)
 * [Gauss-Jacobi](quadpy/line_segment/_gauss_jacobi.py)
 * [Gauss-Legendre](line_segment/_gauss_legendre.py) (arbitrary degree)
 * [Gauss-Lobatto](quadpy/line_segment/_gauss_lobatto.py) (arbitrary degree)
 * [Gauss-Kronrod](quadpy/line_segment/_gauss_kronrod.py) (arbitrary degree)
 * [Gauss-Patterson](quadpy/line_segment/_gauss_patterson.py) (9 nested schemes up to degree 767)
 * [Gauss-Radau](quadpy/line_segment/_gauss_radau.py) (arbitrary degree)
 * [Newton-Cotes](quadpy/line_segment/_newton_cotes.py) (open and closed, arbitrary degree)
 * [tanh-sinh quadrature](quadpy/tanh_sinh.py) (see above)

[See
her](https://github.com/nschloe/quadpy/wiki/Creating-your-own-Gauss-quadrature-in-two-simple-steps)
for how to generate Gauss formulas for your own weight functions.

Example:
```python
import numpy
import quadpy

scheme = quadpy.line_segment.gauss_patterson(5)
scheme.show()
val = scheme.integrate(lambda x: numpy.exp(x), [0.0, 1.0])
```

### 1D half-space with weight function exp(-r)
<img src="https://nschloe.github.io/quadpy/e1r-gauss-laguerre-3.svg" width="50%">

 * [Generalized Gauss-Laguerre](quadpy/e1r/_gauss_laguerre.py)

Example:
```python
import quadpy

scheme = quadpy.e1r.gauss_laguerre(5, alpha=0)
scheme.show()
val = scheme.integrate(lambda x: x**2)
```


### 1D space with weight function exp(-r<sup>2</sup>)
<img src="https://nschloe.github.io/quadpy/e1r2-gauss-hermite-8.svg" width="50%">

 * [Gauss-Hermite](quadpy/e1r2/_gauss_hermite.py) (arbitrary degree)
 * [Genz-Keister](quadpy/e1r2/_genz_keister.py) (1996, 8 nested schemes up to degree 67)

Example:
```python
import quadpy

scheme = quadpy.e1r2.gauss_hermite(5)
scheme.show()
val = scheme.integrate(lambda x: x**2)
```

### Circle
<img src="https://nschloe.github.io/quadpy/circle-krylov-30.svg" width="25%">

 * [Krylov](quadpy/circle/_krylov.py) (1959, arbitrary degree)

Example:
```python
import quadpy

scheme = quadpy.circle.krylov(7)
scheme.show()
val = scheme.integrate(lambda x: numpy.exp(x[0]), [0.0, 0.0], 1.0)
```

### Triangle
<img src="https://nschloe.github.io/quadpy/triangle-dunavant-15.svg" width="25%">

Apart from the classical centroid, vertex, and seven-point schemes we have

 * [Hammer-Marlowe-Stroud](quadpy/triangle/_hammer_marlowe_stroud.py)
   (1956, 5 schemes up to degree 5, also appearing in [Hammer-Stroud](https://doi.org/10.1090/S0025-5718-1958-0102176-6))
 * via [Stroud](quadpy/triangle/_stroud.py) (1971):
   - [Albrecht-Collatz](quadpy/triangle/_albrecht_collatz.py) (1958, degree 3)
   - conical product scheme (degree 7)
 * [Franke](quadpy/triangle/_franke.py) (1971, 2 schemes of degree 7)
 * [Strang-Fix/Cowper](quadpy/triangle/_strang_fix_cowper.py) (1973, 10 schemes up to degree 7),
 * [Lyness-Jespersen](quadpy/triangle/_lyness_jespersen.py) (1975, 21
   schemes up to degree 11, two of which are used in [TRIEX](https://doi.org/10.1145/356068.356070)),
 * [Lether](quadpy/triangle/_lether.py) (1976, degree 2n-2, arbitrary
   n, not symmetric),
 * [Hillion](quadpy/triangle/_hillion.py) (1977, 10 schemes up to
   degree 3),
 * [Laursen-Gellert](quadpy/triangle/_laursen_gellert.py) (1978, 17 schemes up to degree
   10),
 * [CUBTRI](quadpy/triangle/_cubtri.py) (Laurie, 1982, degree 8),
 * [Dunavant](quadpy/triangle/_dunavant.py) (1985, 20 schemes up to degree 20),
 * [Cools-Haegemans](quadpy/triangle/_cools_haegemans.py) (1987, degrees 8 and 11),
 * [Gatermann](quadpy/triangle/_gatermann.py) (1988, degree 7)
 * [Berntsen-Espelid](quadpy/triangle/_berntsen_espelid.py) (1990, 4 schemes of degree
   13, the first one being [DCUTRI](https://dl.acm.org/citation.cfm?id=131772)),
 * [Liu-Vinokur](quadpy/triangle/_liu_vinokur.py) (1998, 13 schemes up to degree 5),
 * [Griener-Schmid](quadpy/triangle/_griener_schmid.py), (1999, 2 schemes of degree 6),
 * [Walkington](quadpy/triangle/_walkington.py) (2000, 5 schemes up to degree 5),
 * [Wandzura-Xiao](quadpy/triangle/_wandzura_xiao) (2003, 6 schemes up to degree 30),
 * [Taylor-Wingate-Bos](quadpy/triangle/_taylor_wingate_bos.py) (2005, 5 schemes up to
   degree 14),
 * [Zhang-Cui-Liu](quadpy/triangle/_zhang_cui_liu.py) (2009, 3 schemes up to
   degree 20),
 * [Xiao-Gimbutas](quadpy/triangle/_xiao_gimbutas) (2010, 50
   schemes up to degree 50),
 * [Vioreanu-Rokhlin](quadpy/triangle/_vioreanu_rokhlin) (2014, 20 schemes up to degree
   62),
 * [Williams-Shunn-Jameson](quadpy/triangle/_williams_shunn_jameson.py) (2014, 8 schemes
   up to degree 12),
 * [Witherden-Vincent](quadpy/triangle/_witherden_vincent) (2015, 19 schemes up to
   degree 20),
 * [Papanicolopulos](quadpy/triangle/_papanicolopulos) (2016, 27 schemes up to degree
   25),
 * [all schemes for the n-simplex](#n-simplex).

Example:
```python
import quadpy

scheme = quadpy.triangle.xiao_gimbutas_05()
scheme.show()
val = scheme.integrate(lambda x: numpy.exp(x[0]), [[0.0, 0.0], [1.0, 0.0], [0.5, 0.7]])
```

### Disk
<img src="https://nschloe.github.io/quadpy/disk-hammer-stroud-20.svg" width="25%">

 * [Peirce](quadpy/disk/_peirce_1957.py) (1957, arbitrary degree)
 * via [Stroud](quadpy/disk/_stroud.py):
   - [Radon](quadpy/disk/_radon.py) (1948, degree 5)
   - [Peirce](quadpy/disk/_peirce_1956.py) (1956, 3 schemes up to degree 11)
   - [Albrecht-Collatz](quadpy/disk/_albrecht_collatz.py) (1958, degree 3)
   - [Hammer-Stroud](quadpy/disk/_hammer_stroud.py) (1958, 8 schemes up to degree 15)
   - [Albrecht](quadpy/disk/_albrecht.py) (1960, 8 schemes up to degree 17)
   - [Mysovskih](quadpy/disk/_mysovskih.py) (1964, 3 schemes up to degree 15)
   - [Rabinowitz-Richter](quadpy/disk/_rabinowitz_richter.py) (1969, 6 schemes up to degree 15)
 * [Lether](quadpy/disk/_lether.py) (1971, arbitrary degree)
 * [Piessens-Haegemans](quadpy/disk/_piessens_haegemans.py) (1975, 1 scheme of degree 9)
 * [Haegemans-Piessens](quadpy/disk/_haegemans_piessens.py) (1977, degree 9)
 * [Cools-Haegemans](quadpy/disk/_cools_haegemans.py) (1985, 3 schemes up to degree 9)
 * [Wissmann-Becker](quadpy/disk/_wissmann_becker.py) (1986, 3 schemes up to degree 8)
 * [Kim-Song](quadpy/disk/_kim_song.py) (1997, 15 schemes up to degree 17)
 * [Cools-Kim](quadpy/disk/_cools_kim.py) (2000, 3 schemes up to degree 21)
 * [all schemes from the n-ball](#n-ball)

Example:
```python
import numpy
import quadpy

scheme = quadpy.disk.lether(6)
scheme.show()
val = scheme.integrate(lambda x: numpy.exp(x[0]), [0.0, 0.0], 1.0)
```

### Quadrilateral
<img src="https://nschloe.github.io/quadpy/quad-maxwell.svg" width="25%">

 * [Hammer-Stroud](quadpy/quadrilateral/_hammer_stroud.py) (1958, 3
   schemes up to degree 7)
 * via [Stroud](quadpy/quadrilateral/_stroud.py) (1971, 15 schemes up to degree 15):
   - [Maxwell](quadpy/quadrilateral/_maxwell.py) (1890, degree 7)
   - [Burnside](quadpy/quadrilateral/_burnside.py) (1908, degree 5)
   - [Irwin](quadpy/quadrilateral/_irwin.py) (1923, 3 schemes up to degree 5)
   - [Tyler](quadpy/quadrilateral/_tyler.py) (1953, 3 schemes up to degree 7)
   - [Albrecht-Collatz](quadpy/quadrilateral/_albrecht_collatz.py) (1958, 4 schemes up to degree 5)
   - [Miller](quadpy/quadrilateral/_miller.py) (1960, degree 1)
   - [Meister](quadpy/quadrilateral/_meister.py) (1966, degree 7)
   - [Phillips](quadpy/quadrilateral/_phillips.py) (1967, degree 7)
   - [Rabinowitz-Richter](quadpy/quadrilateral/_rabinowitz_richter.py) (1969, 6 schemes up to degree 15)
 * [Franke](quadpy/quadrilateral/_franke.py) (1971, 10 schemes up to degree 9)
 * [Piessens-Haegemans](quadpy/quadrilateral/_piessens_haegemans.py) (1975, 2 schemes of degree 9)
 * [Haegemans-Piessens](quadpy/quadrilateral/_haegemans_piessens.py) (1977, degree 7)
 * [Schmid](quadpy/quadrilateral/_schmid.py) (1978, 3 schemes up to degree 6)
 * [Cools-Haegemans](quadpy/quadrilateral/_cools_haegemans_1985.py) (1985, 3 schemes up to degree 13)
 * [Dunavant](quadpy/quadrilateral/_dunavant.py) (1985, 11 schemes up to degree 19)
 * [Morrow-Patterson](quadpy/quadrilateral/_morrow_patterson.py) (1985, 2 schemes up to degree 20, single precision)
 * [Cohen-Gismalla](quadpy/quadrilateral/_cohen_gismalla.py), (1986, 2 schemes up to degree 3, single precision)
 * [Wissmann-Becker](quadpy/quadrilateral/_wissmann_becker.py) (1986, 6 schemes up to degree 8)
 * [Cools-Haegemans](quadpy/quadrilateral/_cools_haegemans_1988.py) (1988, 2 schemes up to degree 13)
 * [Waldron](quadpy/quadrilateral/_waldron.py) (1994, infinitely many schemes of degree 3)
 * [Sommariva](quadpy/quadrilateral/_sommariva.py) (2012, 55 schemes up to degree 55)
 * [Witherden-Vincent](quadpy/quadrilateral/_witherden_vincent.py) (2015, 11 schemes up to degree 21)
 * products of line segment schemes
 * [all schemes from the n-cube](#n-cube)

Example:
```python
import numpy
import quadpy

scheme = quadpy.quadrilateral.stroud_c2_7_2()
val = scheme.integrate(
    lambda x: numpy.exp(x[0]),
    [[[0.0, 0.0], [1.0, 0.0]], [[0.0, 1.0], [1.0, 1.0]]],
    )
```
The points are specified in an array of shape (2, 2, ...) such that `arr[0][0]`
is the lower left corner, `arr[1][1]` the upper right. If your quadrilateral
has its sides aligned with the coordinate axes, you can use the convenience
function
```python
quadpy.quadrilateral.rectangle_points([x0, x1], [y0, y1])
```
to generate the array.


### 2D space with weight function exp(-r)
<img src="https://nschloe.github.io/quadpy/e2r-rabinowitz-richter-5.svg" width="25%">

 * via [Stroud](quadpy/e2r/_stroud.py) (1971):
   - [Stroud-Secrest](quadpy/e2r/_stroud_secrest.py) (1963, 2 schemes up to degree 7)
   - [Rabinowitz-Richter](quadpy/e2r/_rabinowitz_richter.py) (1969, 4 schemes up to degree 15)
   - [a scheme of degree 4](quadpy/e2r/_stroud.py)
 * [Haegemans-Piessens](quadpy/e2r/_haegemans_piessens.py) (1977, 2 schemes up to degree 9)
 * all schemes from the nD space with weight function exp(-r)

Example:
```python
import quadpy

scheme = quadpy.e2r.rabinowitz_richter_5()
scheme.show()
val = scheme.integrate(lambda x: x[0]**2)
```


### 2D space with weight function exp(-r<sup>2</sup>)
<img src="https://nschloe.github.io/quadpy/e2r2-rabinowitz-richter-3.svg" width="25%">

 * via [Stroud](quadpy/e2r2/_stroud.py) (1971):
   - [Stroud-Secrest](quadpy/e2r2/_stroud_secrest.py) (1963, 2 schemes up to degree 7)
   - [Rabinowitz-Richter](quadpy/e2r2/_rabinowitz_richter.py) (1969, 5 schemes up to degree 15)
   - [3 schemes up to degree 7](quadpy/e2r2/_stroud.py)
 * [Haegemans-Piessens](quadpy/e2r2/_haegemans_piessens.py) (1977, 2 schemes of degree 9)
 * all schemes from the nD space with weight function exp(-r<sup>2<sup>)

Example:
```python
import quadpy

scheme = quadpy.e2r2.rabinowitz_richter_3()
scheme.show()
val = scheme.integrate(lambda x: x[0]**2)
```


### Sphere
<img src="https://nschloe.github.io/quadpy/sphere.png" width="25%">

 * via [Stroud](quadpy/sphere/_stroud.py) (1971):
   - [Albrecht-Collatz](quadpy/sphere/_albrecht_collatz.py) (1958, 5
     schemes up to degree 7)
   - [McLaren](quadpy/sphere/_mclaren.py) (1963, 10 schemes up to degree 14)
 * [Lebedev](quadpy/sphere/_lebedev.py) (1976, 34 schemes up to degree 131)
 * [Bažant-Oh](quadpy/sphere/_bazant_oh.py) (1986, 3 schemes up to degree 11)
 * [Heo-Xu](quadpy/sphere/_heo_xu.py) (2001, 27 schemes up to degree 39,
   single-precision)
 * [Fliege-Maier](quadpy/sphere/_fliege_maier.py) (2007, 4 schemes up to degree 4,
   single-precision)
 * [all schemes from the n-sphere](#n-sphere)

Example:
```python
import numpy
import quadpy

scheme = quadpy.sphere.lebedev_019()
scheme.show()
val = scheme.integrate(lambda x: numpy.exp(x[0]), [0.0, 0.0, 0.0], 1.0)
```
Integration on the sphere can also be done for function defined in spherical
coordinates:
```python
import numpy
import quadpy

scheme = quadpy.sphere.lebedev_019()
val = scheme.integrate_spherical(
    lambda azimuthal, polar: numpy.sin(azimuthal)**2 * numpy.sin(polar),
    )
```

### Ball
<img src="https://nschloe.github.io/quadpy/ball.png" width="25%">

 * [Hammer-Stroud](quadpy/ball/_hammer_stroud.py) (1958, 6 schemes up to degree 7)
 * via: [Stroud](quadpy/ball/_stroud.py) (1971):
   - [Ditkin](quadpy/ball/_ditkin.py) (1948, 3 schemes up to degree 7)
   - [Mysovskih](quadpy/ball/)mysovskih.py) (1964, degree 7)
   - [2 schemes up to degree 14](quadpy/ball/_stroud.py)
 * [all schemes from the n-ball](#n-ball)

Example:
```python
import numpy
import quadpy

scheme = quadpy.ball.hammer_stroud_14_3()
scheme.show()
val = scheme.integrate(
    lambda x: numpy.exp(x[0]),
    [0.0, 0.0, 0.0], 1.0,
    )
```


### Tetrahedron
<img src="https://nschloe.github.io/quadpy/tet.png" width="25%">

 * [Hammer-Marlowe-Stroud](quadpy/tetrahedron/_hammer_marlowe_stroud.py)
   (1956, 3 schemes up to degree 3, also appearing in [Hammer-Stroud](https://doi.org/10.1090/S0025-5718-1958-0102176-6))
 * [Stroud](quadpy/tetrahedron/_stroud.py) (1971, degree 7)
 * [Grundmann-Möller](quadpy/tetrahedron/_grundmann_moeller.py) (1978, arbitrary degree),
 * [Yu](quadpy/tetrahedron/_yu.py) (1984, 5 schemes up to degree 6)
 * [Keast](quadpy/tetrahedron/_keast.py) (1986, 10 schemes up to degree 8)
 * [Beckers-Haegemans](quadpy/tetrahedron/_beckers_haegemans.py) (1990, degrees 8 and 9)
 * [Gatermann](quadpy/tetrahedron/_gatermann.py) (1992, degree 5)
 * [Liu-Vinokur](quadpy/tetrahedron/_liu_vinokur.py) (1998, 14 schemes up to degree 5)
 * [Walkington](quadpy/tetrahedron/_walkington.py) (2000, 6 schemes up to degree 7)
 * [Zhang-Cui-Liu](quadpy/tetrahedron/_zhang_cui_liu.py) (2009, 2 schemes up to degree
   14)
 * [Xiao-Gimbutas](quadpy/tetrahedron/_xiao_gimbutas/) (2010, 15 schemes up to degree
   15)
 * [Shunn-Ham](quadpy/tetrahedron/_shunn_ham.py) (2012, 6 schemes up to degree 7)
 * [Vioreanu-Rokhlin](quadpy/tetrahedron/_vioreanu_rokhlin.py) (2014, 10 schemes up to
   degree 13)
 * [Williams-Shunn-Jameson](quadpy/tetrahedron/_williams_shunn_jameson.py) (2014, 1
   scheme with degree 9)
 * [Witherden-Vincent](quadpy/tetrahedron/_witherden_vincent.py) (2015, 9 schemes up to
   degree 10)
 * [Jaśkowiec-Sukumar](quadpy/tetrahedron/_jaskowiec_sukumar/) (2020, 21
   schemes up to degree 20)
 * [all schemes for the n-simplex](#n-simplex).

Example:
```python
import numpy
import quadpy

scheme = quadpy.tetrahedron.keast_10()
scheme.show()
val = scheme.integrate(
    lambda x: numpy.exp(x[0]),
    [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.5, 0.7, 0.0], [0.3, 0.9, 1.0]],
    )
```

### Hexahedron
<img src="https://nschloe.github.io/quadpy/hexa.png" width="25%">

 * Product schemes derived from line segment schemes
 * via: [Stroud](quadpy/hexahedron/_stroud.py) (1971):
   - [Sadowsky](quadpy/hexahedron/_sadowsky.py) (1940, degree 5)
   - [Tyler](quadpy/hexahedron/_tyler.py) (1953, 2 schemes up to degree 5)
   - [Hammer-Wymore](quadpy/hexahedron/_hammer_wymore.py) (1957, degree 7)
   - [Albrecht-Collatz](quadpy/hexahedron/_albrecht_collatz.py) (1958, degree 3)
   - [Hammer-Stroud](quadpy/hexahedron/_hammer_stroud.py) (1958, 6 schemes up to degree 7)
   - [Mustard-Lyness-Blatt](quadpy/hexahedron/_mustard_lyness_blatt.py) (1963, 6 schemes up to degree 5)
   - [Stroud](quadpy/hexahedron/_stroud_1967.py) (1967, degree 5)
   - [Sarma-Stroud](quadpy/hexahedron/_sarma_stroud.py) (1969, degree 7)
 * [all schemes from the n-cube](#n-cube)

Example:
```python
import numpy
import quadpy

scheme = quadpy.hexahedron.product(quadpy.line_segment.newton_cotes_closed(3))
scheme.show()
val = scheme.integrate(
    lambda x: numpy.exp(x[0]),
    quadpy.hexahedron.cube_points([0.0, 1.0], [-0.3, 0.4], [1.0, 2.1]),
    )
```

### Pyramid
<img src="https://nschloe.github.io/quadpy/pyra.png" width="25%">

 * [Felippa](quadpy/pyramid/_felippa.py) (2004, 9 schemes up to degree 5)

Example:
```python
import numpy
import quadpy

scheme = quadpy.pyramid.felippa_5()

val = scheme.integrate(
    lambda x: numpy.exp(x[0]),
    [
      [0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.5, 0.7, 0.0], [0.3, 0.9, 0.0],
      [0.0, 0.1, 1.0],
    ]
    )
```

### Wedge
<img src="https://nschloe.github.io/quadpy/wedge.png" width="15%">

 * [Felippa](quadpy/wedge/_felippa.py) (2004, 6 schemes up to degree 6)
 * [Kubatko-Yeager-Maggi](quadpy/wedge/_kubatko_yeager_maggi.py) (2013, 21 schemes up to
   degree 9)

Example:
```python
import numpy
import quadpy

scheme = quadpy.wedge.felippa_3
val = quadpy.wedge.integrate(
    lambda x: numpy.exp(x[0]),
    [
      [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.5, 0.7, 0.0]],
      [[0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.5, 0.7, 1.0]],
    ]
    )
```


### 3D space with weight function exp(-r)
<img src="https://nschloe.github.io/quadpy/e3r.png" width="25%">

 * via [Stroud](quadpy/e3r/_stroud.py) (1971):
   - [Stroud-Secrest](quadpy/e3r/_stroud_secrest.py) (1963, 5 schemes up to degree 7)
 * [all schemes from the nD space with weight function
   exp(-r)](nd-space-with-weight-function-exp-r)

Example:
```python
import quadpy

scheme = quadpy.e3r.stroud_secrest_09()
scheme.show()
val = scheme.integrate(lambda x: x[0]**2)
```


### 3D space with weight function exp(-r<sup>2</sup>)
<img src="https://nschloe.github.io/quadpy/e3r2.png" width="25%">

 * via [Stroud](quadpy/e3r/_stroud.py) (1971):
   - [Stroud-Secrest](quadpy/e3r/_stroud_secrest.py) (1963, 7 schemes up to degree 7)
   - [scheme of degree 14](quadpy/e3r/_stroud.py)
 * [all schemes from the nD space with weight function
   exp(-r<sup>2</sup>)](nd-space-with-weight-function-exp-r2)

Example:
```python
import quadpy

scheme = quadpy.e3r2.stroud_secrest_10a()
scheme.show()
val = scheme.integrate(lambda x: x[0]**2)
```

### n-Simplex
 * via [Stroud](quadpy/nsimplex/_stroud.py):
   - [Lauffer](quadpy/nsimplex/_lauffer.py) (1955, 5 schemes up to degree 5)
   - [Hammer-Stroud](quadpy/nsimplex/_hammer_stroud.py) (1956, 3 schemes up to degree 3)
   - [Stroud](quadpy/nsimplex/_stroud_1964.py) (1964, degree 3)
   - [Stroud](quadpy/nsimplex/_stroud_1966.py) (1966, 7 schemes of degree 3)
   - [Stroud](quadpy/nsimplex/_stroud_1969.py) (1969, degree 5)
 * [Silvester](quadpy/nsimplex/_silvester.py) (1970, arbitrary degree),
 * [Grundmann-Möller](quadpy/nsimplex/_grundmann_moeller.py) (1978, arbitrary degree)
 * [Walkington](quadpy/nsimplex/_walkington.py) (2000, 5 schemes up to degree 7)

Example:
```python
import numpy
import quadpy

scheme = quadpy.nsimplex.GrundmannMoeller(dim, 3)
dim = 4
val = scheme.integrate(
    lambda x: numpy.exp(x[0]),
    numpy.array([
        [0.0, 0.0, 0.0, 0.0],
        [1.0, 2.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 3.0, 1.0, 0.0],
        [0.0, 0.0, 4.0, 1.0],
        ])
    )
```

### n-Sphere
 * via [Stroud](quadpy/nsphere/_stroud.py) (1971):
   - [Stroud](quadpy/nsphere/_stroud_1967.py) (1967, degree 7)
   - [Stroud](quadpy/nsphere/_stroud_1969.py) (1969, 3 <= n <= 16, degree 11)
   - [6 schemes up to degree 5](quadpy/nsphere/_stroud.py)
 * [Dobrodeev](quadpy/nsphere/_dobrodeev.py) (1978, n >= 2, degree 5)
 * [Mysovskikh](quadpy/nsphere/_mysovskikh.py) (1980, 2 schemes up to degree 5)

Example:
```python
import numpy
import quadpy

scheme = quadpy.nsphere.dobrodeev_1978(dim)
dim = 4
val = scheme.integrate(lambda x: numpy.exp(x[0]), numpy.zeros(dim), 1.0)
```


### n-Ball
 * [McNamee-Stenger](quadpy/nball/_mcnamee_stenger.py) (1967, 6 schemes up to degree 9)
 * [Dobrodeev](quadpy/nball/_dobrodeev.py) (1970, n >= 3, degree 7)
 * via [Stroud](quadpy/nball/_stroud.py) (1971):
   - [Stroud](quadpy/nball/_stroud_1957.py) (1957, degree 2)
   - [Hammer-Stroud](quadpy/nball/_hammer_stroud.py) (1958, 2 schemes up to degree 5)
   - [Stroud](quadpy/nball/_stroud_1966.py) (1966, 4 schemes of degree 5)
   - [Stroud](quadpy/nball/_stroud_1967a.py) (1967, 4 <= n <= 7, 2 schemes of degree 5)
   - [Stroud](quadpy/nball/_stroud_1967b.py) (1967, n >= 3, 3 schemes of degree 7)
   - [Stenger](quadpy/nball/_stenger.py) (1967, 6 schemes up to degree 11)
 * [Dobrodeev](quadpy/nball/_dobrodeev.py) (1978, 2 <= n <= 20, degree 5)
 * [Stoyanova](quadpy/nball/_stoyanova.py) (1997, n >= 5, degree 7)

Example:
```python
import numpy
import quadpy

scheme = quadpy.nball.dobrodeev_1970(dim)
dim = 4
val = scheme.integrate(lambda x: numpy.exp(x[0]), numpy.zeros(dim), 1.0)
```

### n-Cube
 * [McNamee-Stenger](quadpy/ncube/_mcnamee_stenger.py) (1967, 6 schemes up to degree 9)
 * [Dobrodeev](quadpy/ncube/_dobrodeev.py) (1970, n >= 5, degree 7)
 * via [Stroud](quadpy/ncube/_stroud.py) (1971):
    - [Ewing](quadpy/ncube/_ewing.py) (1941, degree 3)
    - [Tyler](quadpy/ncube/_tyler.py) (1953, degree 3)
    - [Stroud](quadpy/ncube/_stroud_1957.py) (1957, 2 schemes up to degree 3)
    - [Hammer-Stroud](quadpy/ncube/_hammer_stroud.py) (1958, degree 5)
    - [Mustard-Lyness-Blatt](quadpy/ncube/_mustard_lyness_blatt.py) (1963, degree 5)
    - [Thacher](quadpy/ncube/_thacher.py) (1964, degree 2)
    - [Stroud](quadpy/ncube/_stroud_1966.py) (1966, 4 schemes of degree 5)
    - [Phillips](quadpy/ncube/_phillips.py) (1967, degree 7)
    - [Stroud](quadpy/ncube/_stroud_1968.py) (1968, degree 5)
 * [Dobrodeev](quadpy/ncube/_dobrodeev.py) (1978, n >= 2, degree 5)
 * [Cools-Haegemans](quadpy/ncube/_cools_haegemans.py) (1994, 2 schemes up to degree 5)

Example:
```python
import numpy
import quadpy

dim = 4
scheme = quadpy.ncube.stroud_cn_3_3(dim)
quadpy.ncube.integrate(
    lambda x: numpy.exp(x[0]),
    quadpy.ncube.ncube_points(
        [0.0, 1.0], [0.1, 0.9], [-1.0, 1.0], [-1.0, -0.5]
        )
    )
```

### nD space with weight function exp(-r)
 * [McNamee-Stenger](quadpy/enr/_mcnamee_stenger.py) (1967, 6 schemes up to degree 9)
 * via [Stroud](quadpy/enr/_stroud.py) (1971):
   - [Stroud-Secrest](quadpy/enr/_stroud_secrest.py) (1963, 4 schemes up to degree 5)
   - [2 schemes up to degree 5](quadpy/enr/_stroud.py)

Example:
```python
import quadpy

dim = 4
scheme = quadpy.enr.stroud_5_4(dim)
val = scheme.integrate(lambda x: x[0]**2)
```

### nD space with weight function exp(-r<sup>2</sup>)
 * [McNamee-Stenger](quadpy/enr2/_mcnamee_stenger.py) (1967, 6 schemes up to degree 9)
 * via [Stroud](quadpy/enr2/_stroud.py) (1971):
   - [Stroud-Secrest](quadpy/enr2/_stroud_secrest.py) (1963, 4 schemes up to degree 5)
   - [Stroud](quadpy/enr2/_stroud_1967a.py) (1967, 2 schemes of degree 5)
   - [Stroud](quadpy/enr2/_stroud_1967b.py) (1967, 3 schemes of degree 7)
   - [Stenger](quadpy/enr2/_stenger.py) (1971, 6 schemes up to degree 11, varying dimensionality restrictions)
   - [5 schemes up to degree 5](quadpy/enr2/_stroud.py)
 * [Phillips](quadpy/enr2/_phillips.py) (1980, degree 5)
 * [Cools-Haegemans](quadpy/enr2/_cools_haegemans.py) (1994, 3 schemes up to degree 7)
 * [Lu-Darmofal](quadpy/enr2/_lu_darmofal.py) (2004, degree 5)

Example:
```python
import quadpy

dim = 4
scheme = quadpy.enr2.stroud_5_2(dim)
val = scheme.integrate(lambda x: x[0]**2)
```


### Installation

quadpy is [available from the Python Package Index](https://pypi.org/project/quadpy/), so with
```
pip install quadpy
```
you can install.

### Testing

To run the tests, just check out this repository and type
```
MPLBACKEND=Agg pytest
```

### License
This software is published under the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html).
