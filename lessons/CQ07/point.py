"""Declaration and associated methods of the Point class."""

from __future__ import annotations


class Point:
    """Class that is used to make and maniputate Point objects that have attributes x and y."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Point constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Function that mutates the point object by scaling it."""
        self.x = self.x * factor  
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Funciton the mutates point object and returns a new Point object."""
        final_pt: Point = Point(self.x, self.y)
        final_pt.scale_by(factor)
        return final_pt

    def __str__(self) -> str:
        """Magic Str function."""
        string: str = "x: " + str(self.x) + "; y: " + str(self.y)
        return string

    def __mul__(self, factor: int | float) -> Point:
        """Magic multiplication funciton."""
        self.x = self.x * factor  
        self.y = self.y * factor
        return self

    def __add__(self, factor: int | float) -> Point:
        """Magic Addition Function."""
        self.x = self.x + factor  
        self.y = self.y + factor
        return self

    
