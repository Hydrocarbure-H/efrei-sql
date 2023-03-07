def fill_degree_table(db, data):
    pass


def fill_school_table(db, data):
    pass


def fill_formation_loc_table(db, data):
    pass


def fill_students_table(db, data):
    pass


def fill_db(db, data):
    data_by_table = parse_data(data)
    fill_degree_table(db, data)
    fill_school_table(db, data)
    fill_formation_loc_table(db, data)
    fill_students_table(db, data)


# Data is a list of following elements
# {
#         "datasetid": "apprentissage_-_effectifs_detailles_2011-2012",
#         "recordid": "ef00d68db4b8efe4e0539aba363467e7bee27362",
#         "fields": {
#             "code_nationalite": 1,
#             "code_depart_jeune_insee": 99,
#             "libelle_origine_annee_prec": "AUTRE SCOLARITE SUPERIEURE",
#             "code_naf_entreprise": "2362Z",
#             "libelle_diplome": "Science environnement, du territoire et de l'\u00e9conomie : ing\u00e9nierie d\u00e9veloppement durable, sp\u00e9cialit\u00e9 science/technique g\u00e9nie logistique Internet, syst info, NTIC (MASTER Versailles)",
#             "code_pcs": 99,
#             "code_groupe_specialite": 311,
#             "code_insee_entreprise": 93074,
#             "code_postal_site": 78047,
#             "libelle_qualite": "Externe",
#             "code_sexe": "M",
#             "num_section": 53,
#             "id_etab": 18,
#             "code_niveau": 1,
#             "annee_formation": 1,
#             "code_qualite": "E",
#             "depart_entreprise": 93,
#             "libelle_specialite": "Transport, manutention, magasinage",
#             "nom_complet_cfa": "CFA Union des Universit\u00e9s",
#             "libelle_statut_jeune": "Contrat d'apprentissage",
#             "code_commune_site_insee": 78297,
#             "libelle_origine_prec_cfa": "AUTRE SCOLARITE SUPERIEURE",
#             "handicap_oui_non_vide": "N",
#             "code_commune_jeune_insee": 99999,
#             "id_og": 17,
#             "code_statut_jeune": "A",
#             "code_uai_site": "0783375V",
#             "age_jeune_decembre": 24,
#             "libelle_nationalite": "France",
#             "code_postal_jeune": 95400,
#             "sexe": "Masculin",
#             "libelle_pcs_parent": "Non renseign\u00e9 (inconnu ou sans objet)",
#             "duree_formation_mois": 24,
#             "diplome": 13531103,
#             "libelle_ville_site": "GUYANCOURT",
#             "libelle_lien_cfa": "Convention L6231-3",
#             "code_origine_annee_prec": 69,
#             "nom_site_formation": "Universit\u00e9 de Versailles Saint-Quentin en Yvelines",
#             "numero_section": 53,
#             "type_diplome": "MASTER PRO",
#             "annee_scolaire": "11/12",
#             "libelle_specialite_com": "Transport, logistique",
#             "adresse1_site": "47 boulevard Vauban",
#             "code_uai_etab_annee_prec": "93",
#             "id_siteformation": 1038,
#             "code_origine_prec_cfa": 69,
#             "libelle_og": "Association Union Universit\u00e9 Economie"
#         },
#         "record_timestamp": "2014-08-13T21:45:51Z"
#     },

# According to the data, we have the following tables:
# - diplome, with the following fields:
# libelle_diplome	varchar(255)
# type_diplome	varchar(255)
# libelle_specialite	varchar(255)
# libelle_specialite_com	varchar(255)
# code_groupe_specialite

# - entreprise with the following fields:
# id_entreprise	int
# code_insee_entreprise	int
# depart_entreprise	int
# code_naf_entreprise	varchar(255)

# - etudiant with the following fields:
# id_etudiant	int
# diplome	int
# id_siteformation	int
# id_entreprise	int
# code_depart_jeune_insee	int
# code_nationalite	int
# code_pcs	int
# code_sexe	varchar(255)
# code_niveau	int
# code_statut_jeune	varchar(255)
# code_commune_jeune_insee	int
# code_postal_jeune	int
# libelle_statut_jeune	varchar(255)
# libelle_qualite	varchar(255)
# libelle_nationalite	varchar(255)
# handicap_oui_non_vide	varchar(255)
# age_jeune_decembre	int
# age_formation	int

# - site_formation with the following fields:
# id_siteformation	int
# nom_site_formation	varchar(255)
# addresse_site	varchar(255)
# libelle_ville_site	varchar(255)

# Now, parse the data and fill the tables


def parse_data(data):
    data_by_table = dict()
    diplome = []
    entreprise = []
    etudiant = []
    site_formation = []
    for item in data:
        diplome.append(item['fields']['libelle_diplome'])
        diplome.append(item['fields']['type_diplome'])
        diplome.append(item['fields']['libelle_specialite'])
        diplome.append(item['fields']['libelle_specialite_com'])
        diplome.append(item['fields']['code_groupe_specialite'])

        entreprise.append(item['fields']['code_insee_entreprise'])
        entreprise.append(item['fields']['depart_entreprise'])
        entreprise.append(item['fields']['code_naf_entreprise'])

        etudiant.append(item['fields']['diplome'])
        etudiant.append(item['fields']['id_siteformation'])
        etudiant.append(item['fields']['id_entreprise'])
        etudiant.append(item['fields']['code_depart_jeune_insee'])
        etudiant.append(item['fields']['code_nationalite'])
        etudiant.append(item['fields']['code_pcs'])
        etudiant.append(item['fields']['code_sexe'])
        etudiant.append(item['fields']['code_niveau'])
        etudiant.append(item['fields']['code_statut_jeune'])
        etudiant.append(item['fields']['code_commune_jeune_insee'])
        etudiant.append(item['fields']['code_postal_jeune'])
        etudiant.append(item['fields']['libelle_statut_jeune'])
        etudiant.append(item['fields']['libelle_qualite'])
        etudiant.append(item['fields']['libelle_nationalite'])
        etudiant.append(item['fields']['handicap_oui_non_vide'])
        etudiant.append(item['fields']['age_jeune_decembre'])
        etudiant.append(item['fields']['age_formation'])

        site_formation.append(item['fields']['nom_site_formation'])
        site_formation.append(item['fields']['adresse1_site'])
        site_formation.append(item['fields']['libelle_ville_site'])

    data_by_table['diplome'] = diplome
    data_by_table['entreprise'] = entreprise
    data_by_table['etudiant'] = etudiant
    data_by_table['site_formation'] = site_formation
    
    return data_by_table
