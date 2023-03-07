def fill_degree_table(db, data):
    """Fill the degree table with the data passed in parameters"""

    db_cursor = db.cursor()
    db_cursor.execute("USE efrei_sql")
    for item in data:
        db_cursor.execute(
            "INSERT INTO diplome (diplome, libelle_diplome, type_diplome, libelle_specialite, libelle_specialite_com, code_groupe_specialite) VALUES (%d, %s, %s, %s, %s, %s)",
            (item[0], item[1], item[2], item[3], item[4], item[5]))
    db_cursor.close()
    print("Table Diplome filled successfully")


def fill_entreprise_table(db, data):
    """Fill the entreprise table with the data passed in parameters"""

    db_cursor = db.cursor()
    db_cursor.execute("USE efrei_sql")
    for item in data:
        db_cursor.execute(
            "INSERT INTO entreprise (code_insee_entreprise, depart_entreprise, code_naf_entreprise) VALUES (%s, %s, %s)",
            (item[0], item[1], item[2]))
    db_cursor.close()
    print("Table Entreprise filled successfully")


def fill_site_formation_table(db, data):
    """Fill the site_formation table with the data passed in parameters"""

    db_cursor = db.cursor()
    db_cursor.execute("USE efrei_sql")
    for item in data:
        db_cursor.execute(
            "INSERT INTO site_formation (id_siteformation, nom_site_formation, addresse_site, libelle_ville_site) VALUES (%s, %s, %s, %s)",
            (item[0], item[1], item[2], item[3]))
    db_cursor.close()
    print("Table Site Formation filled successfully")


def fill_students_table(db, data):
    """Fill the student table with the data passed in parameters"""

    db_cursor = db.cursor()
    db_cursor.execute("USE efrei_sql")
    for item in data:
        db_cursor.execute(
            "INSERT INTO etudiant (id_etudiant, id_siteformation, code_insee_entreprise, code_groupe_specialite, code_postal_jeune, libelle_statut_jeune, libelle_qualite, libelle_nationalite, handicap_oui_non_vide, age_jeune_decembre, age_formation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10],
             item[11]))
    db_cursor.close()
    print("Table Etudiant filled successfully")


def fill_db(db, data):
    data_by_table = parse_data(data)
    print(data_by_table)
    # fill_degree_table(db, data_by_table["diplome"])
    fill_entreprise_table(db, data_by_table["entreprise"])
    # fill_site_formation_table(db, data_by_table["site_formation"])
    # fill_students_table(db, data_by_table["etudiant"])


def parse_data(data):
    """Parse the data to fill the tables"""

    data_by_table = dict()
    diplome = []
    entreprise = []
    etudiant = []
    site_formation = []

    diplome_counter = 0
    for item in data:
        # Diplome
        if "diplome" in item["fields"]:
            diplome.append(item['fields']['diplome'])
        else:
            diplome.append(diplome_counter)
            diplome_counter += 1
        if "libelle_diplome" in item["fields"]:
            diplome.append(item['fields']['libelle_diplome'])
        else:
            diplome.append("unknown")
        if "type_diplome" in item["fields"]:
            diplome.append(item['fields']['type_diplome'])
        else:
            diplome.append("unknown")
        if "libelle_specialite" in item["fields"]:
            diplome.append(item['fields']['libelle_specialite'])
        else:
            diplome.append("unknown")
        if "libelle_specialite_com" in item["fields"]:
            diplome.append(item['fields']['libelle_specialite_com'])
        else:
            diplome.append("unknown")
        if "code_groupe_specialite" in item["fields"]:
            diplome.append(item['fields']['code_groupe_specialite'])
        else:
            diplome.append(0)

        # Entreprise
        if "code_insee_entreprise" in item["fields"]:
            entreprise.append(item['fields']['code_insee_entreprise'])
        else:
            entreprise.append(0)
        if "depart_entreprise" in item["fields"]:
            entreprise.append(item['fields']['depart_entreprise'])
        else:
            entreprise.append("unknown")
        if "code_naf_entreprise" in item["fields"]:
            entreprise.append(item['fields']['code_naf_entreprise'])
        else:
            entreprise.append(0)

        # Etudiant
        if "diplome" in item["fields"]:
            etudiant.append(item['fields']['diplome'])
        else:
            etudiant.append(diplome_counter)
        if "id_siteformation" in item["fields"]:
            etudiant.append(item['fields']['id_siteformation'])
        else:
            etudiant.append(0)
        if "code_depart_jeune_insee" in item["fields"]:
            etudiant.append(item['fields']['code_depart_jeune_insee'])
        else:
            etudiant.append(0)
        if "code_nationalite" in item["fields"]:
            etudiant.append(item['fields']['code_nationalite'])
        else:
            etudiant.append(0)
        if "code_pcs" in item["fields"]:
            etudiant.append(item['fields']['code_pcs'])
        else:
            etudiant.append(0)
        if "code_sexe" in item["fields"]:
            etudiant.append(item['fields']['code_sexe'])
        else:
            etudiant.append("U")
        if "code_niveau" in item["fields"]:
            etudiant.append(item['fields']['code_niveau'])
        else:
            etudiant.append(0)
        if "code_statut_jeune" in item["fields"]:
            etudiant.append(item['fields']['code_statut_jeune'])
        else:
            etudiant.append("U")
        if "code_commune_jeune_insee" in item["fields"]:
            etudiant.append(item['fields']['code_commune_jeune_insee'])
        else:
            etudiant.append(0)
        if "code_postal_jeune" in item["fields"]:
            etudiant.append(item['fields']['code_postal_jeune'])
        else:
            etudiant.append(0)
        if "libelle_statut_jeune" in item["fields"]:
            etudiant.append(item['fields']['libelle_statut_jeune'])
        else:
            etudiant.append("unknown")
        if "libelle_qualite" in item["fields"]:
            etudiant.append(item['fields']['libelle_qualite'])
        else:
            etudiant.append("unknown")
        if "libelle_nationalite" in item["fields"]:
            etudiant.append(item['fields']['libelle_nationalite'])
        else:
            etudiant.append("unknown")
        if "handicap_oui_non_vide" in item["fields"]:
            etudiant.append(item['fields']['handicap_oui_non_vide'])
        else:
            etudiant.append("unknown")

        if "age_jeune_decembre" in item["fields"]:
            etudiant.append(item['fields']['age_jeune_decembre'])
        else:
            etudiant.append(0)
        if "annee_formation" in item["fields"]:
            etudiant.append(item['fields']['annee_formation'])
        else:
            etudiant.append(0)

        # Site de formation
        if "nom_site_formation" in item["fields"]:
            site_formation.append(item['fields']['nom_site_formation'])
        else:
            site_formation.append("")
        if "adresse1_site" in item["fields"]:
            site_formation.append(item['fields']['adresse1_site'])
        else:
            site_formation.append("")
        if "libelle_ville_site" in item["fields"]:
            site_formation.append(item['fields']['libelle_ville_site'])
        else:
            site_formation.append("")

        # do the all previous actions but with a if to check if the key is in the dict

    data_by_table['diplome'] = diplome
    data_by_table['entreprise'] = entreprise
    data_by_table['etudiant'] = etudiant
    data_by_table['site_formation'] = site_formation

    return data_by_table
