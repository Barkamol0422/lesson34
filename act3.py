class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+"("+self.meaning+")"
flash=[]
while True:
    word=input("Enter a word: ")
    meaning=input("Enter the meaning of the word: ")
    flash.append(flashcard(word,meaning))
    a=int(input("Do you want to add flashcard 0 to enter 1 to stop: "))
    if (a):
        break
for i in flash:
    print(">",i)
