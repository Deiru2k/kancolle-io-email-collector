from pony.orm import Database

config = {
    "host": "localhost",
    "database": "kancolle_email",
    "user": "kancolle_email",
    "password": "shigure"
}

db = Database('postgres', **config)
