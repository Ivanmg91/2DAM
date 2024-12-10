import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dbrootpass',
    database='employees'
)

# Crear un cursor
cursor = conexion.cursor()

# Ejecutar una consulta SELECT
cursor.execute("SELECT first_name FROM employees")

# Obtener y mostrar los resultados
for emp_no, first_name, last_name in cursor:
    print(f"Nombre: {first_name}")
    print("")

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()