"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730652641"


class Simpy:
    """Simpy object class."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, list: list[float]):
        """Constructs a Simpy object."""
        self.values = list

    def __str__(self) -> str:
        """Produce a string visualization of the Simpy."""
        return "Simpy(" + str(self.values) + ")"
    
    def fill(self, flt: float, num_vals: int) -> None:
        """Fills a `Simpy`'s `values` with a specific number of repeating values."""
        new_values: list[float] = []
        for i in range(0, num_vals):
            new_values.append(flt)
        self.values = new_values

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in values like the range funciton but for floats."""
        new_values: list[float] = []
        iterations: int = int((stop - start) / step)
        start1: float = start - step
        for i in range(iterations):
            start1 += step
            new_values.append(start1)
        self.values = new_values

    def sum(self) -> float:
        """Adds all elements of simpy object together."""
        sum: int = 0
        for i in (self.values):
            sum += i 
        return sum

    def __add__(self, simp: Union[float, Simpy]) -> Simpy:
        """Adds simpy object and simpy object or float together."""
        new_list: list[float] = []
        if (type(simp) is type(self)):
            assert len(self.values) == len(simp.values)
            for i in range(0, len(self.values)):
                new_list.append(float(self.values[i]) + float(simp.values[i]))
            return Simpy(new_list)
        elif (type(simp) is type(1.0)):
            for i in range(0, len(self.values)):
                new_list.append(float(self.values[i] + simp))
            return Simpy(new_list)

    def __pow__(self, simp: Union[float, Simpy]) -> Simpy:
        """Exponentiates simpy object."""
        new_list: list[float] = []
        if (type(simp) is type(self)):
            assert len(self.values) == len(simp.values)
            for i in range(0, len(self.values)):
                new_list.append(float(self.values[i]) ** float(simp.values[i]))
            return Simpy(new_list)
        elif (type(simp) is type(1.0)):
            for i in range(0, len(self.values)):
                new_list.append(float(self.values[i] ** simp))
            return Simpy(new_list)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns list of value equality comparisons."""
        new_list: list[bool] = []
        if (type(rhs) is type(self)):
            for i in range(len(self.values)):
                if (self.values[i] == rhs.values[i]):
                    new_list.append(True)
                else:
                    new_list.append(False)
        if (type(rhs) is type(1.0)):
            for i in range(len(self.values)):
                if (self.values[i] == rhs):
                    new_list.append(True)
                else:
                    new_list.append(False)
        return new_list

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns list of value greater than comparisons."""
        new_list: list[bool] = []
        if (type(rhs) is type(self)):
            for i in range(len(self.values)):
                if (self.values[i] > rhs.values[i]):
                    new_list.append(True)
                else:
                    new_list.append(False)
        if (type(rhs) is type(1.0)):
            for i in range(len(self.values)):
                if (self.values[i] > rhs):
                    new_list.append(True)
                else:
                    new_list.append(False)
        return new_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads subscription notation to filter with mask."""
        if (type(rhs) is type(1)):
            return float(self.values[rhs])
        
        new_list: list(float) = []
        if (type(rhs) is type([True])):
            for i in range(len(self.values)):
                if rhs[i] is True:
                    new_list.append(self.values[i])
        return Simpy(new_list)