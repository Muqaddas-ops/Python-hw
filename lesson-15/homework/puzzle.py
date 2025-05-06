import pyodbc

connection = pyodbc.connect( 
                               'DRIVER={SQL Server};'
                               'Server=DESCTOP-NN1OP7Q;'
                               'Database=practice_day;'
                               'trusted_Connection=yes;'
                               )

print('Connected Successfully')
