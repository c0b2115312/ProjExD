import random


mondai = ["サザエの旦那の名前は？","カツオの妹の名前は","タラオはカツオから見てどんな関係？"]
kotae = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]

num = random.randint(0,2)
def shutudai():
    print(mondai[num])

def kaito():
    ans = input("回答:")
    if ans in kotae[num]:
        print("正解!")
    else:
        print("不正解!!!")

shutudai()
kaito()
