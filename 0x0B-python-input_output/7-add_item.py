#!/usr/bin/python3
"""Functions called save_to_json_file
and load_from_json_file"""

from sys import argv
import os.path


sf = __import__('5-save_to_json_file').save_to_json_file
lf = __import__('6-load_from_json_file').load_from_json_file

lx = []

if os.path.exists("add_item.json"):
    lx = lf("add_item.json")

for x in argv[1:]:
    lx.append(x)

sf(lx, "add_item.json")
