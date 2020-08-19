import pathlib

from ...helpers import article
from .._helpers import _read, register

_source = article(
    authors=["Philip Rabinowitz", "Nira Richter"],
    title="Perfectly Symmetric Two-Dimensional Integration Formulas with Minimal Numbers of Points",
    journal="Mathematics of Computation",
    volume="23",
    number="108",
    month="oct",
    year="1969",
    pages="765-779",
    url="https://doi.org/10.2307/2004962",
)

this_dir = pathlib.Path(__file__).resolve().parent


def rabinowitz_richter_1():
    return _read(this_dir / "rabinowitz_richter_1.json", _source)


def rabinowitz_richter_2():
    return _read(this_dir / "rabinowitz_richter_2.json", _source)


def rabinowitz_richter_3():
    return _read(this_dir / "rabinowitz_richter_3.json", _source)


def rabinowitz_richter_4():
    return _read(this_dir / "rabinowitz_richter_4.json", _source)


def rabinowitz_richter_5():
    return _read(this_dir / "rabinowitz_richter_5.json", _source)


register([rabinowitz_richter_1, rabinowitz_richter_2, rabinowitz_richter_3,
    rabinowitz_richter_4, rabinowitz_richter_5])
