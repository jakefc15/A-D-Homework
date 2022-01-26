class GPA:
    def __init__(self):
        self.Eng = 100
        self.Hist = 95
        self.__Math =60
    def get_score_Math(self):
        return self.__Math
    def get_score_Eng(self):
        return self.Eng
    def get_score_Hist(self):
        return self.Hist


Student1 = GPA()
print('Eng: \t',Student1.get_score_Eng())
print('Hist: \t',Student1.get_score_Hist())
#print('Eng:\t',Student1.__Math)
print('Math:\t',Student1.get_score_Math())
