import pandas as pd
import os

cwd = os.getcwd()
Lexique383Path = ['..','datas','Lexique383','Lexique383.tsv']
filepath = os.path.join(cwd + os.sep, Lexique383Path[0], Lexique383Path[1], Lexique383Path[2], Lexique383Path[3])

lex = pd.read_csv(filepath,sep='\t')
print(lex.head(8))
