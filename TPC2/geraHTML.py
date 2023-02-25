import json

def ordCidade(cidade):
    return cidade['nome']

def ordLigacao(ligacao):
    return ligacao['id']

f = open("mapa.json")
mapa = json.load(f)
cidades = mapa['cidades']
cidades.sort(key=ordCidade)

distritos = dict()

for c in cidades:
    distrito = c['distrito']
    if distrito not in distritos:
        distritos[distrito] = []
    distritos[distrito].append(c['nome'])

distritos_sorted = sorted(distritos.keys())

#print(distritos)

pagHTML = """

    
        <title>Distritos de Portugal</title>
        <meta charset="utf-8">
    
    
        <h1>Distritos de Portugal</h1>
    
"""

for d in distritos_sorted:
    pagHTML+= f"<h2>{d}</h2>"
    for cidade in distritos[d]:
        pagHTML += f"<li><a href='/{cidade.replace(' ','')}'>{cidade}</a></li>"


print(pagHTML)