from dice import Die

class DiceRoller:
    def __init__(self):
        self.dice_types = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
        self.selected_die = None
        self.num_dice = 1
        self.roll_results = []

    def select_die(self, name):
        self.selected_die = Die(name)
        self.roll_results = []  # Clear previous results

    def increase_count(self):
        if self.num_dice < 10:
            self.num_dice += 1

    def decrease_count(self):
        if self.num_dice > 1:
            self.num_dice -= 1

    def roll(self):
        if self.selected_die:
            self.roll_results = [self.selected_die.roll() for _ in range(self.num_dice)]
        else:
            self.roll_results = ["No die selected!"]
