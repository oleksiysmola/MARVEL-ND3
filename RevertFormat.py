import pandas as pd
# Reads a text file and then copies back all the entries into the same text file
# This is purely to have consistent formating within the file

df = pd.read_csv("GroundStateTransitionsTaggedAddVibrationalTransitions.txt", delim_whitespace=True)

df = df.to_string(index=False)
TaggedFile = "GroundStateTransitionsTaggedAddVibrationalTransitions.txt"
with open(TaggedFile, "w+") as FileToWriteTo:
    FileToWriteTo.write(df)