import random
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Laver liste med tilfældige OEE values:
oeeList = []
# Headers til CSV eksport
kolonner = ['OEE value:']
# bool til godkendelse af OEE værdier
godkendt = False


for i in range (10):
    oeeList.append(random.randrange(60,100))

# Printer gennemsnit, højeste, laveste og standardafvigelsen i listen

# Gennemsnit

gennemsnit = sum(oeeList) / len(oeeList)
print("Det gennemsnitlige OEE tal er: ", gennemsnit)

# Højeste
højesteTal = max(oeeList)
print("Det højeste tal i datasættet er: ", højesteTal)

# Laveste

lavesteTal = min(oeeList)
print("Det laveste tal i datasættet er: ", lavesteTal)


# Standardafvigelsen

# tager hvert datapunkt (x), og minusser med gennemsnittet, hvorefter det sættes i potens - gør dette for hele listen.
squared_diffs = [(x - gennemsnit) ** 2 for x in oeeList]
# divider summen af den nye liste med længden af den nye liste
variance = sum(squared_diffs) / len(squared_diffs)
# square root af lortet = standardafvigelsen
variancesqr = math.sqrt(variance)

print("oee liste: ", oeeList)
print("manipuleret liste: ", squared_diffs)
print("standardafvigelsen: ", variancesqr)

if gennemsnit > 78:
    godkendt = True
else:
    godkendt = False

print("Er det gennemsnitlige OEE godkendt?: ", godkendt)

# konverter liste til pandas dataframe

df = pd.DataFrame(oeeList, columns = kolonner)

# Eksporter dataframe til CSV - index=false stopper pandas i at skrive række indekser i csv filen

df.to_csv('OEEListe.csv', index=False)

# læs csv fil

data = pd.read_csv("OEEListe.csv")

# sæt seaborn style -> visualiser lineplot med x og y akser
# juster xticks, så x aksen viser 0-9 range og ikke 

sns.set_style("whitegrid")
g = sns.lineplot(x=range(0,10), y='OEE value:', data=data)
g.set_xticks(range(10))

# show lineplot til sidst
plt.show()