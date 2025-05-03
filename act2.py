import random
class FruitQuiz:
    def __init__(self):
        self.fruits={"apple":"red",
                            "banana":"yellow",
                            "orange":"orange",
                            "watermelon":"green"}
    def quiz(self):
        while True:
            fruit,color=random.choice(list(self.fruits.items()))
            a=input("What is the color of {}".format(fruit))
            if a.lower()==color:
                print("correct")
            else:
                print("incorrect")
            b=int(input("Do you want to try again (1) if you want else (0)"))
            if not(b):
                break
print("Welcome to fruit quiz")
f1=FruitQuiz()
f1.quiz()
