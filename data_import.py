from cs50 import SQL
import csv
import sys
import pandas as pd

data = pd.read_csv (r'2023YOFHLStats.csv')
df = pd.DataFrame(data)

db = SQL("sqlite:///hockey.db")

for row in df.itertuples():
    db.execute("INSERT INTO stats(ID,Player,NHLTeam,Position,SeasonRank,YOFHLTeam,Age,FPTS,FPG,Year) VALUES (?,?,?,?,?,?,?,?,?,?)", row.ID, row.Player, row.NHLTeam, row.Position, row.SeasonRank, row.YOFHLTeam, row.Age, row.FPts, row.FPG, row.Year)