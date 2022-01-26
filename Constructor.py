class GPA:
    def __init__(self, Eng, Hist, Math):
        self.Eng = Eng
        self.Hist = Hist
        self.__Math = Math
    def get_score_Math(self):
        return self.__Math


Student1 = GPA(100,95,60)

print('Eng: \t',Student1.Eng)
print('Hist: \t',Student1.Hist)
print('Math:\t',Student1.get_score_Math())

