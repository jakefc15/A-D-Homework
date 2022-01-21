class Person:
    age=0
    name=" "
    def PrintData(self):
        print("age = ", self.age, "\t", "name = ", self.name, "\n")
        return

John = Person()
John.age=25
John.name="John"
print(John.age)
print(John.name)
John.PrintData()
