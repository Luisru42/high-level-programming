#!/user/bin/env python3
"""Module that defines a class and an instance to show how Python
looks up attributes."""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an instance of a_class or an instance of a
        class that inherited from a_class ; otherwise False.
    """
    return isinstance(obj, a_class)
