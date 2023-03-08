from pprint import pprint


def fill_degree_table(db, data):
    """
    Fill the degree table with the data passed in parameters
    :param db:
    :param data:
    :return:
    """

    db_cursor = db.cursor(buffered=True)
    db_cursor.execute("USE efrei_sql")
    for item in data:
        # Check if the degree already exists
        db_cursor.execute("SELECT * FROM diplome WHERE diplome = " + str(item[0]))
        if db_cursor.rowcount == 0:
            sql = "INSERT INTO diplome (diplome, libelle_diplome, type_diplome, libelle_specialite, libelle_specialite_com, code_groupe_specialite) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (item[0], item[1], item[2], item[3], item[4], item[5])

            db_cursor.execute(sql, val)
            db.commit()
    db_cursor.close()
    print("Table Diplome filled successfully")


def fill_entreprise_table(db, data):
    """
    Fill the entreprise table with the data passed in parameters
    :param db:
    :param data:
    :return:
    """

    db_cursor = db.cursor(buffered=True)
    db_cursor.execute("USE efrei_sql")
    for item in data:
        # Check if the entreprise already exists
        db_cursor.execute("SELECT * FROM entreprise WHERE id_entreprise = " + str(item[0]))
        if db_cursor.rowcount == 0:
            db_cursor.execute(
                "INSERT INTO entreprise (id_entreprise, code_insee_entreprise, depart_entreprise, code_naf_entreprise) VALUES (%s, %s, %s, %s)",
                (item[0], item[1], item[2], item[3]))
            db.commit()
    db_cursor.close()
    print("Table Entreprise filled successfully")


def fill_site_formation_table(db, data):
    """
    Fill the site formation table with the data passed in parameters
    :param db:
    :param data:
    :return:
    """

    db_cursor = db.cursor(buffered=True)
    db_cursor.execute("USE efrei_sql")
    for item in data:
        # Check if the site formation already exists
        db_cursor.execute("SELECT * FROM site_formation WHERE id_siteformation = " + str(item[0]))
        if db_cursor.rowcount == 0:
            sql = "INSERT INTO site_formation (id_siteformation, nom_site_formation, addresse_site, libelle_ville_site) VALUES (%s, %s, %s, %s)"
            val = (item[0], item[1], item[2], item[3])
            db_cursor.execute(sql, val)
            db.commit()
    db_cursor.close()
    print("Table Site Formation filled successfully")


def fill_students_table(db, data):
    """
    Fill the student table with the data passed in parameters
    :param db:
    :param data:
    :return:
    """

    db_cursor = db.cursor(buffered=True)
    db_cursor.execute("USE efrei_sql")
    for item in data:
        sql = "INSERT INTO etudiant " \
              "(diplome, id_siteformation, id_entreprise, code_depart_jeune_insee," \
              " code_nationalite, code_pcs, code_sexe, code_niveau, code_statut_jeune, code_commune_jeune_insee," \
              " code_postal_jeune, libelle_statut_jeune, libelle_qualite, libelle_nationalite, handicap_oui_non_vide, " \
              "age_jeune_decembre, annee_formation) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (
            item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10],
            item[11], item[12], item[13], item[14], item[15], item[16])

        db_cursor.execute(sql, val)
        db.commit()
    db_cursor.close()
    print("Table Etudiant filled successfully")


def fill_db(db, data):
    """
    Fill all the database with the data passed in parameters
    :param db:
    :param data:
    :return:
    """
    # Parse the data from the json file
    data_by_table = parse_data(data)

    # Fill the tables
    fill_degree_table(db, data_by_table["diplome"])
    fill_entreprise_table(db, data_by_table["entreprise"])
    fill_site_formation_table(db, data_by_table["site_formation"])
    fill_students_table(db, data_by_table["etudiant"])


