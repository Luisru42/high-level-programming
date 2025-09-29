#!/usr/bin/python3
def class_to_json(obj):
    return obj.__dict__
    """Return the dictionary description with simple data structure"""
    """for JSON serialization of an object."""
