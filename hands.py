import json
import sys
import argparse

from TestHierarchyData import TestHierarchyData
from HierarchyAndStructure import HierarchyAndStructure

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--get")
arg_parser.add_argument("--query")
arg_parser.add_argument("--source")
arg_parser.add_argument("--values")
arg_parser.add_argument("--obj_keys")
arg_parser.add_argument("--py_keys")

args = arg_parser.parse_args()

print(args)

data = None
filepath = None

#piped input takes precedence over file source
if not sys.stdin.isatty():
    data = json.load(sys.stdin)
elif args.source is not None and len(args.source) > 0:
    filepath = args.source

if data is not None or filepath is not None:
    hands = HierarchyAndStructure(data, filepath)
