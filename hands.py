import json
import sys
import argparse

from TestHierarchyData import TestHierarchyData
from HierarchyAndStructure import HierarchyAndStructure

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--get")
arg_parser.add_argument("--query")
arg_parser.add_argument("--source")
arg_parser.add_argument("--values", action='store_const', const=True, default=False)
arg_parser.add_argument("--obj_keys", action='store_const', const=True)
arg_parser.add_argument("--py_keys", action='store_const', const=True)

args = arg_parser.parse_args()

#print(args)

data = None
filepath = None

#piped input takes precedence over file source
if not sys.stdin.isatty():
    data = json.load(sys.stdin)
elif args.source is not None and len(args.source) > 0:
    filepath = args.source
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)

hands = HierarchyAndStructure(data)

if args.get is not None:
    print(hands.get(args.get))
elif args.py_keys is not None:
    print(hands.direct_access_keys(args.values))
elif args.obj_keys is not None:
    print(hands.obj_access_keys(args.values))
