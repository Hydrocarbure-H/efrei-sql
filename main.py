from extract_package import extract_data

from construct_db import construct_db
from fill_db import fill_db
from db import connect_to_db
from requests import my_requests

data = extract_data()

db = connect_to_db()

construct_db(db)

fill_db(db, data)

my_requests(db)

db.close()
