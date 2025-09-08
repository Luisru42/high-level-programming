#! /usr/bin/env python3
"""Module that contains a function that returns the JSON
   representation of an object (string)."""


from json import dumps


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return dumps(my_obj)
