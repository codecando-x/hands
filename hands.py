import json
import sys
import argparse
import mimetypes

from HierarchyAndStructure import HierarchyAndStructure

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--get", help="get a flattened key's value")
arg_parser.add_argument("--source", help="path to json file")
arg_parser.add_argument("--separator", help="separator to use for obj_keys (default : . )", default=".")
arg_parser.add_argument("--values", action='store_const', const=True, default=False, help="show values")
arg_parser.add_argument("--obj_keys", action='store_const', const=True, help="show flatened access keys")
arg_parser.add_argument("--py_keys", action='store_const', const=True, help="show python statements as access keys")

arg_parser.add_argument("--query", help="for later")
arg_parser.add_argument("--stats", help="for later")
arg_parser.add_argument("--no-wrap", help="for later")

args = arg_parser.parse_args()

data = None
filepath = None

#piped input takes precedence over file source
if not sys.stdin.isatty():
    data = json.load(sys.stdin)
elif args.source is not None and len(args.source) > 0:
    if mimetypes.MimeTypes().guess_type(args.source)[0] == 'application/json':
        with open(args.source, 'r') as json_file:
            data = json.load(json_file)

hands = HierarchyAndStructure(data, args.separator)

if args.get is not None:
    print(hands.get(args.get))
elif args.py_keys is not None:
    print(hands.direct_access_keys(args.values))
elif args.obj_keys is not None:
    print(hands.obj_access_keys(args.values))
elif args.values is not None:
    print(hands.values())
