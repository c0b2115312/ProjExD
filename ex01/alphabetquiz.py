import random

global taisyou,kesson

taisyou = ["M","I","Z","U","S","E","N","A"]
kesson = random.choices(taisyou,k=2)
t_k_and = set(taisyou) & set(kesson)
t_k_and = list(t_k_and)

taisyou2 = taisyou

random.shuffle(taisyou)

print("対象文字:")
print(taisyou)

taisyou2.remove(t_k_and[0])
taisyou2.remove(t_k_and[1])

print("表示文字:")
print(taisyou2)

ans = input("欠損文字はいくつあるでしょうか？")
if ans=="2":
    print("正解です。それでは具体的に欠損文字を一つずつ入力してください")
    mozi1 = input("一つ目の文字を入力して下さい:")
    mozi2 = input("二つ目の文字を入力して下さい:")
    if (mozi1==t_k_and[0] and mozi2==t_k_and[1]) or (mozi1==t_k_and[1] and mozi2==t_k_and[0]):
        print("正解です。")
    else:
        print("間違っています。")
else:
    print("間違ってます。")