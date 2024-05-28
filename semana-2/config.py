import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/codigo_18_backend'
    #para flask este escuchando por si se realiza las modificaciones
    SQLALCHEMY_TRACK_MODIFICATIONS = True