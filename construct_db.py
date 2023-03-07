def construct_db(db):
    create_students_table(db)
    create_school_table(db)
    create_degree_table(db)
    create_formation_loc_table(db)



def create_students_table(db):
    """Create a table to store students data"""
    pass


def create_school_table(db):
    pass

def create_degree_table(db):
    """Create a table in the db passed in parameters to store degree data"""
    db_cursor = db.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS efrei_sql")
    db_cursor.execute("USE efrei_sql")
    db_cursor.execute("CREATE TABLE IF NOT EXISTS degree ("
                        "id INT AUTO_INCREMENT PRIMARY KEY,"
                        "degree_name VARCHAR(255) NOT NULL,"
                        "degree_type INT NOT NULL"
                        ")")
    db_cursor.close()

    print("Table degree created successfully")

def create_formation_loc_table(db):
    pass