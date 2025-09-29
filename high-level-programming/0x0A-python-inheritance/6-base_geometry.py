#!/user/bin/env python3
"""Module that defines a class and an instance to show how Python
looks up attributes."""


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        """Raise an Exception with a message."""
        raise Exception("area() is not implemented")
