#!/usr/bin/python3
"""Defines an inherited ls class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in ls class."""

    def print_sorted(self):
        """Print a ls in sorted ascending order."""
        print(sorted(self))

