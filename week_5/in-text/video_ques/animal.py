class Animal (object):
    def __init__(self,age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self,newage):
        self.age = newage

    def set_name(self,newname=""):
        self.name = newname

    def __str__(self):
        return "animal: "+str(self.name)+" : "+str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat: "+str(self.name)+" : "+str(self.age)

"""
jelly = Cat(1)
jelly.set_name("JellyBelly")
print(jelly)

print(Animal.__str__(jelly))

bob = Animal(1)
print(bob)

bob.set_name()
print(bob)
"""

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit: "+str(self.name)+" : "+str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self,age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.get_age()-other.get_age()
        if self.age > other.age:
            print(self.name , "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person: "+str(self.name)+" : "+str(self.age)