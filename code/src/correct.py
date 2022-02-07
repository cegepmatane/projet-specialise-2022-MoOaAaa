from contextlib import suppress
from numpy import transpose
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
#print(cwd)
Lexique383Path = cwd/"datas"/"Lexique383"/"Lexique383.tsv"
filepath = Path(Lexique383Path)
#print(filepath)
lex = pd.read_csv(filepath,sep='\t')
#print(lex.head(8))

#PoC 2, corriger un mot en s'aidant de lexique
lex1 = lex[["ortho", "phon", "lemme", "cgram", "freqfilms2", "freqlivres"]]
a = lex1[lex1["ortho"] == 'a']
#print(a)
#print("--------------------------")
aVerb = lex1[(lex1["ortho"] == 'a') & (lex1["cgram"] == "VER")]
#print(aVerb)
#print("--------------------------")

print(lex1[lex1["ortho"] == mot])
print("--------------------------")

words = lex1["ortho"].to_string(index=False)
words = words.split("\n")
words = [word.lstrip() for word in words]
# print(words)



#---------------------------------
def freq(mot, lex):
    "Moyenne des frequences de `mot`"
    freqfilm = lex.loc[lex["ortho"].isin([mot]),["freqfilms2"]]
    freqlivres = lex.loc[lex["ortho"].isin([mot]),["freqlivres"]]
    return (freqfilm["freqfilms2"] + freqlivres["freqlivres"]).to_string(index=False)

#print(freq(mot,lex1))

def correction(mot):
    "Retournes les corrections possibles pour `mot`"
    return max(candidats(mot), key=freq)

def candidats(mot):
    "Candidats possible a la correction"
    return (connu([mot]) or connu(edit1(mot)) or connu(edit2(mot)) or [mot])

def connu(mots):
    "les entrees de `mot` dans Lexique"
    return lex1.loc[lex1["ortho"].isin([mots]),["ortho"]]["ortho"].to_string(index=False)

def edit1(mot):
    "Mots qui sont a une lettre de `mot`"
    lettres     = 'abcdefghijklmnopqrstuvwxyzàâæçéèêëîïôœùûüÿ'
    coupes      = [(mot[:i], mot[i:])        for i in range(len(mot)+1)]
    suppr       = [G + D[1:]                for G, D in coupes if D]
    transpose   = [G + D[1] + D[0] + D[2:]  for G, D in coupes if len(D)>1]
    remplace    = [G + l + D[1:]            for G, D in coupes if D for l in lettres]
    insert      = [G + l + D                for G, D in coupes for l in lettres]
    return set(suppr + transpose + remplace + insert)

def edit2(mot):
    "Mots qui sont a 2 lettre de `mot`"
    return (e2 for e1 in edit1(mot) for e2 in edit1(e1))

print(connu(mot))