class Lion:
    Age = 7
    Gender = 'Male'

    def sleeping(self):
        print('sleeping...\n')
    def eating(self):
        print('eating...\n')
    def fighting(self):
        print('fighting...\n');

Lion_A = Lion()
Lion_B = Lion()

print("Age of lion_A:\t",Lion_A.Age)
print("Lion_A is\n")
Lion_A.eating()
print("Age of lion_B:\t",Lion_B.Age)
print("Lion_B is \n")
Lion_B.sleeping()
