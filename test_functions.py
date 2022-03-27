from main import *




def test_addOne():
    for i in range(1,10):
        assert addOne(i) == i+1


def test_subtractOne():
    for i in range(10):
        assert subtractOne(i) == i-1


def test_mult():
    for i in range(10):
        assert multBy2(i) == 2*i