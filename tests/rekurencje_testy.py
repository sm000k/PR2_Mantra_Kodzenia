import pytest

import rekurencje.rekurencje
from main import *


def test_first_test():
    assert print_hi("HULK") == f'Hi, HULK'


def test_numerated_text():
    rekurencje.rekurencje.numerated_text(10, 'asc')