import pandas as pd
from pathlib import Path
import sys

argc = len(sys.argv)
argv = sys.argv
mot = argv[1]

if(argc > 2) :
    print("Ajouter un seul mot")
    exit(0)

#PoC 1, acceder words Lexique avec python
cwd = Path.cwd()
Lexique383Path = cwd.parent/"datas"/"Lexique383"/"Lexique383.tsv"
filepath = Path(Lexique383Path)
lex = pd.read_csv(filepath,sep='\t')
print(lex.head(8))

#PoC 2, corriger un mot en s'aidant de lexique
lex1 = lex[["ortho", "phon", "lemme", "cgram"]]
a = lex1[lex1["ortho"] == 'a']
print(a)
print("--------------------------")
aVerb = lex1[(lex1["ortho"] == 'a') & (lex1["cgram"] == "VER")]
print(aVerb)
print("--------------------------")

print(lex1[lex1["ortho"] == mot])

words = lex["ortho"].to_string(index=False)
words = words.split("\n")
words = [word.lstrip() for word in words]
# print(words)
