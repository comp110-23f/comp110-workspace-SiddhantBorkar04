"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Initializes a fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Ages a fish by 1 day."""
        self.age += 1
        return None