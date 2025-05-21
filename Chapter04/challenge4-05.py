#入力されたfloatをstringに変換
def f(s):
    return float(s)

try :
    print(f(0.1))
except ValueError:
    print("エラー")
