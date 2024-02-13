import _sqlite3

conn = _sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES1 VALUES (90,'VINCENT',22,56000.00)")
conn.execute(" INSERT INTO EMPLOYEES1 VALUES (91,'JANE',28,27400.00)")
conn.execute(" INSERT INTO EMPLOYEES1 VALUES (92,'ALLAN',29,128400.00)")
conn.execute("INSERT INTO EMPLOYEES1 VALUES (93,'REY',40,89000.00)")
conn.commit()

print("Records inserted successfully")

conn.close()
