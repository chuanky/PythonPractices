class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.master = "haoke"

    def sit(self):
        print(self.name + " is sitting")
        self.roll_over()

    def roll_over(self):
        print(self.name + " is rolling")

    def rename(self, name):
        self.name = name

def roll_over():
    print("rolling outside")


class Bage(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        # y = a * x + b
        # y=a*x+b
    def bark(self):
        print("Bage is barking")

    #override
    def roll_over(self):
        print("Bage cannot roll over")


class LittleBage(Bage):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    #override
    def sit(self):
        print("litte bage cannit sit")

# erjiang = Bage("erjiang", 3)
# # erjiang.name = "hengha"
# erjiang.rename("hengha")
# print(erjiang.name + " age: " + str(erjiang.age))
# print(erjiang.master)
# erjiang.sit()
# erjiang.bark()
