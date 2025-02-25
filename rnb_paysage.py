import os

import pandas as pd
import requests

DATA_PATH = "C:/Users/jgrandha/Downloads"

os.chdir(DATA_PATH)

res = requests.get('https://api.bdnb.io/v1/bdnb/geocodage?',
                   params={'q': '12 rue Charrel Grenoble'})

bgi = res.json()["features"][0]["properties"]["id"]

resultat = requests.get('https://api.bdnb.io/v1/bdnb/donnees/batiment_groupe_complet/adresse',
                        params={"cle_interop_adr": f"eq.{bgi}", "select": "batiment_groupe_id"})

resultat2 = resultat.json()[0]["batiment_groupe_id"]

r = requests.get('https://api.bdnb.io/v1/bdnb/donnees/batiment_construction',
                 params={'limit': 5,
                         'batiment_groupe_id': f'eq.{resultat2}', "select": "rnb_id"})

rnb = r.json()[0]["rnb_id"]

aut = pd.read_csv("Liste-des-autorisations-durbanisme-creant-des-logements.2025-01.csv",
                  sep=";", engine="python")
aut = aut.loc[aut["Numéro de voie du terrain"] != "ADR_NUM_TER"]

aut2 = aut.loc[(aut["Numéro de voie du terrain"].notna()) | (aut["Type de voie du terrain"].notna()) | (aut["Libellé de la voie du terrain"].notna()) | (aut["Localité du terrain"].notna()) | (aut["Code postal du terrain"].notna())]

aut2["adresses"] = aut2["Numéro de voie du terrain"] + " " + aut2["Type de voie du terrain"] + " " + aut2["Libellé de la voie du terrain"] + " " + aut2["Localité du terrain"] + " " + aut2["Code postal du terrain"]

liste_adresses = list(aut2.loc[aut2["adresses"].notna(), "adresses"].unique())

dict_res_adresses = {"adresse": [], "bgi": []}
for adresse in liste_adresses:
    res = requests.get('https://api.bdnb.io/v1/bdnb/geocodage?',
                       params={'q': adresse})

    if res.status_code == 200:
        bgi = res.json()["features"][0]["properties"]["id"]
        dict_res_adresses["adresse"].append(adresse)
        dict_res_adresses["bgi"].append(bgi)

dict_res_clef = {"bgi": [], "clef": []}
for bgi in dict_res_adresses["bgi"]:
    resultat = requests.get('https://api.bdnb.io/v1/bdnb/donnees/batiment_groupe_complet/adresse',
                            params={"cle_interop_adr": f"eq.{bgi}", "select": "batiment_groupe_id"})

    if resultat.status_code == 200:
        resultat2 = resultat.json()[0]["batiment_groupe_id"]
        dict_res_clef["bgi"].append(bgi)
        dict_res_clef["clef"].append(resultat2)

dict_res_rnb = {"clef": [], "rnb": []}
for clef in dict_res_clef["clef"]:
    r = requests.get('https://api.bdnb.io/v1/bdnb/donnees/batiment_construction',
                     params={'limit': 5,
                             'batiment_groupe_id': f'eq.{clef}', "select": "rnb_id"})

    if r.status_code == 200:
        rnb = r.json()[0]["rnb_id"]
        dict_res_rnb["clef"].append(clef)
        dict_res_rnb["rnb"].append(rnb)

ods = pd.read_csv("fr-esr-patrimoine-immobilier-des-operateurs-de-l-enseignement-superieur.csv",
                  sep=";", engine="python")