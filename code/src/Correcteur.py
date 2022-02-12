import pandas as pd
from pathlib import Path


class OrthoCorrect:
    here = Path(__file__).resolve()
    parent2 = here.parents[1]
    Lexique383Path = parent2 / "datas" / "Lexique383" / "Lexique383.tsv"
    filepath = Path(Lexique383Path)
    lex = pd.read_csv(filepath, sep='\t')
    lex1 = lex[["ortho", "phon", "lemme", "cgram", "freqfilms2", "freqlivres"]]
    words = lex1["ortho"].to_string(index=False)
    words = words.split("\n")
    words = [word.lstrip() for word in words]

    def __init__(self, text):
        self.text = text

    def freq(self, mot):
        "Moyenne des frequences de `mot`"
        freqfilm = self.lex1.loc[self.lex1["ortho"].isin([mot]),["freqfilms2"]]
        freqlivres = self.lex1.loc[self.lex1["ortho"].isin([mot]),["freqlivres"]]
        return (freqfilm["freqfilms2"] + freqlivres["freqlivres"]).to_string(index=False)


    def correction(self, mot):
        "Retournes les corrections possibles pour `mot`"
        return max(self.candidats(mot), key=self.freq)

    def candidats(self, mot):
        "Candidats possible a la correction"
        return (self.connu([mot]) or self.connu(self.edit1(mot)) or self.connu(self.edit2(mot)) or [mot])

    def connu(self, mots):
        "les entrees de `mot` dans Lexique"
        return list(self.lex1.loc[self.lex1["ortho"].isin(mots),["ortho"]]["ortho"])

    def edit1(self, mot):
        "Mots qui sont a une lettre de `mot`"
        lettres     = 'abcdefghijklmnopqrstuvwxyzàâæçéèêëîïôœùûüÿ'
        coupes      = [(mot[:i], mot[i:])       for i in range(len(mot)+1)]
        suppr       = [G + D[1:]                for G, D in coupes if D]
        transpose   = [G + D[1] + D[0] + D[2:]  for G, D in coupes if len(D)>1]
        remplace    = [G + l + D[1:]            for G, D in coupes if D for l in lettres]
        insert      = [G + l + D                for G, D in coupes for l in lettres]
        return list(suppr + transpose + remplace + insert)

    def edit2(self, mot):
        "Mots qui sont a 2 lettre de `mot`"
        return (e2 for e1 in self.edit1(mot) for e2 in self.edit1(e1))

def main():
    mot = "bnjour"
    correct = OrthoCorrect(mot)
    print(correct.correction(correct.text))

if __name__ == '__main__':
    main()
