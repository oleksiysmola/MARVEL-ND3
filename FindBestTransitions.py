import pandas as pd

# Here we look for transitions to the vibrational bands ideally to the lowest possible J

df = pd.read_csv("/home/asmola/Documents/Marvel-ND3/Marvel-ND3-Transitions.txt", delim_whitespace=True)

df = df[df["v4U"] == 1]
df = df[df["JU"] == 0]
print(df)