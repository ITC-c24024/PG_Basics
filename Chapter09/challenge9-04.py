
li=[
    ["トップガン","リスキービジネス","マイノリティーレポート"],
    ["タイタニック","ザ レブナント","インセプション"],
    ["トレーニングデイ","マン オン ファイア","フライト"]
   ]

import csv

with open ("movie.csv","w",encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for s in li:
        w.writerow(s)