def parse_data(data):
    """
    Parse the data to get the data by table
    :param data:
    :return: a dict with the data by table
    """

    data_by_table = dict()

    # Prepare lists
    diplome = []
    entreprise = []
    etudiant = []
    site_formation = []

    # Set a counter for the diplome, due to some missing infos in the json file, according to the french developpement logic.
    # This counter is used as a primary key for the diplome table
    diplome_counter = 0
    for item in data:
        change_diplome_counter = False
        reccord_diplome = []
        # Diplome
        if "diplome" in item["fields"]:
            reccord_diplome.append(item['fields']['diplome'])
        else:
            reccord_diplome.append(diplome_counter)
            change_diplome_counter = True
        if "libelle_diplome" in item["fields"]:
            reccord_diplome.append(item['fields']['libelle_diplome'])
        else:
            reccord_diplome.append("unknown")
        if "type_diplome" in item["fields"]:
            reccord_diplome.append(item['fields']['type_diplome'])
        else:
            reccord_diplome.append("unknown")
        if "libelle_specialite" in item["fields"]:
            reccord_diplome.append(item['fields']['libelle_specialite'])
        else:
            reccord_diplome.append("unknown")
        if "libelle_specialite_com" in item["fields"]:
            reccord_diplome.append(item['fields']['libelle_specialite_com'])
        else:
            reccord_diplome.append("unknown")
        if "code_groupe_specialite" in item["fields"]:
            reccord_diplome.append(item['fields']['code_groupe_specialite'])
        else:
            reccord_diplome.append(0)
        diplome.append(reccord_diplome)

        # Entreprise

        reccord_entreprise = []
        if "id_entreprise" in item["fields"]:
            reccord_entreprise.append(item['fields']['id_entreprise'])
        else:
            reccord_entreprise.append(0)
        if "code_insee_entreprise" in item["fields"]:
            reccord_entreprise.append(item['fields']['code_insee_entreprise'])
        else:
            reccord_entreprise.append(0)
        if "depart_entreprise" in item["fields"]:
            reccord_entreprise.append(item['fields']['depart_entreprise'])
        else:
            reccord_entreprise.append(0)
        if "code_naf_entreprise" in item["fields"]:
            reccord_entreprise.append(item['fields']['code_naf_entreprise'])
        else:
            reccord_entreprise.append(0)

        entreprise.append(reccord_entreprise)

        # Etudiant

        reccord_etudiant = []
        if "diplome" in item["fields"]:
            reccord_etudiant.append(item['fields']['diplome'])
        else:
            reccord_etudiant.append(diplome_counter)
        if "id_siteformation" in item["fields"]:
            reccord_etudiant.append(item['fields']['id_siteformation'])
        else:
            reccord_etudiant.append(0)
        if "id_entreprise" in item["fields"]:
            reccord_etudiant.append(item['fields']['id_entreprise'])
        else:
            reccord_etudiant.append(0)
        if "code_depart_jeune_insee" in item["fields"]:
            reccord_etudiant.append(item['fields']['code_depart_jeune_insee'])
        else:
            reccord_etudiant.append(0)
        if "code_nationalite" in item["fields"]:
            reccord_etudiant.append(item['fields']['code_nationalite'])
        else:
            reccord_etudiant.append(0)
        if "code_pcs" in item["fields"]:
            reccord_etudiant.append(item['fields']['code_pcs'])
        else:
            reccord_etudiant.append(0)
        if "code_sexe" in item["fields"]:
            reccord_etudiant.append(item['fields']['code_sexe'])
        else:
            reccord_etudiant.append("U")
        if "code_niveau" in item["fields"]:
            reccord_etudiant.append(item['fields']['code_niveau'])
        else:
            reccord_etudiant.append(0)
        if "code_statut_jeune" in item["fields"]:
            reccord_etudiant.append(item['fields']['code_statut_jeune'])
        else:
            reccord_etudiant.append("U")
        if "code_commune_jeune_insee" in item["fields"]:
            reccord_etudiant.append(item['fields']['code_commune_jeune_insee'])
        else:
            reccord_etudiant.append(0)
        if "code_postal_jeune" in item["fields"]:
            reccord_etudiant.append(item['fields']['code_postal_jeune'])
        else:
            reccord_etudiant.append(0)
        if "libelle_statut_jeune" in item["fields"]:
            reccord_etudiant.append(item['fields']['libelle_statut_jeune'])
        else:
            reccord_etudiant.append("unknown")
        if "libelle_qualite" in item["fields"]:
            reccord_etudiant.append(item['fields']['libelle_qualite'])
        else:
            reccord_etudiant.append("unknown")
        if "libelle_nationalite" in item["fields"]:
            reccord_etudiant.append(item['fields']['libelle_nationalite'])
        else:
            reccord_etudiant.append("unknown")
        if "handicap_oui_non_vide" in item["fields"]:
            reccord_etudiant.append(item['fields']['handicap_oui_non_vide'])
        else:
            reccord_etudiant.append("unknown")

        if "age_jeune_decembre" in item["fields"]:
            reccord_etudiant.append(item['fields']['age_jeune_decembre'])
        else:
            reccord_etudiant.append(0)
        if "annee_formation" in item["fields"]:
            reccord_etudiant.append(item['fields']['annee_formation'])
        else:
            reccord_etudiant.append(0)
        etudiant.append(reccord_etudiant)

        # Site de formation

        reccord_site_formation = []
        if "id_siteformation" in item["fields"]:
            reccord_site_formation.append(item['fields']['id_siteformation'])
        else:
            reccord_site_formation.append(0)
        if "nom_site_formation" in item["fields"]:
            reccord_site_formation.append(item['fields']['nom_site_formation'])
        else:
            reccord_site_formation.append("")
        if "adresse1_site" in item["fields"]:
            reccord_site_formation.append(item['fields']['adresse1_site'])
        else:
            reccord_site_formation.append("")
        if "libelle_ville_site" in item["fields"]:
            reccord_site_formation.append(item['fields']['libelle_ville_site'])
        else:
            reccord_site_formation.append("")

        site_formation.append(reccord_site_formation)

        # Do our stuff about the primary key of the diplome table
        if change_diplome_counter:
            diplome_counter += 1
            change_diplome_counter = False

    # Create a dictionary to return
    data_by_table['diplome'] = diplome
    data_by_table['entreprise'] = entreprise
    data_by_table['etudiant'] = etudiant
    data_by_table['site_formation'] = site_formation

    return data_by_table
