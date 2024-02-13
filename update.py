import _sqlite3

conn = _sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute("UPDATE EMPLOYEES1 SET AGE=67 WHERE ID=92")
conn.commit()

cursor = conn.execute("SELECT ID,NAME,AGE,SALARY FROM EMPLOYEES1;")

for row in cursor:
    print("ID", row[0])
    print("NAME", row[1])
    print("AGE", row[2])
    print("SALARY", row[3])
print("records found")
conn.close()