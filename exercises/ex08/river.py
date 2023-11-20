"""File to define River class."""

__author__ = "730652641"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """If the animal is not too old, this adds them to the river."""
        new_bear_list = [] 
        new_fish_list = [] 
        for i in self.fish:
            if (i.age <= 3):
                new_fish_list.append(i)
        for i in self.bears:
            if (i.age <= 5):
                new_bear_list.append(i)
        self.bears = new_bear_list
        self.fish = new_fish_list
        return None
    
    def remove_fish(self, amount: int):
        """Removes a fish from the river."""
        for i in range(0, amount):
            self.fish.pop(0)

    def bears_eating(self):
        """Function where bears eat 3 fish."""
        for i in self.bears:
            if (len(self.fish) >= 5):
                self.remove_fish(3)
                i.eat(3)
    
    def check_hunger(self):
        """Checks hunger level of bear and deletes bear if level is below 0."""
        new_bears_list: list[Bear] = []
        for i in self.bears:
            if (i.hunger_score >= 0):
                new_bears_list.append(i)
        self.bears = new_bears_list
        return None
        
    def repopulate_fish(self):
        """Adds fish to river by factor of 4."""
        num_fish = (len(self.fish) // 2) * 4
        i: int = 0
        while (i < num_fish):
            self.fish.append(Fish())
            i += 1
        return None
    
    def repopulate_bears(self):
        """Adds bears to river by factor of 1."""
        num_bears = len(self.bears) // 2
        i: int = 0
        while (i < num_bears):
            self.bears.append(Bear())
            i += 1
        return None
    
    def view_river(self):
        """Prints river population."""
        print("~~~ Day " + str(self.day) + ": ~~~")
        print("Fish population: " + str(len(self.fish)))
        print("Bear population: " + str(len(self.bears)))
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Simulates 7 days of the river."""
        for i in range(0, 7):
            self.one_river_day()
        return None