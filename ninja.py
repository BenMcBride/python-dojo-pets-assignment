import pet
class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__( self ,  first_name , last_name , treats , pet_food , pet_name ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet_name = pet_name
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet_name.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if(self.pet_food > 1):
            self.pet_name.eat()
            self.pet_food -= 1
        else:
            print('Not enough pet food!')
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet_name.noise()
        return self

# Create a Ninja class with the ninja attributes listed above.

# Create a Pet class with the pet attributes listed above.

# Implement walk(), feed(), bathe() on the ninja class.

# Implement sleep(), eat(), play(), noise() methods on the pet class.

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
Malcolm = pet.Dog('Malcolm', 'dog', 'sit',  100, 100, 'bark!', 'Border Collie')
Murr = Ninja('Murr', 'McLovin', 40, 20, Malcolm)
print(Murr.pet_name.name, Murr.pet_name.type, Murr.pet_name.tricks, Murr.pet_name.health, Murr.pet_name.energy, Murr.pet_name.breed)

# Have the Ninja feed, walk , and bathe their pet.
Murr.feed().walk().bathe()
print(Murr.pet_name.name, Murr.pet_name.type, Murr.pet_name.tricks, Murr.pet_name.health, Murr.pet_name.energy)

# NINJA BONUS: Use modules to separate out the classes into different files.
    # changed pet attribute in Ninja to pet_name

# SENSEI BONUS: Use Inheritance to create sub classes of pets.


# Compress or zip up assignment and upload it.