
import pyodbc
connection = pyodbc.connect( 
                               'DRIVER={SQL Server};'
                               'Server=DESCTOP-NN1OP7Q;'
                               'Database=practice_day;'
                               'trusted_Connection=yes;'
                               )

cursor = connection.cursor()
cursor.execute("SELECT name FROM sys.tables")  # Example query
for row in cursor.fetchall():
    print(row)







