def construct_db(db):
    create_company_table(db)
    create_degree_table(db)
    create_siteformation_table(db)
    create_students_table(db)


def create_students_table(db):
    """Create a table to store students data"""
    db_cursor = db.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS efrei_sql")
    db_cursor.execute("USE efrei_sql")
    db_cursor.execute("CREATE TABLE IF NOT EXISTS etudiant ("
                      "id_etudiant INT PRIMARY KEY AUTO_INCREMENT,"
                      "diplome INT NOT NULL,"
                      "id_siteformation INT NOT NULL,"
                      "id_entreprise INT NOT NULL,"
                      "FOREIGN KEY (diplome) REFERENCES diplome(diplome),"
                      "FOREIGN KEY (id_siteformation) REFERENCES site_formation(id_siteformation),"
                      "FOREIGN KEY (id_entreprise) REFERENCES entreprise(id_entreprise),"
                      "code_depart_jeune_insee INT NOT NULL,"
                      "code_nationalite INT NOT NULL,"
                      "code_pcs INT NOT NULL,"
                      "code_sexe VARCHAR(255) NOT NULL,"
                      "code_niveau INT NOT NULL,"
                      "code_statut_jeune VARCHAR(255) NOT NULL,"
                      "code_commune_jeune_insee INT NOT NULL,"
                      "code_postal_jeune INT NOT NULL,"
                      "libelle_statut_jeune VARCHAR(255) NOT NULL,"
                      "libelle_qualite VARCHAR(255) NOT NULL,"
                      "libelle_nationalite VARCHAR(255) NOT NULL,"
                      "handicap_oui_non_vide VARCHAR(255) NOT NULL,"
                      "age_jeune_decembre INT NOT NULL,"
                      "age_formation INT NOT NULL"
                      ")")
    db_cursor.close()

    print("Table Student created successfully")


def create_siteformation_table(db):
    """Create a table to store site formation data"""
    db_cursor = db.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS efrei_sql")
    db_cursor.execute("USE efrei_sql")
    db_cursor.execute("CREATE TABLE IF NOT EXISTS site_formation ("
                      "id_siteformation INT PRIMARY KEY,"
                      "nom_site_formation VARCHAR(255) NOT NULL,"
                      "addresse_site VARCHAR(255) NOT NULL,"
                      "libelle_ville_site VARCHAR(255) NOT NULL"
                      ")")
    db_cursor.close()

    print("Table Site Formation created successfully")


def create_degree_table(db):
    """Create a table in the db passed in parameters to store degree data"""
    db_cursor = db.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS efrei_sql")
    db_cursor.execute("USE efrei_sql")
    db_cursor.execute("CREATE TABLE IF NOT EXISTS diplome ("
                      "diplome INT PRIMARY KEY,"
                      "libelle_diplome VARCHAR(255) NOT NULL,"
                      "type_diplome VARCHAR(255) NOT NULL,"
                      "libelle_specialite VARCHAR(255) NOT NULL,"
                      "libelle_specialite_com VARCHAR(255) NOT NULL,"
                      "code_groupe_specialite INT NOT NULL"
                      ")")
    db_cursor.close()

    print("Table degree created successfully")


def create_company_table(db):
    """Create a table to store company data"""
    db_cursor = db.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS efrei_sql")
    db_cursor.execute("USE efrei_sql")
    db_cursor.execute("CREATE TABLE IF NOT EXISTS entreprise ("
                      "id_entreprise INT PRIMARY KEY AUTO_INCREMENT,"
                      "code_insee_entreprise INT NOT NULL,"
                      "depart_entreprise INT NOT NULL,"
                      "code_naf_entreprise VARCHAR(255) NOT NULL"
                      ")")
    db_cursor.close()

    print("Table Company created successfully")
