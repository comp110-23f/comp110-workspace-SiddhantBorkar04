"""File to define Bear class."""


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Makes a new bear object."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Ages and hungers a bear by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bear eats input number of fish."""
        self.hunger_score += num_fish

    