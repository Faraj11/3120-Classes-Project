class Animal:
    def __init__(self, name, habitat, prey, population):
        self.name = name
        self.habitat = habitat
        self.prey = prey
        self.population = population
        
    def species(self):
        print('This animal is a', self.name)

    def details(self):
        print('The', self.name, 'has a population of', self.population, 'and they live in a', self.habitat)
        print('The', self.prey, 'is the main food source for a', self.name)