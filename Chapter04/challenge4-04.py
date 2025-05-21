#入力された値の半分の値を返す
def f1(i):
    print(int(i/2))
    return int(i/2)

#f1で返された値の４倍の値を返す
def f2(n):
    return n*4


print(f2(f1(10)))
