
import json

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

pagHTML = """


    
        <title>Mapa Virtual</title>
        <meta charset="utf-8">
    
    
        <h1>Mapa Virtual</h1>
        <table>
            <tbody><tr>
                <!-- Coluna do índice -->
                <td width="30%" valign="top">
                    <a name="indice">
                    <h3>Índice</h3>
                    </a><ol><a name="indice">
"""

for c in cidades:
    pagHTML += f"<li><a href='#{c['id']}'>{c['nome']}</a></li>"

pagHTML += """
</ol>
                </td>
                <!-- Coluna do conteúdo -->
                <td width="70%">
"""

for c in cidades:
    pagHTML += f"""
                    <a name="{c['id']}">
                    <h3>{c['nome']}</h3>
                    <p><b>Distrito:</b> {c['distrito']}</p>
                    <p><b>População:</b> {c['população']}</p>
                    <p><b>Descrição:</b> {c['descrição']}</p>
                    <adress>[</adress></a><a href="#indice">Voltar ao índice</a>]
                    <center>
                        <hr width="80%">
                    </center>
                    <h3>Ligações:</h3>
    """
    for l in ligacoes:
        if l['origem'] == c['id']:
            pagHTML += f"""
                            <li><a href='#{l['destino']}'>{dictNomes[l['destino']]}</a> : {l['distância']}km</li>
            """

pagHTML += """
                </td>
            </tr>
        </tbody></table>
    

"""

print(pagHTML)