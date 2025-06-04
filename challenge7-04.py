li=[1,3,5,7,9]
b=False

while b==False:
    i=input()
    if i=="q":
        b=True
    elif int(i) in li:
        print("正解")
        b=True
    elif int(i) not in li:
        print("不正解")
    else:
        print("数字を入力するか、qで終了します")

