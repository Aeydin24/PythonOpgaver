import random
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time as t

# tom liste til oee værdier:
oeeList = []
# Headers til CSV eksport
kolonner = ['OEE værdi:']
# bool til godkendelse af OEE værdier
godkendt = False

# byg liste med OEE værdier
for i in range (10):
    oeeList.append(random.randrange(60,100))

# Spørg om der vil tilføjes en værdi til listen:
while True:
    choice = input("Vil du tilføje en værdi til listen? (Y/N): ")
    if choice == "y":
        while True:
            try:
                value = int(input("Indtast en integer: "))
                oeeList.append(value)
                break  # integer ok -> break det indre loop
            except ValueError:
                print("Det var ikke en integer. Prøv igen.")   # integer ikke ok -> spørg brugeren igen:
    elif choice == "n":
        break
    else:
        print("Godkendte input = y/n, prøv igen.")


# Printer gennemsnit, højeste, laveste og standardafvigelsen i listen

# Gennemsnit

gennemsnit = sum(oeeList) / len(oeeList)
print("Det gennemsnitlige OEE tal er: ", gennemsnit)

t.sleep(2)

# Højeste
højesteTal = max(oeeList)
print("Det højeste tal i datasættet er: ", højesteTal)
t.sleep(2)

# Laveste
lavesteTal = min(oeeList)
print("Det laveste tal i datasættet er: ", lavesteTal)
t.sleep(2)

# Standardafvigelsen

# tager hvert datapunkt (x), og minusser med gennemsnittet, hvorefter det sættes i potens - gør dette for hele listen.
squared_diffs = [(x - gennemsnit) ** 2 for x in oeeList]
# divider summen af den nye liste med længden af den nye liste
variance = sum(squared_diffs) / len(squared_diffs)
# square root af lortet = standardafvigelsen
variancesqr = math.sqrt(variance)

print("OEE liste værdier: ", oeeList)
print("Manipuleret liste værdier: ", squared_diffs)
t.sleep(2)
print("Standardafvigelsen i datasættet er: ", variancesqr)
t.sleep(2)

if gennemsnit > 78:
    godkendt = True
else:
    godkendt = False

print("Er det gennemsnitlige OEE godkendt?: ", godkendt)
t.sleep(2)

print("Visualiserer data, vent venligst...")
t.sleep(2)
# konverter liste til pandas dataframe

df = pd.DataFrame(oeeList, columns = kolonner)

# Eksporter dataframe til CSV - index=false stopper pandas i at skrive række indekser i csv filen

df.to_csv('OEEListe.csv', index=False)

# læs csv fil

data = pd.read_csv("OEEListe.csv")

# sæt seaborn style -> visualiser lineplot med x og y akser
# juster xticks, så x aksen viser tal:

sns.set_style("whitegrid")
g = sns.lineplot(x=range(1, len(oeeList) + 1), y='OEE værdi:', data=data)
g.set_xticks(range(1, len(oeeList) + 1))

# show lineplot til sidst
plt.show()