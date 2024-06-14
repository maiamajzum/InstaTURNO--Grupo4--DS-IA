from APLICACION.mysql import connector

# modificar los datos entre comillas por los correspondientes con sus credenciales de acceso configuradas en la instalación de MySQL
def conectar_base_datos():
    return connector.connect(
        host="localhost",
        user="configured_mySQL_user",
        password="configured_mySQL_password",
        database="Turnero"
    )
