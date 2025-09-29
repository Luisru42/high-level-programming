#!/usr/bin/python3
import sys
from os import path
from importlib import import_module


save_to_json_file = import_module('7-save_to_json_file').save_to_json_file
load_from_json_file = (
    import_module('8-load_from_json_file').load_from_json_file
)


filename = 'add_item.json'
items = load_from_json_file(filename) if path.exists(filename) else []
items.extend(sys.argv[1:])
save_to_json_file(items, filename)
