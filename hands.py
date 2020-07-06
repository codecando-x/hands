
'''

cat file.json | hands.py -s z.one.two.three
cat file.json | hands.py -q "select * from cities"
hands.py -s file.json -s z.one.two.three

#prints access keys of how they would be used as parameters to -s
hands.py -s file.json -k

we could write something similar in javascript and create a UI for it under jsonsql.co
where people can paste in or load json files and then query them easier
for prototyping and getting fast insights from json datasets

'''

import json
import sys
import types

from TestHierarchyData import TestHierarchyData
from HierarchyAndStructure import HierarchyAndStructure

data  = TestHierarchyData().sample()

print(data)
#print(json.dumps(test_hierarchy, indent=4))

#data = json.load(sys.stdin)

'''
def access_keys(self, current, hier: str = ''):

    current_type = type(current)

    if current_type in self.empties.keys():
        empty = self.empties[current_type]
        if len(current) == 0:
            print(hier + ' : ' + empty)
            return
        template = self.templates[current_type]
    else:
        empty = str(None)

    if current_type is dict:
        items = list(current.items())
    elif current_type in [list, tuple, set]:
        items = list(enumerate(current))

    for key, val in items:
        val_type = type(val)
        h = template.format(hier,str(key))
        if val_type in [dict, list, tuple, set]:
            self.access_keys(val, h)
        else:
            v = str(val)
            if val_type is str and len(v) == 0:
                v = '""'

            print("{} : {}".format(h, v))
'''

hands = HierarchyAndStructure(data)

print(hands.get('X.t.0'))

'''
print(obj.Z.one.two.three)
print(obj.i2)
print(obj.s.i0)
print(obj.s.i3.i0)
print(obj.i1.i0)
print(obj.i1.i4.one)
'''
