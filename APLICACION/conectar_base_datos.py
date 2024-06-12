import mysql.connector

# modificar los datos entre comillas por los correspondientes a su usuario de MYSQL
def conectar_base_datos():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1sami2astorga", 
        database="Turnero"
    )
