li=[
    ["Top Gun","Risky Business","Minority Report"],
    ["Titanic","The Revenant","Inception"],
    ["Traning Day","Man on Fire","Flight"]
   ]

import csv

with open ("movie.csv","w") as f:
    w = csv.writer(f,delimiter=",")
    for s in li:
        w.writerow(s)


