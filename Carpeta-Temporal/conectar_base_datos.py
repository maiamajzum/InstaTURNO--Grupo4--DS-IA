import mysql.connector


def conectar_base_datos():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="instaturno"
    )