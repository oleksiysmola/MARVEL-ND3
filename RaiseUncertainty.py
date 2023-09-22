import pandas as pd
from pandarallel import pandarallel
pandarallel.initialize(progress_bar=True)
# Reads a text file and then copies back all the entries into the same text file
# This is purely to have consistent formating within the file

df = pd.read_csv("Marvel-ND3-Transitions.txt", delim_whitespace=True)
badLines = pd.read_csv("BadLines.txt", delim_whitespace=True)

def raiseUncertainty(row, badLines):
    if len(badLines[badLines["Source"] == row["Source"]]) != 0:
        print("Bad line matched")
    return row

df = df.parallel_apply(lambda x: raiseUncertainty(x, badLines), result_type="expand", axis=1)

df = df.to_string(index=False)
TaggedFile = "Marvel-ND3-Transitions.txt"
with open(TaggedFile, "w+") as FileToWriteTo:
    FileToWriteTo.write(df)