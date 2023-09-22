import pandas as pd
from pandarallel import pandarallel
pandarallel.initialize(progress_bar=True)

df = pd.read_csv("/home/asmola/Documents/Marvel-ND3/OriginalSources/23CaDiFu-TableS3.txt", delim_whitespace=True)
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
c = 29979245800
df["s'"] = df["s'"].map(inversionMap)
df["s\""] = df["s\""].map(inversionMap)
# df["NU"] = df["OBS/MHz"]*1e6/c
# df["UNC"] = df["UNCERTAINTY/MHz"]*1e6/c

def obtainVibrationalQuantumNumbers(row):
    if row["v'"] == 1:
        row["v2U"] = 2
    if row["v\""] == 1:
        row["v2L"] = 2
    if row["v'"] == 2:
        row["v4U"] = 1
        row["l4U"] = -1
    if row["v\""] == 2:
        row["v4L"] = 1
        row["l4L"] = -1
    if row["v'"] == 3:
        row["v4U"] = 1
        row["l4U"] = 1
    if row["v\""] == 3:
        row["v4L"] = 1
        row["l4L"] = 1
    if row["v'"] == 4:
        row["v2U"] = 1
    if row["v\""] == 4:
        row["v2L"] = 1         
    return row

df = df.parallel_apply(lambda x:obtainVibrationalQuantumNumbers(x), axis=1, result_type="expand")


df = df[["OBS", "UNCERTAINTY", "J'",  "K'",  "v1U", "v2U", "v4U", "l4U", 
         "s'", "J\"",  "K\"", "v1L", "v2L", "v4L", "l4L", "s\""]]
df["Source"] = "23CaDiFu"
df = df.to_string(index=False)
TaggedFile = "/home/asmola/Documents/Marvel-ND3/ProcessedSources/23CaDiFu-TableS3.transitions"
with open(TaggedFile, "w+") as FileToWriteTo:
    FileToWriteTo.write(df)