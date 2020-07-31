
import unittest

from .HierarchyAndStructure import HierarchyAndStructure

class TestHierarchyAndStructure:

    __data = None

    def __init__(self):
        self.__data = {
            'Z':{"one":{"two":{"three":"four"}}},
            'hello': 'there',
            "2": 4,
            "empty_string_dq":"",
            "empty_string_sq":'',
            "zero":0,
            "empty":None,
            "set": {'e',4,'wow',(9,0)},
            "s": (1,4,{'one':'five'},[3,4,"f",{"wo":'ho'}]),
            "1":[
                3,
                {},
                (),
                [],
                {'one':'two'}
            ],
            "t":[1,3,4],
            "x":["e","r"]
        }

    def test_values(self):
        hands = HierarchyAndStructure(self.__data)
