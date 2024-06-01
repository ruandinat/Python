import cx_Oracle

user = "user"
password = "senha"
dsn = "localhost/XE"

connection = cx_Oracle.connect(user,password,dsn)

try:
    cursor = connection.cursor()
     
    drop_table_employee = "DROP TABLE EMPLOYEE"
    drop_table_training = "DROP TABLE TRAINING"
    drop_table_status = "DROP TABLE STATUS"
    drop_table_et = "DROP TABLE EMPLOYEE TRAINING"
   
    cursor.execute(drop_table_employee)
    cursor.execute(drop_table_training)
    cursor.execute(drop_table_status)
    cursor.execute(drop_table_et)

    connection.commit()

finally:
    cursor.close()
    connection.close()