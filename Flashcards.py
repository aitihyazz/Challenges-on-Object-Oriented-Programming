class falshcard:
    def __init__(self,word,meaning):
        self.word= word
        self.meaning=meaning
    def __str__(self):
        return self.word +' ('+self.meaning+')'
flash =[]
while(True):
    word=input("word")
    meaning=input("meaing")
    flash.append(falshcard(word,meaning))
    option=int(input("0=continue,1orothrers=stop"))
    if option:
        break
print("\n your flash cards")
for i in flash:
    print(">",i)