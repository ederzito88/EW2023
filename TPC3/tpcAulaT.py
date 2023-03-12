import json

f = open("dataset-extra1.json")
pessoas = json.load(f)
f.close()

for index, p in enumerate(pessoas['pessoas']):
    p['id'] = 'p' + str(index)
    
nf = open("dataset-extra2_with_id.json","w")
json.dump(pessoas, nf)
nf.close()