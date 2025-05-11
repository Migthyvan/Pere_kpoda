import pandas as pd

df = pd.read_excel('bd.xlsx')

def ajouter_element(df, nom, prenoms):
    nouvelle_ligne = pd.DataFrame({
        "nom": [nom],
        "prenoms": [prenoms]
    })
    return  pd.concat([df, nouvelle_ligne], ignore_index= True)

#df = ajouter_element(df, 'Tanoh', 'Charles')

print(df)
#df.to_excel('bd.xlsx', index)