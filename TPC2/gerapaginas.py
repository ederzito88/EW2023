import json
#import os
#import string
from urllib.parse import quote

"""
first try to solve non-ascii characters

def remove_non_ascii(a_str):
    ascii_chars = set(string.printable)

    return ''.join(
        filter(lambda x: x in ascii_chars, a_str)
    )
"""

def ordCidade(cidade):
    return cidade['nome']

def ordLigacao(ligacao):
    return ligacao['id']

f = open("mapa.json")
mapa = json.load(f)
cidades = mapa['cidades']
cidades.sort(key=ordCidade)
ligacoes = mapa['ligações']
ligacoes.sort(key=ordLigacao)

dictNomes = dict()

for c in cidades:
    dictNomes[c['id']] = c['nome']

for cidade in cidades:
    filename = cidade['nome'].replace(" ","") + '.html'
    with open(filename, 'w') as f:
        f.write('<!DOCTYPE html>')
        f.write('<html>\n')
        f.write('<meta charset="utf-8">')
        f.write('<head>\n')
        f.write(f'<title>{cidade["nome"]}</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write(f'<h1>{cidade["nome"]}</h1>\n')
        f.write(f'<p><b>População:</b> {cidade["população"]}</p>\n')
        f.write(f'<p><b>Descrição:</b> {cidade["descrição"]}</p>\n')
        f.write(f'<p><b>Distrito:</b> {cidade["distrito"]}</p>\n')
        f.write(f'<p><b>Ligações:</b></p>\n')
        for l in ligacoes:
            if l['origem'] == cidade['id']:
                f.write(f"<li><a href='/{dictNomes[l['destino']].replace(' ','')}'>{dictNomes[l['destino']]}</a> : {l['distância']}km</li>")
        f.write('</body>\n')
        f.write('</html>\n')

    #os.remove(f"{remove_non_ascii(cidade['nome'].replace(' ',''))}.html") #for cleaning wrong files while testing
    
