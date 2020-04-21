import sys
sys.path.append(".")
from utils import ConverterFparaC


def test_FtoC():
    assert 0 == ConverterFparaC(32)
    assert 1 != ConverterFparaC(32)
    assert 37,78 != ConverterFparaC(100)