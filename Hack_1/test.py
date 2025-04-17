class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 1
        self.tricks = []

    def eat(self):
        if self.hunger <= 2:
            self.hunger = 0
        else:
            self.hunger -= 3
            self.happiness += 1
        
        print(f"Pet ate, happiness increased\n")
        print(f"Hunger level: {self.hunger}, Happiness_level: {self.happiness}")
    def sleep(self):
        if self.energy >= 5:
            self.energy = 10
        else:
            self.energy += 5
        print(f"{self.name} slept.\n")
        print(f"Current energy level: {self.energy}")
    def play(self):
        if self.energy <= 2:
            self.energy = 0
        else:
            self.energy -= 2
            self.happiness +=2
            self.hunger += 1
        print(f"Pet played, happiness increased\n")

    def train(self, trick):
        """This function takes trick from user as input and
        adds trick to the pet's tricks list"""
        self.tricks.append(trick)
    
    def show_tricks(self):
        
        # for i in range(len(self.tricks)):
        #     print(f"Trick {i+1}: {self.tricks[i]}")
        # print("Tricks learned by the pet:")

        for i, trick in enumerate(self.tricks):
            print(f"Trick {i+1}: {trick.strip()}")  # Strip removes any extra whitespace
            print("Tricks learned by the pet:")

    
    def get_status(self):
        
        print("Current status of the pet:")
        print(f"Pet name: {self.name}")
        print(f"Hunger level: {self.hunger}")
        print(f"Energy level: {self.energy}")
        print(f"Happiness level: {self.happiness}")
        print(f"Tricks learned: {self.tricks}")
