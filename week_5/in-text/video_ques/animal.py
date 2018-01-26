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


class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent(self):
        return self.parent2
    def __add__(self, other):
        #r1 and r2 are 2 rabbits, r3 = r1+r2 will give a new rabbit r3
        return Rabbit(0,self,other)
    def __eq__(self, other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent1.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite

"""
peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1,peter,hopsy)
cotton.set_name('cottontail')
mopsy = peter + hopsy
mopsy.set_name('Mopsy')
print(mopsy == cotton)
"""