class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self, direction):
        print(self.name, "walks to the", direction)

    def talk(self, speech):
        print(self.name, "Says:", speech)


class Wizard(Human):
    def __init__(self, name, age, spell_points):  # this overrides the superclass Human init method and attribute
        super().__init__(name, age)  # this calls and initialized the superclass' init method
        self.spell_points = spell_points

    def cast_spell(self, spell):
        print(self.name, "casts", spell)


class Parent:
    def __init__(self, test):
        self.test = test


class Child(Parent):
    def __init__(self, test, test1):
        super().__init__(test)  # Calls __init() method pf parent
        self.test1 = test1


