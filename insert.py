import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',234,345.56,'hi')")
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',235,345.56,'hi')")
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',236,345.56,'hi')")
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',237,345.56,'hi')")
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',238,345.56,'hi')")
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',239,345.56,'hi')")
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',240,345.56,'hi')")
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',241,345.56,'hi')")
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',242,345.56,'hi')")
mycursor.execute("INSERT INTO test1_ds.test_table VALUES(2345,'Dip',243,345.56,'hi')")
mydb.commit()
mydb.close()