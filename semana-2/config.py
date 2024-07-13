import os
#os es una funcion de python permite a ingregar tipos de archivos
class Config:
    #'' se orieta la ruta de donde se guarda la BD
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/codigo_18_backend'
    #para flask este escuchando por si se realiza las modificaciones
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = 'my_secret_key'