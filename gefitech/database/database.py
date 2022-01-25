import sqlite3

band_test = 'Fugazi'
connexion = sqlite3.connect("test_base_sqlite.db")

def band_infos_from_database(band_test):
    band = {}
    curseur = connexion.cursor()
    band_id = curseur.execute(
        "SELECT id FROM 'band' WHERE name = '{band}'".format(band=band_test)).fetchone()[0]
    info_band = curseur.execute(
        "SELECT * FROM 'band' WHERE id = {band_id}".format(band_id=band_id)).fetchall()[0] 
    item = [column[0] for column in curseur.description]
    print(item)

    for i in range(len(item)):
        band[item[i]] = info_band[i]
    
    return(band)


print(band_infos_from_database(band_test))