import pandas as pd
from pathlib import Path

cwd = Path.cwd()
Lexique383Path = cwd.parent/"datas"/"Lexique383"/"Lexique383.tsv"
filepath = Path(Lexique383Path)
lex = pd.read_csv(filepath,sep='\t')
print(lex.head(8))
