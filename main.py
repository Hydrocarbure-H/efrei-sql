from extract_package import extract_data

from construct_db import construct_db
from db import connect_to_db

data = extract_data()

db = connect_to_db()

construct_db(db)