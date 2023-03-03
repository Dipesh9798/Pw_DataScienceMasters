import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS test1_ds")
mycursor.execute("CREATE TABLE IF NOT EXISTS test1_ds.test_table(c1 INT,c2 VARCHAR(50),c3 INT,c4 FLOAT,c5 VARCHAR(40) )")
mydb.close()