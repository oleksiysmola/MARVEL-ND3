import pandas as pd

df = pd.read_csv("GroundState23CaDiFu.txt", delim_whitespace=True)
df["v1U"] = 0
df["v2U"] = 0
df["v4U"] = 0
df["l4U"] = 0
df["v1L"] = 0
df["v2L"] = 0
df["v4L"] = 0
df["l4L"] = 0
inversionMap = {
    "s": 0,
    "a": 1
}
df["s'"] = df["s'"].map(inversionMap)
df["s\""] = df["s\""].map(inversionMap)
df = df[["OBS/CM-1", "UNC/CM-1", "J'",  "k'",  "v1U", "v2U", "v4U", "l4U", 
         "s'", "J\"",  "k\"", "v1L", "v2L", "v4L", "l4L", "s\""]]
df["Source"] = "23CaDiFu"
df = df.to_string(index=False)
TaggedFile = "GroundStateTransitions23CaDiFuTagged.txt"
with open(TaggedFile, "w+") as FileToWriteTo:
    FileToWriteTo.write(df)