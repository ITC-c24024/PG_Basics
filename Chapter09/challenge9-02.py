s=input("あなたの名前は？")

with open("name.txt","w",encoding="utf-8") as f:
    f.write(s)
