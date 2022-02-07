import pandas as pd
from pathlib import Path

#PoC 1, acceder words Lexique avec python
cwd = Path.cwd()
Lexique383Path = cwd.parent/"datas"/"Lexique383"/"Lexique383.tsv"
filepath = Path(Lexique383Path)
lex = pd.read_csv(filepath,sep='\t')
print(lex.head(8))

#PoC 2, corriger un mot en s'aidant de lexique
a = lex[lex["ortho"] == 'a']
print(a)
print("--------------------------")
aVerb = lex[(lex["ortho"] == 'a') & (lex["cgram"] == "VER")]
print(aVerb)
print("--------------------------")
