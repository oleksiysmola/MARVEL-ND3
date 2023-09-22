import pandas as pd

# Find transitions missing from 23CaDiFu that were included in the transitions that were sent

df = pd.read_csv("GroundState23CaDiFu.txt", delim_whitespace=True)
df2 = pd.read_csv("GroundStateTransitionsTaggedAddVibrationalTransitions.txt", delim_whitespace=True)

for i in range(len(df2)):
    if len(df[df["OBS/CM-1"] == df2["OBS/CM-1"][i]]) == 0:
        print(df2["OBS/CM-1"][i])
        
# Turns out none are missing