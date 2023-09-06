from duck import Duck

class RubberDuck(Duck):
    species = "-"

    def __init__(self):
        super().__init__()

    def quack(self):
        print("Squeak!")

    def fly(self):
        pass
