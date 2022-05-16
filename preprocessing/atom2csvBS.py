from bs4 import BeautifulSoup
from pathlib import Path
import csv

pathfolder = "licitacionesPerfilesContratanteCompleto3_2019"

with open('docs.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['descripcion', 'CPV']) 
    j=0
    for p in Path(pathfolder).glob('*.atom'):
        j = j + 1
        print(f"Processing:\t {p.name}:\n")
        soup = BeautifulSoup(open(p, encoding='utf8'), 'html.parser')
        entries = soup.find_all("entry")
        am = len(entries)
        print('Number of posts in RSS feede :', am)
        i=0
        for entry in entries:
            desc = entry.find('title').getText()
            #print('Description :', desc)
            cpvs = entry.find_all('cbc:itemclassificationcode')
            curr_cpvs = []
            for cpv in cpvs:
                if cpv.getText() not in curr_cpvs:
                    curr_cpvs.append(cpv.getText())   
            str_cpv=",".join(curr_cpvs) 
            #print('CPV :', str_cpv)
            writer.writerow(['\"' + desc + '\"', str_cpv]) 
            i = i + 1  
            #print(i, " : ", am, "\t", j, " / ", 479)
        print(j, " / ", 479)

