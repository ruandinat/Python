import mysql.connector

host = "127.0.0.1"

user = "root"

password = "root123456"

database = "teste"

connection = mysql.connector.connect(
        host=host,
        user=user,
        password = password,
        database = database

    )

   

cursor = connection.cursor()

create_table_sql = """
    CREATE TABLE teste (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        nome VARCHAR(50),
        sobrenome VARCHAR(50)
    );
   
   """


drop_table_sql = "DROP TABLE teste"

drop_table_sql1 = "DROP TABLE exemplo"
cursor.execute(drop_table_sql)
cursor.execute(drop_table_sql1)




cursor.close()
connection.close()